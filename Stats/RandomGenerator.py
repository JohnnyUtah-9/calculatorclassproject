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
        try:
            self.result = random.sample(range(low,high), size)
            return self.result
