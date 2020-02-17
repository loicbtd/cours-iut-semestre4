from networkx import Graph


class BetterGraph(Graph):

    def __init__(self, **attr):
        super().__init__(**attr)
        self.nodes_properties = []

    def copy_graph(self, graph):
        self.remove_nodes_from(self.nodes())
        self.remove_edges_from(self.edges())
        self.add_nodes_from(graph.nodes())
        for node in graph.nodes():
            self.nodes_properties.append({'node': node})
        for edge in graph.edges():
            # TODO: copy all the edge datas
            self.add_edge(edge[0], edge[1], weight=graph.get_edge_data(edge[0], edge[1], ['weight']).get('weight'))
        return self

    def add_node(self, node_for_adding, **attr):
        super().add_node(node_for_adding, **attr)
        for node_property in self.nodes_properties:
            if node_property.get('node') == node_for_adding:
                return
        self.nodes_properties.append({'node': node_for_adding})

    def add_nodes_from(self, nodes_for_adding, **attr):
        super().add_nodes_from(nodes_for_adding, **attr)
        nodes_for_adding_tmp = [nodes_for_adding]
        for node_property in self.nodes_properties:
            if node_property.get('node') in nodes_for_adding_tmp:
                nodes_for_adding_tmp.remove(node_property.get('node'))
        for node in nodes_for_adding_tmp:
            self.nodes_properties.append({'node': node})

    def remove_node(self, n):
        super().remove_node(n)
        for i in range(0, len(self.nodes_properties)):
            if self.nodes_properties[i].get('node') == n:
                del self.nodes_properties[i]
                return

    def remove_nodes_from(self, nodes):
        super().remove_nodes_from(nodes)
        counter = 0
        for node_property in self.nodes_properties:
            if node_property.get('node') in nodes:
                self.nodes_properties.remove(node_property)
                counter += 1
            if counter >= len(nodes):
                return

    def set_node_property(self, node, key, value):
        for i in range(0, len(self.nodes_properties)):
            if self.nodes_properties[i].get('node') == node:
                self.nodes_properties[i].update({key: value})
                return

    def get_node_property(self, node, key):
        for i in range(0, len(self.nodes_properties)):
            if self.nodes_properties[i].get('node') == node:
                # print("node found: ", self.nodes_properties[i].get(key) )
                return self.nodes_properties[i].get(key)
        return None

    def get_all_nodes_with_property(self, key, value):
        nodes_with_property = []
        for node_property in self.nodes_properties:
            if node_property.get(key) == value:
                nodes_with_property.append(node_property.get('node'))
        return nodes_with_property
    #
    # def get_note_with_property(self, key, value):
    #     for node_property in self.nodes_properties:
    #         if node_property.get(key) == value:
    #             nodes_with_property.append(node_property.get('node'))