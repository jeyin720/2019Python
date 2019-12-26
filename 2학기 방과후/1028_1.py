import turtle();
t=turtle.Turtle();

do=input("도형을 입력하시오(사각형 또는 원):");

if(do=="원"):
    r=int(input("원의 반지름: "))
    t.circle(r);
elif(do=="사각형"):
    w=int(input("가로: "))
    h=int(input("세로: "))

    t.forward(x)
    t.left(90)
    t.forward(h)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(h)
    t.left(90)
else:
    print("잘못 입력함요")
    
