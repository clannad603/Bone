
def move(n, a, b, c, i):
    if n == 1:
        print('[STEP {0:>3}]'.format(int(i)),'{:}->{:}'.format(a,c))  #根部迭代，一次情况下，直接 a --> c 移动 
        return
    move(n-1, a, c, b, i-2**(n-2))              #把a中的n-1个盘移动到b，途中经转c
    print("[STEP {0:>3}]".format(int(i)), '{:}->{:}'.format(a,c))      #把a中的1个盘移动到c
    
    move(n-1, b, a, c,i+2**(n-2))              #把b中的n-1个盘移动到c，途中经转a
n=int(input())
move(n, 'A', 'B', 'C', (2**n)/2)
