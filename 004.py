# 与えられた3つの整数の積を計算するプログラム
def multiply_numbers():
    A1, A2, A3 = map(int, input().split())
    return A1 * A2 * A3

result = multiply_numbers()
print(result)