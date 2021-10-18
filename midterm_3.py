import numpy as np

#1번 문제의 값을 가져온다.
arr = np.ones([3,3])

#배열의 메모리 사이즈 
#배열 요소의 전체 개수인 size 함수와 배열 요소의 바이트 크기인 itemsize를 곱해주면 전체 메모리 사이즈가 나온다.
print("=====배열의 메모리 사이즈 계산=====")
print("%d bytes" %(arr.size * arr.itemsize))

# 간단하게 nbytes를 사용해도 된다.)
#print("%d bytes"%(arr.nbytes))