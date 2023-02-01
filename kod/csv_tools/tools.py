import random
def get_csv(file_name,enc='utf-8',div=';'):
    return [line.strip().split(div) for line in open(file_name,encoding=enc)]
def print_csv(data):
    for d in data:
        print(d)