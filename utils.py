import json

def insert_carrage_by_idx(text, carrage_idx):
    c = 0
    prev = -1
    new_text = ''
    for i in carrage_idx:
        new_text += text[prev+1:i]
        new_text += "\n"
        prev = i
    return new_text

def read_dataset(path="dataset"):
    with open(f"{path}/corpus.txt") as f:
        texts = f.read().split("\n\n")
    
    with open(f"{path}/annotation.json") as f:
        annot = json.load(f)
    assert len(annot) == len(texts)
    return texts, annot