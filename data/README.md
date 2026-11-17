# Balochi lexical data staging area

This directory is reserved for reviewed Suleimani Balochi data. Do not place
Kurdish entries here, and do not copy entries from the legacy `kmr` resources
without independent Balochi verification.

## Bilingual TSV schema

`bal-eng-lexicon.tsv` is a UTF-8, tab-separated staging file. Its header is:

```text
bal_lemma	bal_pos	eng_lemma	sense	dialect	source	reviewer	status
```

- `bal_lemma`: canonical Latin/Roman Suleimani Balochi lemma (Unicode NFC).
- `bal_pos`: project lexical category, to be mapped to the final Apertium tagset.
- `eng_lemma`: English equivalent; separate senses should be separate rows.
- `sense`: short gloss or sense identifier.
- `dialect`: variety restriction; use `suleimani` when verified for the target.
- `source`: traceable citation, corpus identifier, or elicitation record.
- `reviewer`: native-speaker/reviewer identifier or documented review record.
- `status`: `draft` or `reviewed`.

No entries are pre-populated. This is intentional: an empty template is safer
than relabelling Kurdish words as Balochi. Only reviewed, traceable entries
should be converted into the production Apertium dictionary.
