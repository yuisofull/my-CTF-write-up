import os
from hashlib import sha1

MESSAGE = b"GET FILE: "
SECRET = os.urandom(1200)