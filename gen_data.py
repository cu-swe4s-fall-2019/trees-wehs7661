import random
import string

def main():
    """
    This program generate rand.txt and sorted.txt, which contain 10000
    key/value pairs in a random and sorted manner, respectively.
    """
    file1 = open('rand.txt', 'w')
    file2 = open('sorted.txt', 'w')

    for i in range(10000):
        key = random.randint(1, 100000)
        file1.write(str(key) + ' ')
        file2.write(str(i) + ' ')
        word_len = random.randint(1, 10)
        for j in range(word_len):
            file1.write(random.choice(string.ascii_letters))
            file2.write(random.choice(string.ascii_letters))
        file1.write('\n')
        file2.write('\n')

if __name__ == '__main__':
    main()







