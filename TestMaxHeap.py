from MaxHeap import Entry, MaxHeap
import unittest, random, time
random.seed(658)

#TODO: Fill out any empty tests below
class TestEntry(unittest.TestCase):

    def test_gt_onepriority(self):
        """Tests Entry's with 1 priority"""
        e1 = Entry([0], 'Keys')
        e2 = Entry([1], 'Wallet')
        
        self.assertTrue(Entry.__gt__(e2,e1))

    def test_gt_threepriorities(self):
        """Tests Entries with with 3 priorities"""
        e1 = Entry([1,0,'a'], 'Keys')
        e2 = Entry([2,1,'b'], 'Wallet')
        e3 = Entry([3,2,'c'], 'Sunglasses')

        self.assertTrue(Entry.__gt__(e2, e1))
        self.assertTrue(Entry.__gt__(e3,e2))

    def test_gt_mismatchedpriorities(self):
        """Test comparisons b/w entries with different numbers of priorities"""
        e1 = Entry([1, 0], 'keys')
        e2 = Entry([1, 0, 'b'], 'wallet')
        
        self.assertTrue(Entry.__gt__(e2,e1))

    def test_eq(self):
        """Test that items w/ exact same priorities are seen as equal"""
        e1 = Entry([2, 1, 'a'], 'keys')
        e2 = Entry([2, 1, 'a'], 'keys')

        self.assertTrue(Entry.__eq__(e2, e1))

class TestMaxHeap(unittest.TestCase):
    def test_add_remove_single(self):
        """Add a single item to the max heap, then remove it. This test is provided for you as an example."""
        e1 = Entry(priority=[0], item="jake")
        mh = MaxHeap()
        self.assertEqual(len(mh), 0)
        mh.put(e1)
        self.assertEqual(len(mh), 1)
        self.assertEqual(mh.remove_max(), "jake")

    def test_add_remove_random(self):
        """Add and remove many random items w/ same number of priorities"""
        alph = "abcdefghijklmnopqrstuvwxyz"
        mh = MaxHeap()

        e1 = Entry([random.choices(alph, k=3), random.randint(1,100)])
        self.assertEqual(len(mh), 0)
        print(e1)
        mh.put(e1)
        self.assertEqual(len(mh), 1)

        e2 = Entry([random.choices(alph, k=3), random.randint(1,100)])
        mh.put(e2)
        self.assertEqual(len(mh), 2)

        self.assertEqual(mh.remove_max(), 'wallet')
        self.assertEqual(len(mh), 1)
        self.assertEqual(mh.remove_max(), 'keys')
        self.asssertEqual(len(mh), 0)

        e3 = Entry([0, 1, 2, 3, 4, random.choices(alph, k=3)], 'keys')
        mh.put(e3)
        print(e3)
        e4 = Entry([0, 1, 2, 3, 4, random.choices(alph, k=3)], 'hat')
        mh.put(e4)
        print(e4)

        self.assertEqual(mh.remove_max(), 'keys')
        

    def test_add_remove_several(self):
        """Add and remove several items with different numbers of priorities"""
        maxh = MaxHeap
        e1 = Entry([0], 'keys')
        self.assertEqual(len(maxh), 0)
        maxh.put(e1)
        self.assertEqual(len(maxh), 1)

        e2 = Entry([0, 1], 'wallet')
        maxh.put(e2)
        self.assertEqual(len(maxh), 2)

        e3 = Entry([0, 1, 2], 'phone')
        maxh.put(e3)
        self.assertEqual(len(maxh), 3)

        self.assertEqual(maxh.remove_max(), 'phone')
        self.assertEqual(len(maxh), 2)

        self.assertEqual(maxh.remove_max(), 'wallet')
        self.assertEqual(len(maxh), 1)


    def test_removefromempty(self):
        """Test Runtime error when removiung from empty"""

    # NOTE: This times heapify_up and _down, but does not test their functionality
    def test_heapify(self):
        """Times heapify up and heapify down approaches. This 'test' provided for you"""
        print() # an extra blank line at the top
        
        # table header
        print('='*40)
        print(f"{'n':<10}{'t_h_up (ms)':<15}{'t_h_down (ms)':<15}"   )
        print('-'*40)

        # table body
        scalar = int(1E3)
        for n in [i*scalar for i in [1, 2, 3, 4, 5]]:
            t_h_up = 1000*time_f(MaxHeap, (list(range(n)), 'up'))
            t_h_down = 1000*time_f(MaxHeap, (list(range(n)), 'down'))
            print(f"{n:<10}{t_h_up:<15.2g}{t_h_down:<15.2g}")

        # table footer
        print("-"*40)

def time_f(func, args, trials=5):
    """Returns minimum time trial of func(args)"""
    t_min = float('inf')

    for i in range(trials):
        start = time.time()
        func(*args)
        end = time.time()
        if end-start < t_min: t_min = end - start

    return t_min

unittest.main()