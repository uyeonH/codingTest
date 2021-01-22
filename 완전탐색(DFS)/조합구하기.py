import sys

sys.stdin = open("in1.txt", "r")


def DFS(L, s):
    global cnt
    if L == m:
        cnt += 1
        for i in range(L):
            print(res[i], end=' ')
        print()

    else:

        for i in range(s, n+1):
            res[L] = i
            DFS(L + 1, i + 1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * (n + 1)
    cnt = 0
    DFS(0, 1)
    print(cnt)
