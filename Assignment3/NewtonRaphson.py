def NewtonRaphson(fpoly, a, tolerance = .00001):
    """Given a set of polynomial coefficients fpoly
    for a univariate polynomial function,
    e.g. (3, 6, 0, -24) for 3x^3 + 6x^2 +0x^1 -24x^0,
    find the real roots of the polynomial (if any)
    using the Newton-Raphson method.
    a is the initial estimate of the root and
    starting state of the search
    This is an iterative method that stops when the
    change in estimators is less than tolerance.
    """
    t = float("inf")
    tries_limit = 50
    c = 0
    while t > tolerance and c<=tries_limit:
        slope = polyval(derivative(fpoly),a)
        k = polyval(fpoly,a)
        t = abs(k/slope)
        a = a - k/slope
        c += 1
    if c > tries_limit: # if there is no solution, return None
        return None
    return a
def polyval(fpoly, x):
    """polyval(fpoly, x)
    Given a set of polynomial coefficients from highest order to x^0,
    compute the value of the polynomial at x. We assume zero
    coefficients are present in the coefficient list/tuple.
    Example: f(x) = 4x^3 + 0x^2 + 9x^1 + 3 evaluated at x=5
    polyval([4, 0, 9, 3], 5)
    returns 548
    """
    res = 0
    for i in range(len(fpoly)):
        res += fpoly[i] * x**(len(fpoly)-1-i)
    return res
def derivative(fpoly):
    """derivative(fpoly)
    Given a set of polynomial coefficients from highest order to x^0,
    compute the derivative polynomial. We assume zero coefficients
    are present in the coefficient list/tuple.
    Returns polynomial coefficients for the derivative polynomial.
    Example:
    derivative((3,4,5)) # 3 * x**2 + 4 * x**1 + 5 * x**0
    returns: [6, 4] # 6 * x**1 + 4 * x**0
    """
    res = []
    for i in range(len(fpoly)-1):
        res.append(fpoly[i]*(len(fpoly)-1-i))
    return res
if __name__ == '__main__':
    print(NewtonRaphson([3,0,4,3,-50],-100))