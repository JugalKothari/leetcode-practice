#Brute Force Solution
def canplacecows(n, dist, cows):
	placed_cows=1
	last_at=locations[0]
	for i in range(1, n):
		if locations[i]-last_at>=dist:
			last_at=locations[i]
			placed_cows+=1
		if placed_cows>=cows:
			return True
	return False


def solvecowproblem(n, c, locations):
	locations.sort()
	limit=locations[n-1]-locations[0]
	for i in range(1, limit+1):
		if not canplacecows(n, i, c):
			return i-1


test_cases = int(input())
for i in range(test_cases):
	n, c = list(map(int, input().strip().split()))
	locations=[]
	for i in range(n):
		locations.append(int(input()))
	
	print(solvecowproblem(n, c, locations))
