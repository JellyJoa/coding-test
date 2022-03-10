def binary_search(arr, target):
    start = 0
    end = arr[-1]

    while (end-start >= 0):
        mid = (start+end)//2
        line = 0

        for i in arr:
            line += i // mid

        if line >= target:
            start = mid + 1
        else:
            end = mid -1
    return end

arr = [215, 513, 712, 803]
target = 10
print(binary_search(arr, target))