ls_cube=[]
ls_div7=[]
for i  in range (1,1001):
  ls_cube.append (i**3)
for i1 in ls_cube:
  r_cube =str(i1)
  s_cube = 0
  for i2 in r_cube:
    s_cube=s_cube+int(i2)
  if s_cube%7==0:
    ls_div7.append(r_cube)
print (ls_div7)