# Difference between yeiid and return

lst = [1, 2, 3, 4, 5]

# example of return
def twice_of_list_function(lst):
    for i in range(len(lst)):
        lst[i] *= 2
    return lst

# example of yield
def twice_of_list(lst):
        for i in range(len(lst)):
            yield lst[i] * 2


for item in lst:
    print (item, end=' ')
print('')
# 1 2 3 4 5

for item in twice_of_list(lst):
    print (item, end=' ')
print ('')
# 2 4 6 8 10


for item in twice_of_list_function(lst):
    print (item, end=' ')
print ('')
# 2 4 6 8 10
