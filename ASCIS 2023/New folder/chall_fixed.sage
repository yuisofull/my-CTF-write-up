from Crypto.Random.random import getrandbits
from Crypto.Util.number import bytes_to_long

nbits = 128
while True:
    mul = getrandbits(nbits)
    add = getrandbits(nbits)
    modulus = getrandbits(nbits)
    if mul < modulus and add < modulus:
        break

def gen_num(bits):
    truncate = bits
    seed = getrandbits(511)
    gen_num = 41

    xx = []
    yy = [] 
    
    for _ in range(gen_num):
        seed = (mul * seed + add) % modulus
        xx.append(seed)
        yy.append(seed >> (nbits-truncate))
    return xx, yy

_, ee = gen_num(18) #
_, ff = gen_num(20)

a = ee[-1] #18 bit, a = 182536
b = ff[-1] #20 bit, b = 732597
a = 182536
b = 732597
c = getrandbits(1024)
p = next_prime(a * c + getrandbits(512)) #1042 bit
q = next_prime(b * c + getrandbits(512)) #1044 bit
p*q
flag = '<REDACTED>'
N = p * q #2085
e = 65537
m = bytes_to_long(flag.encode())
enc = pow(m, e, N)

print(f'enc = {enc}')
print(f'N = {N}')
print(f'ee = {ee[:-1]}')
print(f'ff = {ff[:-1]}')
print(f'a = {mul}')
print(f'c = {add}')
print(f'm = {modulus}')


from Crypto.Util.number import long_to_bytes
e = 65537
enc = 4782207738169357679017263311695366580149461241803922088835452812820137537830281562950634059939171784035642202164746425519370563906663225547286363495366866588141853586109553019469599011984795232666657032457349167541183811442599555965876853759790930565452169138123206051344200109808603093521161556603615660329142949615063443855551027286822234646698015310643407246009689006200152818931447476595216569044114220319818061396623338764899012025923470408152189436065437542065068815744124506169026323905222443334212867601172364249248963768649488580249031694113977946046461290930755706144535271632419505875554486279354334709794323960679
N = 3964970058588757148381961704143056706462468814335020245520977895524549102412775370911197710398920529632256746343939593559572847418983212937475829291172342816906345995624544182017120655442222795822907477729458438770162855927353619566468727681852742079784144920419652981178832687838498834941068480219482245959017445310420267641793085925693920024598052216950355088176712030006651946591651283046071005648582501424036467542988971212512830176367114664519888193885765301505532337644978456428464159474089450883733342365659030987687637355512103402573155030916404165387863932234088255017821889649456947853403395704387479968208359004918561
p=31431249988172282588448767875539383078270520610885068858894594350040664294089631831898187839710370441685270767030754635557928414643087264016495427842079478763643907923013313402216294673271331719335552788028954573534461929535970634245151789537569696550609948093753009761080068097372824084476376283889917608424955747
q=N//p
phi=(p-1)*(q-1)

d=pow(e,-1, phi)

print(long_to_bytes(pow(enc,d,N)))