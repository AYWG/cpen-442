import hashlib
import time

salt = "vI"
hashed_result = "C0835C26F2186914B068CF697945E63DCB315568" # h(password, salt)
possible_pw = ["%04d" % x for x in range(10000)]

startTime = time.time()

for pw in possible_pw:
    hash_input = salt + pw
    m = hashlib.sha1()
    m.update(hash_input)
    if m.hexdigest().upper() == hashed_result:
        print "Found pw: ", pw
        break

endTime = time.time()

print 'Time took: ', endTime - startTime