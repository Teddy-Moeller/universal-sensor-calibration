# Standard Operating Procedure (SOP)

## Calibration Using a Reference Thermometer

### Purpose

This procedure performs **relative calibration** (aligning a sensor to match a chosen reference instrument) by comparing the sensor to a **reference thermometer** under the same environmental conditions.

For the purposes of this procedure, the **reference thermometer** is simply the thermometer you have chosen as your reference. Unless it has been calibrated against a **traceable reference standard** (an instrument with a documented calibration certificate), it should not be assumed to provide absolute accuracy. This method improves consistency between sensors but does not establish **traceable accuracy**.

### Requirements

* One or more sensors measuring temperature
* One thermometer chosen as the reference
* Home Assistant or another method of viewing sensor values
* A location with stable environmental conditions

### Procedure

#### 1. Select the Reference Thermometer

Choose the thermometer that will serve as the reference for the calibration. This may be the thermometer you trust the most, one with the best specifications, or simply the one you wish all other sensors to match.

The reference thermometer does not need to be laboratory calibrated. It simply serves as the measurement that all other sensors will be aligned to.

#### 2. Co-locate the Sensors

Place the reference thermometer and all sensors in close proximity (within a few centimeters, approximately one inch of one another) so that each sensing element is exposed to the same environment. This minimizes **spatial gradients** (small differences in temperature caused by location).

Avoid:

* Direct sunlight
* Radiant heat sources (heaters, electronics, lighting)
* HVAC vents
* Open windows
* Drafts (moving air)

#### 3. Allow the Sensors to Reach Thermal Equilibrium

Allow the sensors and the reference thermometer to stabilize for at least **15 minutes** so they reach **thermal equilibrium** (their temperature readings have stabilized). During this period, keep the ambient conditions as stable as possible and avoid introducing drafts or moving the sensors.

#### 4. Record the Measurements

Once the readings have stabilized, record the value reported by the reference thermometer and each sensor. Record all readings as close together in time as practical so they represent the same environmental conditions.

For example:

| Device                | Reading |
| --------------------- | ------: |
| Reference Thermometer | 22.0 °C |
| Living Room Sensor    | 21.8 °C |
| Bedroom Sensor        | 22.3 °C |

#### 5. Calculate the Calibration Offset

For each sensor, calculate its **offset** (the reference thermometer reading minus the sensor reading). This is the value that will be entered into `calibration.yaml`.

Example:

| Sensor      | Reading | Offset to Apply |
| ----------- | ------: | --------------: |
| Living Room | 21.8 °C |         +0.2 °C |
| Bedroom     | 22.3 °C |         −0.3 °C |

#### 6. Apply the Calibration Offset

Add the calculated offset for each sensor to your `calibration.yaml` file using the following format:

yaml:
sensor.living_room_temperature: 0.2
sensor.bedroom_temperature: -0.3

Where the key is the sensor's entity ID and the value is the calculated offset. Positive values increase the reported measurement, while negative values decrease it.

Save the file and restart Home assistant for the new offsets to take effect.

### Notes

* This procedure performs **relative calibration** (making sensors agree with a chosen reference), not **absolute calibration** (matching a traceable reference standard).
* The quality of the calibration depends on the quality and stability of the chosen reference thermometer.
* If a sensor differs significantly from the reference thermometer, investigate the cause before applying an offset, as large deviations may indicate a faulty sensor or unsuitable placement.
* If a traceable reference thermometer is available, it can be used in place of the chosen reference thermometer to establish traceable accuracy.
