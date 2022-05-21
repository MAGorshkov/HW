print ("Введите продолжительность в секундах:")
duration=int(input())
d=duration//86400
h=(duration-d*86400)//3600
m=((duration-d*86400)%3600)//60
s=((duration-d*86400)%3600)%60
if d!=0:
  print (d, ' дня', h, " часов", m, " мин", s, ' сек.')
elif d==0 and h!=0:
  print (h, " часов", m, " мин", s, ' сек.')
elif d==0 and h==0 and m!=0:
  print (m, " мин", s, ' сек.')
else:
  print (s, ' сек.')