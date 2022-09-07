class StringCalculator:
    def add(self, numbers):
        if numbers == '':
            return 0
        lst = list(map(int, numbers.split(",")))
        sum = 0
        for i in lst:
            sum += i
        return sum
        
obj = StringCalculator()
stri = input()
print(obj.add(stri))