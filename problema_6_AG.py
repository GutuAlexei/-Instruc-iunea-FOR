#6.1
n=eval(input('introduceti numarul='))
s1=0
for t in range  (1, n+1):
     s1+=t
print(s1)

#6.2
n=eval(input('introduceti numarul='))
s2=0
for t in range  (1, n+1):
     s2+=(t-1)*t
print(s2)

#6.3
n = eval(input('introduceti numarul='))
s3=0
p = 1
for t in range(1,n+1):
	p*=t
	s3+=p	
print(s3)

#6.4
n = eval(input('introduceti numarul='))
s4=0
for t in range(12,n*10+3,10):
	s4+=t
print(s4)

#6.5
n=eval(input('introduceti numarul=')) 
s5=0 
for t in range (1, n+1): 
    s5+=t/(t+1) 
print(s5)

