import threading

the_count = 5
last_by = 5

def increment_count(by):
    global the_count
    global last_by
    
    the_count += by
    last_by = by
    
def main(*args):
    lock = threading.Lock()
    with lock:
        print("Lock acquired by Thread:" + str(args[0]))
        increment_count(args[1])

if __name__ == '__main__':
    
    no_of_thread = 5
    list_of_threads = [threading.Thread(target=main, args=(t_id, 2)) for t_id in range(no_of_thread)]
    
    for curr_thread in list_of_threads:
        curr_thread.start()
    
    for curr_thread in list_of_threads:
        curr_thread.join()
     
    print(the_count)
    print(last_by)