ls=['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
str_r=''
str_name=''
ls_words=[]
name=''
for i in ls:
  str_r=i[::-1]
  ls_words=str_r.split()
  name=ls_words[0]
  name=name[::-1]
  print('Привет,'+'', name.lower().capitalize()+'!') 