import unittest
import sys
from pathlib import Path

# 1. Get the directory of the current test file
# .resolve() gets the absolute path, .parent is like '../'
current_file = Path(__file__).resolve()
project_root = current_file.parent.parent 

# 2. Add the project root to sys.path so we can find 'src'
sys.path.append(str(project_root))

from src.pipeline_builder import build_pipeline

class TestModelPipeline(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 3. Define the config path using the '/' operator (Pathlib magic!)
        cls.config_path = project_root / "config" / "pipeline_config.yaml"
        cls.pipeline = build_pipeline(str(cls.config_path))

    def test_pipeline_initialization(self):
        self.assertIsNotNone(self.pipeline)
        self.assertEqual(len(self.pipeline.steps), 3)

    def test_text_cleaner_transformation(self):
        dirty_text = ["  AGENT INPUT  "]
        cleaner = self.pipeline.named_steps['cleaner']
        result = cleaner.transform(dirty_text)
        self.assertEqual(result[0], "agent input")

if __name__ == '__main__':
    unittest.main()