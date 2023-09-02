import sys

def main():
    if len(sys.argv) < 2:
        print('usage: python3 ex1.py [filename].txt')
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

if __name__ == '__main__':
    main()
