num =int(input("정수를 입력하세요"))
sum=0

while(num>0):
    sum+=num%10;
    num//=10;

print("자릿수의 합:",sum)
