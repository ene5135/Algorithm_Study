### Language Spec
e =  
    | e + e  
    | e - e  
    | e * e  
    | e / e  
    | - e   단, double unary 금지  
    | + e   단, double unary 금지  
    | (e)  
    | NUM  
  
NUM =  
    | NUMNUM    단, 0001 금지  
    | NUM.NUM   단, 1.100000 금지  
    | 0~9  
    
### 문제
주어진 수식(문자열)이 위 Expression의 정의에 부합하는지를 판단하여 Boolean을 반환하는 함수 isValid()를 작성하라.
