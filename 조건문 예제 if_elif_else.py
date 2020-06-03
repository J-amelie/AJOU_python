custGrade = input('회원 등급을 입력하세요 : ')
orgPrice = int(input('제품의 가격을 입력하세요 : '))

if custGrade == 'Diamond' :
    discRate = 0.4
elif custGrade == 'Gold' :
    discRate = 0.3
elif custGrade == 'Silver' :
    discRate = 0.2
else:
    discRate = 0

price = orgPrice - (orgPrice * discRate) #할인율 계산
print('제품의 가격은 {}원입니다. 할인율 : {} = {}'\
      .format(price, custGrade,discRate))