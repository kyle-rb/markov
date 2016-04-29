# Holds a dictionary where keys are words and values are tuples of the word's 
# total weight plus a dictionary which contains the word and its associated 
# probability
class PostModel:
    def __init__(self, prevData = None):
        if prevData is None:
            self.words = {}
        else:
            self.words = prevData
        self.incentivize = []

    def addWord(self, word):
        if word not in self.words:
            self.words[word] = [0, {}]

    def addTransition(self, fromWord, toWord):
        if fromWord not in self.words:
            self.addWord(fromWord)
        self.words[fromWord][0] += 1 # increment word weight by 1
        if toWord in self.words[fromWord][1]:
            self.words[fromWord][1][toWord] += 1 # increment toWord weight
        else:
            self.words[fromWord][1][toWord] = 1 # initialize toWord with weight
        
        # for increased hilarity
        for word in self.incentivize:
            if toWord == word:
                self.words[fromWord][0] += 30
                self.words[fromWord][1][toWord] += 30

    # Removes punctuation from a large string, and splits it into a list
    # TODO: modify to make it so that periods get read as stops or something
    #       also something for exclamation and question marks, plus newlines
    #       maybe other stuff later
    def parse(self, text):
        punctuation = ",/<>?;:'\"[]{}`~!@#$%^&*()-_=+\\|" # add '\t' and '.'?
        for char in punctuation:
            text = text.replace(char, ' ')
        text = text.replace('\n', " <stop> <start> ") # also do this for '.'?
        list = text.split()
        return list

    def readList(self, list):
        prevWord = "<start>"
        for word in list:
            self.addTransition(prevWord, word)
            prevWord = word
        self.addTransition(prevWord, "<stop>")
        # to prevent empty posts:
        self.words["<start>"][0] -= self.words["<start>"][1]["<stop>"]
        self.words["<start>"][1]["<stop>"] = 0
