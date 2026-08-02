text=input("Enter a word or sentence: ")
remove_space= text.strip()
replaced_text= remove_space.replace(" ","_")
split_text= remove_space.split()
vowels="aeiouAEIOU"
count=0
for character in remove_space:
    if character in vowels:
        count=count + 1

if text == text[::-1]:
    result="Yes, it is a palindrome"
else:
    result="no, it is not a palindrome"

print("-------Display Results-------")
print("Original text: {}".format(text))
print("Text using strip(): {}".format(remove_space))
print("Text using replace:{}".format(replaced_text))
print("Text using split():{}".format(split_text))
print("vowels:{}".format(count))
print("Palindrome text:{}".format(result))