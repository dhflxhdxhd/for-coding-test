#List > 배열, 테이블
#여러 개의 데이터를 연속적으로 담아 처리하기 위해 사용.

a = [1, 2, 3, 4, 5]
print(a)

#인덱스 3, 네번째 원소에 접근
print(a[3])

#빈 리스트 선언 1)
a = list()
print(a)

#빈 리스트 선언 2)
a = []
print(a)

#in coding-test
#크기가 N인 1차원 리스트 초기화 방법
n = 10
a = [0] * n
print(a)

#리스트의 인덱싱과 슬라이싱
a = [1,2,3,4,5]

#인덱싱 : 리스트의 특정한 원소에 접근
print(a[-1])
#두번째 원소 값 변경
a[1] = 5
print(a)

#슬라이싱 : 리스트에서 연속적인 위치를 갖는 원소들을 갖와야 할 때.
#두 번째부터 네 번째 원소까지
print(a[1:4])

#리스트 컴프리헨션
#: 리스트를 초기화하는 방법 중 하나.
#0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i%2 == 1]
print(array)

#1부터 9까지의 수의 제곱값을 포함하는 리스트
array = [i * i for i in range(1,10)]
print(array)

#2차원 리스트 초기화
#N X M
n = 3
m = 3
array = [[0] * m for _ in range(n)]
print(array)
