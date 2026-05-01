import csv
import datetime
import os

class TestLogger:
    def __init__(self, filename="test_results.csv"):
        self.filename = filename
        # Write CSV header if file is new
        if not os.path.exists(filename):
            with open(filename, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([
                    "timestamp", "rail_name", "voltage",
                    "nominal", "result"
                ])

    def log(self, rail_name, voltage, nominal, passed):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = "PASS" if passed else "FAIL"
        with open(self.filename, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, rail_name, voltage, nominal, result])
        print(f"{result}: {rail_name} = {voltage}V")

    def summary(self):
        """Print pass/fail count at end of test session."""
        import pandas as pd
        df = pd.read_csv(self.filename)
        passed = len(df[df["result"] == "PASS"])
        failed = len(df[df["result"] == "FAIL"])
        print(f"\n--- TEST SUMMARY ---")
        print(f"PASS: {passed}  |  FAIL: {failed}  |  TOTAL: {passed+failed}")
