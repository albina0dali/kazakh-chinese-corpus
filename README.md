# Kazakh–Chinese Corpus

This collection contains 66,119 existing pairs and 147,881 additional
machine-translated pairs (69.1% of all rows). For the additions, Kazakh and
English texts come from the main KazParC kk–en training split; the English
side was translated into Simplified Chinese using Qwen2.5-7B-Instruct.

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

## License

The MIT License applies only to the code and notebooks in this repository.
Corpus texts remain subject to their respective source licenses.
See [LICENSES.md](LICENSES.md) for source-specific conditions and the current
redistribution review. Review of the complete mixed corpus remains incomplete.

## Quality and Limitations

The packaged files contain 214,000 rows. File checksums and row counts were
verified; no empty Kazakh or Chinese texts or duplicate record IDs were found.
All additional pairs have stored LaBSE scores of at least 0.72 for kk–zh,
kk–en and en–zh. These scores are not translation accuracy percentages.

Using NFKC normalization, case folding and whitespace normalization, there
are 8 repeated pairs in train and 1 in development. These rows are retained.
Three Kazakh texts occur in both development and test with different Chinese
texts. No exact normalized Kazakh or Chinese text overlap was found between
train and either held-out split. Semantic and document-level independence
has not been established. The corpus has not undergone comprehensive human
validation; automated filtering may miss omissions and mistranslations.

## Provenance and Attribution

Existing pairs originate from OPUS, Wikipedia and Weblate. Row-level source
labels and the available URLs are retained. Some records do not identify the
original project or both aligned source pages; see LICENSES.md.

KazParC: Rustem Yeshpanov, Alina Polonskaya and Huseyin Atakan Varol.
*KazParC: Kazakh Parallel Corpus for Machine Translation*, LREC-COLING 2024,
pp. 9633–9644.
- Dataset: https://huggingface.co/datasets/issai/kazparc
- Paper: https://aclanthology.org/2024.lrec-main.842/
- Upstream license: https://creativecommons.org/licenses/by/4.0/

Changes to the KazParC-derived material: selection of rows, addition of
Chinese machine translations through the existing English side, filtering
and repackaging. No endorsement by the original authors is implied.
Model and scoring revisions are recorded in manifest.json.

## Preparation and Checksums

The Colab notebooks collect the base corpus and generate additional pairs.
Reading the packaged data requires only the dependencies in requirements.txt;
GPU generation dependencies are installed separately inside the notebooks.
Set the Drive paths and obtain any required upstream access before running.
The expansion notebook pins the Qwen and LaBSE revisions used in this release.
Changing online sources and execution environments can still affect a rebuild;
exact regeneration of all records is not guaranteed.

In manifest.json, `files` stores hashes of the original uncompressed whole
TSV splits. `distribution_files` stores hashes and row counts of the actual
published gzip parts. The original TSV hashes can be reproduced by joining
each split's decompressed parts in manifest order, keeping only the first header.
