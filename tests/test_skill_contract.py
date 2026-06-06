import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = (ROOT / "photo-reference-coach" / "SKILL.md").read_text()
SCRIPT = (
    ROOT / "photo-reference-coach" / "scripts" / "extract_image_metadata.py"
).read_text()


class SkillContractTests(unittest.TestCase):
    def test_metadata_is_automatic_and_non_blocking(self):
        self.assertIn(
            "For every attached image, first look for an accessible local file path",
            SKILL,
        )
        self.assertIn("automatically attempt metadata extraction", SKILL)
        self.assertIn("continue with visual analysis", SKILL)
        self.assertNotIn("unless the user supplies the original file", SCRIPT)

    def test_editor_is_known_before_detailed_recipe(self):
        self.assertIn("identify the editing tool before detailed editing steps", SKILL)
        self.assertIn("references/editing-tools.md", SKILL)
        self.assertIn("do not prescribe controls the selected tool lacks", SKILL)


if __name__ == "__main__":
    unittest.main()
