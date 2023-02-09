# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
cities = ['Salvador', 'Ubatuba', 'Belo Horizonte']
states = ['BA', 'SP', 'MG', 'RJ']

def union(cities, states):
    union = []

    if len(cities) > len(states):

        union = [(cities[ind], states[ind]) for ind in range(len(states))]
    else:

        union = [(cities[ind], states[ind]) for ind in range(len(cities))]


    return union

# could be zip function...
print(union(cities, states))    
