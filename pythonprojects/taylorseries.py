
import math

def func_cos(x, n):
    
    cos_approx = 0
    
    for i in range(n):
        
        coef = (-1)**i
        num = x**(2*i)
        denom = math.factorial(2*i)
        cos_approx += ( coef ) * ( (num)/(denom) )
    
    return cos_approx

real_value = 0.809016994
angle_rad = (math.radians(36))
out = func_cos(angle_rad,2)
print("Real value: ",real_value)
print("Estimated value: ",out)


truncation_error = real_value - out

print("Truncation Error: " , truncation_error)


