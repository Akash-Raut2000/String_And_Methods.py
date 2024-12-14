# String: Slicing, Indexing, and Common Methods

# Sample string
sample_string = "  Hello, Python World!  "

# 1. Indexing
print("Original String:", sample_string)
print("First character:", sample_string[0])         # Accessing the first character
print("Last character:", sample_string[-1])        # Accessing the last character
print("5th character:", sample_string[4])          # Accessing the 5th character

# 2. Slicing
print("Substring (0-5):", sample_string[0:5])       # Slicing characters from index 0 to 4
print("Substring (7 to end):", sample_string[7:])  # From index 7 to the end
print("Substring (start to 5):", sample_string[:5]) # From start to index 4
print("Substring (step 2):", sample_string[::2])   # Every second character

# 3. String Methods
# a. Strip (removes leading/trailing whitespace)
stripped_string = sample_string.strip()
print("Stripped String:", stripped_string)


# b. Uppercase and Lowercase
print("Uppercase:", stripped_string.upper())
print("Lowercase:", stripped_string.lower())

# c. Split (splits by spaces by default)
split_string = stripped_string.split()
print("Split String:", split_string)

# d. Join (joins list elements with a delimiter)
joined_string = "-".join(split_string)
print("Joined String:", joined_string)

# e. Replace
replaced_string = stripped_string.replace("Python", "Java")
print("Replaced String:", replaced_string)

# f. Find (returns the index of the first occurrence of a substring)
index_of_python = stripped_string.find("Python")
print("Index of 'Python':", index_of_python)

# g. Count (counts occurrences of a substring)
count_o = stripped_string.count("o")
print("Count of 'o':", count_o)

# h. Startswith and Endswith
print("Starts with 'Hello':", stripped_string.startswith("Hello"))
print("Ends with 'World!':", stripped_string.endswith("World!"))

# 4. Immutable Nature of Strings
# Strings are immutable, so modifications create new strings
new_string = stripped_string + " Let's learn more!"
print("New String:", new_string)

# 5. Check Membership
print("'Python' in string:", "Python" in stripped_string)
print("'Java' not in string:", "Java" not in stripped_string)
