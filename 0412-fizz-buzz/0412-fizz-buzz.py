class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        def Jjack(i):
            if (i % 3) == 0 and (i % 5) == 0:
                
                return "FizzBuzz"
            elif i% 3 == 0:
                return "Fizz"
            elif i%5 == 0:
                return "Buzz"
            else :
                return str(i)
        answer = []
        for i in range(1, n+1) :
            answer.append(Jjack(i))
        
        return answer