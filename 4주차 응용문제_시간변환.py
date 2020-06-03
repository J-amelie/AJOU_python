"""
Project W3-01. 시간 변환

COPYRIGHT (c) AJOU University
Author       : 홍길동
Details      : 초 단위 시간을 입력받아 분, 초 단위로 출력하는 프로그램
Input        : 초 단위 시간
Output       : 분, 초
File Name    : timeConv.py
History      : (1차) 0000년 00월 00일
"""
time = int(input("시간을 입력하세요 : "))

min = time // 60            """ 초 / 60의 몫은 분  """
sec = time % 60             """ 초 / 60의 나머지는 초 """

print(min, sec)
print(str(time)+"은 "+str(min)+"분 "+str(sec)+"초 입니다.")
print("{0}초는 {1}분 {2}초 입니다.".format(time, min, sec))
print("{input}초는 {outMin}분 {outSec}초 입니다" ＼ .format(input = time, outMin = min, outSec = sec))
