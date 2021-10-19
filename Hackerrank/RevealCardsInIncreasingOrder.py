def deckRevealedIncreasing(self, deck):
    d = []
    deck.sort(reverse=True)
    for i in deck:
        if d:
            d.insert(0, d.pop())
        d.insert(0, i)
    return d


print(deckRevealedIncreasing([17,13,11,2,3,5,7]))
