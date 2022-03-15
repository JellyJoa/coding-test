def validate_brace_pair(str):
    arr = []
    for i in range(len(str)):
        if str[i] == '{':
            arr.append(str[i])
        else:
            if len(arr)>0:
                arr.pop()
    if len(arr) != 0:
        print('유효하지 않은 중괄호 쌍입니다.')
    else:
        print('유효한 중괄호 쌍입니다.')



validate_brace_pair("{{}}{}")
validate_brace_pair("{{}")
validate_brace_pair("{{{}}}")
validate_brace_pair("}{{{}}}{")




# MAX_STACK_SIZE = 3
#
# class Stack:
#     def __init__(self):
#         self.arr = [None]*MAX_STACK_SIZE
#         self.top = -1
#
#     def is_full(self):
#         if self.top >= MAX_STACK_SIZE-1:
#             return True
#         else:
#             return False
#
#     def push(self, value):
#         if self.is_full():
#             print("스택이 가득 찼습니다.")
#         else:
#             self.top += 1
#             self.arr[self.top] = value
#
#     def is_empty(self):
#         if self.top < 0:
#             return True
#         else:
#             return False
#
#     def pop(self):
#         if (self.is_empty()):
#             print('스택이 비어있습니다.')
#         else:
#             value = self.arr[self.top]
#             self.top -= 1
#             return value
#
#
# stack = Stack()
# stack.pop()
#
# stack.push("data 1")
# stack.push("data 2")
# stack.push("data 3")
#
# print("pop:",stack.pop())
# print("pop:",stack.pop())
# print("pop:",stack.pop())
# print("pop:",stack.pop())




# from threading import Thread
# import time
#
# arr = ['곰', '코뮤', '모각코', '망고', '밥']
#
# def delete_unliked_name(index):
#     global arr
#     time.sleep(1)
#
#     arr = arr[0:index] + arr[index+1:]
#
# def print_liked_names():
#     global arr
#     # length = len(arr)
#
#     time.sleep(2)
#
#     print(f'변경전:')
#     for i in range(len(arr)):
#         print(arr[i])
#
# th1 = Thread(target=delete_unliked_name, args=(3,))
# th2 = Thread(target=print_liked_names, args=())
#
# th1.start()
# th2.start()



# print(f'변경후:')
# arr[3] = None
#
# for i in range(len(arr)):
#     print(arr[i])