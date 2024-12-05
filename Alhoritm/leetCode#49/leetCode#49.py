strs = ["автопромышленность", "ерлоатопыштсмоьнвн", "кофе", "офек","планер", "джунгарик" ]

grouped_words = {}

for word in strs:
    sorted_letters = "".join(sorted(word))
    if sorted_letters in grouped_words:
        grouped_words[sorted_letters].append(word)
    else:
        grouped_words[sorted_letters] = [word]

result = list(grouped_words.values())
print(result)

