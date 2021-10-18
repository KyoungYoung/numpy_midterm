import numpy as np

# 1에서 51미만(1부터 50까지)의 수를 나타내는 함수 arange 에다가 간격 2를 넣어주고 1차원 함수를 만든다
# 1차원 함수의 정렬을 위해 sort 함수를 사용한다.
print("======1부터 50까지의 2간격 배열 생성=======")
arr = np.arange(1,51,2)
print(np.sort(arr))

# 내림차순으로 2차원 함수로 정렬해주기 위해 resize라는 함수를 사용(resize 함수는 원본 데이터를 변경)
# 행과 열 모두 뒤집히려면 np.flip 함수를 이용한다. 
print("=========2차원으로 변환(거꾸로)========")
arr.resize(5,5)
print(np.flip(arr))