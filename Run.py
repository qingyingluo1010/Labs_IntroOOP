import Classes as dtClasses

# dictionary for terminal nodes
#               //key: cost
dicTerminals = {'t1': 10,
                't2': 20,
                't3': 30,
                't4': 40};

# dictionary for chance nodes
#           // key: cost, [future nodes],       [probabilities]
dicChances = {'c1': [0,   ['c2', 't4'],         [0.5, 0.5]],
              'c2': [15,  ['t1', 't2', 't3'],   [0.1, 0.3, 0.7]]};


# create the future nodes of C2
C2FutureNodes =[T1, T2, T3]
# create C2
C2 = dtClasses.ChanceNode('C2', 15, C2FutureNodes, [0.1, 0.3, 0.7])
# create the future nodes of C1
C1FutureNodes = [C2, T4]
# create C1
C1 = dtClasses.ChanceNode('C1', 0, C1FutureNodes, [0.5, 0.5])

# print the expect cost of C1
print(C1.get_expected_cost())