"""
    Project 03. 세 수 가운데 가장 큰 수 찾기

    COPYRIGHT @ AJOU University
    Author        : 이유성
    Details       : 세 개의 정수를 입력 받아 가장 큰 수를 출력한다.
    Input         : 세 개의 정수
    Output        : 입력된 수 가운데 가장 큰 수
    File Name     : project03.py
    History       : (1차) 2020년 05월 29일
"""
A = int(input('첫 번째 정수 : '))
B = int(input('두 번째 정수 : '))
C = int(input('세 번째 정수 : '))

if (A > B) :
    max = A
else :
    max = B
if (max > C) :
    print("큰 수는", max)
else :
    print("큰 수는", C)