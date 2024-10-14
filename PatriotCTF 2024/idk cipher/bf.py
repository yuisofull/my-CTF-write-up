import base64

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
srt_key = 'secretkey'
i = 0
ct = "QRVWUFdWEUpdXEVGCF8DVEoYEEIBBlEAE0dQAURFD1I="
ct = base64.b64decode(ct).decode()
res = [0]*len(ct)

while True:
    if i == len(ct) // 2:
        print(res)
        break
    found = False
    for c1 in chars:
        for c2 in chars:
            enc_p1 = chr(ord(c1) ^ ord(srt_key[i % len(srt_key)]))
            enc_p2 = chr(ord(c2) ^ ord(srt_key[i % len(srt_key)]))
            temp = enc_p1 + enc_p2
            if temp == ct[i*2:i*2+2]:
                res[i]=c1
                res[len(ct)-i-1]=c2
                i += 1
                found = True
                break
        if found:
            break

# for i in range(int(len(ct) / 2)):
#     c1 = ord(usr_input[i])
#     c2 = ord(rsv_input[i])
#     enc_p1 = chr(c1 ^ ord(srt_key[i % len(srt_key)]))
#     enc_p2 = chr(c2 ^ ord(srt_key[i % len(srt_key)]))