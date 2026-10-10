# Kazakh–Chinese Corpus

## Files

| Split | Rows |
|---|---:|
| Train | 211,994 |
| Development | 1,006 |
| Test | 1,000 |
| **Total** | **214,000** |

- `data/` — compressed TSV files.
- `notebooks/` — data preparation notebooks.
- `scripts/` — loading and verification utilities.
- `metadata/` — source and license records.
- `manifest.json` — configuration, counts and checksums.

## Usage

Install dependencies:

```bash
pip install -r requirements.txt
```

Verify the files and load the splits:

```bash
python scripts/verify.py
python scripts/load_data.py
```

Files use UTF-8 encoding and tab-separated columns. The `kk` and `zh` columns contain Kazakh and Chinese text.

## Data Format

Each `.tsv.gz` file contains a header followed by tab-separated records.

| Column | Description |
|---|---|
| `id` | Record identifier |
| `kk` | Kazakh text |
| `zh` | Chinese text |
| `source` | Source identifier |
| `license` | Recorded source license |
| `labse` | Sentence similarity score |

Additional columns contain provenance and processing metadata.
Column availability varies between splits.

When reading with pandas, use `sep="\t"`, `quoting=csv.QUOTE_NONE`,
`dtype=str` and `keep_default_na=False`.

Row counts include retained duplicate records. Similarity scores
are filtering signals, not estimates of translation accuracy.

## Licensing and Provenance

The MIT License applies only to the preparation code.
Corpus texts remain subject to their source licenses.

Source information and translation provenance are recorded in
`manifest.json` and `metadata/`. See `LICENSES.md` for source-specific
conditions and outstanding redistribution checks.
