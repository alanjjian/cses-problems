seq = input()
longest = 0
curr_len = 1
curr_letter = ''
for letter in seq:
    if curr_letter == letter:
        curr_len += 1
    if curr_letter != letter:
        curr_letter = letter
        curr_len = 1
    longest = max(longest, curr_len)
print(longest)