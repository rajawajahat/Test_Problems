my_list = [["mouse", 4.5, 4.3, 49], [8, 4, 6], ['a']]

for list_ in enumerate(my_list):
    print("List: {}".format(str(list_[0])))
    
    sum_ = sum([each for each in list_[1] if isinstance(each, int) or isinstance(each, float)])
    print("Sum:  {}".format(str(sum_)))