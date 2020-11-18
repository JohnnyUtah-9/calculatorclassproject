import random


class RandomGenerator:
    result = 0

    def __init__(self):
        pass


    #Generate random number w/o seed between range of two numbers
    def generate_random_number_by_range_wo_seed (self, low, high):
        self.result = random.uniform (low,high)
        return self.result


    #Generate random number w/ seed between range of two numbers
    def generate_random_number_by_range_w_seed (self, seed, version, low, high):
        random.seed (seed,version)
        self.result = random.uniform (low,high)
        return self.result


    #Generate list of N random numbers w/ seed between range of numbers
    def get_random_number_list_by_range_w_seed (self, size, seed, version, low, high):
        random.seed (seed, version)
        self.result = random.sample(range(low,high), size)
        return self.result


    #Set seed and randomly select same value
    def set_seed_and_get_random_value_from_list (self, seed, version, number_list):
        random.seed (seed, version)
        self.result = random.choice(number_list)
        return self.result

    #Select a random item from list
    def get_random_item_from_list(self, number_list):
        self.result = random choice(number_list)
        return self.result

    #Select N number of items w/o seed
    def get_random_number_list_wo_seed(self, size,number_list):
        try:
            self.result = random.sample(number_list, size)
        except ValueError:
            print('sample size exceeds population size')
            return self.result

    #Select N number of items from a list with seed
    def get_random_number_list_w_seed(self, size, seed, version, number_list):
        random.seed(seed, version)
        try:
            self.result = random.sample(number_list, size)
        except ValueError:
            print ('sample size exceeds population size')
            return self.result
