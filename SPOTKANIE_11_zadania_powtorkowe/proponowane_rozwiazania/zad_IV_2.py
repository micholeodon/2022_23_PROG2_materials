class Dec2Bit:

    def convert(n):
        y = ""
        
        x = n
        while x > 0:
            # print(x) # test
            b = str(x%2)
            y += b
            x //= 2
        
        y = y[::-1]
        return y


print(Dec2Bit.convert(31))