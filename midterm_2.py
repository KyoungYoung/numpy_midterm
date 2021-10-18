import numpy as np

print("=====1차원 변환=====")
#1번 문제의 값을 가져온다.
arr = np.ones([3,3])

#1차원 배열로 바꾼다. ravel 함수 사용
arr = arr.ravel()
print(arr)