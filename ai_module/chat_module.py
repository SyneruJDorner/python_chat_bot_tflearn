try:
    import nltk
    from nltk.stem import PorterStemmer
    stemmer = PorterStemmer()

    import numpy
    import pickle
    import random
    from ai_module.ai_module import brain
    import json
except ImportError:
    pass

def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    tokenized_words = nltk.word_tokenize(s)
    tokenized_words = [stemmer.stem(word.lower()) for word in tokenized_words]

    for tokenized_word in tokenized_words:
        for i, w in enumerate(words):
            if w == tokenized_word:
                bag[i] = 1

    return numpy.array(bag)

def chat():
    with open("training_data\\intents.json") as file:
        data = json.load(file)

    with open("trained_data\\data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)

    model = brain(training, output)
    model.load("trained_data\\model.tflearn")

    print("start talking with the bot! (type 'quit' to stop)")
    while True:
        inp = input("You: ")
        if (inp.lower() == "quit"):
            break

        results = model.predict([bag_of_words(inp, words)])[0]
        results_index = numpy.argmax(results)
        tag = labels[results_index]
                
        if results[results_index] > 0.7:
            for tg in data["intents"]:
                if tg["tag"] == tag:
                    responses = tg['responses']
            print(random.choice(responses))
        else:
            print("I didn't get that, try again.")