import threading

def increment_count(by):
    
    global the_count
    global last_by
    
    the_count += by
    last_by = by
    
if __name__ == '__main__':
    
    the_count = 10
    last_by = 2
    
    lock = threading.Lock()
    with lock:
        t1 = threading.Thread(target=increment_count, args=(4,))
        
        # start threads 
        t1.start()
        
        # wait until threads finish their job 
        t1.join()
        
    print(the_count)
    print(last_by)