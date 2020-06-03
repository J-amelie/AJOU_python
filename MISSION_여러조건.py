height = int(input('키를 입력해주세요 : '))

if(height > 130 and height < 190) :
    print ('탑승이 가능합니다.')
elif  (height < 130 ):
    print('130cm 미만은 탑승이 불가능합니다.')
if(height > 190) :
    print( ' 190cm 초과는 탑승이 불가능합니다.')
