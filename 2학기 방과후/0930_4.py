num=int(input("시프트할 숫자는?"))
shift=int(input("출력할 횟수는?"))

for i in range(1,shift+1):
    result=num<<i
    print("%d << %d == %d"% (num,i,result))

for i in range(1,shift+1):
    result= num>>i
    print("%d >> %d = %d" % (num,i,result))
