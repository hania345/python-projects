bad_words = ["star", "light", "sky"]
string = input("Enter in the chat:\n")
string = string.split(" ")
new_sentence = []

for word in string:
    if word in bad_words:
        new_sentence.append(len(word) * "*")
    else:
        new_sentence.append(word)

print("\nChat Box:\n")
print(" ".join(new_sentence))

