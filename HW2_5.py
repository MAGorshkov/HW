ls=[1.5,23.4,45,2.45,9.08,10.32,20,23.43,15.89,19.43,16.32,20.34]
r=0
kk=0
new_line=''
ls_new=[]
ls_new2=[]

def rub (e):
  r_n=0
  ls_str=e.split(' ')
  r_n=int(ls_str[0])
  return r_n

for i in ls:
  r=int(i)
  kk=int((i-r)*100)
  if len(str(kk))<2:
    new_line=new_line+str(r)+' руб '+'0'+str(kk) +' коп'+','
    ls_new.append(str(r)+' руб '+'0'+str(kk) +' коп')
  else:
    new_line=new_line+str(r)+' руб '+str(kk) +' коп'+','
    ls_new.append(str(r)+' руб '+str(kk) +' коп')
print("Цены в строку, в формате 'руб' и 'коп':", new_line)
print ("Индификатор списка до сортировки:", id(ls_new))
ls_new.sort(key=rub)
print ("Индификатор списка после сортировки:", id(ls_new))
print ('Список сортировка по возрастанию:', ls_new)
ls_new.sort(reverse=True, key=rub)
for i1 in ls_new:
  ls_new2.append(i1)
print ('Список сортировка по убыванию:', ls_new2)
print ('Пять самых больших цен:', ls_new2[0:5])
ls_new2.sort(key=rub)
print ('Пять самых больших цен по возрастанию:', ls_new2[-5:])