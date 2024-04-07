from pwn import *
io = process(["python3", "server.py"])
# io = remote("157.245.147.89" , 20098)
sla = io.sendlineafter 
sa = io.sendafter 
sl = io.sendline 


def hamming_dst_num(a, b):
    return sum([1 if i == "1" else 0 for i in bin(a ^ b)[2:]])

def hamming_distance_list(a, b): #hamming distance, a and b are lists
    return sum([i != j for i, j in zip(a,b)])

def int2bool_arr(state, N): #N: length
    return [int(i) for i in bin(state)[2:].zfill(N)]


def bool_arr2int(arr):
    return int("".join("1" if i else "0" for i in arr), 2)

def gadget(idx, val):
    return f"( sheep[{idx}] == {val} )"

def gadget_of_state(state):
    return "( " + " and ".join([gadget(idx, i) for idx, i in enumerate(state)]) + " )"

def gadget_of_list_state(list_state):
    return "( " + " or ".join([gadget_of_state(i) for i in list_state]) + " )"



def creating_sequence(q, n, err): #q : number question, n : number of sheep
    sequence = []
    for i in range(2 ** q):
        condition = True 
        for j in sequence:
            if hamming_dst_num(i, j) <= err * 2 :
                condition = False
                break 
        if condition:
            sequence.append(i)
        
        if len(sequence) >= 2 ** n :
            print(f"create enough space for {2 ** n} with error {err}")
            break 
    return sequence

def nearest_neighbor(state, sequence_state):
    idx, ans = 0, 100
    numstate = bool_arr2int(state) 
    for i in sequence_state:
        if hamming_dst_num(numstate, i) < ans:
            idx = i
            ans = hamming_dst_num(numstate, i)
    return idx 


def solve_stage2(q, n, err, roundnum):
    questions = [[] for i in range(q)]
    sequence_state = creating_sequence(q, n, err)
    # print("finish generate sequence")
    for idx, state in enumerate(sequence_state): #idx is the state with n bits, state is the mapping state of idx with q bits
        arrstate = int2bool_arr(state, q)
        for i in range(q):  
            if arrstate[i]:
                questions[i].append(int2bool_arr(idx, n))
    
    for ROUND in range(roundnum):
        state = []
        io.recvuntil(f"ROUND".encode())
        for i in range(q):
            sla(b"question:\n", gadget_of_list_state(questions[i]).encode())
            msg = io.recvline(0).decode()
            if "Yes" == msg:
                state.append(1)
            else:
                state.append(0)
            print(f"done ask {i}-th question")
        ans = nearest_neighbor(state, sequence_state)
        ans = int2bool_arr(sequence_state.index(ans), n)
        sla(b"Who are them?\n", " ".join(str(int(i)) for i in ans).encode())
        # io.interactive()

# def cheating_stage1():
#     for i in range(10):
#         io.recvuntil(b"Who is guilty?\n")
#         ans = io.recvline(0)
#         io.sendline(ans)

graph = [[] for i in range(50)]
low = [None for i in range(50)]
num = [None for i in range(50)]

cnt = 0

wolves = []
def dfs(u, par):
    global cnt, wolves, graph
    cnt += 1 
    num[u] = cnt
    low[u] = cnt 
    for v in graph[u]:
        if v != par :
            if num[v] != -1:
                low[u] = min(low[u], num[v])
            else:
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if num[v] == low[v]:
                    # print(f"{u} {v}")
                    if not (v in wolves):
                        wolves.append(v)
                    if not (u in wolves):
                        wolves.append(u)



def solve_stage1(roundnum):
    
    io.recvuntil(b"STAGE 1\n")
    # io.interactive()
    for rnd in range(roundnum):
        io.recvuntil(b"ROUND")
        io.recvline(0)
        # io.interactive()
        #reset state
        for i in range(50):
            graph[i] = []
        wolves = []
        num = [-1 for i in range(50)]
        low = [-1 for i in range(50)]
        cnt = 0

        for i in range(50):
            io.recvuntil(b"trust: ")
            graph[i] = eval(io.recvline(0).decode())
        dfs(0, -1)
        sla(b"guilty?\n", str(wolves).encode())
    pass



def solve():
    solve_stage1(50)
    print("STAGE 1 complete")
    solve_stage2(11, 5, 1, 20)
    print("DONE 1")
    solve_stage2(15, 7, 2, 20)
    print("STAGE 2 complete")
    pass


solve()

io.interactive()
