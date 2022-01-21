
wordFile = open("words.txt", "r")
wordList = wordFile.readlines()

for i in range(len(wordList)):
    wordList[i] = wordList[i].strip()

letters = str.lower(input("Enter the centre letter: "))
letters += str.lower(input("Enter the other letters: "))
answers = []
pangram = []
valid = False

for i in range(len(wordList)):
    valid = False
    if(letters[0] in wordList[i] and len(wordList[i]) > 3):
        valid = True
        for j in range(len(wordList[i])):
            if(wordList[i][j] not in letters):
                valid = False
    if(valid):
        answers.append(wordList[i])

for i in range(len(answers)):
    pan = True
    for j in range(7):
        if(letters[j] not in answers[i]):
            pan = False
    if(pan):
        pangram.append(answers[i])



for i in range(len(answers)):
    print(answers[i])

print(pangram)
