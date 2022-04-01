# 현재 배열에는 9, 6, 7, 3, 5의 순서로 데이터가 저장되어 있습니다.
# 이 때, 선택 정렬 기법을 사용해 자료를 오름차순으로 정렬하면서,
# 배열의 위치 교환이 일어날 때 마다 전체 배열을 출력해 주세요.

arr = [9,6,7,3,5]
length = len(arr)
print(f"정렬전:{arr}")

for i in range(length-1):
    for j in range(i, length):
        minimum = min(arr[i:])
        if minimum == arr[j]:
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    print(arr)

print(f"정렬후:{arr}")





# 버블정렬
# arr = [5,2,9,1,6]
# length = len(arr)
#
# print(f"정렬전:{arr}")
#
# for i in range(length):
#     for j in range(0, length-i-1):
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]
#
# print(f"정렬후:{arr}")

# def quick_sort(arr):
#     if len(arr)>1:
#         pivot = arr[len(arr)-1]
#         left = 0
#
#         for right in range(len(arr)):
#             if arr[right] < pivot:
#                 arr[right], arr[left] = arr[left], arr[right]
#                 left += 1
#
#         arr[len(arr)-1], arr[left] = arr[left], arr[len(arr)-1]
#
#         left_side = quick_sort(arr[:left])
#         right_side = quick_sort(arr[left+1:])
#
#         return left_side + [arr[left]] + right_side
#     else:
#         return arr
#
# arr = [5,3,7,6,2,1,4]
# start, end = 0, len(arr)-1
# print(quick_sort(arr))