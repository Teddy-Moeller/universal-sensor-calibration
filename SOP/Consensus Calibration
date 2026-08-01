# Standard Operating Procedure (SOP)

## Calibration Using "Consensus" method

### Purpose

Consensus calibration is a method of **relative calibration** (aligning multiple sensors to agree with one another) that uses the consensus of a group of sensors exposed to the same environmental conditions. This method improves consistency between sensors but does not establish **traceable accuracy** (calibration against a certified reference standard).

### Requirements

* Three or more sensors measuring the same parameter
* Home Assistant or another method of viewing sensor values
* A location with stable environmental conditions

### Procedure

#### 1. Co-locate the Sensors

Place all sensors in close proximity (within a few centimeters, approximately one inch) so that each sensing element is exposed to the same environment. This minimizes **spatial gradients** (small differences in temperature or humidity caused by location).

Avoid:

* Direct sunlight
* Radiant heat sources (heaters, electronics, lighting)
* HVAC vents
* Open windows
* Drafts (moving air)

#### 2. Allow the Sensors to Reach Thermal Equilibrium

Allow the sensors to stabilize for at least 15 minutes so they reach thermal equilibrium (their temperature readings have stabilized). During this period, keep the ambient conditions as stable as possible and avoid introducing drafts or moving the sensors.

#### 3. Record the Measurements

Once the readings have stabilized, record the value reported by each sensor. Read all sensors within as short a time as practical so they represent the same environmental conditions.

#### 4. Determine the Consensus Value

Calculate the **arithmetic mean (average)** of all sensor readings. This value becomes the **consensus value** used as the reference value for calculating each sensor's offset.

For example:

| Sensor | Reading |
| ------ | ------: |
| A      | 21.8 °C |
| B      | 22.0 °C |
| C      | 22.2 °C |

Consensus value = **22.0 °C**

#### 5. Calculate the Offset

For each sensor, calculate its **Calibration offset** (the difference between the sensor reading and the consensus value).

Example:

| Sensor | Reading | Offset to Apply |
| ------ | ------: | --------------: |
| A      | 21.8 °C |         +0.2 °C |
| B      | 22.0 °C |          0.0 °C |
| C      | 22.2 °C |         −0.2 °C |

#### 6. Apply the Offset

Add the calculated offset for each sensor to your calibration.yaml file using the following format:

sensor.living_room_temperature: 0.2
sensor.bedroom_temperature: -0.1
sensor.garage_temperature: 0

Where the key is the sensor name and the value is the calculated offset. Positive values increase the reported measurement, while negative values decrease it.

Save the file and reload the calibration configuration (or restart Home Assistant, if required) for the new calibration offsets to take effect.

### Notes

* This procedure performs **relative calibration** (making sensors agree with one another), not **absolute calibration** (matching a traceable reference).
* Increasing the number of sensors generally improves confidence in the consensus value.
* If one sensor is a clear **outlier** (its reading differs significantly from the rest of the group), investigate the sensor before applying the calibration offset, as it may indicate a faulty device or incorrect placement.
