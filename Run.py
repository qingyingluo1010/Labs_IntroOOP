import Classes as dtClasses

# dictionary for terminal nodes
#               //key: cost
dictTerminals = {'T1': 10,
                 'T2': 20,
                 'T3': 30,
                 'T4': 40};

# dictionary for chance nodes
#           // key:  cost,  [future nodes],     [probabilities]
dictChances = {'C1': [0,    ['C2', 'T4'],       [0.5, 0.5]],
               'C2': [15,   ['T1', 'T2', 'T3'], [0.1, 0.2, 0.7]]};

C1 = dtClasses.ChanceNode('C1', dictChances, dictTerminals)

# print the expect cost of C1
print(C1.eCost)
