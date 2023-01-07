import random

num = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}
col = {'Club':'C', 'Heart':'H', 'Spade':'S', 'Diamond':'D'}


class Card:
    def __init__(self, c, n):
        self.number = num[n]
        self.color = col[c]

    def __add__(self, other):
        sum = self.number + other.number
        return sum

    def __str__(self):
        return str(self.number) + str(self.color)


class Cardsets:
    def create(self):
        sets = []
        for i in col:
            for j in num:
                sets.append(Card(i, j))
        return sets


a = Cardsets()
b = a.create()
c = random.sample(b, 4)
print("This is a black jack poker game.")
print("Here are your cards :", c[0], c[1], c[2], c[3])
formula = str(input("Please enter your formula."))
if eval(formula) == 21:
    print("You win.")
else:
    print("You lose.")
