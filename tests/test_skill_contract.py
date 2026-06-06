import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "photography-coach"
SKILL = (SKILL_DIR / "SKILL.md").read_text()
README = (ROOT / "README.md").read_text()
OPENAI_YAML = (SKILL_DIR / "agents" / "openai.yaml").read_text()
SCRIPT = (
    SKILL_DIR / "scripts" / "extract_image_metadata.py"
).read_text()


class SkillContractTests(unittest.TestCase):
    def test_skill_uses_photography_coach_name(self):
        self.assertTrue(SKILL_DIR.is_dir())
        self.assertIn("name: photography-coach", SKILL)
        self.assertIn("# Photography Coach", SKILL)
        self.assertIn("$photography-coach", README)
        self.assertIn('display_name: "Photography Coach"', OPENAI_YAML)
        self.assertNotIn("$photo-reference-coach", README + OPENAI_YAML)

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
