import heapq
def kSmallest(lst, k):
    heap = lst[:k]
    heapq._heapify_max(heap) #create heap
    n = len(lst)
    for i in range(k ,n):
        if heap[0] > lst[i]: #if heap at 0 index is greater then whtever we insert then replace it
            heapq._heapreplace_max(heap,lst[i])
    return heap

# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kSmallest(lst, k)
ans.sort()
print(*ans, sep=' ')
