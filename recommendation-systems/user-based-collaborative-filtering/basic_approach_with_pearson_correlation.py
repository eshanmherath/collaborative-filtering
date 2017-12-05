import operator
from math import sqrt

# Critics
critics = {'Clerk Kent': {'Avengers': 4.0, 'Matrix': 4.2, 'Wonder Woman': 3.0, 'Pacific Rim': 3.5, 'Harry Potter': 3.0,
                          'Hunger Games': 1.0},
           'Bruce Wayne': {'Avengers': 3.0, 'Matrix': 3.5, 'Wonder Woman': 1.5, 'Pacific Rim': 5.0, 'Harry Potter': 3.0,
                           'Hunger Games': 3.5},
           'Pepper Pots': {'Avengers': 2.5, 'Matrix': 3.0, 'Pacific Rim': 3.5, 'Harry Potter': 4.0},
           'Bruce Banner': {'Matrix': 3.5, 'Wonder Woman': 3.0, 'Harry Potter': 4.5, 'Pacific Rim': 4.0,
                            'Hunger Games': 2.5},
           'Thor Odinson': {'Avengers': 3.0, 'Matrix': 4.0, 'Wonder Woman': 2.0, 'Pacific Rim': 3.0,
                            'Harry Potter': 3.0, 'Hunger Games': 2.0},
           'Kara Kent': {'Avengers': 3.0, 'Matrix': 4.0, 'Harry Potter': 3.0, 'Pacific Rim': 5.0,
                         'You, Me and Dupree': 3.5},
           'Oliver Queen': {'Matrix': 4.5, 'Hunger Games': 1.0, 'Pacific Rim': 4.0}}

# My ratings
test = {'Eshan Herath': {'Avengers': 4.5, 'Matrix': 4.7,
                         'Wonder Woman': 3.5, 'Pacific Rim': 4.0, 'Harry Potter': 3.5,
                         'Hunger Games': 1.5}}


# Objective is to find the critic who has a similar taste to mine on movies


def similarity_score(critic, me):
    # Shared Items
    si = {}
    for item in critic:
        if item in me:
            si[item] = 1

    # Number of elements
    n = len(si)

    # No items in common
    if n == 0:
        return 0

    # Preferences Sum
    sum_critic = sum([critic[it] for it in si])
    sum_me = sum([me[it] for it in si])

    # Preferences Squared Sum
    sum_square_critic = sum([pow(critic[it], 2) for it in si])
    sum_square_me = sum([pow(me[it], 2) for it in si])

    # Sum of products
    sum_of_products = sum([critic[it] * me[it] for it in si])

    # Calculating Pearson score
    numerator = sum_of_products - (sum_critic * sum_me / n)
    denominator = sqrt((sum_square_critic - pow(sum_critic, 2) / n) * (sum_square_me - pow(sum_me, 2) / n))

    if denominator == 0:
        return 0

    r = numerator / denominator

    return r


matches = {}
for c in critics.keys():
    matches[c] = similarity_score(critics[c], test['Eshan Herath'])

# Higher the similarity score closer the critic's flavor as ours
matches_sorted = sorted(matches.items(), key=operator.itemgetter(1), reverse=True)
print(matches_sorted)
