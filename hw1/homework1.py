# rebecca (marks) leopold, 2017
# emoji haikus
import sys
import random

rawEmoji = open("emojinames.txt")
readEmoji = rawEmoji.read()
rawEmoji.close()

skin = 'skin tone'
skinTone = []
poem = []
one = []
two = []
three = []

# find all emoji names that include the words 'skin tone'
# put them in a list

for lines in readEmoji.split('\n'):
	if skin in lines:
		skinTone.append(lines)

for i in range(5):
	words = random.choice(skinTone)
	# poem = random.sample(skinTone, words)
	# print ' || '.join(poem)
	one.append(words)

for words in range(7):
	words = random.choice(skinTone)
	two.append(words)

for words in range(5):
	words = random.choice(skinTone)
	three.append(words)

for i in one:
	print i
print "\n"
for i in two:
	print i
print "\n"
for i in three:
	print i
