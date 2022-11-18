def solution(x, y): #Bunny Worker
    val=0
    for i in range(0,x+1):
        val+=i
    if(y>=1):
        for i in range(0,y-1):
            val+=(x+i)
    print(val)
    return str(val)
  
solution(6, 1)
