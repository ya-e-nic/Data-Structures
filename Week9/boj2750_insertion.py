import sys

def insertion_sort(a, key=lambda x: x):
    for i in range(1, len(a)):
        current = a[i]
        j = i - 1
        while j >= 0 and key(a[j]) > key(current):
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = current
    return a

def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    if not values:
        return
    n = values[0]
    a = values[1:]
    if len(a) != n:
        raise ValueError("입력 개수와 N이 다릅니다.")
    insertion_sort(a)
    sys.stdout.write("\n".join(map(str, a)))
    if a:
        sys.stdout.write("\n")

if __name__ == "__main__":
    main()
