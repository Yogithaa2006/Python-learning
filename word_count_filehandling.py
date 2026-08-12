file= open("text.txt","w")
file.write("Python is a simple and easy language")
file.close()

file = open("text.txt","r")
content=file.read()
words=content.split()
print("no of words: ",len(words))

file.close()
print("FIle content:",content)

