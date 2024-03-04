from typing import Dict, Set
from collections import defaultdict

class Graph:
    def __init__(self):
        self.adj_list:Dict[str, Set[str]] = defaultdict(set)

    def add_vertex(self, vertex:str) ->bool:
        if not isinstance(vertex, str):
            raise ValueError('Vertax has to be a string type.')
        
        if not self.adj_list.get(vertex):
            self.adj_list[vertex]
            return True
        
        return False
    
    def add_edge(self, vertex1:str, vertex2:str) -> bool:
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            self.adj_list.get(vertex1).add(vertex2)
            self.adj_list.get(vertex2).add(vertex1)
            return True
        
        return False

    def remove_edge(self, vertex1:str, vertex2:str) -> bool:
        if vertex1 in self.adj_list.get(vertex2) and vertex2 in self.adj_list.get(vertex1):
            self.adj_list.get(vertex1).remove(vertex2)
            self.adj_list.get(vertex2).remove(vertex1)
            return True
        
        return False

    def remove_vertex(self, vertex:str) -> bool:
        if not vertex in self.adj_list:
            return False
        
        edges_to_remove = self.adj_list.get(vertex)
        for ver in edges_to_remove:
            self.adj_list.get(ver).remove(vertex)
        
        del self.adj_list[vertex]
        return True

     
    def print_graph(self):
        if not bool(self.adj_list):
            return '{}'
        str_graph = '{ \n'
        for vertex, edges in self.adj_list.items():
            str_graph += f'  {vertex}: '
            str_graph += '['
            if edges:
                for edge in edges:
                    str_graph += f' {edge}, '
            str_graph += '],\n'
        str_graph += '}'

        return str_graph



graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_edge("A", "B")
print(graph.print_graph())
graph.remove_vertex("B")
print(graph.print_graph())
