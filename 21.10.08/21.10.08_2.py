##연산자##

s1,s2,s3='100','100.123','999999999999'
print(int(s1)+1, float(s2)+1, int(s3)+1) #숫자를 정수(int())또는, 실수(float()) 변경
print(float(s1)+1)   #float(정수) - 소수점 한자리까지만 출력

'''
a=100; b=100.123
print(str(a)+'1', str(b)+'1') #숫자를 문자열로변환(str)
'''
#대입연산자#
a=10
a+=5;print(a) #10+5
a-=5;print(a) #15-5
a*=5;print(a) #10*5
a/=5;print(a) #50/5
a//=5;print(a) #10//5 (몫)
a%=5;print(a) #2/5 (나머지)
a**=5;print(a) #2^5
