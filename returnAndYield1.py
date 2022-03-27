# Exiting a function

lst = [1, 2, 3, 4, 5]

# using yield for a generator
def twice_the_list(lst):
  for i in range(len(lst)):
    lst[i] *= 2
  yield lst

print (twice_the_list(lst))
# gives a generator stored at a memory address

print (list(twice_the_list(lst)))
# [[2, 4, 6, 8, 10]]
