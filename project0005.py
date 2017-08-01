a = [1]

for i in range(2,21):
  for j in a:
    if i%j==0:
      i=i/j
  a.append(i)

prod=1
for n in a:
  prod*=n

print prod
