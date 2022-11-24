with open("alice.txt","r") as fin:
    csv = fin.read()
csv
chapters = csv.split('CHAPTER')
chapters = chapters[1:]
i = 1
for chapter in chapters:
    with open('chapter'+ str(i)+'.txt', 'w') as f:
        f.write(chapter)
        f.close()
    i += 1
