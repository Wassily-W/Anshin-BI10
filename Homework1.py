text = input("Введите текст: ")

text = text.lower()
for ch in ",.!?;:":
    text = text.replace(ch, '')

words = text.split()

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

for word, count in sorted_words:
    print(word, count)
