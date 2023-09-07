# link para as stopwords utilizadas neste exercício
# https://gist.github.com/sebleier/554280

import sys

def get_stopwords(filepath: str) -> set[str]:
    stopwords: set[str]
    with open(filepath, 'r') as file:
        stopwords = set([x.removesuffix('\n') for x in file.readlines()])

    return stopwords

def remove_stopwords_from_text(words: dict[str, int], stopwords: set[str]) -> dict[str, int]:
    return {word: count for word, count in words.items() if word not in stopwords} 

def main():
    if len(sys.argv) < 2:
        print('usage: python3 ex2.py <text_filename>.txt <stopwords_filename>.txt')
        return

    filename = sys.argv[1]
    text: list[str]
    with open(filename, 'r') as file:
        text = file.readlines()

    words: dict[str, int] = {}
    for line in text:
        for word in line.split():
            word = word.replace(',', '').replace('.', '')
            if word in words.keys():
                words[word] += 1
            
            else:
                words[word] = 1

    stopwords = get_stopwords(sys.argv[2])
    words = remove_stopwords_from_text(words, stopwords)

    print('\nWITHOUT STOPWORDS\n')
    print(words)

if __name__ == '__main__':
    main()
