# 연결 리스트를 만들고 노드 추가하기
""" 구현할 단일 연결 리스트의 메서드는 다음과 같다.

appendleft(x): 연결 리스트의 처음에 x를 추가한다.
append(x): 연결 리스트의 끝 x를 추가한다.
popleft(): 연결 리스트에서 첫 노드의 값을 반환하고, 노드는 삭제한다.
pop(): 연결 리스트에서 마지막 노드의 값을 반환하고, 노드는 삭제한다.
insert(i, x): 연결 리스트의 i번 인덱스에 x를 추가한다.
remove(x): 연결 리스트에서 값이 x인 노드를 찾아 삭제한다.
reverse(): 연결 리스트를 제자리에서 순서를 뒤집는다.


위의 메서드 외에 연결 리스트를 출력하고, 길이를 반환하고, 값을 검색하는 메서드도 만든다.
이들은 클래스의 특수 메소드로 구혆란다.
__len__: len() 함수를 사용할 때 연결 리스트의 길이를 반환한다.
__contains__: 연산자 in과 not in을 사용할 때 연결 리스트 내의 값을 검사하여 True, False를 반환한다.
__str__: str()과 print() 함수를 사용할 때 출력할 문자열을 반환한다.
"""

# Node class Definition
class Node:
    def __init__(self, data, _next = None):
        self.data = data
        self.next = _next

# Linked List class Definition
class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length

    def appendleft(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            self.head = Node(data, self.head)
        self.length += 1

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = Node(data)
        self.length += 1

    def __str__(self):
        res = "Head"
        if self.head is None:
            return f"{res} → None"
        node = self.head
        while node is not None:
            res = f"{res} → {str(node.data)}"
            node = node.next
        return res

    def __contains__(self, target):
        if self.head is None:
            return False
        node = self.head
        while node is not None:
            if node.data == target:
                return True
            node = node.next
        return False

    def popleft(self):
        if self.head is None:
            return None
        node = self.head
        self.head = self.head.next
        self.length -= 1
        return node.data

    def pop(self):
        if self.head is None:
            return None
        prev = None
        node = self.head
        while node.next is not None:
            prev = node
            node = node.next
        if prev is None:
            self.head = None
        else:
            prev.next = None
        self.length -= 1
        return node.data

    def remove(self, target):
        node = self.head
        while node is not None and node.data != target:
            prev = node
            node = node.next
        if node is None:
            return False
        if node == self.head:
            self.head = self.head.next
        else:
            prev.next = node.next
        self.length -= 1
        return True

    def insert(self, idx, data):
        if idx <= 0:
            self.appendleft(data)
        elif idx >= self.length:
            self.append(data)
        else:
            node = self.head
            for _ in range(idx - 1):
                node = node.next
            newNode = Node(data, node.next)
            node.next = newNode
            self.length += 1

    def reverse(self):
        if self.length < 2:
            return
        prev = None
        ahead = self.head.next
        while ahead:
            self.head.next = prev
            prev = self.head
            self.head = ahead
            ahead = ahead.next
        self.head.next = prev
        
        
if __name__ == "__main__":

    def get_data(msg):
        data = input(msg)
        if data.isdigit():
            return int(data)
        return None

    menu = """
1: appendleft  2: append  3: popleft  4: pop  5: search  6: insert  7: remove  8: reverse
9: Exit
"""
    my_list = LinkedList()
    while True:
        print("\n-------\nCurrent List: ", my_list)
        command = int(input(f"{menu}\nEnter your choice: "))
        print()

        if command == 1:
            data = get_data("Input number to append at start: ")
            my_list.appendleft(data)
        elif command == 2:
            data = get_data("Input number to append: ")
            my_list.append(data)
        elif command == 3:
            data = my_list.popleft()
            if data is not None:
                print(f"Poped from start: {data}")
            else:
                print("Linked list is empty!")
        elif command == 4:
            data = my_list.pop()
            if data is not None:
                print(f"Poped from end: {data}")
            else:
                print("Linked list is empty!")
        elif command == 5:
            data = get_data("Input number to search: ")
            if data in my_list:
                print(f"{data} is exists.")
            else:
                print(f"{data} is not exists.")
        elif command == 6:
            data = get_data("Input number to insert: ")
            index = int(get_data("Input index to insert at: "))
            my_list.insert(index, data)
        elif command == 7:
            data = get_data("Input number to remove: ")
            if my_list.remove(data):
                print(f"Removed {data}.")
            else:
                print(f"{data} is not exists.")
        elif command == 8:
            my_list.reverse()
            print(f"Reversed the linked list.")
        elif command == 9:
            break