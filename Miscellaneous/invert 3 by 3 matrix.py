a1=eval(input('a1='))
a2=eval(input('a2='))
a3=eval(input('a3='))
b1=eval(input('b1='))
b2=eval(input('b2='))
b3=eval(input('b3='))
c1=eval(input('c1='))
c2=eval(input('c2='))
c3=eval(input('c3='))

def det(a1,a2,a3,b1,b2,b3,c1,c2,c3):
    result=a1*(b2*c3-b3*c2)-a2*(b1*c3-b3*c1)+a3*(b1*c2-b2*c1)
    print('The determinent is')
    print (result) 

def cof(a1,a2,a3,b1,b2,b3,c1,c2,c3):
    na1=b2*c3-b3*c2
    na2=-(b1*c3-b3*c1)
    na3=b1*c2-b2*c1
    nb1=-(a2*c3-a3*c2)
    nb2=a1*c3-a3*c1
    nb3=-(a1*c2-a2*c1)
    nc1=a2*b3-a3*b2
    nc2=-(a1*b3-a3*b1)
    nc3=a1*b2-a2*b1
    print ('The cofactor matrix is')
    print ('|',na1,na2,na3,'|')
    print ('|',nb1,nb2,nb3,'|')
    print ('|',nc1,nc2,nc3,'|')

def trp(a1,a2,a3,b1,b2,b3,c1,c2,c3):
    print ('The transpose matrix is')
    print ('|',a1,b1,c1,'|')
    print ('|',a2,b2,c2,'|')
    print ('|',a3,b3,c3,'|')

det(a1,a2,a3,b1,b2,b3,c1,c2,c3)
print ('''
       ''')
cof(a1,a2,a3,b1,b2,b3,c1,c2,c3)
print ('''
       ''')
trp(a1,a2,a3,b1,b2,b3,c1,c2,c3)
print ('''
       ''')       
def coftrp(a1,a2,a3,b1,b2,b3,c1,c2,c3):
    na1=(b2*c3-b3*c2)/(a1*(b2*c3-b3*c2)-a2*(b1*c3-b3*c1)+a3*(b1*c2-b2*c1))
    na2=-(b1*c3-b3*c1)/(a1*(b2*c3-b3*c2)-a2*(b1*c3-b3*c1)+a3*(b1*c2-b2*c1))
    na3=(b1*c2-b2*c1)/(a1*(b2*c3-b3*c2)-a2*(b1*c3-b3*c1)+a3*(b1*c2-b2*c1))
    nb1=-(a2*c3-a3*c2)/(a1*(b2*c3-b3*c2)-a2*(b1*c3-b3*c1)+a3*(b1*c2-b2*c1))
    nb2=(a1*c3-a3*c1)/(a1*(b2*c3-b3*c2)-a2*(b1*c3-b3*c1)+a3*(b1*c2-b2*c1))
    nb3=-(a1*c2-a2*c1)/(a1*(b2*c3-b3*c2)-a2*(b1*c3-b3*c1)+a3*(b1*c2-b2*c1))
    nc1=(a2*b3-a3*b2)/(a1*(b2*c3-b3*c2)-a2*(b1*c3-b3*c1)+a3*(b1*c2-b2*c1))
    nc2=-(a1*b3-a3*b1)/(a1*(b2*c3-b3*c2)-a2*(b1*c3-b3*c1)+a3*(b1*c2-b2*c1))
    nc3=(a1*b2-a2*b1)/(a1*(b2*c3-b3*c2)-a2*(b1*c3-b3*c1)+a3*(b1*c2-b2*c1))
    round(na1,3)
    round(na2,3)
    round(na3,3)
    round(nb1,3)
    round(nb2,3)
    round(nb3,3)
    round(nc1,3)
    round(nc2,3)
    round(nc3,3)
    print ('The inverse matrix is' )
    print ('|',na1,nb1,nc1,'|')
    print ('|',na2,nb2,nc2,'|')
    print ('|',na3,nb3,nc3,'|')

coftrp(a1,a2,a3,b1,b2,b3,c1,c2,c3)



