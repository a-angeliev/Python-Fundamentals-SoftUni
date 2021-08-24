data = input().split()
result = 0
word_1 = data[0]
word_2 = data[1]
min_len = min(len(word_2), len(word_1))

for i in range(min_len):
    result += ord(word_1[i])*ord(word_2[i])

largest_word = word_2 if len(word_2)>len(word_1) else word_1
max_len = max(len(word_2), len(word_1))
for i in range(min_len,max_len):
    result += ord(largest_word[i])

print(result)