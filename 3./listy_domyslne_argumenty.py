def my_broken_function(my_list=[]):
    my_list.append(3)
    print(my_list)

my_broken_function()
my_broken_function([1, 2])
my_broken_function()
#domyslne argumenty

def my_working_function(my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(3)
    print(my_list)

my_working_function()
my_working_function([1, 2])
my_working_function()