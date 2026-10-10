# Kazakh–Chinese Corpus

## Dataset Files

| Split | Rows |
|---|---:|
| Training | 211,994 |
| Development | 1,006 |
| Test | 1,000 |
| **Total** | **214,000** |

Data is stored as UTF-8, gzip-compressed TSV files in `data/`.
The training split consists of 11 parts. Each part includes a header.

## Repository Structure

- `data/` — corpus files.
- `scripts/` — loading and integrity-checking utilities.
- `notebooks/` — preparation notebooks.
- `metadata/` — source and license records.
- `manifest.json` — configuration, provenance and checksums.
- `LICENSES.md` — source-specific licensing information.

## Usage

Install dependencies:

    pip install -r requirements.txt

Verify the packaged files:

    python scripts/verify.py

Load the dataset splits:

    python scripts/load_data.py

## Format

The `kk` and `zh` columns contain Kazakh and Chinese text.
Other columns provide identifiers and available processing metadata.
Column availability varies between splits.

For pandas, use `sep="\t"`, `quoting=csv.QUOTE_NONE`,
`dtype=str` and `keep_default_na=False`.

Row counts include retained duplicates. Similarity scores are
filtering signals, not measurements of translation accuracy.

## Provenance and Licensing

See [manifest.json](manifest.json) for data origins and translation
methods, and [LICENSES.md](LICENSES.md) for attribution, source
conditions and outstanding redistribution checks.

The [MIT License](LICENSE) applies only to the code and notebooks.
Corpus texts remain subject to their respective source licenses.
