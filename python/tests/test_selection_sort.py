# test_selection_sort.py

from selection_sort import selection_sort

def test_sort_positive_numbers():
    assert selection_sort([3, 1, 2]) == [1, 2, 3], "Should sort positive numbers"

def test_sort_negative_numbers():
    assert selection_sort([-2, -3, -1]) == [-3, -2, -1], "Should sort negative numbers"

def test_sort_mixed_numbers():
    assert selection_sort([0, -1, 1]) == [-1, 0, 1], "Should sort mixed numbers"

def test_empty_array():
    assert selection_sort([]) == [], "Should handle empty array"

def test_array_with_one_element():
    assert selection_sort([1]) == [1], "Should handle single-element array"

def test_array_with_repeat_elements():
    assert selection_sort([-1, 0, 50, -20, 0, 50, -1, 100]) == [-20, -1, -1, 0, 0, 50, 50, 100], "Should handle repeated elements"