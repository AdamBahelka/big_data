with open("stop_words.txt","r") as fin:
    csv = fin.read()
    fin.close()
s_words = csv.split()
with open("alice.txt","r") as fin:
    csv = fin.read()
a_special_words = csv.split()
a_words = []
import re
for word in a_special_words:
    new_word = re.sub(r"[^a-zA-Z0-9']", '', word)
    new_word = new_word.lower()
    a_words.append(new_word)
#print(a_special_words[:200])
#print(a_words[:200])
words = []
import collections
c = collections.Counter()
for word in a_words:
    if word not in s_words:
        words.append(word)
print(words)
most_common = collections.Counter(words).most_common(3)
print (most_common)


