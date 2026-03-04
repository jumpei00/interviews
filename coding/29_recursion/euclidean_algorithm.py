def gcd(a: int, b: int) -> int:
	if a < b:
		a, b = b, a
	
	r = a % b
	if r == 0:
		return b
	
	return gcd(b, r)