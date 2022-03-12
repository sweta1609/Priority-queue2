import heapq
def kLargest(lst, k):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    pass
    heap = lst[:k]
    heapq.heapify(heap) #create heap
    n = len(lst)
    for i in range(k ,n):
        if heap[0] < lst[i]: #if heap at 0 index is greater then whtever we insert then replace it
            heapq.heapreplace(heap,lst[i])
    return heap

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kLargest(lst, k)
print(*ans, sep='\n')
