# Suleimani Balochi Latin/Roman orthography

## Status

**Selected:** Latin/Roman is the canonical script for the first version of
this language pair.

**Not yet specified:** the exact Suleimani Balochi grapheme inventory and
spelling conventions. Those are linguistic decisions and must be confirmed
with speakers or reliable, cited language resources. This file deliberately
does not invent a transliteration standard.

## Rules for repository data

1. All authored Balochi lexical and example data must be UTF-8.
2. Normalize canonical stored text to Unicode NFC.
3. Use Latin/Roman spellings in dictionary lemmas, inflectional forms, and
   canonical test output.
4. Record approved alternate spellings explicitly; do not silently collapse
   spellings that may represent different phonemes.
5. Keep punctuation and tokenization conventions consistent across the
   monolingual dictionary, bilingual dictionary, and tests.
6. Keep future Arabic-derived-script input/output conversion separate from
   morphological analysis and bilingual transfer.

## Inventory to approve before lexicon expansion

The project needs a speaker-reviewed table with these columns:

| Phoneme / contrast | Canonical Latin spelling | Accepted variants | Example word | Source / reviewer |
| --- | --- | --- | --- | --- |
| Vowels | TBD | TBD | TBD | TBD |
| Long vowels (if contrastive) | TBD | TBD | TBD | TBD |
| Consonants | TBD | TBD | TBD | TBD |
| Retroflexes (if contrastive) | TBD | TBD | TBD | TBD |
| Aspiration (if contrastive) | TBD | TBD | TBD | TBD |
| Other dialect-specific contrasts | TBD | TBD | TBD | TBD |

Do not populate this table by copying Kurdish spelling conventions or by
assuming that a general Balochi romanization exactly describes the requested
Suleimani variety.

## Validation

Once the inventory is approved, add tests for:

- NFC normalization.
- Every approved spelling variant and its canonical analysis.
- Preservation of phonemic distinctions.
- Analyzer/generator round trips.
- Consistent spelling in both `bal-eng` and `eng-bal` examples.
