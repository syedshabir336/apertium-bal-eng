# Round 1 and Round 2 speaker data and research notes

## Data provenance

Round 1 examples are stored in `data/speaker-corpus-round1.tsv`.
Round 2 examples are stored in `data/speaker-corpus-round2.tsv`.
All twenty English prompts and Balochi equivalents were supplied by a
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
  The article identifies Sulaimani as a Balochi dialect and associates it
  with Eastern/Northern/Rindi naming in earlier descriptions. Its abstract
  places speakers in Sindh, Punjab, and eastern Balochistan.
- University of Arizona, Iranian Languages, “Balochi”:
  https://iranian-languages.arizona.edu/balochi
  Provides a broad morphosyntactic overview and warns, by its dialectal
  description, against assuming one dialect's paradigm represents all Balochi.
- Cambridge, “Progressive constructions in different Balochi dialects from
  a diachronic and an areal linguistic point of view”:
  https://doi.org/10.1017/S0041977X24000144
  Documents multiple progressive constructions across Balochi varieties.
- Uppsala University's Balochi Language Project:
  https://www.uu.se/en/department/linguistics-and-philology/research/proj/the-balochi-language
  Documents broad dialect groupings and dialect variation.

These references establish a useful research baseline; they do not
independently verify every speaker-provided Sulaimani word or construction.
General Balochi paradigms must not be copied into the Sulaimani grammar
without matching evidence.

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

The four elicited sentences are:

- `man rog aan` — I am going.
- `tho rog ee` — You are going (singular).
- `aan rog een` — He is going.
- `aan rog een` — She is going.

The sequence `rog` remains constant while the final forms vary
(`aan`, `ee`, `een`). This is consistent with a person/number-marked
finite element or copula-like ending, but segmentation is not established.
The identical third-person forms for “he” and “she” are consistent with
Balochi's widely described lack of grammatical gender, but this must be
checked in the target variety and against further pronouns. Do not create
separate masculine/feminine forms from these examples.

### Past

- `man shuzagan` — I went.

This is a single past example. The stem, tense marker, and person marking
cannot yet be segmented confidently. Elicit other persons and a contrasting
present form before building a past paradigm.

### Negation

- `man av aa na lotan` — I do not want water.

Compare with Round 1 `man av a lotan` — I want water. The added sequence
`aa na` occurs before `lotan` in the negative example. Its segmentation
and exact function are unknown. Do not assume it is a single negation prefix;
it may include an aspectual/modal particle or other element.

### Demonstratives and possession

- `ae mainn log een` — This is my house.
- `aan thai log een` — That is your house.

These examples suggest candidate demonstrative/possessive forms:
`ae`, `aan`, `mainn`, and `thai`. The same final `een` occurs in both
copular sentences. Confirm each form in isolation and in contrasting
possessor/demonstrative contexts before assigning tags.

### Eating and imperative

- `ma nagn warag un` — We are eating food.
- `mana av aa de` — Give me water.

The eating example suggests `nagn` as food and `warag` as a candidate
verbal/infinitival form, with `un` at the end. The imperative example
suggests `mana` as “to me/me”, `av` as water, and `de` as “give”, but
the precise syntax and morphology are not yet established.

## Cross-dialect caution from research

Published descriptions of Balochi report no grammatical gender in the
language generally, but case marking, pronoun forms, tense alignment, and
progressive constructions vary by dialect. Cambridge's comparative work
specifically documents multiple progressive strategies. These findings make
the speaker's identical “he/she” sentence a plausible pattern, but they do
not license importing a standard paradigm into this dialect.

## Next elicitation targets

Next test the same verbs across person and number, and separate the elements
in the negative and possessive constructions. Ask for short, natural
sentences, preserve raw speaker spellings, and only then propose a canonical
orthography and paradigms.
