hangs = [
"    _________\n    |/      |\n" + "    |\n" * 7 + "____|____",
"    _________\n    |/      |\n    |       O\n" + "    |\n" * 6 + "____|____",
"    _________\n    |/      |\n    |       O\n" + "    |       |\n" * 2 + "    |\n" * 4 + "____|____",
"    _________\n    |/      |\n    |       O\n    |      /|\n    |       |\n" + "    |\n" * 4 + "____|____",
"    _________\n    |/      |\n    |       O\n    |      /|\\\n    |       |\n" + "    |\n" * 4 + "____|____",
"    _________\n    |/      |\n    |       O\n    |      /|\\\n    |       |\n    |      /\n" + "    |\n" * 2 + "____|____",
"    _________\n    |/      |\n    |       O\n    |      /|\\\n    |       |\n    |      / \\\n" + "    |\n" * 2 + "____|____"
]
reveal = []
goodInputs = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
dead = False
win = False
wrongs = []
def printBoard(reveal, wrong, good):
    global hangs, dead
    print(hangs[len(wrong)])
    if len(wrong) == 6:
        dead = True
    wrong2 = ""
    reveal2 = ""
    good2 = ""
    for i in reveal:
        reveal2 += " " + i
    for i in wrong:
        wrong2 += " " + i
    for i in good:
        good2 += " " + i
    print("\n" + reveal2 + "\n\nIncorrect letters:" + wrong2 + "\nAvailable letters:" + good2 + "\n")
input("Type your word into hangmanInput.txt and save the file (ctrl + s). Once you do that, press Enter\n")
wordDefault = open("hangmanInput.txt").read().upper().replace(" ", "").replace("\n", "")
word = [char for char in wordDefault]
for i in range(len(word)):
    reveal.append("_")
printBoard(reveal, wrongs, goodInputs)
while not dead:
    goodInput = False
    x = 0
    while not goodInput:
        inp = input("What letter do you wanna input?\n").upper()
        if goodInputs.count(inp) == 1:
            goodInput = True
    for i in range(len(word)):
        if word[i] == inp:
            reveal[i] = inp
            x += 1
            if reveal == word:
                win = True
    if x == 0:
        wrongs.append(inp)
    goodInputs.remove(inp)
    printBoard(reveal, wrongs, goodInputs)
    if win:
        print("Congrats! You won!\nThe word was " + wordDefault + "!")
        break
    if dead:
        print("Oh no, you lost!\nThe word was " + wordDefault + "!")
        break
input("Press enter to close this program\n")