# Speaker elicitation and research notes: Rounds 1–4

## Data provenance

- Round 1: `data/speaker-corpus-round1.tsv`
- Round 2: `data/speaker-corpus-round2.tsv`
- Round 3: `data/speaker-corpus-round3.tsv`
- Round 4: `data/speaker-corpus-round4.tsv`

All forty English prompts and Balochi equivalents were supplied by a
native speaker. Original Latin spellings, word boundaries, capitalization,
and punctuation are preserved, except where the speaker explicitly
corrected an entry. No automatic transliteration or spelling correction
has been applied.

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
The corpus file contains the corrected form and marks it
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

## Round 4 observations (hypotheses only)

Round 4 adds eight speaker-supplied examples, preserved in
`data/speaker-corpus-round4.tsv`.

### Simple present: eating food

| English | Speaker's exact form |
| --- | --- |
| I eat food. | `Man nagn waranga.` |
| You eat food (one person). | `tho nagn warage.` |
| He eats food. | `aan nagn warange.` |
| We eat food. | `ma nagn warangu.` |

The repeated sequence `nagn warang-` is a useful candidate for a stable
food/eating construction, while the endings differ by subject in these
four examples: `-a`, `-e`, `-e`, and `-u` as visible surface endings.
This is only a descriptive observation: do not yet segment `waranga`,
`warage`, `warange`, or `warangu` into stem and suffix, and do not
assume the exact ending boundaries. In particular, the forms for singular
“you” and “he” are not identical even though both visibly end in `e`.

These examples contrast with Round 2/3 progressive examples containing
`warag` (e.g. `Ma nagn warag aan`). The difference may be grammatical,
but more examples are needed before defining a tense/aspect rule.

### Negative motion

- `Man narogan.` — I am not going.
- `Tho naroge.` — You are not going (one person).

Compare with positive motion:
- `man rog aan` — I am going.
- `tho rog ee` — You are going (one person).

The negative examples contain `naro-`/ `narog-` on the surface where
positive examples contain `rog`, and their endings differ (`-an`,
`-e`). It is tempting to analyse an attached negative marker, but the
exact boundary and the relation between `na`, `naro`, and `rog` are
not established. Keep the complete forms intact.

### Demonstrative and possessive noun phrases

- `Ee mainn av een.` — This is my water.
- `Ee mainn nagn een.` — This is my food.

Compare with Round 1–3:
- `ae mainn log een` — This is my house.
- `Main ab.` — My water.
- `Thai av.` — Your water.

The new pair holds `Ee mainn ... een` constant while changing the noun
(`av` / `nagn`). This supports treating the two as parallel sentence
examples, but does not yet establish the precise grammatical role or
meaning range of `Ee`, `mainn`, or final `een`. Preserve `Ee` exactly;
do not normalize it to earlier `ae` without speaker confirmation.

## Cross-round working hypotheses (not confirmed rules)

- `man`, `tho`, `aan`, `ma`, and `Sha kul` occur in subject positions
  with different English person/number meanings. Capitalization is retained
  as supplied and may or may not reflect pronunciation.
- Motion examples show positive `rog` and negative `narog-` forms, but
  negation morphology is not yet segmented.
- Eating examples show `warag` in progressive constructions and
  `waranga/warage/warange/warangu` in simple-present translations.
  These may be related forms; do not impose a paradigm yet.
- Possessive examples include `mainn` and `Main`; the demonstratives
  `ae` and `Ee` must remain distinct until checked.
- The Round 3 correction `ma shuzagun` remains authoritative.

## Current implementation boundary

These observations support a speaker corpus and hypotheses for further
elicitation, not yet reliable finite-state morphology or transfer rules.
Do not relabel the Kurdish scaffold or claim a working translator until
Balochi monolingual resources, bilingual entries, transfer rules, and tests
are implemented and built.

## Next elicitation targets

Continue with short everyday sentences that distinguish person, number,
tense/aspect, negation, and demonstratives. Ask the speaker in ordinary
English, and retain exact raw answers before proposing any standardized
spelling or grammatical segmentation.
