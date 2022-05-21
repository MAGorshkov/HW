for i in range (1,21):
  if i<5 and i!=1:
      print (i,'процента')
  elif i>5:
    print (i,'процентов')
  elif i==1:
    print (i,'процент')
for i1 in range (21,101): 
  sec_num=int(str(i1)[1])
  if sec_num==0 or sec_num==5 or sec_num==6 or sec_num==7 or sec_num==8 or sec_num==9:
    print (i1,'процентов')
  elif sec_num==2 or sec_num==3 or sec_num==4:
    print (i1,'процента')
  else:
    print (i1,'процент')
