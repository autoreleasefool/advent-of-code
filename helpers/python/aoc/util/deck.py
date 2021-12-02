class Deck:
    def __init__(self, size=52):
        self.size = size
        self.cards = list(range(size))

    def __str__(self):
        return " ".join([str(i) for i in self.cards])

    def position_of_card(self, n):
        return self.cards.index(n)

    def cut(self, n):
        self.cards = self.cards[n:] + self.cards[0:n]

    def reverse(self):
        self.cards.reverse()

    def deal(self, n):
        from_pos = 0
        to_pos = 0
        new_cards = self.cards[:]
        while from_pos < self.size:
            new_cards[to_pos] = self.cards[from_pos]
            to_pos = (to_pos + n) % self.size
            from_pos += 1
        self.cards = new_cards
