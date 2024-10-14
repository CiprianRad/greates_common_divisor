def get_valid_input(): 
       while True: 
            try:
                n = int(input("Enter an integer:" ))
                #if type(n) is int:
                return n
            except ValueError:
                print("Invalid input. Enter a valid integer:")


        

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)



if __name__=="__main__":
    num1 = get_valid_input()
    num2 = get_valid_input()
    print("The greatest common divisor of the numbers is", gcd(num1, num2))
