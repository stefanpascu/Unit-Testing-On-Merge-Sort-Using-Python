from http.client import MULTI_STATUS
from unittest import TestCase
import unittest
import pandas
import timeit
import sys
import pytest
sys.path.append('C:\\Users\\Stefan-Liviu Pascu\\Documents\\GitHub\\Unit-Testing-On-Merge-Sort-Using-Python\\code')
from merge_sort import mergeSort as merge_sort
from merge_sort import merge
import random
    
class MergeSortTest(TestCase):
    
    # Black box tests
    @pytest.mark.blackbox
    def test_merge_sort(self):
        myList = [201, 999, 0, 100, -9999]
        merge_sort(myList, 0, len(myList) - 1)
        self.assertEqual(myList, [-9999, 0, 100, 201, 999], "Tests do not work on regular list")
    
    @pytest.mark.blackbox
    def test_merge_sort_nullmyListAux(self):
        myList = []
        merge_sort(myList, 0, len(myList) - 1)
        self.assertEqual(myList, [], "Tests do not work on empty list")
    
    @pytest.mark.blackbox
    def test_merge_sort_alreadysorted(self):
        myList = [1, 2, 2, 2, 3, 4, 4, 5, 6, 23, 66]
        merge_sort(myList, 0, len(myList) - 1)
        self.assertEqual(myList, [1, 2, 2, 2, 3, 4, 4, 5, 6, 23, 66], "Tests do not work on already sorted list")
    
    @pytest.mark.blackbox
    def test_merge_sort_sameelem(self):
        myList = [9, 9, 9, 9]
        merge_sort(myList, 0, len(myList) - 1)
        self.assertEqual(myList, [9, 9, 9, 9], "Tests do not work on list with elements of equal value")
    
    @pytest.mark.blackbox
    def test_merge_sort_reversed(self):
        myList = [66, 23, 6, 5, 4, 4, 3, 2, 2, 2, 1]
        merge_sort(myList, 0, len(myList) - 1)
        self.assertEqual(myList, [1, 2, 2, 2, 3, 4, 4, 5, 6, 23, 66], "Tests do not work on reverse sorted list")
    
    @pytest.mark.blackbox
    def test_merge_sort_time(self):
        myList = pandas.read_csv("C:\\Users\\Stefan-Liviu Pascu\\Documents\\GitHub\\Unit-Testing-On-Merge-Sort-Using-Python\\code\\test1.csv", index_col=0)
        import_module = "import merge_sort"
        testcode = '''def test():
        mergeSort(myList, 0, len(myList) - 1)
        '''
        print("It took ", timeit.timeit(stmt=testcode, setup=import_module), " seconds for the myListAuxay to be sorted using Merge Sort.")
        
        # Testing if our sorting algorithm can finish on a long list with high value numbers in under 3 seconds 
        # assert timeit.timeit(stmt=testcode, setup=import_module) < 3, "List sorted too slow"
        self.assertGreaterEqual(3, timeit.timeit(stmt=testcode, setup=import_module), "List sorted too slow")
    
    # @pytest.mark.blackbox
    @pytest.mark.skip   # Not a necessary test
    def test_merge_sort_random(self):
        myList = [0] * 999
        for i in range(999):
            myList[i] = int(random.uniform(-99999999, 99999999))
        
        # Bubble Sort is used in order to safely, but inefficiently, sort the auxiliary array
        myListAux = myList   
        n = len(myListAux)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if myListAux[j] > myListAux[j + 1] :
                    myListAux[j], myListAux[j + 1] = myListAux[j + 1], myListAux[j]
        
        merge_sort(myList, 0, len(myList) - 1)
        
        self.assertEqual(myList, myListAux, "Tests do not work on list with randomly selected elements")
        
    
    # White box tests
    @pytest.mark.whitebox
    def test_merge01(self):
        myList = [201, 999, 0, 100, -9999, 21, 9999, 10, 100, -99]
        merge(myList, 0, 4, 9)
        self.assertEqual(myList,  [21, 201, 999, 0, 100, -9999, 9999, 10, 100, -99], "Tests do not work on function 'merge()'")
    
    @pytest.mark.whitebox
    def test_merge02(self):
        myList = [201, 999, 0, 100, -9999, 21, 9999, 10, 100, -99]
        merge(myList, 0, 1, 3)
        self.assertEqual(myList,  [0, 100, 201, 999, -9999, 21, 9999, 10, 100, -99], "Tests do not work on function 'merge()'")
    
    @pytest.mark.whitebox
    def test_merge03(self):
        myList = [201, 999, 0, 100, -9999, 21, 9999, 10, 100, -99]
        merge(myList, 4, 6, 9)
        self.assertEqual(myList,  [201, 999, 0, 100, -9999, 10, 21, 100, -99, 9999], "Tests do not work on function 'merge()'")
    
    @pytest.mark.whitebox
    def test_merge04(self):
        myList = [201, 999, 0, 100, -9999, 21, 9999, 10, 100, -99]
        merge(myList, 2, 3, 6)
        self.assertEqual(myList,  [201, 999, -9999, 0, 21, 100, 9999, 10, 100, -99], "Tests do not work on function 'merge()'")
    
    @pytest.mark.whitebox
    def test_merge05(self):
        myList = [201, 999, 0, 100, -9999, 21, 9999, 10, 100, -99]
        merge(myList, 7, 6, 6)
        self.assertEqual(myList,  [201, 999, 0, 100, -9999, 21, 9999, 10, 100, -99], "Tests do not work on function 'merge()'")
    
    # # This test is not necessary as L is teatsed in order to have a lower value than R
    # # This test will fail on mutant testing
    # @pytest.mark.xfail
    # def test_merge_nullmyListAux(self):
    #     myList = []
    #     merge(myList, 0, 0, 0)
    #     self.assertEqual(myList,  [])
    
    @pytest.mark.whitebox
    def test_merge_alreadysorted(self):
        myList = [1, 2, 2, 2, 3, 4, 4, 5, 6, 23, 66]
        merge(myList, 0, 4, 10)
        self.assertEqual(myList,  [1, 2, 2, 2, 3, 4, 4, 5, 6, 23, 66], "Tests do not work on function 'merge()' with already sorted list")

    @pytest.mark.whitebox
    def test_merge_sameelem(self):
        myList = [9, 9, 9, 9]
        merge(myList, 0, 1, 3)
        self.assertEqual(myList,  [9, 9, 9, 9], "Tests do not work on function 'merge()' when all elements in list share the same value")
    
    @pytest.mark.whitebox
    def test_merge_reversed(self):
        myList = [66, 23, 6, 5, 4, 4, 3, 2, 2, 2, 1]
        merge(myList, 0, 4, 10)
        self.assertEqual(myList,  [4, 3, 2, 2, 2, 1, 66, 23, 6, 5, 4], "Tests do not work on function 'merge()' with reverse sorted list")

# if __name__ ==  '__main__':   
#     unittest.main()