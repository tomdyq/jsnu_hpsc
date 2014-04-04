def sqrt1(x):
    s = 1.
    tol = 1.e-14
    for k in range(10000):
        print "Before iteration %s, s = %s" % (k, s)
        s0 = s
        s = 0.5 * (s + x/s)
        delta_s = s - s0
        if abs(delta_s / x) < tol:
            break
    print "After %s iterations, s = %s" % (k+1, s)
