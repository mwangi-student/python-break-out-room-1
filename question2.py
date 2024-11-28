def is_sorted(list):
    return list == sorted(list) # mwangi - the sorted() function is an in-built python function for sorting data. By default sort functions sort data in an ascending order.
# Also the sorted() method sorts the data and returns a new list without modifying the original list.

#returns False
print(is_sorted([2,4,5,3,1,6])) 
 #returns true
print(is_sorted([1,2,3,4,5,6]))


#sorting a list in descending order.
new_list= [2,8,3,9,5,3,0]
new_list.sort(reverse=True)

print(new_list) 