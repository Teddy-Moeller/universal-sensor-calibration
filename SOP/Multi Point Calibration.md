# Standard Operating Procedure (SOP)

## Multi point Calibration Using a Reference Thermometer

### Purpose

To Be Written

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

#### 5. Enter the Calibration Data

For each sensor, add the sensor's measured value together with the reference value to your calibration.yaml file using the following format:

```yaml
sensor.livingroom_temperature:
  - measured: 21.8
    reference: 22.0

sensor.office_temperature:
  - measured: 22.3
    reference: 22.0
```

The Universal Sensor Calibration will automatically calculate the offset and apply it to the sensor.

Save the file and restart Home Assistant for the new offsets to take effect.

#### 6. Change environment

Change the measured environment with at least 5 degrees. This is to strengthen the calibration as a cluster of measurements will make the calibration inaccurate, and in extreme cases worse than not calibrating.

I advise that raising the environment temperature to make it easy to follow the points in the calibration.yaml file.

#### 7. Repeat

Evaluate if you desire more calibration measurements at this point.

***If yo do*** - Repeat the process from **step 3.**

***If you don't*** - Skip to **step 8.**

#### 8. Common Sense Evaluation

Home sensors vary naturally in quality and precision. Instead of complex math, use your common sense after calibration:
* **The 2-Degree Suggestion:** I suggest that all sensors should ideally stay within 2 degrees of each other (or the reference) after calibration.
* **What to do:** If a sensor still drifts more than 2 degrees away, it might just be a low-quality unit. Consider placing it in a less critical room (like a hallway or garage) rather than throwing it away, or try changing the battery.

### Notes

* This procedure performs **relative calibration** (making sensors agree with a chosen reference), not **absolute calibration** (matching a traceable reference standard).
* The quality of the calibration depends on the quality and stability of the chosen reference thermometer, and the amount of calibration measurements.
* Few measurement points can hurt the accuracy, and too many may not yield much value. I will suggest between 2 and 5 measurement points.
* If a traceable reference thermometer is available, it can be used in place of the chosen reference thermometer to establish traceable accuracy.
