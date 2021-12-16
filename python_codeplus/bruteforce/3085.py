# 3085.py 사탕 게임
# 행, 열의 사탕갯수를 초기화하기전에 최댓값을 갱신하는 것을 놓침...

def get_candy(arr: list, n: int) -> int:
    ret = 1
    for i in range(n):
        cnt_row, cnt_column = 1, 1
        for j in range(n-1):
            # row
            if arr[i][j] == arr[i][j+1]:
                cnt_row += 1
            else: cnt_row = 1
            # print(f"row: {cnt_row}")

            # column
            if arr[j][i] == arr[j+1][i]:
                cnt_column += 1
            else: cnt_column = 1
            # print(f"column: {cnt_column}")
            ret = max(ret, cnt_row, cnt_column)

    return ret


n = int(input())
arr = [list(input()) for _ in range(n)]
ret = get_candy(arr, n)

# 다른 사탕이 있을 때 교환
for i in range(n):
    for j in range(n-1):
        arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
        ret = max(ret, get_candy(arr, n))
        arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]

for i in range(n):
    for j in range(n-1):
        arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]
        ret = max(ret, get_candy(arr, n))
        arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]

print(ret)