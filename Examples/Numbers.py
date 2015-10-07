#!/usr/bin/python

counter = 100                # An integer assignment
miles   = 1000.0             # A floating point
name    = "Hello John"       # A string

tuple_var = (1, 2,3, 4)
dict_var = {'name': 'john','code':6734, 'dept': 'sales'}

print "counter = ", counter , " Data Type of counter:" , type(counter)
print "miles = ", miles ,"Data Type of miles:" , type(miles)
print "name =", name , "Data Type of name:" , type(name)
print "tuple_var =", tuple_var , "Data Type of tuple_var:" , type(tuple_var)
print "dict_var = ", dict_var , "Data Type of dict_var:" , type(dict_var)


print name[0]
print name[0:2]