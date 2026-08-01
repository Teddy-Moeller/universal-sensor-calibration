# Universal Sensor Calibration

A custom Home Assistant integration that applies calibration only to selected sensor entities without creating duplicate entities.

## Features

- Offset calibration
- Selected sensors only
- No duplicate entities
- Works with any Home Assistant sensor platform
  - Zigbee
  - Matter
  - ESPHome
  - MQTT
  - Modbus
  - REST/API sensors

## Requirements

- Home Assistant
- Access to the `custom_components` folder

## Installation

1. Copy the integration to:
   /config/custom_components/sensor_calibration/

2. Edit calibration.yaml and enter your measured and reference values.
Do not include units.

Example:
   
```yaml
sensor.office_temperature:
  - measured: 25.0
    reference: 25.52

sensor.bedroom_temperature:
  - measured: 21.0
    reference: 20.17
```

4. Edit configuration.yaml
   sensor_calibration:

5. Restart Home Assistant.

## Scope

Universal Sensor Calibration only processes numeric sensor states.

Non-existing sensor entities are ignored by design.
USC subscribes to configured entities.
If no state updates are received, no calibration actions are performed.

Sensors returning text values such as `33%`, `25°C`, `ON`, `OFF`, `OPEN`, `55°40'34.0"N`, `55.6761,12.5683`, or other non-numeric values are ignored.

Examples of valid numeric equivalents include:

- `33` instead of `33%`
- `25` instead of `25°C`
- `55.6761` instead of `55°40'34.0"N`
- `55.6761` and `12.5683` instead of `55.6761,12.5683`

Values such as `ON`, `OFF`, and `OPEN` have no meaningful numeric equivalent and are therefore not calibration candidates.

# Current Version
## v0.1.0

Single-point offset calibration
Calibration applied to original sensor entity
No duplicate entities created
Recursion protection included

## v0.2.0

New calibration point format:

sensor.name:
  measured: x
  reference: y

# Roadmap

## v0.3.0

Two-point linear calibration

## v0.4.0

Multi-point interpolation calibration

## v0.5.0

First Public Release (HACS)

# Attribution

Original Author:
- Teddy Møller

Original Repository:
- https://github.com/teddy-moeller/universal-sensor-calibration

Please retain attribution when creating forks or derivative works.

---

## A Personal Note

Universal Sensor Calibration was created to solve a practical calibration need in Home Assistant.

My background is primarily in software testing, calibration techniques, laboratory processes, and quality assurance rather than software development. The project is therefore developed with a strong focus on documentation, testing, traceability, and practical usability.

While I continue to learn Python and Home Assistant development, feedback and constructive suggestions are always welcome.
