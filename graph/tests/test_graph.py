import pytest 
from graph.graph import Queue,Vertex,Edge,Graph

def test_add_vertex():
    g = Graph()
    vertex = g.add_vertex('A')
    assert vertex in g.get_vertices()

def test_add_edge():
    g = Graph()
    vertex_a = g.add_vertex('A')
    vertex_b = g.add_vertex('B')
    g.add_edge(vertex_a, vertex_b)
    assert len(g.get_neighbors(vertex_a)) == 1
    assert len(g.get_neighbors(vertex_b)) == 1



def test_get_neighbors_with_weight():
    g = Graph()
    vertex_a = g.add_vertex('A')
    vertex_b = g.add_vertex('B')
    g.add_edge(vertex_a, vertex_b, weight=5)
    neighbors = g.get_neighbors(vertex_a)
    assert len(neighbors) == 1
    neighbor = neighbors[0]
    assert neighbor.vertex == vertex_b
    assert neighbor.weight == 5

def test_graph_size():
    g = Graph()
    vertices = ['A', 'B', 'C', 'D', 'E']
    for vertex_name in vertices:
        g.add_vertex(vertex_name)
    assert g.size() == len(vertices)

def test_single_vertex_edge():
    g = Graph()
    vertex = g.add_vertex('A')
    edge_weight = 10
    g.add_edge(vertex, vertex, weight=edge_weight)
    neighbors = g.get_neighbors(vertex)
    assert len(neighbors) == 2
    neighbor = neighbors[0]
    assert neighbor.vertex == vertex
    assert neighbor.weight == edge_weight


