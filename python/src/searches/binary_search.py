
def binary_search_recursive_h(search_list, search_value, left_bound, right_bound):

    # Base case, item not found.
    if right_bound < left_bound:
        return None 

    # Calculate the mid point.
    mid_point = (right_bound + left_bound) // 2

    if search_list[mid_point] == search_value:
        return mid_point
    elif search_list[mid_point] < search_value: 
        return binary_search_recursive_h(search_list, 
                                         search_value, 
                                         mid_point + 1,
                                         right_bound)
    else:
        # elif search_list[mid_point] > search_value:
        return binary_search_recursive_h(search_list,
                                         search_value, 
                                         left_bound,
                                         mid_point - 1)


def binary_search_recursive(search_list, search_value):

    return binary_search_recursive_h(search_list, search_value, 0, len(search_list) - 1)


def binary_search(search_list, search_value):

    # Boundaries for our search window. 
    left_bound = 0
    right_bound = len(search_list) - 1

    while (right_bound >= left_bound): 
        # Find the mid point of the search window.
        mid_point = (right_bound + left_bound) // 2

        if search_list[mid_point] == search_value:
            return mid_point
        elif search_list[mid_point] < search_value: 
            left_bound = mid_point + 1
        else:
            # elif search_list[mid_point] > search_value:
            right_bound = mid_point - 1

    return None

def main():
    pass

if __name__ == '__main__':
    main()