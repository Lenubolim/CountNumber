import argparse
import re


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--file", "-f", help="the text file to be counted")
    args = argparser.parse_args()
    print("选择的文件为", args.file)
    funtion(args.file)


def funtion(path):
    total_cnt = 0
    with open(path, encoding='utf-8') as file:
        content = file.readlines()
        for line in content:
            temp = re.sub("[\[\]a-zA-Z0-9@.()（）？。，,“”：:_\"’'/=\-\\n、!]", ' ', line).replace(" ", "")
            total_cnt += len(temp)
    print("中文总字数：", total_cnt)


if __name__ == '__main__':
    main()
