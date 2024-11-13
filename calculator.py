class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        result = 0
        for i in range(abs(b)):
            result = self.add(result, abs(a))

        if (a < 0 and b > 0) or (a > 0 and b < 0):
            result = -result

        return result

    def divide(self, a, b):
        if b == 0 or a == 0:
            return 0
        elif b < 0 and a <0:
            b = -b 
            a = -a
            result = 0
            while a >= b:
                a = self.subtract(a, b)
                result += 1
            return result
        elif b < 0:
            b = -b
            result = 0
            while a >= b:
                a = self.subtract(a, b)
                result += 1
            return -result
        elif a < 0:
            a = -a
            result = 0
            while a >= b:
                a = self.subtract(a, b)
                result += 1
            return -result
        else:
            result = 0
            while a >= b:
                a = self.subtract(a, b)
                result += 1
            return result
    
    def modulo(self, a, b):
        if b == 0 and a > 0:
            return a
        elif b>0 and a >0:
            while a >= b:
                a = a-b
            return a
        elif b<0 and a >0:
            while a >= b:
                a = a-b
            return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(-100, -150))
    print("Example: subtraction: ", calc.subtract(-4, -2))
    print("Example: multiplication: ", calc.multiply(2, -3))
    print("Example: division: ", calc.divide(-10, 2))
    print("Example: modulo: ", calc.modulo(10, 90))