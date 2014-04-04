def sqrt_1(x, kmax):
  s = 1.
  for k in range(kmax):
    s = 0.5 * (s + x/s)
  return s