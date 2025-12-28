import unittest
from graph import Graph

class TestGraph(unittest.TestCase):
    
    def test_empty_graph(self):
        g = Graph()
        self.assertEqual(g.get_vertices(), [])
        self.assertEqual(g.dfs(), [])
        self.assertEqual(g.bfs(), [])
    
    def test_single_vertex(self):
        g = Graph()
        g.add_vertex('A')
        self.assertEqual(g.get_vertices(), ['A'])
        self.assertEqual(g.dfs('A'), ['A'])
        self.assertEqual(g.bfs('A'), ['A'])
    
    def test_undirected_graph_dfs(self):
        g = Graph(directed=False)
        g.add_edge('A', 'B')
        g.add_edge('A', 'C')
        g.add_edge('B', 'D')
        g.add_edge('B', 'E')
        g.add_edge('C', 'F')
        
        dfs_result = g.dfs('A')
        self.assertTrue(dfs_result[0] == 'A')
        self.assertEqual(len(dfs_result), 6)
        self.assertEqual(set(dfs_result), {'A', 'B', 'C', 'D', 'E', 'F'})
    
    def test_directed_graph_dfs(self):
        g = Graph(directed=True)
        g.add_edge('A', 'B')
        g.add_edge('A', 'C')
        g.add_edge('B', 'D')
        g.add_edge('C', 'E')
        g.add_edge('D', 'F')
        
        dfs_result = g.dfs('A')
        self.assertTrue(dfs_result[0] == 'A')
        self.assertEqual(len(dfs_result), 6)
    
    def test_disconnected_graph(self):
        g = Graph()
        g.add_edge('A', 'B')
        g.add_edge('B', 'C')
        g.add_vertex('D')
        g.add_edge('E', 'F')
        
        dfs_from_a = g.dfs('A')
        self.assertEqual(set(dfs_from_a), {'A', 'B', 'C'})
        
        dfs_from_d = g.dfs('D')
        self.assertEqual(dfs_from_d, ['D'])
        
        dfs_from_e = g.dfs('E')
        self.assertEqual(set(dfs_from_e), {'E', 'F'})
    
    def test_dfs_recursive(self):
        g = Graph()
        g.add_edge('A', 'B')
        g.add_edge('A', 'C')
        g.add_edge('B', 'D')
        g.add_edge('C', 'E')
        
        dfs_iterative = g.dfs('A')
        dfs_recursive = g.dfs_recursive('A')
        
        self.assertEqual(set(dfs_iterative), set(dfs_recursive))
        self.assertEqual(len(dfs_iterative), len(dfs_recursive))
    
    def test_bfs(self):
        g = Graph()
        g.add_edge('A', 'B')
        g.add_edge('A', 'C')
        g.add_edge('B', 'D')
        g.add_edge('B', 'E')
        g.add_edge('C', 'F')
        
        bfs_result = g.bfs('A')
        self.assertEqual(bfs_result[0], 'A')
        self.assertEqual(len(bfs_result), 6)
    
    def test_iteration(self):
        g = Graph()
        g.add_edge('A', 'B')
        g.add_edge('A', 'C')
        g.add_edge('B', 'D')
        
        dfs_order = g.dfs('A')
        iter_order = [vertex for vertex in g]
        
        self.assertEqual(iter_order, dfs_order)
        
        for i, vertex in enumerate(g):
            self.assertEqual(vertex, dfs_order[i])
    
    def test_multiple_iterations(self):
        g = Graph()
        g.add_edge(1, 2)
        g.add_edge(1, 3)
        
        first_iter = [v for v in g]
        second_iter = [v for v in g]
        
        self.assertEqual(first_iter, second_iter)
    
    def test_remove_vertex(self):
        g = Graph()
        g.add_edge('A', 'B')
        g.add_edge('B', 'C')
        g.add_edge('C', 'A')
        
        self.assertTrue('B' in g)
        self.assertEqual(len(g), 3)
        
        g.remove_vertex('B')
        
        self.assertFalse('B' in g)
        self.assertEqual(len(g), 2)
        self.assertEqual(g.get_neighbors('A'), [])
        self.assertEqual(g.get_neighbors('C'), [])
    
    def test_remove_edge(self):
        g = Graph()
        g.add_edge('A', 'B')
        g.add_edge('B', 'C')
        g.add_edge('C', 'A')
        
        self.assertTrue(g.has_edge('A', 'B'))
        
        g.remove_edge('A', 'B')
        
        self.assertFalse(g.has_edge('A', 'B'))
        self.assertTrue(g.has_edge('B', 'C'))
        self.assertTrue(g.has_edge('C', 'A'))
    
    def test_directed_vs_undirected(self):
        undirected = Graph(directed=False)
        undirected.add_edge('A', 'B')
        self.assertTrue(undirected.has_edge('A', 'B'))
        self.assertTrue(undirected.has_edge('B', 'A'))
        
        directed = Graph(directed=True)
        directed.add_edge('A', 'B')
        self.assertTrue(directed.has_edge('A', 'B'))
        self.assertFalse(directed.has_edge('B', 'A'))

if __name__ == '__main__':
    unittest.main()
