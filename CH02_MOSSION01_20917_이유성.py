jua = float(input("첫 번째 점의 x좌표를 입력하세요 :  "))
fja = float(input("첫 번째 점의 y좌표를 입력하세요 :  "))
spy = float(input("두 번째 점의 x좌표를 입력하세요 :  "))
stw = float(input("두 번째 점의 y좌표를 입력하세요 :  "))
import math
gye = math.pow((spy-jua),2)
san = math.pow((stw-fja),2)
rut = math.sqrt(gye+san)

print("두 점({0}, {1}), ({2}, {3}) 사이의 거리는 {4}입니다.".format(jua,fja,spy,stw,rut))