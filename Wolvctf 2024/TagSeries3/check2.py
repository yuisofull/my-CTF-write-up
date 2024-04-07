def sha_padding(message, extra_len):
    """Extra_Len is in bytes. ONLY for the purposes of adding to the
    64-bit big-endian integer at the end of the padding.
    """
    assert type(message) == type(str())
    ml = 8 * len(message) # ML is in bits
    n_bytes_to_add = (448 - (ml % 512)) // 8
    if n_bytes_to_add < 0:
        n_bytes_to_add += 64
    padding_string = ""
    for i in range(n_bytes_to_add):
        if i > 0:
            padding_string += '\x00'
        else:
            padding_string += '\x80'
    newml = 8 * (len(message) + extra_len) # NEWML is in bits
    for i in range(8):
        byte_val = newml >> (64 - 8 * (i + 1)) & 0xff
        # Big endian means R shift by 56, 48, ... , 8, 0.
        padding_string += chr(byte_val)
    message += padding_string # only for testing, not for return.
    assert len(message) % (512/8) == 0
    return padding_string

def i2h(n):
    string = hex(n)
    if string[-1] =="L":
        return string[2:-1]
    else:
        return string[2:]

def restart_sha(hh, newmessage, extra_len):
    """Add arbitrary data to a SHA-signed message, and make it look like
    it was signed by the same key as the original message.

    In brief, perform length extension attack on SHA-1. Given hh =
    SHA1(key+original+pad1), and a guess at length of
    key+original+pad1, return SHA1(key+message+pad1+newmessage+pad2).
    In other words, add data and produce valid signature without
    knowing the key. Assumption: recipient doesn't care that there are
    weird pad1 characters in the middle of what sender claims is the
    message.

    HH is the hash of the previous message as a (usually rather big)
    integer. Should be decomposable into exactly five 32-bit words.
    Newmessage is what you want to add.

    Extra_Len is a guess, in bytes, at len(key+original+pad1). Should
    be multiple of 64 bytes. This amounts to a guess at the length of
    the key within about a 64-byte range (because len(message) is
    known and padding always gets it to multiple of 64). *Outside* of
    this function you will have to guess key length *exactly*, in
    order to guess pad1 exactly and generate the supposed signed
    message.
    """
    h0 = (hh >> 128) & 0xffffffff
    h1 = (hh >> 96) & 0xffffffff
    h2 = (hh >> 64) & 0xffffffff
    h3 = (hh >> 32) & 0xffffffff
    h4 = hh & 0xffffffff
    return sha_fixated(newmessage, h0, h1, h2, h3, h4, extra_len)

message = "GET FILE: "
auth_code="f5fef094bb9d3a20c3c2bdf78cf8075a72a8431c"
# Construct a new message.
keylen = 1200 # Need perfect guess to get perfect glue.
glue_guess = sha_padding(("A" * keylen) +  message, 0)
file = "flag.txt"

new_message = message + glue_guess + file

# Construct the MAC for that message.
KOG_len_guess = int(math.ceil((keylen + len(message)) / 64.0)) * 64
  # Len of key+original+glue
print ("Key + original + glue length =    ", KOG_len_guess)
new_auth_code = restart_sha(auth_code, file, KOG_len_guess)
print ("Guessed auth code for new message ", i2h(new_auth_code))