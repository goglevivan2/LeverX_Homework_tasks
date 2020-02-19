from threading import Thread,Lock

mutex = Lock()
a = 0
# используем мьютексы для синхорнизации потоков
def function(arg):
    global a
    mutex.acquire()
    try:
        for _ in range(arg):
            a += 1
    finally:
        mutex.release()



def main():
    threads = []
    for i in range(5):
        thread = Thread(target=function, args=(1000000,))
        thread.start()

        threads.append(thread)

    [t.join() for t in threads]
    print("----------------------", a)  # ???


main()
