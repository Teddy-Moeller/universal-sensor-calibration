# TC001 - Calibrate Value
---
# Result

## PASS:

## FAIL:
### Notes and/or details of failure:

---
## Objective

Verify that a configured offset changes the sensor value according to the configured calibration value.

## Steps

1. Configure three sensors with the following offsets:
   a. 100
   b. -100
   c. 0
2. Restart Home Assistant.
3. Wait for a sensor update.
4. Compare original and calibrated values.

## Expected Result
(checked mean passed)

- [ ] The sensor configured with offset 100 reports a value increased by 100.
- [ ] The sensor configured with offset -100 reports a value decreased by 100.
- [ ] The sensor configured with offset 0 reports the original value unchanged.
