import heapq
def kthLargest(lst, k):
    ######################
    #PLEASE ADD CODE HERE#
    ######################
    heap = lst[:k]
    heapq.heapify(heap)
    n = len(lst)

    for i in range(k, n):
        if heap[0] < lst[i]:
            heapq.heapreplace(heap, lst[i])
    return heap[0]    
 

# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kthLargest(lst, k)
print(ans)
