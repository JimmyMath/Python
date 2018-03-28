from fractions import Fraction
def productExceptSelf(nums, m):
    S, T = 1, 0
    for x in nums:
        S *= x
        T += Fraction(1, x)
    return (S * T.numerator / T.denominator) % m
