import itertools
import config as c

# key: tier
# value: all the possible combinations of attribute values
# for example combination "4, 4, 2, 1" belongs to tier 5 since the sum of the values is 11
attribute_value_combinations_per_tier = {
1 : [], 2 : [], 3 : [], 4 : [], 5 : [], 6 : []
}

def get_NFT_rarity_tier(score):
    #skipping highest tier since they are handcrafted NFTs
    if 10 <= score <= 12:
        return 5
    elif 8 <= score <= 9:
        return 4
    elif 6 <= score <= 7:
        return 3
    elif score == 5:
        return 2
    elif score <= 4:
        return 1

# in order to create the NFTs we first find all the possible combinations of attribute values
# for example "4, 4, 2, 1" means a shirt with value 4, hat with value 4, face with value 2 and wing with 1
# for each generated combination we then see what tier it belongs to, and save it in a dictionary
def get_attribute_value_combinations(attributes):
    # list of lists which contain every possible value of its respective attribute
    value_lists = []
    for a in attributes:
        value_lists.append(a.keys())
    value_combinations = list(itertools.product(*value_lists))
    for values in value_combinations:
        attribute_value_combinations_per_tier[get_NFT_rarity_tier(sum(values))].append(values)
