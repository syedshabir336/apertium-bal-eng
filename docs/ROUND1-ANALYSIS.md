# Speaker elicitation and research notes: Rounds 1–5

## Data provenance

- Round 1: `data/speaker-corpus-round1.tsv`
- Round 2: `data/speaker-corpus-round2.tsv`
- Round 3: `data/speaker-corpus-round3.tsv`
- Round 4: `data/speaker-corpus-round4.tsv`
- Round 5: `data/speaker-corpus-round5.tsv`

All speaker examples are native-speaker elicitation. Original Latin spellings,
word boundaries, capitalization, and punctuation are preserved, except where
the speaker explicitly corrected an entry. No automatic transliteration or
spelling correction has been applied. Round 5 includes a follow-up answer
for “They do not eat food”; its fifth prompt/form mismatch remains flagged.

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
This is only a descriptive observation: do not yet segment these forms
into stem and suffix or assume exact ending boundaries.

These examples contrast with Round 2/3 progressive examples containing
`warag` (e.g. `Ma nagn warag aan`). More examples are needed before
defining a tense/aspect rule.

### Negative motion

- `Man narogan.` — I am not going.
- `Tho naroge.` — You are not going (one person).

Compare with positive motion:
- `man rog aan` — I am going.
- `tho rog ee` — You are going (one person).

The negative examples contain `narog-` on the surface where positive
examples contain `rog`. The exact boundary and relation between `na`,
`naro`, and `rog` are not established.

### Demonstrative and possessive noun phrases

- `Ee mainn av een.` — This is my water.
- `Ee mainn nagn een.` — This is my food.

Compare with `ae mainn log een` — This is my house. Preserve `Ee`
distinct from earlier `ae` until the speaker confirms their relationship.

## Round 5 observations (hypotheses only)

Round 5 is recorded in `data/speaker-corpus-round5.tsv`.

### Negative eating forms

- `Ma nagn na waranga.` — I do not eat food.
- `Tho nagn na warage.` — You do not eat food (one person).
- `Aan nagn na warage.` — He does not eat food.
- `Maa nagn na warangu.` — We do not eat food.
- `Aan nagn na warangan.` — They do not eat food. (confirmed in follow-up)

Across these five confirmed negative examples, `nagn na` occurs before
the eating form. This supports testing `na` as a negative element in this
construction, but do not generalize it to all clauses or assume its exact
grammatical scope yet. The positive Round 4 forms
(`Man nagn waranga`, `tho nagn warage`, `aan nagn warange`,
`ma nagn warangu`) offer a comparison. Note the speaker's exact `Maa`
in Round 5 versus `ma` in Round 4; do not normalize the difference.

### Plural “they” and prompt/form mismatch

The fifth Round 5 response was supplied against the prompt “They eat food”
as exactly `Aan nagn na warangan.`. The speaker subsequently supplied
the same exact form as the answer to “They do not eat food”:
`Aan nagn na warangan.` This follow-up is recorded separately as R5-06
and confirms that this form means “They do not eat food” in this context.

The original R5-05 entry remains unchanged and flagged
`speaker-provided-needs-meaning-confirmation`; do not treat it as a
confirmed positive (“They eat food”) translation. The positive plural
eating form is still needed. Round 3 contains `Aan rog an` for “They are
going”, but that does not establish the positive simple-present form.

### Demonstrative and possessive noun phrases

- `Aa mai av een.` — That is my water.
- `Aa mai nagn een.` — That is my food.

These two parallel examples preserve `Aa` and `mai` exactly. Compare
with Round 4 `Ee mainn av een` / `Ee mainn nagn een`, and earlier
`ae mainn log een`. The differences `Aa` vs `Ee`, and `mai` vs
`mainn`, may be meaningful or may reflect spelling variation; no
normalization or morphological segmentation should be applied without
speaker confirmation.

## Cross-round working hypotheses (not confirmed rules)

- Subject forms include `man`, `Man`, `ma`, `Maa`, `tho`, `Tho`,
  `aan`, `Aan`, and `Sha kul`. Preserve case and spelling as supplied.
- Motion examples show positive `rog` and negative `narog-` forms, but
  negation morphology is not yet segmented.
- Eating examples show `warag` in progressive constructions and
  `waranga/warage/warange/warangu` in simple-present translations.
  Round 5 supplies negative forms `nagn na waranga/warage/warangu/warangan`.
  The positive plural form remains unelicited.
- Possessive/demonstrative examples include `mainn`, `Main`, `mai`,
  `ae`, `Ee`, and `Aa`; keep them distinct until confirmed.
- The Round 3 correction `ma shuzagun` remains authoritative.
- The Round 5 form `Aan nagn na warangan` is confirmed for the negative
  “They do not eat food”; it is not confirmed for the positive prompt.

## Current implementation boundary

These observations support a speaker corpus and hypotheses for further
elicitation, not yet reliable finite-state morphology or transfer rules.
Do not relabel the Kurdish scaffold or claim a working translator until
Balochi monolingual resources, bilingual entries, transfer rules, and tests
are implemented and built.

## Next elicitation targets

Elicit the positive plural “They eat food” form, and continue short everyday
sentences that distinguish person, number, tense/aspect, negation, and
demonstratives. Retain exact raw answers before proposing standardized
spellings or grammatical segmentation.
