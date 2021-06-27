# # 정수 3개 입력받아 짝수만 출력하기
# # 복수 데이터를 입력받으면서 모두 숫자형으로 바꾸고 싶을 때 : map(자료형, input( '출력문' ). split( ) )
# a, b, c = map(int, input().split(" "))
#
# if(a % 2 == 0):
#     print(a)
# if(b % 2 == 0):
#     print(b)
# if(c % 2 == 0):
#     print(c)

# # 정수 3개 입력받아 짝/홀 출력하기
# a, b, c = map(int, input().split(" "))
#
# if (a % 2 == 0):
#     print("even")
# else:
#     print("odd")
#
# if (b % 2 == 0):
#     print("even")
# else:
#     print("odd")
#
# if (c % 2 == 0):
#     print("even")
# else:
#     print("odd")

# # 정수 1개가 입력되었을 때, 음(minus)/양(plus)과 짝(even)/홀(odd)을 출력
#
# a = int(input())
#
# print(type(a))
#
# if(a > 0):
#     if (a % 2 == 0):
#         print("plus")
#         print("even")
#     else:
#         print("plus")
#         print("odd")
# elif(a < 0):
#     if (a % 2 == 0):
#         print("minus")
#         print("even")
#     else:
#         print("minus")
#         print("odd")

# # 점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.
#
# a = int(input())
#
# if(90 <= a <= 100):
#     print('A')
# elif(70 <= a <= 89):
#     print('B')
# elif(40 <= a <= 69):
#     print('C')
# else:
#     print('D')


