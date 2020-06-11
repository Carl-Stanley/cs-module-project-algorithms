'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    if n == 0:
        return 1
    elif n < 1:
        return 0
    else:

        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)


   
    eating_cookies(n-1)
    
    eating_cookies(n-2)
   
    eating_cookies(n-3)


if __name__ == "__main__":     
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")