data = input().split(chr(92))
i = len(data)
last_word = data[i-1].split('.')
print(f"File name: {last_word[0]}")
print(f"File extension: {last_word[1]}")