#packages needed: spacy --> need english version --> py -m spacy download en
import spacy

nlp = spacy.load('en_core_web_sm')

document = nlp(
    "In 1994, Tim Berners-Lee founded the World Wide Web Consortium (W3C), devoted to developing web technologies. Stanford Federal Credit Union was the first financial institution to offer online Internet banking services. In 1996, OP Financial Group, also a cooperative bank, became the second online bank in the world and the first in Europe."
)

for entity in document.ents:
        print(entity.text, ":", entity.label_)

from pathlib import Path

doctument1 = nlp(Path('RomeoAndJuliet.txt').read_text())
doctument2 = nlp(Path('EdwardTheSecond.txt').read_text())

print(doctument1.similarity(doctument2))
