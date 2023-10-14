
name = "Nagashree"
print(name.upper())
print(name.lower())
print(name.swapcase())
print(name.startswith('N'))
print(name.startswith('s'))
print(name.endswith('e'))
print(name.count('s'))
print(name.count('e'))
print(name.index('g'))
print(name.index('e'))
print(name.isdigit())
print(name.isalpha())
print(name.isspace())
print(name.index('s'))

print("slice")
print(name[1:4])


print(name.strip('s'))

forstrip ="                       my name is                        "
print(forstrip)

print(forstrip.strip())
print(forstrip.lstrip())
print(forstrip.rstrip())

mystring="my|name|is"
print(mystring.split('|'))

word ='hello'
j_word='+'.join(word)
print(j_word)

raw_string = r"This is a raw string. It ignores escape characters like \n and \t."

print(raw_string)

file_path = r"C:\Users\Administrator\Pictures\Screenshots"
print(file_path)


name="shree"
age = 22

print(f"Hello {name} you are {age} years of age")

print(f"heyyyy {age} me {name}  ee")


