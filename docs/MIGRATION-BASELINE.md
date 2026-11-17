# Migration baseline: legacy Kurdish scaffold

This snapshot records why the first code migration must not be a blind rename.

## Confirmed from the current source files

| File | Current state | Consequence |
| --- | --- | --- |
| `configure.ac` | Package is `apertium-kmr-eng`; language dependency is `apertium-kmr` plus `apertium-eng`. | The configure dependency still requires Kurdish resources. |
| `Makefile.am` | `LANG1=kmr`, `LANG2=eng`, `BASENAME=apertium-kmr-eng`. | Build targets and source paths are tied to the Kurdish package. |
| `modes.xml` | Modes and transducer filenames use `kmr-eng`; transfer filenames use `apertium-kmr-eng`. | Runtime modes still invoke the legacy pipeline. |
| `apertium-kmr-eng.kmr-eng.dix` | The fetched file content is empty. | There is no usable bilingual dictionary in this file to convert. |
| `apertium-kmr-eng.kmr-eng.t1x` | Contains Kurdish-specific lemmas/tags and rules (for example `di`, `xwe`, and Kurdish verb categories). | Transfer rules must be redesigned, not mechanically renamed. |
| `apertium-kmr-eng.eng-kmr.t1x` | English-to-Kurdish transfer rules. | This direction also requires a new Balochi target grammar. |

## Safe migration order

1. Confirm the exact Suleimani Balochi variety and speaker-reviewed Latin
   grapheme inventory.
2. Collect licensed and reviewed Balochi monolingual lexical/morphological
   data; create the `apertium-bal` source package.
3. Populate and review `data/bal-eng-lexicon.tsv`; run
   `python3 tools/check_bal_orthography.py` for data-hygiene checks.
4. Generate/validate the Balochi monolingual transducer and bilingual
   dictionary.
5. Write Balochi-specific transfer rules in both directions and add
   native-reviewed regression examples.
6. Only then switch `configure.ac`, `Makefile.am`, `modes.xml`, install
   paths, and test commands to `bal-eng` / `eng-bal`.

## Scope and verification

This report is based on the files listed above, not a full build or a complete
repository-wide audit. No build or translation-quality test is claimed by
this baseline. The new TSV validator checks spelling/encoding hygiene only;
it cannot verify that a word or grammatical analysis is genuinely Balochi.
