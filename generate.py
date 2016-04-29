from input import PostModel
from output import PostGenerator

inputFileNames = ["trump_aipac.txt",
                  "trump_foreign_policy.txt",
                  "trump_victory.txt",
                  "trump_announcement.txt"]
inputText = ""
for name in inputFileNames:
    inputFile = open(name)
    inputText += inputFile.read()

# ------------------------ #
notations = ["(APPLAUSE)", "(CHEERS, APPLAUSE)", "(LAUGHTER)"]
for note in notations:
    inputText = inputText.replace(note, '')
# ------------------------ #


model = PostModel()
model.incentivize = [] # eg. Hillary, Mexico, etc.
data = model.parse(inputText)
print("INPUT TEXT PARSED\n")
model.readList(data)
print("MODEL CREATED FROM INPUT\n\n")

generator = PostGenerator(model.words)
post = generator.generatePost()

print(post)
print("\n\nDONE\n")
if post == "":
    print(generator.model["<start>"])
    totalWeight = 0
    for toWord in generator.model["<start>"][1]:
        totalWeight += generator.model["<start>"][1][toWord]
    print(generator.model["<start>"][0], totalWeight)
