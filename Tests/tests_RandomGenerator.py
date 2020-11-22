import unittest
from Stats.RandomGenerator import RandomGenerator

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.random_generator = RandomGenerator()

    #Generate random number w/o seed between range of two numbers
    def test_generate_rand_num_by_range_wo_seed(self):
        self.assertLessEqual(self.random_generator.generate_rand_num_by_range_wo_seed(1, 5), 5)
        self.assertGreaterEqual(self.random_generator.generate_rand_num_by_range_wo_seed(1, 5), 1)

    #Generate random number w/ seed between range of two numbers
    def test_generate_rand_num_by_range_w_seed(self):
        self.assertLessEqual(self.random_generator.generate_rand_num_by_range_w_seed(5, 1, 3, 5), 5)
        self.assertGreaterEqual(self.random_generator.generate_rand_num_by_range_w_seed(5, 1, 3, 5), 3)

    #Generate list of N random numbers w/ seed between range of numbers
    def test_get_rand_num_list_by_range_w_seed(self):
        data = self.random_generator.get_rand_num_list_by_range_w_seed(5, 2, 2, 1, 9)
        for num in range(len(data)):
            self.assertLessEqual(data[num], 9)
            self.assertGreaterEqual(data[num], 1)

    #Set seed and randomly select same value
    def test_set_seed_and_get_rand_from_list(self):
        self.assertEqual(self.random_generator.set_seed_and_get_rand_from_list(3, 2, [5, 3, 2, 1, 9]), 3)

    #Select a random item from list
    def test_get_rand_item_from_list(self):
        self.assertTrue(self.random_generator.get_rand_item_from_list([5, 3, 2, 1, 9]) in [5, 3, 2, 1, 9])

    #Select N number of items w/o seed
    def test_get_rand_num_list_wo_seed(self):
        self.assertEqual(len(self.random_generator.get_rand_num_list_wo_seed(3, [5, 3, 2, 1, 9])), 3)
        self.assertTrue(set(self.random_generator.get_rand_num_list_wo_seed(3, [5, 3, 2, 1, 9])).issubset(set([5, 3, 2, 1, 9])))

    #Select N number of items from a list with seed
    def test_get_rand_num_list_w_seed(self):
        self.assertEqual(len(self.random_generator.get_rand_num_list_w_seed(3, 2, 2, [5, 3, 2, 1, 9])), 3)
        self.assertTrue(set(self.random_generator.get_rand_num_list_w_seed(3, 2, 2, [5, 3, 2, 1, 9])).issubset(set([5, 3, 2, 1, 9])))


if __name__ == '__main__':
    unittest.main()
