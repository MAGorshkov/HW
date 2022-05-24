ls=['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
c_num=0
newline=''
for i in ls:
  try:
    if int(i)== float (i):
      print(i)
      if int (i)<10:
        ls[c_num]='"'+'0'+i+'"'
      else:
        ls[c_num]='"'+i+'"'
  except:
    i=i
  if '+' in i:
    ls[c_num]= '"'+'+' + '0'+i[1] + '"'
  c_num=c_num+1
for i2 in ls:
  newline=newline+i2+' '
print (newline)