from src.searches.binary_search import *

def test_binary_search():

    int_list = [2, 4, 6, 8, 10, 15, 75]
    
    # Middle of list
    assert binary_search(int_list, 8) == 3 
    
    # Beginning of list
    assert binary_search(int_list, 2) == 0

    # End of list
    assert binary_search(int_list, 75) == len(int_list) - 1 

    # Value not in list
    assert binary_search(int_list, 45) == None

def test_binary_search_recursive():

    int_list = [2, 4, 6, 8, 10, 15, 75]
    
    # Middle of list
    assert binary_search_recursive(int_list, 8) == 3 
    
    # Beginning of list
    assert binary_search_recursive(int_list, 2) == 0

    # End of list
    assert binary_search_recursive(int_list, 75) == len(int_list) - 1 

    # Value not in list
    assert binary_search_recursive(int_list, 45) == None

