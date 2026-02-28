import unittest
import random
from hypothesis import given, strategies as st, settings
from heapsort import heapsort

class TestHeapsort(unittest.TestCase):
    
    def test_empty_list(self):
        self.assertEqual(heapsort([]), [])
    
    def test_single_element(self):
        self.assertEqual(heapsort([5]), [5])
    
    def test_sorted_list(self):
        self.assertEqual(heapsort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
    
    def test_reverse_sorted(self):
        self.assertEqual(heapsort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
    
    def test_duplicates(self):
        self.assertEqual(heapsort([3, 1, 2, 1, 3]), [1, 1, 2, 3, 3])
    
    def test_negative_numbers(self):
        self.assertEqual(heapsort([-5, -1, -3, 0, 2]), [-5, -3, -1, 0, 2])
    
    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            heapsort([1, 'a', 3])
    
    @given(st.lists(st.integers(), max_size=100))
    @settings(max_examples=100)
    def test_sorts_correctly(self, arr):
        result = heapsort(arr.copy())
        expected = sorted(arr)
        self.assertEqual(result, expected)
    
    @given(st.lists(st.integers(), min_size=1, max_size=100))
    @settings(max_examples=50)
    def test_same_length(self, arr):
        result = heapsort(arr.copy())
        self.assertEqual(len(result), len(arr))
    
    @given(st.lists(st.integers(), min_size=2, max_size=100))
    @settings(max_examples=50)
    def test_idempotent(self, arr):
        sorted_once = heapsort(arr.copy())
        sorted_twice = heapsort(sorted_once.copy())
        self.assertEqual(sorted_once, sorted_twice)
    
    def bubble_sort(self, arr):
        n = len(arr)
        arr = arr.copy()
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr
    
    def insertion_sort(self, arr):
        arr = arr.copy()
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
    
    @given(st.lists(st.integers(), max_size=50))
    @settings(max_examples=20)
    def test_against_bubble_sort(self, arr):
        heap_result = heapsort(arr.copy())
        bubble_result = self.bubble_sort(arr.copy())
        self.assertEqual(heap_result, bubble_result)
    
    @given(st.lists(st.integers(), max_size=50))
    @settings(max_examples=20)
    def test_against_insertion_sort(self, arr):
        heap_result = heapsort(arr.copy())
        insertion_result = self.insertion_sort(arr.copy())
        self.assertEqual(heap_result, insertion_result)
    
    def test_very_large_list(self):
        arr = list(range(1000, 0, -1))
        result = heapsort(arr.copy())
        self.assertEqual(result, list(range(1, 1001)))
    
    def test_all_same_elements(self):
        arr = [7] * 100
        result = heapsort(arr.copy())
        self.assertEqual(result, arr)
    
    def test_floating_point(self):
        arr = [3.14, 1.41, 2.71, 0.0]
        result = heapsort(arr.copy())
        self.assertEqual(result, sorted(arr))
    
    def test_presorted_with_gaps(self):
        arr = [1, 100, 2, 99, 3, 98]
        result = heapsort(arr.copy())
        self.assertEqual(result, sorted(arr))

if __name__ == '__main__':
    unittest.main()
