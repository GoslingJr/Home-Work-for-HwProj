from collections import defaultdict, deque

class Graph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.vertices = set()
        self.directed = directed
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.vertices.add(u)
        self.vertices.add(v)
        
        if not self.directed:
            self.graph[v].append(u)
    
    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []
        self.vertices.add(v)
    
    def remove_edge(self, u, v):
        if u in self.graph and v in self.graph[u]:
            self.graph[u].remove(v)
            
            if not self.directed and v in self.graph and u in self.graph[v]:
                self.graph[v].remove(u)
    
    def remove_vertex(self, v):
        if v in self.graph:
            del self.graph[v]
            self.vertices.discard(v)
            
            for vertex in self.graph:
                if v in self.graph[vertex]:
                    self.graph[vertex].remove(v)
    
    def get_neighbors(self, v):
        return self.graph.get(v, [])
    
    def has_edge(self, u, v):
        return v in self.graph.get(u, [])
    
    def get_vertices(self):
        return list(self.vertices)
    
    def get_edges(self):
        edges = []
        for u in self.graph:
            for v in self.graph[u]:
                if not self.directed and (v, u) not in edges:
                    edges.append((u, v))
                elif self.directed:
                    edges.append((u, v))
        return edges
    
    def dfs(self, start_vertex=None):
        if not self.vertices:
            return []
        
        if start_vertex is None:
            start_vertex = next(iter(self.vertices))
        elif start_vertex not in self.vertices:
            raise ValueError(f"Vertex {start_vertex} not in graph")
        
        visited = []
        stack = [start_vertex]
        visited_set = set()
        
        while stack:
            vertex = stack.pop()
            
            if vertex not in visited_set:
                visited.append(vertex)
                visited_set.add(vertex)
                
                for neighbor in self.graph.get(vertex, []):
                    if neighbor not in visited_set:
                        stack.append(neighbor)
        
        return visited
    
    def dfs_recursive(self, start_vertex=None):
        if not self.vertices:
            return []
        
        if start_vertex is None:
            start_vertex = next(iter(self.vertices))
        elif start_vertex not in self.vertices:
            raise ValueError(f"Vertex {start_vertex} not in graph")
        
        visited = []
        visited_set = set()
        
        def dfs_util(vertex):
            visited.append(vertex)
            visited_set.add(vertex)
            
            for neighbor in self.graph.get(vertex, []):
                if neighbor not in visited_set:
                    dfs_util(neighbor)
        
        dfs_util(start_vertex)
        return visited
    
    def bfs(self, start_vertex=None):
        if not self.vertices:
            return []
        
        if start_vertex is None:
            start_vertex = next(iter(self.vertices))
        elif start_vertex not in self.vertices:
            raise ValueError(f"Vertex {start_vertex} not in graph")
        
        visited = []
        queue = deque([start_vertex])
        visited_set = set([start_vertex])
        
        while queue:
            vertex = queue.popleft()
            visited.append(vertex)
            
            for neighbor in self.graph.get(vertex, []):
                if neighbor not in visited_set:
                    queue.append(neighbor)
                    visited_set.add(neighbor)
        
        return visited
    
    def __iter__(self):
        self._dfs_order = self.dfs()
        self._index = 0
        return self
    
    def __next__(self):
        if self._index < len(self._dfs_order):
            vertex = self._dfs_order[self._index]
            self._index += 1
            return vertex
        raise StopIteration
    
    def __len__(self):
        return len(self.vertices)
    
    def __contains__(self, vertex):
        return vertex in self.vertices
    
    def __str__(self):
        result = []
        result.append(f"Graph (directed={self.directed}):")
        for vertex in sorted(self.vertices):
            neighbors = sorted(self.graph.get(vertex, []))
            result.append(f"  {vertex}: {neighbors}")
        return "\n".join(result)
    
    def __repr__(self):
        return f"Graph(directed={self.directed}, vertices={len(self.vertices)}, edges={len(self.get_edges())})"
