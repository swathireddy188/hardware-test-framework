 import pytest
 from sensor_simulator import SensorSimulator
 
 # Create sensor objects for each power rail
 rail_3v3  = SensorSimulator("3.3V_rail",  nominal_v=3.3,  tolerance=0.05)
 rail_5v   = SensorSimulator("5V_rail",    nominal_v=5.0,  tolerance=0.05)
 rail_12v  = SensorSimulator("12V_rail",   nominal_v=12.0, tolerance=0.05)

 def check_pass_fail(voltage, nominal, tolerance):
     """Return True if voltage is within tolerance band."""
     low  = nominal * (1 - tolerance)
     high = nominal * (1 + tolerance)
     return low <= voltage <= high
 
 # --- TEST CASES --- 
 def test_3v3_rail_nominal():
    """3.3V rail must be within 5% of nominal."""
     voltage = rail_3v3.read_voltage()
     assert check_pass_fail(voltage, 3.3, 0.05), \
         f "FAIL: 3.3V rail = {voltage}V (expected 3.135–3.465V)"
 
 def test_5v_rail_nominal():
     """5V rail must be within 5% of nominal."""
     voltage = rail_5v.read_voltage()
     assert check_pass_fail(voltage, 5.0, 0.05), \
        f "FAIL: 5V rail = {voltage}V (expected 4.75–5.25V)"

 def test_12v_rail_nominal():
    """12V rail must be within 5% of nominal."""
     voltage = rail_12v.read_voltage()
     assert check_pass_fail(voltage, 12.0, 0.05), \
         f "FAIL: 12V rail = {voltage}V (expected 11.4–12.6V)"
 
 def test_3v3_stability():
     """3.3V rail must stay stable across 10 readings."""
    readings = rail_3v3.read_multiple(count=10)
     for v in readings:
         assert check_pass_fail(v, 3.3, 0.05), \
             f "FAIL: Unstable reading {v}V on 3.3V rail"
