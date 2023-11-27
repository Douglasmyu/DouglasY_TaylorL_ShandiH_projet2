f = open("input.txt",'r')
import dynamic.py
import exhaustive.py

for i in range(0,10):
  n = f.readline()
  s_and_v = f.readline()
  amount = f.readline()
  f.readline()
  max_amount_exhaustive = exhaustive(n, s_and_v, amount)
  max_amount_dynamic = dynamic(n, s_and_v, amount)
  
f.close()
