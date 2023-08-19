def word_count(text):
    words = text.split()
    return len(words)

paragraph = input('Enter a paragraph: ')
count = word_count(paragraph)
print('Word count:', count)