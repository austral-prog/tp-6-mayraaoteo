def remove_elements(to_remove):

    if len(to_remove) == 0:
        return to_remove
    else:
        del to_remove[0]

        if len(to_remove) >= 5:
            del to_remove[3:5]
            return to_remove
        elif len(to_remove) == 4:
            del to_remove[3]
            return to_remove
        else:
            return to_remove


def add_elements(add_elements):

    add_elements.insert(0, "Pink")
    add_elements.append("Yellow")
    return add_elements


def is_empty(to_check):
   return len(to_check) == 0


def check_lists(list_to_compare1, list_to_compare2):
    
    if len(list_to_compare1) >= 3 and len(list_to_compare2) >= 3:
        return (list_to_compare1[2] == list_to_compare2[2])
    else:
        return False


def list_of_lists(to_modify):
    var1 = to_modify[0][0:2]
    var2 = to_modify[1][1:4]
    var3 = to_modify[2][-2:]
    return [var1, var2, var3]
