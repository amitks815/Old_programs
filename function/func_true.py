def is_avail(grp,n):
	for data in grp:
		if data==n:
			return True
		
	return False
		


print(is_avail([1,2,3,5],2))