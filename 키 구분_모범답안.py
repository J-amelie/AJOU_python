'''
    Project w5-02. 여러 조건 2

    COPYRIGHT @ AJOU University

    Author    :홍길동
    Details   :AjouLand 자동차 서킷의 규정에 따라 탑승가능 여부를 출력한다.
    Input     :키와 연령
    Output    :상세 탑승 가능 여부
    File Name :project_w3_3.py
    History   :(1차) 2020년 06월 01일
'''

height = int(input('키를 입력하세요 : '))
age = int(input('나이를 입력하세요 : '))

if 130 <= height <= 190 and 15 <= age <= 70 :
    print('탑승이 가능합니다.')
else :
    if  130 <= height <= 190 and (age < 15 or age > 70) :
        if age < 15 :
            print('15세 미만은 탑승이 불가능합니다.')
        else:
            print('70세 초과는 탑승이 불가능합니다.')
    elif (height < 130 or height > 190) and 15 <= age <= 70 :
        if height < 130 :
            print('130cm 미만은 탑승이 불가능합니다.')
        else :
            print('190cm 초과는 탑승이 불가능합니다.')
    else :
        print('키와 연령 모두 기준에 충족되지 않습니다.')