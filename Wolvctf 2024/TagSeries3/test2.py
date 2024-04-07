import HashTools
from os import urandom

# setup context
secret = urandom(1200)        # idk ¯\_(ツ)_/¯
original_data = b"GET FILE: "
sig = HashTools.new(algorithm="sha1", raw=secret+original_data).hexdigest()

sig="6dd0776ac94ededd8d953861c036e80df1e5ebf5"


print("original hash: ", sig)

# attack
append_data = b"flag.txt"
magic = HashTools.new("sha1")
new_data, new_sig = magic.extension(
    secret_length=1200, original_data=original_data,
    append_data=append_data, signature=sig
)
target_sig = HashTools.new(algorithm="sha1", raw=secret+new_data).hexdigest()
print("target hash: ", target_sig)

print("new data: ", new_data)
print("new hash: ", new_sig)