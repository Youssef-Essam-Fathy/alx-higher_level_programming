def test_find_peak():
    # Test case 1: List with a peak in the middle
    list1 = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
    assert find_peak(list1) == 6

    # Test case 2: List with a peak at the beginning
    list2 = [6, 5, 4, 3, 2, 1]
    assert find_peak(list2) == 6

    # Test case 3: List with a peak at the end
    list3 = [1, 2, 3, 4, 5, 6]
    assert find_peak(list3) == 6

    # Test case 4: Empty list
    list4 = []
    assert find_peak(list4) is None

    # Test case 5: List with only one element
    list5 = [2]
    assert find_peak(list5) == 2

    # Test case 6: List with two elements
    list6 = [2, 4]
    assert find_peak(list6) == 4

test_find_peak()