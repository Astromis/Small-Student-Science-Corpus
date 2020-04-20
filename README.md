# Paragraph corpus

## Overview

This Russian corpus is annotated in the way to investigate the paragraph segmentation techniques.  The scheme is pretty simple. The source text are articles from various unindexed by Russian Index of Scientific Cites magazines, so the scientific values of these articles is in doubt, but it's still text written by humans.

## Tag structure
* <pa></pa> bounds the paragraphs
* <p> bounds the end of page.
* <h></h> bounds the header of the articles
* <en></en> English abstract(TBD).
* <l><l> list lines (TBD)

Corpus contains 24210 paragraphs (including lists as a paragraph)
## TODO list

- [ ] Add new tags
- [ ] Provide a corpus statistic
- [ ] Provide a script for dividing corpus on train and test
- [x] Make a verification of corpus. (Pay attention on pieces of corpus where text flows like symbol stream)
