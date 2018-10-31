# Replace the hashed password in the given application with the hash of any password

import sys
import hashlib
OFFSET = 0x1E3DB

def main(app, pw):
    f = open(app, "r+b")
    f.seek(OFFSET, 0)

    m = hashlib.sha1()
    m.update(pw)
    pw_hash = m.hexdigest()
    f.write(pw_hash.decode("hex"))
    
    f.close()


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])