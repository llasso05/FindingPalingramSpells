from functions.loader import load_dictionary

word_list = load_dictionary('greenteapress.txt')


# find word-pair palingrams

def find_palingrams():
    # Finde dictionary Palingrams
    pali_list = []
    for word in word_list:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in word_list:
                    pali_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in word_list:
                    pali_list.append((rev_word[:end-i], word))
    return pali_list

palingram = find_palingrams()
palingram_sorted = sorted(palingram)

print(f'\n Number of palingrams = {len(palingram_sorted)}\n')
for first, second in palingram_sorted:
    print("{first} {second}")

                 
