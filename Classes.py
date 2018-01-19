from enum import Enum
import Support as dtSupport


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

    def __init__(self, name, dict_chances, dict_terminals):
        """
        :param dict_chances: dictionary of chance nodes
        :param dict_terminals: dictionary of terminal nodes
        """
        Node.__init__(self, name)
        self.futureNodes = []  # list of future node objects
        self.pFutureNodes = []  # probabilities of future nodes

        self.cost = dict_chances[name][Properties.COST.value]  # find cost
        self.pFutureNodes = dict_chances[name][Properties.PROB.value]  # find probability of each future nodes

        # find the names of future nodes for this chance node
        names = dict_chances[name][Properties.NODES.value]
        # add the future nodes
        self.futureNodes = dtSupport.create_future_nodes(names, dict_chances, dict_terminals)

        # calculate expected cost and utility of this node
        self.eCost = self.cost          # adding the immediate cost
        i = 0  # iterator in future nodes
        for node in self.futureNodes:
            # add the expected cost of this future node
            self.eCost += node.eCost * self.pFutureNodes[i]
            # increment i
            i += 1


class TerminalNode(Node):

    def __init__(self, name, dict_terminals):
        """ Instantiating a terminal node
        :param name: key of this node
        :param dict_terminals: dictionary of terminal nodes
        """
        # create the node
        Node.__init__(self, name)
        # find the eCost of this node (for terminal nodes eCost = immediate cost)
        self.eCost = dict_terminals[name]



