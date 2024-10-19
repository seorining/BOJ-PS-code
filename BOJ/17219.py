import sys

n, m = map(int, sys.stdin.readline().split())

pass_dict = {}
for _ in range(n):
    site, password = sys.stdin.readline().rstrip().split()
    pass_dict[site] = password
    
for _ in range(m):
    ask_site = sys.stdin.readline().rstrip()
    print(pass_dict[ask_site])