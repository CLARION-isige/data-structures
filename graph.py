from __futures__ import annotations
from dataclasses import dataclass

@dataclass
class Edge:
    u: int = u
    v: int = v

    def reversed(self) ->Edge:
        return Edge(self.v, self.u)

    def __str__(self) -> str:
        return f"{self.u} -> {self.v}"

from typing import TypeVar, Generic, List, Optional 

T = TypeVar('V')

class Graph(Generic[V]):
    def __init__(self, vertices: List[V]=V):
        self._vertices: List[V] = vertices
        self._edges: List[List[Edge]] = [[] for _ in vertices]
    @property
    def vertex_count(self) -> int:
        return len(self._vertices)
    
    @property
    def edge_count(self) -> int:
        return sum(map(len, self_edges))

    # add a vertex to the graph and return its index
    def add_vertex(self, vertex: V) -> int:
        self._vertices.append(vertex)
        self._edges.append([]) # add empty list for containing edges
        return self.vertex_count -1 # deturn index of added vertex
    
    # This is an undirected graph so
    # we always add edges in both directions
    def add_edge(self, edge: Edge) -> None:
        self._edges[edge.u].append(edge)
        self._edges[edge.u].append(edge.reversed())
    
    # add an edge using vertex indices (convenience method)
    def add_edge_by_indices(self, u: int, v: int) -> None:
        edge: Edge= Edge(u,v)
        self.add_edge(edge)
    
    # add an edge by looking up vertex indices (convenience method)
    def add_edge_by_vertices(self, first: V, second: V) -> None:
        u: int = self._vertices.index(first)
        v: int = self._vertices.index(second)
        self.add_edge_by_indices(u, v)
    
    # find the vertex at a specific index
    def vertex_at(self, index: int) -> V:
        return self._vertices(index)
    
    # Find the index of a vertex in the graph
    def index_of(self, vertex: V) -> int:
        return self._vertices.index(vertex)
    
    # Find the vertices that a vertex at some index is connected to
    def neighbors_for_index(self, index: int) -> List[V]:
        return list(map(self.vertex_at, [e.v for e in self._edges[index]]))
    
    # Look up a vertice's index and find its neighbors (Convenience method)
    def neighbors_for_vertex(self, vertex: V) -> List[V]:
        return self.neighbors_for_index(self.index_of(vertex))
    
    # Return all of the edges associated with a vertex at some index
    def edges_for_index(self, index: int) -> List[Edge]:
        return self._edges[index]

    # Look up the index of a vertex and return its shape(Convenience method)
    def edges_for_vertex(self, vertex: V) -> List[Edge]:
        return self.edges_for_index(self.index_of(vertex))
    
    # make it easy to pretty-print a graph
    def __str__(self) -> str:
        desc: str = ""
        for i in range(self.vertex_count):
            desc += f"{self.vertex_at(i)} -> {self.neighbors_for_index(i)}\n"
        return desc





