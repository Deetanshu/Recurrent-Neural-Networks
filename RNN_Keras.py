# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 12:10:09 2018

@author: deept
"""
#Imports
import numpy as np
from numpy import array
from pickle import dump
from keras.preprocessing.text import Tokenizer
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, LSTM, Embedding
from keras.callbacks import EarlyStopping, TensorBoard

#Loading document:
data = open('Data/kafka_sequences.txt').read()
lines = data.split('\n')
tokenizer = Tokenizer()
tokenizer.fit_on_texts(lines)
sequences = tokenizer.texts_to_sequences(lines)
vocab_size = len(tokenizer.word_index) + 1

sequences = array(sequences)
X, y = sequences[:,:-1], sequences[:,-1]
y = to_categorical(y, num_classes = vocab_size)
seq_length = X.shape[1]

#Defining model
model = Sequential()
model.add(Embedding(vocab_size, 50, input_length = seq_length))
model.add(LSTM(100, return_sequences=True))
model.add(LSTM(100))
model.add(Dense(100, activation='relu'))
model.add(Dense(vocab_size, activation = 'softmax'))
print(model.summary())

#Compiling
model.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])
tensorboard = TensorBoard(log_dir='./Graph', histogram_freq=0, batch_size=32, write_graph=True, write_images=True)
model.fit(X, y, batch_size=128, epochs=100, callbacks=[tensorboard])


#Saving Model
model.save('kafka.h5')
#Dumping tokenizer
dump(tokenizer, open('tokenizer.pkl', 'wb'))

