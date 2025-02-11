def isParenString(string):
    lparen = 0
    rparen = 0
    for i in string:
        if i=="(":
            lparen += 1
        elif i==")":
            rparen += 1
        if (lparen<rparen):
            return "NO"
    if (lparen!=rparen):
        return "NO"
    return "YES"


loop = int(input())
for i in range(loop):
    paren_string = input()
    print(isParenString(paren_string))