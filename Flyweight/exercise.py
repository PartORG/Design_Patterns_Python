"""
Flyweight Coding Exercise
You are given a class called Sentence ,
 which takes a string such as 'hello world'.
 You need to provide an interface such that
 the indexer returns a flyweight that can be used
 to capitalize a particular word in the sentence.

Typical use would be something like:

sentence = Sentence('hello world')
sentence[1].capitalize = True
print(sentence)  # writes "hello WORLD"
"""


class WordFlyweight:
    def __init__(self, word):
        self.word = word
        self.capitalize = False

    def __str__(self):
        if self.capitalize:
            return self.word.upper()
        return self.word


class Sentence:
    def __init__(self, plain_text):
        self.words = plain_text.split()
        self.flyweights = {}

    def __getitem__(self, index):
        if index not in self.flyweights:
            self.flyweights[index] = WordFlyweight(self.words[index])
        return self.flyweights[index]

    def __str__(self):
        return ' '.join(str(self.flyweights.get(index, WordFlyweight(word))) for index, word in enumerate(self.words))


if __name__ == '__main__':
    print('Solution')
    sentence = Sentence('hello world')
    sentence[1].capitalize = True
    print(sentence)  # Output: "hello WORLD"
