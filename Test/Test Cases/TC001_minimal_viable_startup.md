# TC001 - Minimal Viable Startup
---
# Result

## PASS:

## FAIL:
### Notes and/or details of failure:

---
## Objective
Verify that Universal Sensor Calibration starts correctly with the minimum viable configuration consisting of an empty calibration.yaml file.

## Steps

1. Backup the current calibration.yaml.
2. Remove all content from calibration.yaml, leaving the file empty.
3. Save calibration.yaml.
4. Restart Home Assistant.
5. Assess test results against expected results.
6. Restore the backed up calibration.yaml.

## Expected Result
(checked mean passed)

- [ ] Home Assistant starts successfully.
- [ ] Universal Sensor Calibration starts successfully.
- [ ] No critical startup errors are generated.
- [ ] An empty calibration.yaml does not affect Home Assistant operation.
- [ ] No sensors are calibrated.
