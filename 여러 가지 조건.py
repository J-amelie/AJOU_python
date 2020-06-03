addr = input('현재 주민등록상의 거주 장소를 입력하세요 : ')
age = int(input('연령을 입력하세요 : '))

if addr == 'Ajou' and age >= 19 :
    print('선거권이 있습니다.')
elif addr == 'Ajpu' and age < 19 :
    print('미성년자로 선거권이 없습니다.')
elif addr != 'Ajou' and age >= 19 :
    print('Ajou시민이 아닙니다.')
else :
    print('Ajou시민이 아니고, 미성년자입니다.')