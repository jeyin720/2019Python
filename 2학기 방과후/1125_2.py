myTurtle, tX,tY,tColor, tSize,tShape=[None]*6
shapeList=[]
playerTurtles=[]
swidth, sheight=500,500

if __name__=="__main__":
    turtle.title('거북 리스트 활용')
    turtle.setup(width=swidth+50,height=sheight+50)
    turtle.screensize(swidth,sheight)

    shapeList=turtle.getshapes()

    for i in range(0,100):
        random.shuffle(shapeList)
        myTurtle.turtle.Turtle(shapeList[0])
        tX=random.randrange(-swidth/2,swidth/2)
        tY=random.randrange(-sheight/2,sheight/2)
        r=rnadom.random(); g=random.random(); b=
