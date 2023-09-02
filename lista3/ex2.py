import sys

def get_stopwords(filepath: str) -> set[str]:
    stopwords: set[str]
    with open(filepath, 'r') as file:
        stopwords = set(file.readlines())

    return stopwords

def remove_stopwords(words: dict[str, int], stopwords: set[str]):
    result = {}
    for word in words:
        if word not in stopwords:
            print(word)
            result[word] = words[word]

    words = result

def main():
    if len(sys.argv) < 2:
        print('usage: python3 ex2.py [filename].txt')
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

    print(words)
    
    print('WITHOUT STOPWORDS\n')
    remove_stopwords(words)
    print(words)

if __name__ == '__main__':
    main()
