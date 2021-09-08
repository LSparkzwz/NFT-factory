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
can_only_appear_within_certain_tiers = {}

attribute_frequency = {

}

def get_total_supply():
    return total_supply

def get_attributes():
    return attributes

def get_tier_limits():
    return can_only_appear_within_certain_tiers
