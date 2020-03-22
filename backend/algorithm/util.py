import json
import config as config
import algorithm.packer as packer

"""convert the preference model object to dict
pref_obj: see in model
"""


def turn_pref_to_dict(pref_obj):
    new_json = json.loads(pref_obj.to_json())
    new_dict = {}
    rest_r = {}
    for key, val in new_json.items():
        try:
            new_dict[config.a_maps[key]] = val
        except KeyError:
            rest_r[key] = val
    return new_dict, rest_r


"""get the preferences and then sort them
    pref_list: the preference object list
    attr: the way of communications to sort
    return list of pairs: [(prefs, other_info)...]
"""


def sort_pref(pref_list, approach, location):  # TODO location
    def compare_tool(i_dict):
        comp_vec = packer.PreferenceVector.build_vector(i_dict[0])
        comp_vec.set_approach(config.sub_category[approach])
        return len(config.sub_category[
                       approach]) - comp_vec.count_approach()  # TODO: add location distance here

    new_d = (turn_pref_to_dict(x) for x in pref_list)
    return sorted(new_d, key=compare_tool)


if __name__ == "__main__":
    import backend.model.UserModel as model

    tObj = model.UserSettings(email="sadasd")
