def get_edge_list(self):
    edge_list = []
    for edge_object in self.edges:
        edge = (edge_object.value, edge_object.node_from.value, edge_object.node_to.value)
        edge_list.append(edge)
    return edge_list

def get_adjacency_list(self):
    max_index = self.find_max_index()
    adjacency_list = [None] * (max_index + 1)
    for edge_object in self.edges:
        if adjacency_list[edge_object.node_from.value]:
            adjacency_list[edge_object.node_from.value].append((edge_object.node_to.value, edge_object.value))
        else:
            adjacency_list[edge_object.node_from.value] = [(edge_object.node_to.value, edge_object.value)]
    return adjacency_list

def get_adjacency_matrix(self):
    max_index = self.find_max_index()
    adjacency_matrix = [[0 for i in range(max_index + 1)] for j in range(max_index + 1)]
    for edge_object in self.edges:
        adjacency_matrix[edge_object.node_from.value][edge_object.node_to.value] = edge_object.value
    return adjacency_matrix

def find_max_index(self):
    max_index = -1
    if len(self.nodes):
        for node in self.nodes:
            if node.value > max_index:
                max_index = node.value
    return max_index