repeat = int(input())
number = 0

def check(thisSet, thisList):
    for i in thisSet:
        check = 0
        last = -1
        while (check != thisList.count(i)):
            now = thisList.index(i,last+1)
            if check == 0:
                last = now
            elif now != last+1:
                return 0
            last = now
            check += 1
    return 1

def solve():   
    wordList = list(input())
    alphabet = set(wordList)
    if check(alphabet, wordList) == 1:
        return 1
    return 0

for x in range(repeat):
    number += solve()
print(number)