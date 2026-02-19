# src/validator.py
import subprocess
import shutil
from pathlib import Path
import tempfile
from typing import Tuple

def apply_fix_and_test(
    original_file: Path,
    fixed_code: str,
    tests_path: Path
) -> Tuple[bool, str]:
    """
    Applies the fixed code to a temp folder, runs pytest,
    and returns (success_boolean, output_string)
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)

        # copy all files from tests_path parent directory
        for f in tests_path.parent.iterdir():
            if f.is_file():
                shutil.copy(f, tmpdir / f.name)

        # write the fixed code into the buggy file
        target = tmpdir / original_file.name
        target.write_text(fixed_code, encoding="utf-8")

        # run tests
        res = subprocess.run(
            ["pytest", "-q"],
            cwd=str(tmpdir),
            capture_output=True,
            text=True
        )

        success = (res.returncode == 0)
        output = res.stdout + "\n" + res.stderr

        return success, output
