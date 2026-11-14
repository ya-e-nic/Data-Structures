import sys

def selection_sort(a, key=lambda x: x):
    for i in range(len(a) - 1):
        min_idx = i
        for j in range(i + 1, len(a)):
            if key(a[j]) < key(a[min_idx]):
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
    return a

def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    if not values:
        return
    n = values[0]
    a = values[1:]
    if len(a) != n:
        raise ValueError("입력 개수와 N이 다릅니다.")
    selection_sort(a)
    sys.stdout.write("\n".join(map(str, a)))
    if a:
        sys.stdout.write("\n")

if __name__ == "__main__":
    main()
