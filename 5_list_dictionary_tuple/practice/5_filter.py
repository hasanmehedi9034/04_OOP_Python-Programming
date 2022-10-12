letters = ['a', 'e', 'i', 'o', 'u']

# sequence = input("name: ")
sequence = 'oomeheediiaa'

filtered = list(filter(lambda x: x in letters, sequence))

letter_count = list(map(lambda x: filtered.count(x), filtered))

# for i in range(len(filtered) - 1):
#     for j in range(i + 1, len(filtered)):
#         if filtered[i] == filtered[j]:
#             letter_count[j] = 0

# letter_count = list(filter(lambda x: x != 0, letter_count))
# filtered = list(set(filtered))

# vowel_list = dict(list(zip(filtered, letter_count)))
# vowel_list = dict(sorted(vowel_list.items()))

vowel_list = dict(zip(filtered, letter_count))
vowel_list = dict(sorted(vowel_list.items()))

for key, value in vowel_list.items():
    print(f'{key}->{value}')