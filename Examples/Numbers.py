#!/usr/bin/python

#Numbers
counter = 100                # An integer assignment
miles   = 1000.012           # A floating point

#string
name    = "Hello John"       # A string

#list, tuple, dict
list_var = [1,2,counter,miles,name]
tuple_var = ('jan', 'feb', 1.01)
dict_var = {'name': 'john','code':6734, 'dept': 'sales'}


print "counter = ", counter , " Data Type of counter:" , type(counter)
print "miles = ", miles ,"Data Type of miles:" , type(miles)
print "name =", name , "Data Type of name:" , type(name)
print "\n"
print "list_var = ", list_var , "Data type of list:", type(list_var)
print "tuple_var =", tuple_var , "Data Type of tuple_var:" , type(tuple_var)
print "dict_var = ", dict_var , "Data Type of dict_var:" , type(dict_var)


#string operations
print name[0]
print name[0:2]

#List operations
list_var.insert(2, "Inserted this string")
print "list_var = ", list_var
list_var[2] = 2000
print "list_var = ", list_var
list_var[2] = dict_var
print "list_var = ", list_var


#we can't do tuple operations. Tuple is a read only list
#tuple_var[2] = 2000


#dict operations
tinydict = {2 : "feb", "check" : "TRUE", 0 : "none"}
print "tinydict = ", tinydict
tinydict[1]="jan"
print "tinydict = ", tinydict

print "Key of tinydict  =" , tinydict.keys()   # returns a list
print "Value of tinydict =" ,tinydict.values() # returns a tuple

#Data type conversion

dict_to_list = list(tinydict) #dict to list; only the keys of dict is converted to list
print "dict_to_list = " , dict_to_list


dict_to_tuple = tuple(tinydict) #dict to tuple; only the keys of dict is converted to tuple
print "dict_to_tuple = ", dict_to_tuple

'''
list_to_dict = dict(dict_to_list) #list to dict ; not possible
print "list_to_dict = ", list_to_dict
tuple_to_dict = dict(dict_to_tuple) #tuple to dict ; not possible
print "tuple_to_dict = ", tuple_to_dict
'''

tupleV = ((1,2),(3,4))
listV = [[5,6],[4,5]]

tuple_to_dict = dict(tupleV)
print "tuple_to_dict" , tuple_to_dict , "\n"
list_to_dict = dict(listV)
print "List to dict" , list_to_dict , "\n"

tryint = int(miles) #float to int
print "miles = " , miles
print "tryint = ", tryint





