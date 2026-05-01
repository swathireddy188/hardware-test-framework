import random
import time

class SensorSimulator:
    """Simulates a DMM reading voltage from a PCB rail.
    In production: replace with SCPI commands to real instrument."""

    def __init__(self, rail_name, nominal_v, tolerance=0.05):
        self.rail_name = rail_name       # e.g. "3.3V_rail"
        self.nominal_v = nominal_v       # expected voltage
        self.tolerance = tolerance       # allowed variation (5%)

    def read_voltage(self):
        """Simulate a voltage reading with small random noise."""
        noise = random.uniform(-0.1, 0.1)
        voltage = self.nominal_v + noise
        return round(voltage, 3)

    def read_multiple(self, count=10, delay=0.1):
        """Take multiple readings over time."""
        readings = []
        for i in range(count):
            readings.append(self.read_voltage())
            time.sleep(delay)
        return readings
