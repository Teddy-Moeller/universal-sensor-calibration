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

        try:
            value = float(new_state.state)
        except Exception:
            return

        offset = calibrations.get(entity_id, 0)

        adjusted = round(value + offset, 2)

        attrs["calibrated_by"] = "sensor_calibration"

        hass.states.async_set(
            entity_id,
            adjusted,
            attrs
        )

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
