# Suleimani Balochi language-pair design

## Purpose

Build a real Apertium translation pair between Suleimani Balochi and English.
The ISO 639-3 language identifier is `bal`; the pair mode names will be
`bal-eng` and `eng-bal`.

This document is a requirements checklist, not a claim that the linguistic
analysis below has already been completed.

## 1. Dialect boundary

Before implementing morphology or adding vocabulary, record:

- The exact community/region meant by "Suleimani Balochi".
- Whether the requested variety is a local Balochi variety associated with
  Suleimani/Sulaimani, and how speakers distinguish it from neighbouring
  Balochi varieties.
- Accepted endonyms and exonyms, including preferred Latin spelling.
- Whether the first release should accept variants from neighbouring Balochi
  varieties, and how those variants will be tagged.
- Native-speaker reviewers and sources for every nontrivial grammatical claim.

Do not infer that "Suleimani" means Sorani Kurdish, Kurmanji Kurdish, or the
Kurdish spoken in Sulaymaniyah. Balochi and Kurdish are distinct languages.

## 2. Orthography policy — Latin/Roman (selected)

The canonical script for the first implementation is **Latin/Roman**. All
dictionary lemmas, inflectional forms, transfer examples, and regression
fixtures must use this canonical representation.

The script choice is settled; the exact dialect-specific spelling inventory
is not. Before adding a large lexicon, native speakers must confirm:

- The canonical Latin grapheme for every vowel and consonant contrast in this
  Suleimani variety.
- Whether long vowels, aspiration, retroflexes, and other contrasts require
  diacritics or digraphs, and the exact spelling of each.
- Whether borrowed words retain source spelling or follow Balochi spelling.
- Word boundaries, clitics, compounds, capitalization, and punctuation.
- Accepted alternate spellings and the normalization rules that map them to
  canonical forms without merging distinct sounds or words.

Engineering defaults:

- Store source files as UTF-8 and normalize authored lexical data to Unicode
  NFC.
- Treat the canonical Latin spelling as the dictionary/generator output.
- Add alternate spellings as explicit, reviewed analysis-side variants;
  do not silently rewrite them when they may encode a phonemic distinction.
- Keep any future Arabic-derived-script transliteration in a separate
  conversion layer. It must not be mixed into the lexical dictionary or
  morphology rules.
- Include round-trip tests for normalization and every approved spelling
  variant.

No speculative transliteration table is imposed by this document. A Latin
script choice alone does not determine the correct Balochi grapheme inventory.

## 3. Balochi monolingual package

Create/use `apertium-bal` as the source of truth for Balochi lexical analysis
and generation. Its dictionary and tagset must be based on the selected
dialect, not copied from the existing `kmr` resources.

Required components:

- Monolingual dictionary (`.dix`) with reviewed lemmas and paradigms.
- Morphological analyzer and generator tests.
- Part-of-speech and morphosyntactic tagset.
- Constraint Grammar / disambiguation rules and a dialect-aware tagger model
  only when sufficient licensed corpus data exists.
- Regression examples for inflection, clitics, compounds, and spelling variants.

## 4. Bilingual lexicon

Each entry should record at least:

- Balochi lemma in canonical Latin spelling and lexical category.
- English equivalent(s), with sense distinctions where necessary.
- Inflectional paradigm or invariant status.
- Transitivity/valency and relevant grammatical features for verbs.
- Register, dialect restriction, source, reviewer, and confidence.
- A test sentence demonstrating the intended sense.

Do not bulk-relabel Kurdish lemmas as Balochi. Similar-looking words must be
independently verified.

## 5. Transfer architecture

Implement and test both directions independently:

- `bal-eng`: analyze Balochi, disambiguate, select lexical senses, transfer
  Balochi syntax to English, and generate English.
- `eng-bal`: analyze English, transfer English syntax to the selected
  Balochi variety, and generate Balochi forms.

Transfer rules must reflect attested Balochi agreement, tense/aspect/mood,
argument structure, negation, pronouns/clitics, noun phrase structure, and
word order. Do not assume Kurdish transfer rules apply.

## 6. Corpus and tests

Use only corpus material whose source and license/permission are recorded.
Build parallel, native-reviewed test sets for both directions. Include:

- Pronouns and person/number distinctions.
- Noun number, possession, and oblique/case marking where applicable.
- Present, past, imperative, negation, and common aspectual constructions.
- Transitive and intransitive clauses.
- Questions, modifiers, adpositions, coordination, and subordination.
- Common daily vocabulary and named entities.
- Dialect-specific forms and spelling variants.

Keep unknown-word, morphological-analysis, generation, and end-to-end
translation tests separate. A passing XML validator is not evidence of
translation quality.

## 7. Repository migration gates

The current repository still has `kmr`-named files and Kurdish linguistic
data. Do not switch `configure.ac`, `Makefile.am`, `modes.xml`, or test
fixtures to `bal` until their referenced Balochi resources and build
dependencies exist.

A release can be called a Suleimani Balochi translator only when:

1. No Kurdish dictionary, corpus, tagger model, or transfer rule is used as
   Balochi linguistic data.
2. Both `bal-eng` and `eng-bal` build and run.
3. The dialect and Latin orthography are documented and reviewed by speakers.
4. Both directions pass reproducible morphological and sentence-level tests.
5. Data sources, attribution, and licenses are documented.
