import Classes as dtClasses


def create_future_nodes(names, dict_chances, dict_terminals):
    """ gets the names of future nodes and return the future node objects
    :param names: names of future nodes
    :param dict_chances: dictionary of chance nodes
    :param dict_terminals: dictionary of terminal nodes
    :return: list of future nodes
    """

    fnodes = []     # list of future nodes to return
    i = 0           # iterator in future nodes
    for name in names:

        # if this name is associated to a chance node
        if name in dict_chances:
            # create a chance node
            cn = dtClasses.ChanceNode(name, cp, dict_chances, dict_terminals)
            # append this node to the collection of future nodes
            fnodes.append(cn)
        # if this name is associated to a terminal node
        elif name in dict_terminals:
            # instantiate a terminal node
            cn = dtClasses.TerminalNode(name, cp, dict_terminals)
            # append this node to the collection of future nodes
            fnodes.append(cn)
        i += 1

    return fnodes