import csv, json
from pathlib import Path
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]
def load_split(split='train'):
    manifest = json.loads((ROOT / 'manifest.json').read_text())
    paths = [ROOT / p['path'] for p in manifest['distribution_files'] if p['split'] == split]
    if not paths:
        raise ValueError('Unknown split: ' + split)
    return pd.concat([pd.read_csv(p, sep='\t', quoting=csv.QUOTE_NONE,
        dtype=str, keep_default_na=False) for p in paths], ignore_index=True)
if __name__ == '__main__':
    for split in ('train', 'dev', 'test'):
        print(split, len(load_split(split)))
