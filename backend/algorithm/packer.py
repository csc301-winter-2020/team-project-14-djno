from algorithm.Vector import Vector
from algorithm.data import VectorData
from config import d_rules
import itertools


class PreferenceVector(Vector):
    def __init__(self, data, rules=d_rules):
        super().__init__(data)
        self._rules = set(rules)
        self.sub_approach = []

    """for debug"""

    def __repr__(self):
        return "{}".format(self.unroll())

    # def unroll(self):
    #     return [(k, v) for k, v in self._data.items() if k in self._rules]
    # def __sub__(self, other):
    #     # other_d = other.unroll()
    #     # current_d = self.unroll()
    #     # return sum((x - y)**2 for x, y in itertools.zip_longest(other_d, current_d, fillvalue=0))
    #     pass
    @staticmethod
    def build_vector(json):
        return PreferenceVector(VectorData(json))

    def count_approach(self):
        # list_t_comp = self.unroll()
        # attr_needed = set(attrs)
        # return sum([len([y for y in x if y in attr_needed]) for x in list_t_comp])
        # list_comp = self.unroll()
        print(self.sub_approach)
        count = len([y for y in self.sub_approach if self._data.to_dict()[y]])
        print("count: {}".format(count))
        return count

    def set_approach(self, sub_approach):
        self.sub_approach = sub_approach


if __name__ == "__main__":
    test_dict = {"REN": 0, "RENA": 1}
    v = PreferenceVector.build_vector(test_dict)
    print(v)
