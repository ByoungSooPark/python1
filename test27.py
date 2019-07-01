tt1 = ((1,2,3),[1,[1,('a','b','c'),3],3],30)

#print(tt1)

tt2 = [1,2,(1,[4,4,4],3)]
#print(tt2)
import operator
tranList = []
tt3 = {'이름':'홍길동','지역':'천안','연령':'20대','보유차량':('그랜져','아반테')}
#tt3 = {0:'홍길동',1:'천안',2:'20대'}
tranList = sorted(tt3.items(),key=operator.itemgetter(0))
print(tranList)