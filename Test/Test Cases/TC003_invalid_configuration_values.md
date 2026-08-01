# TC003 - Invalid Configuration Values
---
# Result

## PASS:

## FAIL:
### Notes and/or details of failure:

---
## Objective
Verify that Universal Sensor Calibration safely handles invalid input values without affecting Home Assistant stability or normal sensor operation.
The selected special characters represent the most commonly used keyboard special characters and are included to verify that accidental user input does not affect Universal Sensor Calibration operation.

## Steps

1. Backup the current calibration.yaml
2. In the calibration.yaml file use the format:

```yaml
sensor.name:
  - measured: 0.0
    reference: XXX
```

Where "sensor.name" is an existing sensor that produces a numerical value.
Each test value shall be assigned to a different sensor.

For each item in the following list, replace XXX with the specified value:

For each item in the following list, replace XXX with the specified value:

```text
a. 123abc           # Numbers then plain text
b. abc123           # Plain text then numbers
c. abc              # Plain text
d. @                # Common special character
e. #                # Common special character
f. $                # Common special character
g. %                # Common special character
h. !                # Common special character
i. 25°C             # Value with unit/special character
j. 55.6761, 12.5683 # Multiple numerical values in a single calibration field. Associated with GPS coordinates
k. [0]              # Structured data
l. {0}              # Structured data
```

3. Also misspell a sensor name on purpose.
```yaml
sensor.name.misspelled:
  - measured: 0.0
    reference: 0.0
```

4. At the end of calibration.yaml, add one known-good calibration entry.
```yaml
sensor.valid_test:
  - measured: 0.0
    reference: 100.0
```

5. Save the calibration.yaml file.
6. Reboot Home Assistant.
7. Assess test results against expected results.
8. Restore the backed up calibration.yaml

## Expected Result
(checked mean passed)

- [ ] Home Assistant continues operating.
- [ ] Universal Sensor Calibration continues operating.
- [ ] The known-good calibration entry functions as expected.
- [ ] Invalid entries in calibration.yaml are ignored.
