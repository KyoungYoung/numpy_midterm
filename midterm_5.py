import numpy as np

print("=====정렬된 랜덤 2차원 배열 생성=====")
print("정렬 전")

#2차원 배열 25미만인 5행5열의 수
arr1 = np.random.randint(25,size=(5,5))
print(arr1)

#오름차순으로 정렬
# 2차원 이상의 배열에서 행이나 열별로 정렬하는 것이 아닌 모든 값들에 대해 정렬을 수행하고자 할 때에는 axis = None 으로 지정한다
print("정렬 후")
arr2 = np.sort(arr1,axis=None)
arr2 = arr2.reshape((5,5))
print(arr2)