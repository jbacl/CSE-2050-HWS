import unittest, random
from MyBSTMap import MyBSTMap

class TestMyBSTMap(unittest.TestCase):
    def test_equal_empty(self):
        """Tests and Compares two empty trees"""
        tree1 = MyBSTMap()
        tree1.put(None, None)

        tree2 = MyBSTMap()
        tree2.put(None, None)

        self.assertEqual(tree1, tree2)

    def test_equal_multiplenodes(self):
        """Tests and Compares two trees w/ same shape"""

        tree1 = MyBSTMap()
        tree1.put(4,3)
        tree1.put(1,5)

        tree2 = MyBSTMap()
        tree2.put(4,3)
        tree2.put(1,5)

        self.assertEqual(tree1, tree2)

    def test_notequal_multiplenodes_difshapes(self):
        """Tests and Compares two trees w/ different shape"""
        
        tree1 = MyBSTMap()
        for x in [3, 1, 5, 0]:
            tree1.put(x, f'value:{x}')
        
        tree2 = MyBSTMap()
        for x in [4, 3, 1, 5, 0]:
            tree2.put(x, f'value:{x}')
        
        self.assertNotEqual(tree1, tree2)
    
    def test_notequal_multiplenodes_difkvs(self):
        """Tests and Compares two trees w/ different vals and keys"""
        tree1 = MyBSTMap()
        for x in [5, 2, 7, 6, 3]:
            tree1.put(x, f'value:{x}')

        tree2 = MyBSTMap()
        for x in [1, 6, 3, 0, 4]:
            tree2.put(x, f'value:{x}')

        self.assertNotEqual(tree1, tree2)

    def test_frompreorder_small(self):
        """Tests and Compares two trees from a preorder func"""
        tree1 = MyBSTMap()
        for x in [3, 1, 5, 0]:
            tree1.put(x, f'value:{x}')
        
        L = [(x, v) for (x, v) in tree1.predorder()]
        tree2 = MyBSTMap.frompreorder(L)

        self.assertEqual(tree1, tree2)

    def test_frompreorder_large(self):
        """Tests and Compares two much larger trees from a preorder func"""
        random.seed(743)
        L = []
        for i in range(100):
            x = random.int(1,100)
            L.append(x)
        
        tree1 = MyBSTMap()
        for n in L:
            tree1.put(n, f'value:{n}')
        
        L = [(n, v) for (n, v) in tree1.predorder()]
        tree2 = MyBSTMap.frompreorder(L)

        self.assertEqual(tree1, tree2)

    def test_frompostorder_small(self):
        """Tests and Compares two trees from a postorder func"""
        tree1 = MyBSTMap()
        for x in [3, 1, 5, 0]:
            tree1.put(x, f'value:{x}')
        
        L = [(x, v) for (x, v) in tree1.postorder(L)]
        tree2 = MyBSTMap.frompostorder(L)

        self.assertEqual(tree1, tree2)

    def test_frompostorder_large(self):
        """Tests and Compares two larger trees from a postorder func"""
        random.seed(743)
        L = []
        for i in range(100):
            x = random.int(1,100)
            L.append(x)
        
        tree1 = MyBSTMap()
        for n in L:
            tree1.put(n, f'value:{n}')
        
        L = [(n, v) for (n, v) in tree1.postdorder()]
        tree2 = MyBSTMap.frompostorder(L)

        self.assertEqual(tree1, tree2)

unittest.main()