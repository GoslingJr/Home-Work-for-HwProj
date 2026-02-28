from typing import Any, Optional, List, Tuple


class HashTable:
    
    def __init__(self, size: int = 128):

        if size != 128:
            raise ValueError("Table size must be 128 according to task requirements")
        
        self.size = size
        self.table: List[List[Tuple[str, Any]]] = [[] for _ in range(size)]
        self._count = 0
    
    def _hash(self, key: str) -> int:
        if not isinstance(key, str):
            raise TypeError("Key must be a string")
        
        hash_value = 0
        for char in key:
            hash_value = (hash_value * 31 + ord(char)) % self.size
        return hash_value
    
    def put(self, key: str, value: Any) -> None:
       
        index = self._hash(key)
        chain = self.table[index]
        
        for i, (k, v) in enumerate(chain):
            if k == key:
                chain[i] = (key, value)
                return
        
        chain.append((key, value))
        self._count += 1
    
    def get(self, key: str) -> Optional[Any]:
        
        index = self._hash(key)
        chain = self.table[index]
        
        for k, v in chain:
            if k == key:
                return v
        
        return None
    
    def remove(self, key: str) -> Optional[Any]:
  
        index = self._hash(key)
        chain = self.table[index]
        
        for i, (k, v) in enumerate(chain):
            if k == key:
                del chain[i]
                self._count -= 1
                return v
        
        return None
    
    def __contains__(self, key: str) -> bool:
        return self.get(key) is not None
    
    def __len__(self) -> int:
        return self._count
    
    def __str__(self) -> str:
        items = []
        for chain in self.table:
            for key, value in chain:
                items.append(f"{key!r}: {value!r}")
        return "{" + ", ".join(items) + "}"
    
    def load_factor(self) -> float:

        return self._count / self.size
    
    def display_stats(self) -> None:
        print("Hash Table Statistics:")
        print(f"Size: {self.size}")
        print(f"Elements: {self._count}")
        print(f"Load factor: {self.load_factor():.3f}")
        
        empty_slots = sum(1 for chain in self.table if not chain)
        print(f"Empty slots: {empty_slots}")
        
        max_chain_length = max(len(chain) for chain in self.table)
        print(f"Longest chain: {max_chain_length}")
