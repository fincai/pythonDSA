# newton iterative method 
def square_root(n):
    root = n / 2   # guess
    EPS = 0.0001
    while True:
        lastroot = root
        root = 1/2 * (lastroot + n/lastroot)
        if abs(root - lastroot) < EPS:
            break
    return root


n = float(input())
print("square root of %f is %f" %(n, square_root(n)))
        
    
