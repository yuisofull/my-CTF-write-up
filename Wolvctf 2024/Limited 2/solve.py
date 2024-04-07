from tqdm import tqdm
from datetime import datetime
import random

def check(limit, i):
    char = []
    for cur in limit:
        random.seed(i + cur)
        if flag[i] == chr(correct[i] ^ random.getrandbits(8)):
            if cur not in char:
                sleep = random.randint(1, 60)
                char.append(cur + sleep)
    return char

start = int(datetime(2023, 12, 31, 0, 0, 0).timestamp())
end = int(datetime(2024, 1, 7, 0, 0, 0).timestamp())
correct = [192, 123, 40, 205, 152, 229, 188, 64, 42, 166, 126, 125, 13, 187, 91]
flag = 'wctf{'

char0 = []
for cur in tqdm(range(start, end + 1)):
    random.seed(cur)
    if flag[0] == chr(correct[0] ^ random.getrandbits(8)):
        if cur not in char0:
            sleep = random.randint(1, 60)
            char0.append(cur + sleep)

char1 = check(char0, 1)
char2 = check(char1, 2)
char3 = check(char2, 3)
char4 = check(char3, 4)

time_current = char4[-1]
for i in range(5, len(correct)):
    random.seed(i + time_current)
    flag += chr(correct[i] ^ random.getrandbits(8))
    sleep = random.randint(1, 60)
    time_current += sleep
print(flag)