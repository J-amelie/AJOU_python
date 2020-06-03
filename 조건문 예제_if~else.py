denominator = int(input('분모를 입력하세요 : '))
numerator = int(input('분자를 입력하세요 : '))

if denominator == 0 :
    print('분모가 0입니다.')

else :
    if numerator > denominator :
        print('가분수입니다.')
    else :
        print('진분수입니다.')

    print('ans = {} / {} = {}'\
          .format(numerator, denominator, numerator/denominator))