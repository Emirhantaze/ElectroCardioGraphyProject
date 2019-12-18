from multiprocessing import Process
from time import sleep
def first():
    global  ax
    while True:
        ax=ax+1
        sleep(0.01)
def second():
    
    while True:
        print(ax)
        sleep(0.01)
if __name__ == "__main__":
    ax=1
    t1 = Process(target = first)
    t2 = Process(target=second)
    t1.start()
 
    t2.start()
    sleep(12)
