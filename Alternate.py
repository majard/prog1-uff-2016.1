import random

A = []
B = []
C = []

for a in range(random.randint(2, 20)):
  A.append(random.randint(0, 100))
for a in range(random.randint(2, 20)):
  B.append(random.randint(0, 100)
for a in range(len(A) + len(C)):
  C.append(0)

index = 0
i = 0
j = 0

while index < len(C):
	if len(A) <= len(B):
		if i < len(A):
			C[index] = A[i]
			index += 1
			i += 1

		if j < len(B):
			C[index] = B[j]
			index += 1
			j += 1
	else:
		if j < len(B):
			C[index] = B[j]
			index += 1
			j += 1

		if i < len(A):
			C[index] = A[i]
			index += 1
			i += 1

print('A: '.format(A))
print('B: '.format(B))
print('C: '.format(C))
