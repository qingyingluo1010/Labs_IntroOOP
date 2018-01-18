from enum import Enum
import Support as dtSupport


class Properties(Enum):
    """ Index of parameters in decision and chance node dictionaries. """
    COST = 0
    NODES = 1
    PROB = 2


class Node:
    """ base class """
    def __init__(self, name, cost):
        """
        :param name: name of this node
        :param cost: cost of this node
        """
        self.name = name
        self.cost = cost

    def get_expected_cost(self):
        """ abstract method to be overridden in derived classes
        :returns expected cost of this node """
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")


class ChanceNode(Node):

    def __init__(self, name, dict_chances, dict_terminals):
        """
        :param dict_chances: dictionary of chance nodes
        :param dict_terminals: dictionary of terminal nodes
        """
        Node.__init__(self, name)
        self.futureNodes = []  # list of future node objects
        self.pFutureNodes = []  # probability of future nodes

        self.cost = dict_chances[name][Properties.COST.value]  # find cost
        self.pFutureNodes = dict_chances[name][Properties.PROB.value]  # find probability of each future nodes

        # find the names of future nodes for this chance node
        names = dict_chances[name][Properties.NODES.value]
        # add the future nodes
        self.futureNodes = dtSupport.create_future_nodes \
            (names, dict_chances, dict_terminals)

    def get_expected_cost(self):
        """
        :return: expected cost of this chance node
        """
        exp_cost = 0  # expected cost initialized at 0
        i = 0
        for node in self.futureNodes:
            exp_cost += self.probs[i]*node.cost
            i += 1
        return exp_cost


class TerminalNode(Node):

    def __init__(self, name, cost):
        Node.__init__(self, name, cost)

    def get_expected_cost(self):
        """
        :return: cost of this chance node
        """
        return self.cost



