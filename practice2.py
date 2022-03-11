# 코드메이트 개발 팀에서는 추후에 들어올 신입 개발자들을 위해
# 개발 환경을 미리 만들어 두려고 한다.
# 이 때, 가장 먼저 해야할 것은 무엇일까 생각해보니,
# 바로 인터넷이 되어야 일을 제대로 처리할 수 있을 것 같다고 생각했다!
# 회사 내에는 현재 아래와 같은 길이의 랜선 4개가 존재한다.
# 215, 513, 712, 803
# 위와 같은 4개의 랜선을 잘라 길이가 같은 10개의 랜선을 만들고자 할 때,
# 만들 수 있는 랜선의 최대 길이는 몇 일까?
# 재귀함수로 풀기!

def binary_search(arr, start, end, target):
    mid = (start + end) // 2
    total = 0

    for i in arr:
        total += (i // mid)

    if total > target:
        return binary_search(arr, mid+1, end, target)
    elif total == target:
        return mid
    else:
        return binary_search(arr, start, mid-1, target)


arr = [215, 513, 712, 803]
start = 0
end = arr[-1]
target = 10
result = binary_search(arr, start, end, target)
print(result)