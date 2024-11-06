n = int(input())

kaibunrippous = []

def is343(suji):
  
  rippos_s = str(suji)

  if len(rippos_s) == 1:
    return True 
  
  kugiri = len(rippos_s)//2
  if rippos_s[:kugiri] == "".join(list(reversed(rippos_s[-kugiri:]))):
    return True
  else:
    return False
  
answer = 1

i = 1
while(i**3 <= n):
  if is343(i**3):
    answer = i**3
  i+=1

print(answer)