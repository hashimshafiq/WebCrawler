import re
import urllib2
import collections
friendslist = []
def find(text):
	match = re.search(r"[^a-zA-Z](InitialChatFriendsList)[^a-zA-Z]", text)
	start = match.start(1) + 36
	fin = False
	while (start < len(text) and not fin):
		if text[start] == '}':
			fin = True
		elif text[start] == '"':
			aux = start
			start += 1
			while text[start] != '"':
				start += 1
			friendslist.append(text[(aux+1):(start-2)])
			start += 1
		else:
			start += 1

	return friendslist

text_file = open('friends.txt','r')
text = text_file.read()
hashim= find(text)

friendslist.count()

for i in hashim:
	url = "https://www.facebook.com/"+str(i)
	print(url)
	#print('\n')

