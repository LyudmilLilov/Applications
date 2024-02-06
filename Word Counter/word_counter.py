def count_words(text):
    words = text.split()
    return len(words)

text = input("Enter some text: ")
word_count = count_words(text)
print(f"Word count: {word_count}")