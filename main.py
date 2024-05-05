from functions.loader import load_dictionary

palindromes = []

def main():
    dictionary = input("Please insert the dictionary file name ")
    word_list = load_dictionary(dictionary)
    for word in word_list:
        if  len(word) > 1 and word == word[::-1]:
            palindromes.append(word)
            print(f'the word "{word}" had been added to palindromes list\n')
    print(f'Total palindromes added {len(palindromes)}')
    print(*palindromes, sep='\n')


if __name__ == '__main__':
    main()




