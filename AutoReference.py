file = open("sample.txt", "r", encoding="UTF-8")
s = file.read()

arr = s.split(':')

topics = []
links = []
authors = []
count = 0

for i, j in enumerate(arr):
    cache = []
    if 'Title' in j:
        if arr[i+1] != None:
            topics.append(arr[i+1].replace("\n", " "))

    if 'Authors' in j:
        if arr[i+1] != None:
            authors.append(arr[i+1].replace("\n", " "))

    if 'References' in j:
        if arr[i+1] != None:
            links.append(
                ((arr[i+1]+":"+arr[i+2]).replace("\n", " ")).split(' ')[1])


print(links)
print(len(links))

s = ""
for i in range(30):
    s += str(i+1)+"."
    s += authors[i]+". "
    s += topics[i]+". "
    s += "Link: "+links[i]+"."
    s += "\n\n"

print(s)
fileWrite = open("references.txt", "w")
fileWrite.write(s)
fileWrite.close()
file.close()
