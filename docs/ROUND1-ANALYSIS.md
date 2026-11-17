# Speaker elicitation and research notes: Rounds 1–3

## Data provenance

- Round 1: `data/speaker-corpus-round1.tsv`
- Round 2: `data/speaker-corpus-round2.tsv`
- Round 3: `data/speaker-corpus-round3.tsv`

All thirty English prompts and Balochi equivalents were supplied by a
native speaker. Original Latin spellings, word boundaries, and punctuation
are preserved, except where the speaker explicitly corrected an entry.
No automatic transliteration or spelling correction has been applied.

The five initial lexical entries in `data/bal-eng-lexicon.tsv` remain marked
`speaker-provided-unreviewed`.

## External references

- Hamid Ali Baloch (2023), “The Sulaimani Dialect of the Balochi Language:
  A Phonological Study,” *Makhz (Research Journal)* 4(4), 67–84,
  DOI: https://doi.org/10.47205/makhz.2023(4-IV)urdu-07.
- University of Arizona, Iranian Languages, “Balochi”:
  https://iranian-languages.arizona.edu/balochi
- Cambridge, “Progressive constructions in different Balochi dialects from
  a diachronic and an areal linguistic point of view”:
  https://doi.org/10.1017/S0041977X24000144
- Uppsala University's Balochi Language Project:
  https://www.uu.se/en/department/linguistics-and-philology/research/proj/the-balochi-language

These references establish a research baseline and dialect variation; they
do not independently verify every speaker-provided Sulaimani form.

## Round 1 observations (hypotheses only)

- `Salam` — greeting.
- `baz minatwar` — gratitude expression; retain as a phrase.
- `av`, `nagn`, `log` — water, food, house.
- `man yak e mard aan` and `man yak e mind e aan` are identity sentences;
  internal segmentation is not yet established.
- `thai nam che in?` and `tho bukho rog ee?` are preserved as complete
  question examples.
- `man av a lotan` — I want water. Do not infer the structure of `a lotan`
  from one example.

## Round 2 observations (hypotheses only)

### Present progressive / motion

- `man rog aan` — I am going.
- `tho rog ee` — You are going (singular).
- `aan rog een` — He is going.
- `aan rog een` — She is going.

The sequence `rog` remains constant while final forms vary
(`aan`, `ee`, `een`). This may reflect a person-marked finite/copular
element; segmentation is not established.

### Past, negation, possession, imperative

- `man shuzagan` — I went. One example only.
- `man av aa na lotan` — I do not want water, compared with
  `man av a lotan` — I want water. The sequence `aa na` is unanalysed.
- `ae mainn log een` — This is my house.
- `aan thai log een` — That is your house.
- `ma nagn warag un` — We are eating food.
- `mana av aa de` — Give me water.

## Round 3 observations (hypotheses only)

### Present progressive / motion

- `man rog aan` — I am going.
- `tho rog ee` — You are going (singular).
- `aan rog een` — He/she is going.
- `Ma rog un.` — We are going.
- `Aan rog an.` — They are going.
- `Sha kul rog ee.` — You all are going.

Provisional surface pattern:

| English subject | Subject form | Ending after `rog` |
| --- | --- | --- |
| I | `man` | `aan` |
| You (singular) | `tho` | `ee` |
| He / she | `aan` | `een` |
| We | `Ma` | `un` |
| They | `Aan` | `an` |
| You all | `Sha kul` | `ee` |

This is a provisional surface table, not a complete morphological analysis.
The speaker should clarify capitalization and whether `man` and `Ma`
differ in pronunciation. The same `ee` occurs with singular and plural
“you”, while `Sha kul` may express plurality.

### Eating

- `Ma nagn warag aan.` — I am eating food. (as elicited in Round 3)
- `Aan nagn warag een.` — He is eating food.
- `ma nagn warag un` — We are eating food. (Round 2)

Preserve capitalization as given. The endings resemble the pattern with
`rog`, but `warag` is not yet analysed as an infinitive or participle.

### Past forms and explicit correction

- `man shuzagan` — I went. (Round 2)
- `ma shuzagun` — We went. (Round 3, explicitly corrected by the speaker)
- `Tho shuzage.` — You went (singular).
- `Aan shuza.` — He went.

**Correction history:** the Round 3 response was initially transcribed as
`Man shuzagun`. The speaker explicitly corrected this to `ma shuzagun`.
The corpus file now contains the corrected form and marks it
`speaker-corrected-unreviewed`. Do not reintroduce `man shuzagun` as
a valid example. The forms `shuzagan`, `shuzagun`, `shuzage`, and
`shuza` suggest subject-conditioned past forms, but their segmentation
and paradigm remain unconfirmed.

### Possessive noun phrases

- `ae mainn log een` — This is my house.
- `aan thai log een` — That is your house.
- `Main ab.` — My water.
- `Thai av.` — Your water.

Keep `mainn` and `Main`, and `ab` and `av`, distinct in raw data until
the speaker confirms whether they sound different or are spelling variants.

## Current implementation boundary

These observations support a speaker corpus and hypotheses for further
elicitation, not yet reliable finite-state morphology or transfer rules.
Do not relabel the Kurdish scaffold or claim a working translator until
Balochi monolingual resources, bilingual entries, transfer rules, and tests
are implemented and built.

## Next elicitation targets

Clarify the sound/spelling contrasts and test the past paradigm and pronoun
forms with controlled everyday examples.
