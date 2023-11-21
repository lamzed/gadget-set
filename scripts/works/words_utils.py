import linecache
import random


def readline_count(file_name):
    with open(file_name, encoding="UTF-8") as f:
        return len(f.readlines())


def is_chinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fa5':
            return True
        return False


if __name__ == '__main__':
    file_path = "../../cncultrue/baijiaxing.txt"
    total_lines = readline_count(file_path)
    while True:
        index = random.randint(1, total_lines - 2)  # skip the first and last line
        xing = linecache.getline(file_path, index)
        if is_chinese(xing):
            break

    print(xing)
