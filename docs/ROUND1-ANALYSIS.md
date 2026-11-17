# Round 1 speaker data and research notes

## Data provenance

The ten English prompts and their Suleimani Balochi equivalents in
`data/speaker-corpus-round1.tsv` were supplied by a native speaker during
Round 1 elicitation. The original Latin spellings and word boundaries are
preserved exactly as received. No automatic transliteration or spelling
correction has been applied.

The five initial lexical entries in `data/bal-eng-lexicon.tsv` are also
marked `speaker-provided-unreviewed`. These are seed data, not yet a
fully reviewed dictionary or a claim of standard orthography.

## External dialect references

- Hamid Ali Baloch (2023), “The Sulaimani Dialect of the Balochi Language:
  A Phonological Study,” *Makhz (Research Journal)* 4(4), 67–84,
  DOI: https://doi.org/10.47205/makhz.2023(4-IV)urdu-07.
  The article identifies Sulaimani as a Balochi dialect and associates it
  with Eastern/Northern/Rindi naming in earlier descriptions. Its abstract
  places speakers in Sindh, Punjab, and eastern Balochistan.
- Uppsala University's Balochi Language Project:
  https://www.uu.se/en/department/linguistics-and-philology/research/proj/the-balochi-language
  This project documents broad Eastern, Western, and Southern groupings,
  dialect variation, and separate orthography/grammar resources. Its general
  standard resources must not automatically replace this project's
  speaker-confirmed Sulaimani forms.

These references establish that Sulaimani Balochi is a legitimate dialect
target and that Balochi has substantial dialect variation. They do not
independently verify every Round 1 word or sentence.

## Initial observations (hypotheses only)

- `Salam` is supplied for a greeting; retain it as an elicited greeting.
- `baz minatwar` is supplied as a gratitude expression. Keep it as a
  multiword expression until its internal structure and spelling are
  confirmed.
- `av`, `nagn`, and `log` are supplied for water, food, and house.
  Do not replace them with forms from other Balochi varieties without
  speaker confirmation.
- The two “I am a ...” sentences share the initial sequence
  `man yak e` and end in `aan`, while the middle noun phrase differs.
  This suggests a useful agreement/identity construction to investigate,
  but the exact segmentation and grammatical role of each token remain
  unanalysed.
- The “What is your name?” and “Where are you going?” examples are retained
  as complete question examples. Their individual tokens are not yet assigned
  grammatical tags.
- `man av a lotan` is the speaker's example for “I want water.” Do not infer
  the lemma, conjugation, or word-boundary analysis of `a lotan` from this
  single sentence.

## Next elicitation targets

The next round should establish pronouns, person contrasts, negation,
possession, and verb forms using short everyday sentences. Each answer should
be stored in the speaker's own spelling first. A normalized spelling can be
proposed only after the sound/letter contrasts are understood and confirmed.
