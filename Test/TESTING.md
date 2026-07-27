# Testing Philosophy

Universal Sensor Calibration is tested on the author's environment and documented through test cases and test reports.

No two Home Assistant installations are identical.

Variations in hardware, virtualization platform, operating system, database backend, sensor count, sensor update frequency, and other integrations may affect system performance.

A passing test report demonstrates that the software functioned correctly in the tested environment and under the tested conditions.

A passing test report does not guarantee identical results on all systems.

Users are encouraged to execute the provided test cases within their own environment.

## Post-Release Validation Strategy

Following the first public release, Universal Sensor Calibration will be validated against the first two Home Assistant monthly releases.
Following the first public release, Universal Sensor Calibration will be validated against the first three Home Assistant monthly releases.

Example:

- HA 2026.x
- HA 2026.y

After this initial validation period, compatibility testing will normally be performed annually and on an ad-hoc basis when:

- Defects are reported.
- Major USC features are released.
- Compatibility concerns arise.

Community testing is encouraged. Published test cases may be executed by any user wishing to validate USC within their own environment.
