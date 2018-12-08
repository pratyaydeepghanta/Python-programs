"""
https://projecteuler.net/problem=2
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""
def fibo_even_bound(n):
    """
    A utility function to generate all even-valued terms in the Fibonacci sequence whose value do not exceed n
    Parameters
    n: a positive integer 
    """
    
    # Initialize the Fibonacci sequence
    F = [1, 2]
    index = 1

    while (F[index] <= n):
        F.append(F[index] + F[index-1])
        index += 1
    
    return [x for x in F if x % 2 == 0 and x <= n]

if __name__ == "__main__":
    n = 4 * pow(10, 6)
    print("Sum of the even-valued terms whose values do not exceed {} in Fibonacci sequence is {}".format(n, sum(fibo_even_bound(n))))
