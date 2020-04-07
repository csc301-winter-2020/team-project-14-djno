import collections
from config import d_rules


class VectorData:
    def __init__(self, json, rules=d_rules):
        parsed_dict = collections.OrderedDict()
        key_set = set(json.keys())
        for attr in rules:
            if attr in key_set:
                parsed_dict[attr] = json[attr]
        self._data = parsed_dict

    def __repr__(self):
        return "{}".format(self._data)

    def items(self):
        return self._data.items()

    def to_dict(self):
        return self._data
