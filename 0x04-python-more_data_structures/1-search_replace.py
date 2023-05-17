#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [
        int(i) for i in (",".join([str(num) for num in my_list]).
                         replace("{},".format(search), "{},".
                         format(replace)).split(","))
    ]
