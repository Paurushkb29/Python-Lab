# Write a Python program to print all Prime Numbers in an Interval.

class primeinterval:
    def prime(self,a,b):
        print("\nThe Prime Number in the Range are :-")
        for n in range(a,b+1):
            if n>1:
                for i in range(2,n):
                    if(n%i)==0:
                        break
                else:
                    print(n)

m1 = primeinterval()
lower_value = int(input("Enter lower Range :- \n"))
upper_value = int(input("Enter Upper Range :- \n"))
m1.prime(lower_value,upper_value)