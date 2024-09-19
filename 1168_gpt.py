class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)
        self.build(1, 0, n - 1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = 1  # 각 사람은 처음에 1명씩 존재
        else:
            mid = (start + end) // 2
            self.build(node * 2, start, mid)
            self.build(node * 2 + 1, mid + 1, end)
            self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def update(self, node, start, end, idx):
        if start == end:
            self.tree[node] = 0  # idx 위치의 사람을 제거
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self.update(node * 2, start, mid, idx)
            else:
                self.update(node * 2 + 1, mid + 1, end, idx)
            self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def query(self, node, start, end, k):
        if start == end:
            return start
        mid = (start + end) // 2
        if self.tree[node * 2] >= k:
            return self.query(node * 2, start, mid, k)
        else:
            return self.query(node * 2 + 1, mid + 1, end, k - self.tree[node * 2])


def josephus_with_segment_tree(N, K):
    tree = SegmentTree(N)
    result = []
    current_position = 0  # 처음에는 0번째 사람부터 시작

    for i in range(N):
        people_left = N - i  # 남은 사람 수
        current_position = (current_position + K - 1) % people_left  # K번째 사람의 위치 계산
        kth_person = tree.query(1, 0, N - 1, current_position + 1)  # K번째 사람 찾기
        result.append(kth_person + 1)  # 사람은 1번부터 N번까지이므로 +1
        tree.update(1, 0, N - 1, kth_person)  # 찾은 사람 제거

    return result


# N과 K 입력 받기
N, K = map(int, input().split())

# 요세푸스 순열 구하기
result = josephus_with_segment_tree(N, K)
printList = list(result)
print("<", end='')
print(*printList, sep=', ', end= '')
print(">")