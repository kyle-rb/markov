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
# remove certain things from text input
notations = ["(APPLAUSE)", "(CHEERS, APPLAUSE)", "(LAUGHTER)"]
for note in notations:
    inputText = inputText.replace(note, '')
# ------------------------ #


model = PostModel()
model.incentivize = [] # eg. Hillary, Mexico, etc.
data = model.parse(inputText) # cleans up text and adds internal annotations
print("INPUT TEXT PARSED\n")
model.readList(data) # model has now processed the data into a graph
print("MODEL CREATED FROM INPUT\n\n")

generator = PostGenerator(model.words) # pass model's data to generator
post = generator.generatePost()

print(post)
print("\n\nDONE\n")
if post == "": # error report type deal for debugging
    print(generator.model["<start>"])
    totalWeight = 0
    for toWord in generator.model["<start>"][1]:
        totalWeight += generator.model["<start>"][1][toWord]
    print(generator.model["<start>"][0], totalWeight)
