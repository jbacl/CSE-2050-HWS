from max_profit import price_to_profit, max_profit_brute, max_profit, max_profit_crossing
import unittest, random

class TestPriceToProfit(unittest.TestCase):
    # Include at least one non-pdf test (remember the docstring)
    def test_PricetoProfit(self):
        L = [100, 200, 180, 250, 100]
        p = [0, 100, -20, 70, -150]
        self.assertEqual(price_to_profit(L), p)

class TestMaxProfitCrossing(unittest.TestCase):
    def test_left(self):
        """Return correct price for buy/sell in left half"""
        L = [100, 150, 180, 170, 210]
        p = price_to_profit(L)

        self.assertEqual(max_profit_crossing(p, left = 0, right=len(L) - 1, median=(len(L) - 1) // 2), 80)


    def test_right(self):
        """Returns correct profit for buy/sell in right half"""
        L = [100, 150, 180, 170, 210]
        p = price_to_profit(L)

        median=(len(L) - 1) // 2

        self.assertEqual(max_profit_crossing(p, left = median+1, right=len(L) - 1, median=(len(L) - 1) // 2), 40)

    def test_crossing(self):
        """Returns correct profit for buy left/sell right"""
        L = [100, 150, 180, 170, 210]
        p = price_to_profit(L)

        median=(len(L) - 1) // 2

        self.assertEqual(max_profit_crossing(p, left = 0, right=len(L) - 1, median=(len(L) - 1) // 2), 110)

class TestMaxProfit(unittest.TestCase):

    def test_min_max(self):
        """Max profit corresponds to buying at minimum, selling at maximum"""
        L = [100, 150, 180, 170, 210]
        p = price_to_profit(L)
        self.assertEqual(max_profit_crossing(p, left = 0, right=len(L) - 1), 110)

    def test_not_min_max(self):
        """Max profit from buying at non-minimum and selling at non-maximum"""
        
    def test_random(self):
        """Tests that random lists give correct result, using brute force to verify"""

        # 1) define list length n. Use at least 100 items to guarantee your algorithm works,
        #    but you can use a smaller value while debugging
        n = 1000
        # 2) for i in range 1000:
            # Create list of n random ints
            # find max profit using brute algorithm (expected result)
            # find max profit using divide-and-conquer algorithm (actual result)
            # assert that expected and actual are the same
        L = [random.randint(0, 100) for i in range(n)]
        self.assertEqual(max_profit_brute(L), max_profit(L))

    # tests from pdf and w/ provided bitcoin csvs are provided below.
    # these are unlikely to be helpful for debugging - take the time
    # to write your own above before trying to debug your code
    def test_pdf(self):
        """Tests from pdf"""
        self.assertEqual(max_profit(price_to_profit([100, 105, 97, 200, 150])), 103)

    # this requires you to be in the same director as the folder "bitcoin_prices"
    def test_bitcoin(self):
        """Tests 5 years of bitcoin"""
        ##### Import and read values from associated csvs, then check if you can become a bitcoin-optimaire
        import csv
        import os

        val_2015 = []
        val_2016 = []
        val_2017 = []
        val_2018 = []
        val_2019 = []
        val_2020 = []

        vals = [val_2015, val_2016, val_2017, val_2018, val_2019, val_2020]

        for file in os.scandir(r'./bitcoin_prices'):
            if (file.path.endswith(".csv")):
                if file.name == "2015.csv": i = 0
                elif file.name == "2016.csv": i = 1
                elif file.name == "2017.csv": i = 2
                elif file.name == "2018.csv": i = 3
                elif file.name == "2019.csv": i = 4
                elif file.name == "2020.csv": i = 5

                with open(file, 'r') as f:
                    reader = csv.reader(f)

                    lst = list(reader)[1:]
                    for j in range(len(lst)):
                        vals[i].append( float(lst[j][1].replace(",","")))


        # find the day-to-day profit list for each year
        year_profits = []
        for year in vals:
            year_profits.append([])
            year_profits[-1] = price_to_profit(year)

        # correct max profits per year, 2015-2020, rounded to ints
        max_profits = [298, 604, 18561, 4476, 9665, 24052]

        # test that max_profit returns the correct profit for each year
        for i, year in enumerate(year_profits):
            self.assertAlmostEqual(max_profit(year), max_profits[i], places=0)

unittest.main()