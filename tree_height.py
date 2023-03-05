# python3

import sys
import threading


def compute_height(n, parents):
    # Write this function
    #print(n,parents)
    max_height = 0
    height={}
    for i in range(n):
        height[i]=[]
    # Your code here
    for i in range(n):
        if parents[i]==-1:
            root=i
        else:
            if parents[i] >= 0 and parents[i]<n:
                height[parents[i]].append(i)

    def fheight(i):
        if len(height[i])==0:
            return 1
        else:
            return 1 + max(fheight(j) for j in height[i])
            

    

    #print(height)
    max_height=fheight(root)
    return max_height


def main():
    # implement input form keyboard and from files
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    mode = input()
    if mode == 'F':
        test_file = input()
        with open(f"/workspaces/tree-height-from-empty-EduardsJ1/test/{test_file}") as f:
            n = int(f.readline().strip())
            
            parents = list(map(int, f.readline().strip().split()))
            
    else:
        n=int(input())
        parents=list(map(int,input().split()))


    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    
    # call the function and output it's result
    print(compute_height(n,parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()