# Small Student Science Corpus

## Description

The small Russian corpus constructed from scientific papers written by high scholl and University entry course students. Be aware that texts are not cleaned from a redundant punctuation and noze. Some tasks that might be suitble for this corpus:

* Paragraph segmentation
* Keyword extraction
* Title generation
* Summurization
* Static word vector construction

The corpus consists of two files in `dataset` dir.
* corpus.txt - contains paper texts separated by double carrage
* annotation.json - file with the whole annotation that's represented as list of dicts

# What is annotatated here?

Each annotation contains next fields:
* header - the original paper title 
* abstract - the proiginal abstract provided by humans
* keys - the keywords written by humans
* carriage_idx - the list of the carriage indicies in a text representing paragraphs
* text_id - the sequential number of text in `corpus.txt` 

# Usage

Just use the `read_dataset` function from `utils.py`. You can also use `visualize` function in order to insert carrage in certain positions.

```
from utils import read_dataset, insert_carrage_by_idx

text_corp, annot = read_dataset()
insert_carrage_by_idx(text_corp[0], annot[0]["carriage_idx"])
```

# Corpus statistics

* 925165 of tokens in total
* 11.5 Mb of text
* 12659 paragraphs with mean sentenc count is 3.2 and std is 2.5
* 1160 papers with mean token length is 798 and std is 532
