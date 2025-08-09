text = "Hello World"

print(text.lower())         # hello world
print(text.upper())         # HELLO WORLD
print(text.find("World"))   # 6, finds the index of the first instance of the string


first_o = text.find("o")
second_o = text.find("o", first_o + 1)
print("Second 'o' at index:", second_o)
