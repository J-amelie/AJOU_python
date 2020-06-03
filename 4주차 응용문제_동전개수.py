"""
project 02.가장 작은 수의 동전

COPYRIGHT (c) AJOU University
Author    : 홍길동
Details   : 금액을 입력받아 가장 작은 수의 동전으로 변환하는 프로그램
Input     : 교환할 금액
Output    : 각 동전 단위별 개수
File Name : project02.py
History   : (1차)  2020년 05월 22일
"""

tatalMoney = input("금액을 투입하세요  : ")
toatlMoney = int(totalMoney)
fiveH = totalMoney // 500
remainder = totalMoney % 500

oneH = remainder // 100
remainder = remainder % 100

fifty = remainder // 50
remainder = remainder % 50

tem = remainder // 10
reaminder % 10

print("500원 {0}개, 100원 {1}개, 50원 {2}개, 10원 {3}개" \ .format(fiveH, oneH, fifty, ten))