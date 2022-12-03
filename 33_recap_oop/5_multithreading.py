from time import sleep, perf_counter
from threading import Thread

start_time = perf_counter()
def task_1():
    for i in range(1, 5):
        print(f'Staring task - {i}')
        sleep(1)
        print()

def task_2():
    for i in range(6, 11):
        print(f'Staring new task - {i}')
        sleep(2)
        
t1 = Thread(target=task_1)
t2 = Thread(target=task_2)

t1.start()
t2.start()
t1.join()
t2.join()

# task_1()
# task_2()
# end_time = perf_counter()
# print(f'Total time {end_time - start_time}')









