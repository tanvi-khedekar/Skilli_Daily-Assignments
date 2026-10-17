def sumOfSeries(n: int, a: int, d: int) -> int:
  # standard AP sum formula: (n / 2) * (2*a + (n - 1) *d)
  return n * (2 * a + (n - 1) * d) // 2