import nltk
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

import numpy
import pickle
import json
from ai_module.ai_module import brain

def train():   
    with open("training_data\\intents.json") as file:
        data = json.load(file)

    words = []
    labels = []
    docs_x = []
    docs_y = []

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            tokenize_words = nltk.word_tokenize(pattern)
            words.extend(tokenize_words)
            docs_x.append(tokenize_words)
            docs_y.append(intent["tag"])

            if intent["tag"] not in labels:
                labels.append(intent["tag"])

    words = [stemmer.stem(w.lower()) for w in words if w not in "?"]
    words = sorted(list(set(words)))
    labels = sorted(labels)

    training = []
    output = []
    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x):
        bag = []
        stem_words = [stemmer.stem(w) for w in doc]

        for w in words:
            if w in stem_words:
                bag.append(1)
            else:
                bag.append(0)
        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)

    training = numpy.array(training)
    output = numpy.array(output)
    
    with open("trained_data\\data.pickle", "wb") as f:
        pickle.dump((words, labels, training, output), f)

    model = brain(training, output)
    model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
    model.save("trained_data\\model.tflearn")
