M = 1000
P, N = map(int, input().split())
total_power = P * N
if total_power <= M:
    print("It's all good! The outlet can handle the load")
else:
    overload = total_power - M
    print(f"Overload! We need another {overload} watts to spare")