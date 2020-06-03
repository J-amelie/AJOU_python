denominator = int(input('분모를 입력하세요'))
numerator = int(input('분자를 입력하세요'))

if numerator > denominator : print('가분수입니다.')

print('ans = {} /{} = {} '\
      .format(numerator, denominator, numerator/denominator))