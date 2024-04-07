from pwn import *
import ast
def parse_data(data):
    dat=list()
    for i in data:
        dat.append(ast.literal_eval(''.join(i.split(' ')[4:])))
    return dat
    
def solve(a, b, c):
    return 10 * (a * pow(10, c-1, b) % b) // b

r = remote('157.245.147.89', 29912)

for i in range(7):
    r.recvuntil(b'\n').decode()

data=list()

for i in range(50):
    data.append(r.recvuntil(b'\n').decode()[:-1])
    print(data[i])


dat=parse_data(data)
print(dat)
print(dat[0][0])
print(type(dat[0][1]))



# while True:
#     print(data)
#     data = data.split(' ')
#     result = solve(int(data[0]), int(data[1]), int(data[2]))
#     print(result)
#     r.send(f'{str(result)}\n'.encode())
#     data = r.recvuntil(b'\n').decode()