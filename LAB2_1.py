# Finite state machine
'''Napisz program symulujący działanie automatu skończonego o grafie przejść jak na Rys. 1 (zbiór stanów i
alfabet są takie, jakie wynikają z grafu). Symulujący, czyli pokazujący konfigurację automatu w kolejnych
krokach (graficznie, na grafie). Umożliw podanie dowolnego wejścia (zgodnego z alfabetem).'''
import networkx as nx
import matplotlib.pyplot as plt

class StateMachine:
    def __init__(self):
        self.state= 0
        self.alphabet = ['a', 'b', 'c']
        self.graph_vis = nx.Graph()
        self.edges_and_labels = dict()
        self.graph_dict = {
            0: {
                'a': 2,
                'b': 2,
                'c': 2
                },
            1: {
                'a': 4,
                'b': 0,
                'c': 3
            },
            2: {
                'a': 1,
                'b': 1,
                'c': 6
            },
            3: {
                'a': 3,
                'b': 3,
                'c': 3
            },
            4: {
                'a': 0,
                'b': 5,
                'c': 5
            },
            5: {
                'a': 4,
                'b': 4,
                'c': 4
            },
            6: {
                'a': 3,
                'b': 3,
                'c': 3
            }
        }

    def input_value(self, input):
        if input not in self.alphabet:
            print('ERROR')
            print('Input not in an ALPHABET')
            quit()
        else:
            self.state = self.graph_dict[self.state][input]
            print(self.state)

    def plot_graph(self):
        for key in self.graph_dict:
            for n in self.graph_dict[key]:
                x = key
                y = self.graph_dict[key][n]
                self.graph_vis.add_edge(x, y)
                if tuple([x, y]) in self.edges_and_labels.keys():
                    self.edges_and_labels[tuple([x, y])] += n
                else:
                    self.edges_and_labels[tuple([x, y])] = n
        print(self.edges_and_labels)


Machine = StateMachine()
Machine.input_value('a')
Machine.input_value('b')
Machine.plot_graph()
print(Machine.edges_and_labels)

pos = nx.spring_layout(Machine.graph_vis)
nx.draw_networkx_nodes(Machine.graph_vis, pos, node_size=500)
nx.draw_networkx_labels(Machine.graph_vis, pos)
nx.draw_networkx_edges(Machine.graph_vis, pos)
nx.draw_networkx_edge_labels(Machine.graph_vis, pos, edge_labels=Machine.edges_and_labels)
plt.show()
