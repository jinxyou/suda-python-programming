import multiprocessing
def func(lst):
    for i in lst:
        print(i)
if __name__=="__main__":
    lst=range(1,1000000)
    pool=multiprocessing.Pool(processes=3)
    pool.apply_async(func(lst[:len(lst)//3:]), (1,))
    pool.apply_async(func(lst[len(lst)//3:len(lst)//3*2:]), (2,))
    pool.apply_async(func(lst[len(lst)//382::]), (3,))
    pool.close()
    pool.join()
    # func(lst)