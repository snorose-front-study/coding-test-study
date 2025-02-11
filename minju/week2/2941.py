croatian = ["dz=","c=","c-","d-","lj","nj","s=", "z="]

word = input()
count = 0
for i in croatian:
    length = len(i)
    n = word.find(i)
    while n!=-1:
        word = word[:n] + " "*length + word[n+length:]
        count += 1
        n = word.find(i)
word = word.replace(" ","")
print(count + len(word))