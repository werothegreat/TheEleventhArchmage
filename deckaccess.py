import pickle

def save_deck(deck, deckname):
    outFile = open(deckname, 'wb')
    print('Saving your deck!')
    pickle.dump(deck, outFile)
    outFile.close()
    print('Deck saved!')

def open_deck(deckname):
    inFile = open(deckname, 'rb')
    print('Opening your deck!')
    deck = pickle.load(inFile)
    inFile.close()
    print('Deck opened!')
    return deck
