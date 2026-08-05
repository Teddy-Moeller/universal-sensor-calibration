import logging
import os
import yaml

from homeassistant.helpers.event import async_track_state_change_event

_LOGGER = logging.getLogger(__name__)

DOMAIN = "sensor_calibration"


async def async_setup(hass, config):

    _LOGGER.info("Universal Sensor Calibration loading.")

    calibration_file = os.path.join(
        hass.config.config_dir,
        "custom_components",
        DOMAIN,
        "calibration.yaml"
    )

    with open(calibration_file, "r") as f:
        calibrations = yaml.safe_load(f) or {}

    _LOGGER.info("calibration.yaml loaded.")

    async def state_changed(event):

        entity_id = event.data.get("entity_id")
        new_state = event.data.get("new_state")

        if new_state is None:
            return

        attrs = dict(new_state.attributes)

        if attrs.get("calibrated_by") == "sensor_calibration":
            return

        calibration = calibrations.get(entity_id, [])

        point_count = len(calibration)

        if point_count == 0:
            # No calibration points configured.
            return

        elif point_count == 1:
            # Offset calibration.

            try:
                value = float(new_state.state)
            except Exception:
                return
            
            try:
                point = calibration[0]
                
                measured = float(point["measured"])
                reference = float(point["reference"])
                
                offset = reference - measured
                
                adjusted = round(value + offset, 2)
    
                attrs["calibrated_by"] = "sensor_calibration"
    
                hass.states.async_set(
                    entity_id,
                    adjusted,
                    attrs
                )
    
                return
                
            except Exception:
                return

        elif point_count >= 2:
            # Piecewise linear interpolation.

            try:
                value = float(new_state.state)
            except Exception:
                return

            try:
                points = sorted(
                    calibration,
                    key=lambda p: p["measured"]
                )

                measured_values = [
                    float(p["measured"])
                    for p in points
                ]

                reference_values = [
                    float(p["reference"])
                    for p in points
                ]

            except Exception:
                _LOGGER.error(
                    "Invalid calibration data for %s",
                    entity_id
                )
                return

            # Require a reasonable calibration span.
            spread = (
                max(reference_values)
                - min(reference_values)
            )

            if spread < 5:
                _LOGGER.warning(
                    "%s calibration span too small "
                    "(%.2f < 5). Skipping calibration.",
                    entity_id,
                    spread
                )
                return

            # Prevent division-by-zero conditions.
            if len(set(measured_values)) != len(measured_values):
                _LOGGER.warning(
                    "%s contains duplicate measured values.",
                    entity_id
                )
                return

            # Below lowest point.
            if value <= measured_values[0]:
                p1 = points[0]
                p2 = points[1]

            # Above highest point.
            elif value >= measured_values[-1]:
                p1 = points[-2]
                p2 = points[-1]

            # Between two calibration points.
            else:
                p1 = None
                p2 = None

                for i in range(len(points) - 1):
                    x1 = float(points[i]["measured"])
                    x2 = float(points[i + 1]["measured"])

                    if x1 <= value <= x2:
                        p1 = points[i]
                        p2 = points[i + 1]
                        break

                if p1 is None:
                    return

            x1 = float(p1["measured"])
            y1 = float(p1["reference"])

            x2 = float(p2["measured"])
            y2 = float(p2["reference"])

            if x1 == x2:
                _LOGGER.warning(
                    "%s contains identical measured values.",
                    entity_id
                )
                return
        
            # Linear interpolation / extrapolation.
            slope = (y2 - y1) / (x2 - x1)

            adjusted = round(
                y1 + slope * (value - x1),
                2
            )

            attrs["calibrated_by"] = "sensor_calibration"

            hass.states.async_set(
                entity_id,
                adjusted,
                attrs
            )

            return

    async_track_state_change_event(
        hass,
        list(calibrations.keys()),
        state_changed
    )

    _LOGGER.info(
        "Universal Sensor Calibration loaded and running with %s sensors.",
        len(calibrations),
    )

    return True
