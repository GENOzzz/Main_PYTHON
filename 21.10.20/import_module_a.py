'''
##모듈 불러오기
import module

##메인코드부분
module.func1()        ##import module 로만 불러올 경우 함수 앞에 출처를 붙여야함.
module.func2()
module.func3()
'''
from module import func1,func2,func3 ##module의 func 1,2,3을 불러와라
##from module import *                        ##module의 모든 것을 불러와라
                                                                
##메인코드부분                                    ##from으로 module을 불러올 경우 함수 앞에 출처 생략가능
func1()
func2()
func3()
