"""
heapq 모듈의 기능 구현
왼쪽부터 꽉 채운 이진트리이므로, 배열을 이용해도 빈 곳이 생기지 않는다. 
직접 구현할 최소 힙도 배열을 이용하여 만든다. 
이미 배열로 이진트리를 표현하는 방법을 공부했으므로, 인덱스를 조작하는 것 자체는 어렵지 않다.

구현할 기능은 다음과 같다.

heappush(heap, data): heap에 data를 삽입한다.
heappop(heap): heap에서 루트 노트의 값을 꺼낸 후 삭제한다.
heapify(x): 배열(리스트) x를 힙 구조로 만든다.

그냥 import heapq 파이썬 라이브러리를 사용하자.
import heapq #최소 힙

heapq.heappush(heap, item) : item을 heap에 추가

heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & 리턴. 
비어 있는 경우 IndexError가 호출됨. 

heapq.heapify(x) : 리스트 x를 즉각적으로 heap으로 변환함 (in linear time, O(N) )
"""

import heapq

def heappush(heap, data):
    heap.append(data)
    current = len(heap) - 1
    while current > 0:
        parent = (current - 1) // 2
        if heap[parent] > heap[current]:
            heap[parent], heap[current] = heap[current], heap[parent]
            current = parent
        else:
            break
        
def heappop(heap):
    if not heap:
        return "Empty Heap!"
    elif len(heap) == 1:
        return heap.pop()
    
    popData, heap[0] = heap[0], heap.pop()
    current, child = 0, 1
    while child < len(heap):
        sibling = child + 1
        if sibling < len(heap) and heap[child] > heap[sibling]:
            child = sibling
        if heap[current] > heap[child]:
            heap[current], heap[child] = heap[child], heap[current]
            current = child
            child = current * 2 + 1
        else:
            break
    return popData

