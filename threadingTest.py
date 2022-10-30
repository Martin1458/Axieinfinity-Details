import threading
from time import sleep

def doOne():
    sleep(2)
    print('1')

def doSeckond():
    sleep(3)
    print('2')

t1 = threading.Thread(target=doOne, args=())
t2 = threading.Thread(target=doSeckond, args=())

print('6546546546')
t1.start()
t2.start()
t2.join()
t1.join()
print(54)


#doOne()
#doSeckond()
