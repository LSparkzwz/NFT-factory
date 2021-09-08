import itertools

# total supply of the NFT prints
total_supply = 6666
# rarity/value tiers of the NFT prints, from worst to best
tiers = [2269, 1999, 1666, 666, 333, 66]
# a NFT print rarity/value is determined by the total score obtained by the sum of its main attributes
# in this example there's 4 main attributes that can have a value that goes from 1 to 4
shirt_value = {
1 : [],
2 : [],
3 : [],
4 : []
}
hat_value = {
0 : [],
1 : [],
2 : [],
3 : [],
4 : []
}
face_value = {
0 : [],
1 : [],
2 : [],
}
wing_value = {
0 : [],
1 : [],
2 : []
}

attributes = [shirt_value, hat_value, face_value, wing_value]

# dictionary to keep track of special attributes that should only appear starting
# from a certain tier upwards so that the combination calculator doesn't use them in lower tiers
# and can't appear past a certain tier so they don't appear in higher tiers
can_only_appear_within_certain_tiers = {

}

# key: tier
# value: all the possible combinations of attribute values
# for example combination "4, 4, 2, 1" belongs to tier 5 since the sum of the values is 11
attribute_value_combinations_per_tier = {
1 : [], 2 : [], 3 : [], 4 : [], 5 : [], 6 : []
}

# since tiers[] starts at pos 0 we increment each value by 1
def get_tier(tier_pos):
    return tier_pos + 1

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

get_attribute_value_combinations(attributes)
print(attribute_value_combinations_per_tier)
