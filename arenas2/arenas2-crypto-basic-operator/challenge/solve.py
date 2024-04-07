from Crypto.Util import number
from Crypto.Util.number import long_to_bytes
from sympy.ntheory import sqrt_mod, discrete_log
from Crypto.Util.number import *


def padding_pkcs7(data, block_size=4):
    tmp = len(data) + (block_size - len(data) % block_size)
    return data.ljust(tmp, bytes([block_size - (len(data) % block_size)]))


def split_block(data, block_size):
    return list(
        int.from_bytes(data[i : i + block_size], "little")
        for i in range(0, len(data), block_size)
    )


def plus_func(data, shift):
    return (data + shift) & 0xFFFFFFFF


def mul_func(data, mul):
    return (data * mul) & 0xFFFFFFFF


def xor_shift_right_func(data, bit_loc):
    return (data ^ (data >> bit_loc)) & 0xFFFFFFFF




def pow_func(data, e, p):
    return pow(data, e, p)


def exp_func(data, base, p):
    return pow(base, data, p)


def ecb_mode(data):
    return list(
        pow_func(
            exp_func(
                xor_shift_right_func(
                    mul_func(plus_func(block, 3442055609), 2898124289), 1
                ),
                e,
                p,
            ),
            e,
            p,
        )
        for block in split_block(padding_pkcs7(data, 4), 4)
    )


def test(data):
    return pow_func(
        exp_func(
            xor_shift_right_func(mul_func(plus_func(data, 3442055609), 2898124289), 1),
            e,
            p,
        ),
        e,
        p,
    )

from sympy.ntheory import sqrt_mod, discrete_log
from Crypto.Util.number import *

def rexor(data):
    bit = bin(data)[2:]
    ans = str(int(bit[0], 2) ^ 0)
    for i in range(1, len(bit)):
        ans += str(int(bit[i], 2) ^ int(ans[-1], 2))
    return int(ans, 2)


# a = x + 3442055609
# y = a * 2898124289
# t = (y>>1) ^ y
# l = 2**t mod 1341161101353773850779
# j = l**2 mod 1341161101353773850779

p = 1341161101353773850779
e = 2
f = []
ct = [
    752589857254588976778,
    854606763225554935934,
    102518422244000685572,
    779286449062901931327,
    424602910997772742508,
    1194307203769437983433,
    501056821915021871618,
    691835640758326884371,
    778501969928317687301,
    1260460302610253211574,
    833211399330573153864,
    223847974292916916557,
]


plus, mul = 3442055609, 2898124289

# x & 0xFFFFFFFF <=> x % (0xFFFFFFFF + 1)
q = 0xFFFFFFFF+1


for j in ct:
    for l in sqrt_mod(j, p, all_roots=True):
        t = discrete_log(p, l, 2)
        y = rexor(t)
        a = y * pow(mul, -1, q)
        x = (a - plus) % q
        try:
            print(long_to_bytes(x).decode())
            f.append(long_to_bytes(x).decode()[::-1])
        except:
            continue
print(''.join(f))
