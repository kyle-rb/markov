import random

class PostGenerator:
    def __init__(self, inputDict):
        self.model = inputDict

    def nextWord(self, word):
        wordInfo = self.model[word]
        wordWeight = wordInfo[0]
        choice = random.randrange(wordWeight)
        for toWord in wordInfo[1]:
            choice -= wordInfo[1][toWord]
            if choice <= 0:
                return toWord
        return "<stop>"

    # TODO: remove <stop> from end
    def generatePost(self):
        currentWord = "<start>"
        postString = ""
        while currentWord != "<stop>":
            currentWord = self.nextWord(currentWord)
            if currentWord != "<stop>":
                postString += currentWord + ' '
        return postString
