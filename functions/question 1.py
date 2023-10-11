# multiply all numbers
def multiply_all_numbers(output):
  sum= 1
  for m in output:
     sum *= m
  return sum
print (multiply_all_numbers((8,2,3,-1,7)))
