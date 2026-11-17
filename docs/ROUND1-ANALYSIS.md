# Speaker elicitation and research notes: Rounds 1–3

## Data provenance

- Round 1: `data/speaker-corpus-round1.tsv`
- Round 2: `data/speaker-corpus-round2.tsv`
- Round 3: `data/speaker-corpus-round3.tsv`

All thirty English prompts and Balochi equivalents were supplied by a
native speaker. Original Latin spellings, word boundaries, and punctuation
are preserved exactly. No automatic transliteration or spelling correction
has been applied.

The five initial lexical entries in `data/bal-eng-lexicon.tsv` remain marked
`speaker-provided-unreviewed`. These are seed data, not a fully reviewed
dictionary or a claim of standard orthography.

## External dialect and grammar references

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

These references establish a useful research baseline and dialect variation;
they do not independently verify every speaker-provided Sulaimani word or
construction. General Balochi paradigms must not be copied into the
Sulaimani grammar without matching evidence.

## Round 1 observations (hypotheses only)

- `Salam` is supplied for a greeting.
- `baz minatwar` is supplied as a gratitude expression. Keep it as a
  multiword expression until its internal structure and spelling are confirmed.
- `av`, `nagn`, and `log` are supplied for water, food, and house.
- The two “I am a ...” sentences share `man yak e` and end in `aan`.
  The exact segmentation and grammatical role of each token remain unknown.
- The question examples are retained as complete examples; their individual
  tokens are not yet assigned grammatical tags.
- `man av a lotan` is the supplied “I want water” example. Do not infer
  the lemma or conjugation of `a lotan` from this one example.

## Round 2 observations (hypotheses only)

### Present progressive / motion

- `man rog aan` — I am going.
- `tho rog ee` — You are going (singular).
- `aan rog een` — He is going.
- `aan rog een` — She is going.

The sequence `rog` remains constant while the final forms vary
(`aan`, `ee`, `een`). This is consistent with a person/number-marked
finite element or copula-like ending, but segmentation is not established.
Identical forms for “he” and “she” may indicate no gender distinction in
this construction; do not create separate masculine/feminine forms.

### Past, negation, possession, and imperative

- `man shuzagan` — I went. One past example only; do not segment it yet.
- `man av aa na lotan` — I do not want water, compared with
  `man av a lotan` — I want water. The sequence `aa na` is not yet analysed.
- `ae mainn log een` — This is my house.
- `aan thai log een` — That is your house.
- `ma nagn warag un` — We are eating food.
- `mana av aa de` — Give me water.

Candidate forms are worth tracking, but token boundaries and grammatical
functions remain unconfirmed.

## Round 3 observations (hypotheses only)

### Present progressive / motion across persons

- `man rog aan` — I am going.
- `tho rog ee` — You are going (singular).
- `aan rog een` — He is going.
- `aan rog een` — She is going.
- `Ma rog un.` — We are going.
- `Aan rog an.` — They are going.
- `Sha kul rog ee.` — You all are going.

The current surface pattern is:

| English subject | Subject form as elicited | Ending after `rog` |
| --- | --- | --- |
| I | `man` | `aan` |
| You (singular) | `tho` | `ee` |
| He / she | `aan` | `een` |
| We | `Ma` | `un` |
| They | `Aan` | `an` |
| You all | `Sha kul` | `ee` |

This is a provisional surface paradigm, not yet a morphological analysis.
Notice the potentially meaningful differences in case/spelling:
`man` vs `Ma`, and `aan` as a subject form for both third-person
singular and plural contexts. These may reflect orthographic capitalization,
pronunciation, or different forms; do not normalize them without confirmation.
The “you all” sentence shares `ee` with singular “you”, suggesting that
number may be expressed in `Sha kul`, but this needs further examples.

### Eating

- `Ma nagn warag aan.` — I am eating food. (Round 3 prompt)
- `Aan nagn warag een.` — He is eating food.
- `ma nagn warag un.` — We are eating food. (Round 2)

The Round 3 first-person singular prompt uses `Ma`, while the earlier
first-person plural prompt used lowercase `ma` with `un`. Preserve both
exactly. The contrast between `aan` and `un` at the end is consistent
with the endings observed with `rog`, but the form `warag` may be a
non-finite verb form. Do not yet label it infinitive or participle.

### Past paradigm candidates

- `man shuzagan` — I went. (Round 2)
- `Man shuzagun.` — We went.
- `Tho shuzage.` — You went (singular).
- `Aan shuza.` — He went.

These examples suggest that past forms vary with subject/person, with
surface forms `shuzagan`, `shuzagun`, `shuzage`, and `shuza`.
The data do not yet establish a single invariant stem plus suffixes:
possible stem alternation, endings, and orthographic variation need testing.
In particular, do not automatically parse `shuzagan` as `shuza + gan`.

### Possessive noun phrases

- `ae mainn log een` — This is my house.
- `aan thai log een` — That is your house.
- `Main ab.` — My water.
- `Thai av.` — Your water.

The possessor forms `mainn` (before `log`) and `Main` (before
`ab`) differ in the supplied spelling; similarly, the water noun appears
as `ab` in “my water” but `av` in “your water” and earlier examples.
These differences may reflect pronunciation, sandhi, case/construct
morphology, or inconsistent raw spelling. They must remain separate raw
forms pending speaker clarification; do not silently merge `ab` and `av`
or `Main` and `mainn`.

## Current implementation boundary

The above observations are suitable for a speaker corpus and future
paradigm investigation. They are not yet sufficient to implement a reliable
finite-state morphology or Apertium transfer rules. Do not alter the
Kurdish scaffold's language identity or claim a working translator until
Balochi monolingual resources, bilingual entries, transfer rules, and tests
are implemented and built.

## Next elicitation targets

Next clarify the surface contrasts and test the past paradigm and the
pronoun/determiner forms with repeated, controlled minimal examples.
