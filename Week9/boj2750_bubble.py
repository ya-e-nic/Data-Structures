import sys

def bubble_sort(a, key=lambda x: x):
    for end in range(len(a) - 1, 0, -1):
        swapped = False
        for j in range(end):
            if key(a[j]) > key(a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a

def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    if not values:
        return
    n = values[0]
    a = values[1:]
    if len(a) != n:
        raise ValueError("입력 개수와 N이 다릅니다.")
    bubble_sort(a)
    sys.stdout.write("\n".join(map(str, a)))
    if a:
        sys.stdout.write("\n")

if __name__ == "__main__":
    main()
