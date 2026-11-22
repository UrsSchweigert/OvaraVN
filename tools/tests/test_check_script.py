import sys, tempfile, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import check_script as C

APPROVED = 'One. Two *here*. "Three," Sefa said. "Four 50%."\n'
GOOD = 'label x:\n    "One."\n    "Two {i}here{/i}."\n    c_sefa "Three,"\n    "Sefa said."\n    c_sefa "Four 50%%."\n'


class T(unittest.TestCase):
    def run_case(self, rpy, md=APPROVED):
        d = Path(tempfile.mkdtemp())
        (d / "game" / "game").mkdir(parents=True)
        (d / "work" / "cut").mkdir(parents=True)
        (d / "game" / "game" / "ch01.rpy").write_text(rpy)
        (d / "work" / "cut" / "ch01.md").write_text("# T\n\n<!-- c01.s01 -->\n\n" + md)
        return C.check(1, d)[0]

    def test_match(self):
        self.assertEqual([e for e in self.run_case(GOOD) if "allowed drop" not in e], [])

    def test_missing(self):
        errs = self.run_case(GOOD.replace('    "One."\n', ""))
        self.assertTrue(any("missing" in e and "One." in e for e in errs))

    def test_extra(self):
        errs = self.run_case(GOOD + '    "Added."\n')
        self.assertTrue(any("extra" in e and "Added." in e for e in errs))

    def test_reordered(self):
        errs = self.run_case('    "Two {i}here{/i}."\n    "One."\n    c_sefa "Three,"\n    "Sefa said."\n    c_sefa "Four 50%%."\n')
        self.assertTrue(any("reordered" in e for e in errs))

    def test_unknown_speaker(self):
        errs = self.run_case(GOOD.replace("c_sefa", "nobody", 1))
        self.assertTrue(any("unknown speaker" in e for e in errs))

    def test_unescaped_text_is_flagged(self):
        errs = self.run_case(GOOD.replace("50%%", "50{x}"))
        self.assertTrue(any("markup" in e for e in errs))


if __name__ == "__main__":
    unittest.main()
