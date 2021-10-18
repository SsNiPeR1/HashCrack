import hashlib, sys, threading, time, multiprocessing


def HashCrack(hash):
    
    global i
    i = 0

    while True:
        if hashlib.sha256(str(i).encode()).hexdigest() == hash:
            return f"The number is {i}"
        
        else:
            i += 1

breakfunc = False
def printi():
    while True:
        time.sleep(1)
        if hashlib.sha256(str(i).encode()).hexdigest() == hash:
            print(f"The number is {i}")
            exit()
        if breakfunc == True:
            break
        print(i)

hashinput = sys.argv[1]
threading.Thread(target=HashCrack, args=(hashinput,)).start()
t1 = threading.Thread(target=printi)
t1.start()
while True:
    if hashlib.sha256(str(i).encode()).hexdigest() == hash:
        breakfunc = True
        break
t1.join()