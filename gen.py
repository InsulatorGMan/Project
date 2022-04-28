import random as rng
#Defined Actions
a1 = "w"
a2 = "a"
a3 = "s"
a4 = "d"
a5 = "space"
a6 = "lookDown"
a7 = "lookUp"
a8 = "lookRight"
a9 = "lookLeft"
a10 = "e"
def logic():
  e = rng.randint(1,10)
  if e==1:
    o = a1
  if e==2:
    o = a2
  if e==3:
    o = a3
  if e==4:
    o = a4
  if e==5:
    o = a5
  if e==6:
    o = a6
  if e==7:
    o = a7
  if e==8:
    o = a8
  if e==9:
    o = a9
  if e==10:
    o = a10
  else:
    o = "Error"
logic()
