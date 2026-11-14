"""World news of Friday 13 November 2026, summed up in one image.

The entry image (entry.jpg) is a newspaper front page: masthead
"WORLD NEWS - 13 NOVEMBER 2026" over six panels picturing the day's
biggest stories - the ~1,200-drone Ukrainian attack on Russia,
the FAA nationwide ground stop, the second day of the global
Microsoft 365 outage, Chinese naval drills in the western Pacific,
the IEA oil-supply surplus outlook, and the Qatar-Turkey defence pact.

This program only copies the bundled picture to /output/entry.png.
It needs no network and writes identical bytes on every run.
"""

import hashlib
import shutil
from pathlib import Path

SRC = Path(__file__).with_name("entry.jpg")
OUT = Path("/output/entry.png")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, OUT)
    # Fail loudly instead of submitting a truncated or corrupted picture.
    if sha256(OUT) != sha256(SRC):
        raise SystemExit("copied picture does not match the bundled image")


if __name__ == "__main__":
    main()
