import collections
from backend.config import d_rules

class VectorData:
    def __init__(self, json, rules=d_rules):
        parsed_dict = collections.OrderedDict()
        key_set = set(json.keys())
        for attr in rules:
            if attr in key_set:
                try:
                    parsed_dict[attr] = int(json[attr])
                except ValueError as v:
                    print("invalid json input, error: {}".format(v))
                    parsed_dict[attr] = 0 # error if format doesn't fit
        self._data = parsed_dict
    def __repr__(self):
        return "{}".format(self._data)
    def items(self):
        return self._data.items()
    