from enum import Enum


class Properties(Enum):
    """ Index of parameters in chance node dictionaries. """
    COST = 0
    NODES = 1
    PROB = 2


class Node:
    """ base class """
    def __init__(self, name):
        """
        :param name: name of this node
        """
        self.name = name
        self.cost = 0   # immediate cost of visiting this node
        self.eCost = 0  # expected cost of visiting this node (includes the immediate cost)


class ChanceNode(Node):

    def __init__(self, name, tree_support):
        """
        :param dict_chances: dictionary of chance nodes
        :param dict_terminals: dictionary of terminal nodes
        """
        Node.__init__(self, name)
        self.futureNodes = []  # list of future node objects
        self.pFutureNodes = []  # probabilities of future nodes

        self.cost = tree_support.get_cost(name)  # find cost
        # add the future nodes and their probabilities
        self.futureNodes = tree_support.create_future_nodes(name)
        self.pFutureNodes = tree_support.get_prob_future_nodes(name)

        # calculate expected cost and utility of this node
        self.eCost = self.cost          # adding the immediate cost
        i = 0  # iterator in future nodes
        for node in self.futureNodes:
            # add the expected cost of this future node
            self.eCost += node.eCost * self.pFutureNodes[i]
            # increment i
            i += 1


class TerminalNode(Node):

    def __init__(self, name, tree_support):
        """ Instantiating a terminal node
        :param name: key of this node
        """
        # create the node
        Node.__init__(self, name)
        # find the eCost of this node (for terminal nodes eCost = immediate cost)
        self.eCost = tree_support.get_cost(name)


class TreeSupport:

    def __init__(self, dict_chances, dict_terminals):
        """
        :param dict_chances: dictionary of chance nodes
        :param dict_terminals: dictionary of terminal nodes
        """
        self.dictChances = dict_chances
        self.dictTerminals = dict_terminals

    def create_future_nodes(self, node_name):
        """ create all future nodes for the node with name provided"""

        # find the names of future nodes for this node
        names = self.dictChances[node_name][Properties.NODES.value]

        future_nodes = []     # list of future nodes to return
        for name in names:

            # if this name is associated to a chance node
            if name in self.dictChances:
                # create a chance node
                cn = ChanceNode(name, self)
                # append this node to the collection of future nodes
                future_nodes.append(cn)

            # if this name is associated to a terminal node
            elif name in self.dictTerminals:
                # instantiate a terminal node
                tn = TerminalNode(name, self)
                # append this node to the collection of future nodes
                future_nodes.append(tn)

        return future_nodes

    def get_cost(self, node_name):
        """ returns the cost of the node with the name provided """
        if node_name in self.dictChances:
            return self.dictChances[node_name][Properties.COST.value]
        elif node_name in self.dictTerminals:
            return self.dictTerminals[node_name]

    def get_prob_future_nodes(self, node_name):
        """ returns the probabilities of future nodes for the node with name provided """
        if node_name in self.dictChances:
            return self.dictChances[node_name][Properties.PROB.value]
        elif node_name in self.dictTerminals:
            return []
