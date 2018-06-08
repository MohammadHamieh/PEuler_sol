def fibonacii():
    l =[1,1]
    i = 0
    x = 1
    sum = 0
    while l[x]<4000000:
          l.append(l[i]+l[x])
          if l[x+1]%2==0:
	     sum+=l[x+1]
          i=i+1
          x=x+1


    print (l)
    print ("sum ="+str( sum))
fibonacii()
