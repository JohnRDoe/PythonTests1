import unittest
from sort import Sort

class TestSort(unittest.TestCase):

    def test_bubble_sort_1(self):
        arr=[]
        self.assertEquals([],Sort.bubble_sort(arr))
        
    def test_bubble_sort_2(self):
        arr=[7]
        self.assertEquals([7],Sort.bubble_sort(arr))
        
    def test_bubble_sort_3(self):
        arr=[15,12,36,22,1,7,18]
        self.assertEquals(sorted(arr),Sort.bubble_sort(arr))
        
    def test_bubble_sort_4(self):
        arr=(15,12,36,22,1,7,18)
        self.assertEquals(sorted(arr),Sort.bubble_sort(arr))
        
    def test_quick_sort_1(self):
        arr=[]
        self.assertEquals([],Sort.quick_sort(arr))
        
    def test_quick_sort_2(self):
        arr=[7]
        self.assertEquals([7],Sort.quick_sort(arr))
        
    def test_quick_sort_3(self):
        arr=[15,12,36,22,1,7,18]
        self.assertEquals(sorted(arr),Sort.quick_sort(arr))
        
    def test_quick_sort_4(self):
        arr=(15,12,36,22,1,7,18)
        self.assertEquals(sorted(arr),Sort.quick_sort(arr))
