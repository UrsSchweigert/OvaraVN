import sys, tempfile, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import play


class PlayTest(unittest.TestCase):
    def test_parse_chapter(self):
        self.assertEqual(play.parse_chapter("2"), 2)
        self.assertEqual(play.parse_chapter("ch02"), 2)
        self.assertEqual(play.parse_chapter("CH18"), 18)
        for bad in ("0", "19", "x", "", "ch"):
            with self.assertRaises(ValueError):
                play.parse_chapter(bad)

    def test_built_chapters_reads_labels(self):
        d = Path(tempfile.mkdtemp())
        (d / "ch01.rpy").write_text("label ch01:\n    return\n")
        (d / "ch03.rpy").write_text("# label ch07:\nlabel ch03:\n    return\n")
        (d / "other.rpy").write_text("label start:\n    jump ch01\n")
        self.assertEqual(play.built_chapters(d), [1, 3])

    def test_build_launch_sets_start_label(self):
        cmd, env = play.build_launch(2, "/sdk")
        self.assertEqual(env["VN_START"], "ch02")
        self.assertTrue(cmd[0].endswith("renpy.sh"))
        _, env = play.build_launch(None, "/sdk")
        self.assertNotIn("VN_START", env)

    def test_unbuilt_chapter_refused(self):
        self.assertEqual(play.main(["99"]), 1)
        self.assertEqual(play.main(["banana"]), 1)


if __name__ == "__main__":
    unittest.main()
