"""
Unit Tests for SOCKONE Data & Application Integrity
"""

import os
import unittest
import pandas as pd
import json

class TestSockOne(unittest.TestCase):
    def setUp(self):
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.csv_path = os.path.join(self.base_dir, "data", "sockone_mock_dataset.csv")
        self.schema_path = os.path.join(self.base_dir, "data", "sockone_schema.json")
        self.long_path = os.path.join(self.base_dir, "data", "sockone_longitudinal_dataset.csv")

    def test_data_files_exist(self):
        """Check if all essential data files are generated."""
        self.assertTrue(os.path.exists(self.csv_path), "Cohort CSV must exist")
        self.assertTrue(os.path.exists(self.schema_path), "Schema JSON must exist")
        self.assertTrue(os.path.exists(self.long_path), "Longitudinal CSV must exist")

    def test_schema_valid_json(self):
        """Check if schema is valid JSON."""
        with open(self.schema_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.assertIn("properties", data)
        self.assertIn("required", data)

    def test_cohort_dataframe_integrity(self):
        """Check data types and required columns."""
        df = pd.read_csv(self.csv_path)
        required_cols = [
            "Patient_ID", "Timestamp", "HRV_RMSSD", "Gait_Symmetry_Score",
            "Fatigue_Level", "Pain_Score_AI", "Alert_Status"
        ]
        for col in required_cols:
            self.assertIn(col, df.columns, f"Missing required column {col}")

        # Check values within boundaries
        self.assertTrue((df["Pain_Score_AI"] >= 0).all() and (df["Pain_Score_AI"] <= 10).all())
        self.assertTrue((df["Gait_Symmetry_Score"] >= 0).all() and (df["Gait_Symmetry_Score"] <= 100).all())
        self.assertGreaterEqual(len(df), 10, "Should have at least 10 rows")

if __name__ == "__main__":
    unittest.main()
