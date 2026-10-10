import csv, gzip, hashlib, json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
m = json.loads((ROOT / 'manifest.json').read_text())
counts = {}
for item in m['distribution_files']:
    p = ROOT / item['path']
    if not p.exists():
        sys.exit('Data files are not included in the public metadata package: ' + str(p))
    assert hashlib.sha256(p.read_bytes()).hexdigest() == item['sha256'], p
    with gzip.open(p, 'rt', encoding='utf-8', newline='') as f:
        rows = csv.DictReader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
        n = 0
        for row in rows:
            assert None not in row and row['kk'].strip() and row['zh'].strip(), p
            n += 1
    assert n == item['rows'], p
    counts[item['split']] = counts.get(item['split'], 0) + n
assert counts == m['split_sizes'], counts
assert sum(counts.values()) == 214000
print('Verified:', counts, '| total:', sum(counts.values()))
