
wordFile = open("words.txt", "r")
wordList = wordFile.readlines()

for i in range(len(wordList)):
    wordList[i] = wordList[i].strip()

centre = str.lower(input("Enter the centre letter: "))
outer = str.lower(input("Enter the other letters: "))
letters = centre + outer
answers = []
valid = False

for i in range(len(wordList)):
    valid = False
    if(centre in wordList[i]):
        valid = True
        for j in range(len(wordList[i])):
            if(wordList[i][j] not in letters):
                valid = False
    if(valid):
        answers.append(wordList[i])

print(answers)
print(len(answers))
