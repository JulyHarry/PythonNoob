import os

NOTE_PATH = "/Users/hang/Documents/Notes/"


def findNote(target):
    for filename in os.listdir(NOTE_PATH):
        if 'md' in filename and 'cloud' not in filename:
            with open(f'{NOTE_PATH}/{filename}', 'r', encoding='utf-8') as f:
                print_flag = True
                for rd in f.readlines():
                    if target in rd:
                        if print_flag:
                            print(filename)
                            print_flag = False
                        print('\t' + rd)


def find_no(no):
    for filename in os.listdir(NOTE_PATH):
        if 'md' in filename and 'cloud' not in filename:
            with open(f'{NOTE_PATH}/{filename}', 'r', encoding='utf-8') as f:
                print_flag = True
                for rd in f.readlines():
                    if rd.startswith(f'## [{no}.') and no in rd and f'[{no}]' not in rd:
                        if print_flag:
                            print(filename.strip())
                            print_flag = False
                        print('\t' + rd.strip())


if __name__ == '__main__':
    while True:
        target = input("请输入查询内容:  ")
        # find_no(target)
        findNote(target)
