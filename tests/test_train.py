import unittest
import pandas as pd
from src.train import main, FEATURES, TARGET

class TrainTest(unittest.TestCase):

    def test_data_loading(self):
        df = pd.read_csv("data/processed_heart.csv")
        self.assertFalse(df.empty)
        self.assertTrue(all(col in df.columns for col in FEATURES + [TARGET]))

if __name__ == "__main__":
    unittest.main()
