import random


class RandomizedSet:

    def __init__(self):
        self.random_set = {}

    def insert(self, val: int) -> bool:
        if val not in self.random_set or self.random_set[val] == 0:
            self.random_set[val] = 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self.random_set or self.random_set[val] <= 0:
            return False
        self.random_set[val] = 0
        return True

    def getRandom(self) -> int:
        random_list = list(set(self.random_set.keys()))
        while True:
            temp = random.choice(random_list)
            if self.random_set[temp] == 1:
                return temp

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()