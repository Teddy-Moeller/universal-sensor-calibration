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

Calculate the **arithmetic mean (average)** of all sensor readings. This value becomes the **consensus value** used as the reference value.

For example:

| Sensor | Reading |
| ------ | ------: |
| A      | 21.8 °C |
| B      | 22.0 °C |
| C      | 22.2 °C |

Consensus value = **22.0 °C**

#### 5. Enter the Calibration Data

For each sensor, add the sensor's measured value together with the reference value to your calibration.yaml file using the following format:

```yaml
sensor.office_temperature:
  - measured: 25.0
    reference: 25.52

sensor.bedroom_temperature:
  - measured: 21.0
    reference: 20.17
```

The Universal Sensor Calibration will automatically calculate the offset and apply it to the sensor.

Save the file and reload the calibration configuration (or restart Home Assistant, if required) for the new calibration offsets to take effect.

#### 6. Common Sense Evaluation

Home sensors vary naturally in quality and precision. Instead of complex math, use your common sense after calibration:
* **The 2-Degree Suggestion:** I suggest that all sensors should ideally stay within 2 degrees of each other (or the reference) after calibration.
* **What to do:** If a sensor still drifts more than 2 degrees away, it might just be a low-quality unit. Consider placing it in a less critical room (like a hallway or garage) rather than throwing it away, or try changing the battery.

### Notes

* This procedure performs **relative calibration** (making sensors agree with one another), not **absolute calibration** (matching a traceable reference).
* Increasing the number of sensors generally improves confidence in the consensus value.
