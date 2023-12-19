#!/usr/bin/python3


# function definition
def list_division(my_list_1, my_list_2, list_length):
    """ Divides element by element 2 lists.

    param:
        my_list_1: First list
        my_list_2: Second list

    :returns: A list containing the result of the divison
    """
    div_list = []

    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print('division by 0')
            result = 0
        except TypeError:
            print('wrong type')
            result = 0
        except IndexError:
            print('out of range')
            result = 0
        finally:
            div_list.append(result)

    return div_list
