import sys
from pathlib import Path


def register_package():
    sys.path.insert(
        0,
        Path(__file__).parent.parent.joinpath("src").as_posix()
    )
    import qtmvvmkit
    qtmvvmkit.__file__
    return None


register_package()