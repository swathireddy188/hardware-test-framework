from sensor_simulator import SensorSimulator
from logger import TestLogger
from report import generate_report

def run_all_tests():
    logger = TestLogger("test_results.csv")

    # Define all rails to test
    rails = [
        SensorSimulator("3.3V_rail",  3.3,  0.05),
        SensorSimulator("5V_rail",    5.0,  0.05),
        SensorSimulator("12V_rail",   12.0, 0.05),
    ]

    print("=== Starting hardware test session ===")

    for rail in rails:
        readings = rail.read_multiple(count=10)
        for v in readings:
            low  = rail.nominal_v * (1 - rail.tolerance)
            high = rail.nominal_v * (1 + rail.tolerance)
            passed = low <= v <= high
            logger.log(rail.rail_name, v, rail.nominal_v, passed)

    logger.summary()
    generate_report()

if __name__ == "__main__":
    run_all_tests()
