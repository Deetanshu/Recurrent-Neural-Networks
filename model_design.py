# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 12:28:38 2018

@author: deept
"""
import string

def load_doc(filename):
    file = open(filename, 'r')
    text = file.read()
    file.close()
    return text

def clean_doc(doc):
    doc = doc.replace('--',' ')
    tokens = doc.split()
    table = str.maketrans('','', string.punctuation)
    tokens = [w.translate(table) for w in tokens]
    tokens = [word for word in tokens if word.isalpha()]
    tokens = [word.lower() for word in tokens]
    return tokens

def save_doc(lines, filename):
    data = '\n'.join(lines)
    file = open(filename, 'w')
    file.write(data)
    file.close()

filename='data/kafka.txt'
doc = load_doc(filename)
print(doc[:200])



tokens = clean_doc(doc)
print(tokens[:200])
print("Total tokens: %d", len(tokens))
print("Unique tokens: %d", len(set(tokens)))
length = 50+1
sequences = list()
for i in range(length, len(tokens)):
    seq = tokens[i-length:i]
    line = ' '.join(seq)
    sequences.append(line)
print("Total Sequences: ", len(sequences))

out_filename = 'data/kafka_sequences.txt'
save_doc(sequences, out_filename)