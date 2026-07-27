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

2. Edit calibration.yaml
   Enter your sensors and offset.
   Example:
     sensor.office_temperature: 0.52
     sensor.bedroom_temperature: -0.83
     sensor.outdoor_humidity: 1.2

4. Edit configuration.yaml
   sensor_calibration:

5. Restart Home Assistant.


# Current Version
## v1.0

Single-point offset calibration
Calibration applied to original sensor entity
No duplicate entities created
Recursion protection included

## v2.0

New calibration point format:

sensor.name:
  measured: x
  referense: y

# Roadmap

## v3.0

Two-point linear calibration

## v4.0

Multi-point interpolation calibration

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
