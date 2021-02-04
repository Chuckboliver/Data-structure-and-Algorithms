class Max_Heap:
    def __init__(self, arr=[]):
        self._heap = []
        if arr is not None:
            for root in arr:
                self.push(root)

    def push(self, value):
        self._heap.append(value)
        _bottom_up(self._heap, len(self) - 1)

    def pop(self):
        if len(self._heap)!=0:
            _swap(self._heap, len(self) - 1, 0)

            root = self._heap.pop()
            _top_down(self._heap, 0)
            
        else:
            root="Heap is empty"
        return root
    def __len__(self):
        return len(self._heap)
    def peek(self):
        if len(self._heap)!=0:
            return(self._heap[0])
        else:
            return("heap is empty")
    def __str__(self) -> str:
        return " ".join(list(map(str, self._heap)))
def _swap(L, i, j):
    L[i], L[j] = L[j], L[i]

def _bottom_up(heap, index):
    root_index = (index - 1) // 2
    
    if root_index < 0:
        return

    if heap[index] > heap[root_index]:
        _swap(heap, index,root_index)
        _bottom_up(heap, root_index)


def _top_down(heap, index):
    child_index = 2 * index + 1
    if child_index >= len(heap):
        return

    if child_index + 1 < len(heap) and heap[child_index] < heap[child_index + 1]:
        child_index += 1

    if heap[child_index] > heap[index]:
        _swap(heap, child_index, index)
        _top_down(heap, child_index)


def getMedian(low, high):

    if len(low) > len(high):
        return float(low.peek())
    return (low.peek() - high.peek())/2

low = Max_Heap()
high = Max_Heap()#Min heap

l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "minHeap and maxHeap"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    l=list(map(int, l))
    #code here
    for i,n in enumerate(l):
        low.push(n)
        high.push(-low.pop())
        if len(low) < len(high):
            low.push(-high.pop())
        print(f"list = {l[:i + 1]} : median = {getMedian(low, high)}")