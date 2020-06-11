'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    
    a = [ 0 for i in range(arr.count(0))]
    x = [i for i in arr if i != 0]
    x.extend(a)
    return(x)

if __name__ == '__main__':
     
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")