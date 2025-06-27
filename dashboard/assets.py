from pathlib import Path
from typing import Generator

from pandas import read_csv, DataFrame


PROJECT_ROOT = Path(__file__).parent.parent
DATASETS_DIR = PROJECT_ROOT / 'data'


def years() -> list:
    return [
        int(path.name)
        for path in DATASETS_DIR.iterdir()
        if path.is_dir() and path.name.isdigit()
    ]

def datasets() -> Generator[tuple[str, DataFrame], None, None]:
    for year in DATASETS_DIR.iterdir():
        if not year.is_dir():
            continue
        for dataset in year.glob('*.csv'):
            yield year.name, read_csv(dataset)
