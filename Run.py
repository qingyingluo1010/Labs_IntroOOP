import Classes as dtClasses

# dictionary for terminal nodes
#               //key: cost
dictTerminals = {'T1': 10,
                 'T2': 20,
                 'T3': 30,
                 'T4': 40};

# dictionary for chance nodes
#           // key:  cost,  [future nodes],     [probabilities]
dictChances = {'C1': [5,    ['C2', 'T3'],   [0.1, 0.9]],
               'C2': [15,   ['T1', 'T2'],   [0.2, 0.8]],
               'C3': [25,   ['T4', 'T5'],   [0.3, 0.7]]};

# dictionary for decision nodes
#              / key:  cost,  [future nodes]
dictDecisions = {'D1': [0,    ['C1', 'C3']]};

# create a tree support object
treeSupport = dtClasses.TreeSupport(dictDecisions, dictChances, dictTerminals)

# create a decision node
D1 = dtClasses.DecisionNode('D1', treeSupport)

# print the expect cost of alternatives
print(D1.get_eCosts())
