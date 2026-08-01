# TC001 - Calibrate Value
---
# Result

## PASS:

## FAIL:
### Notes and/or details of failure:

---
## Objective

Verify that a configured calibration point set changes the sensor value according to the configured calibration values.

## Steps

1. Configure three available sensors with the following calibration point sets: (replace sensor names to match your setup.)
   a. sensor.temp_plus100:
         - measured: 0.0
           reference: 100.0
   b. sensor.temp_minus100:
         - measured: 0.0
           reference: -100.0
   c. sensor.temp_original:
         - measured: 0.0
           reference: 0.0
2. Restart Home Assistant.
3. Wait for a sensor update.
4. Compare original and calibrated values.

## Expected Result
(checked mean passed)

- [ ] The sensor configured to produce an offset of 100 reports a value increased by 100.
- [ ] The sensor configured to produce an offset of -100 reports a value decreased by 100.
- [ ] The sensor configured to produce an offset of 0 reports the original value unchanged.
