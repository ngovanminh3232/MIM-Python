if __name__ == '__main__':
    numm = 600851475143
    largestFact = 0
    print(test(numm))





def test(numm):
    largestFact = 0
    for i in range(2,numm):
        if numm % i == 0: # It is a divisor
            isPrime = True
            for j in range(2,i):
                if i % j == 0:
                    isPrime = False
                    break
            if isPrime:
                largestFact = i

    return largestFact