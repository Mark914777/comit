def squre_digits(num):
 res = []
 num = str(num)
 for dight  in num:
  squre =int(dight)**2
  squre = str(squre)
  res.append(squre)
 res = "".join(res)
 return  int(res)

print(squre_digits(9119))