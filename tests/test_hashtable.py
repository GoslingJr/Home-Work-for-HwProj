import pytest
from src.hashtable import HashTable


class TestHashTable:
    
    def test_init_default_size(self):
        ht = HashTable()
        assert ht.size == 128
        assert len(ht.table) == 128
        assert len(ht) == 0
    
    def test_init_custom_size(self):
        ht = HashTable(128)
        assert ht.size == 128
        
        with pytest.raises(ValueError):
            HashTable(100)
    
    def test_hash_function_range(self):
        ht = HashTable()
        
        test_keys = ["hello", "world", "test", "key", "python", "hash", "table"]
        
        for key in test_keys:
            hash_value = ht._hash(key)
            assert 0 <= hash_value < 128, f"Hash for '{key}' out of range: {hash_value}"
    
    def test_put_and_get(self):
        ht = HashTable()
        
        ht.put("name", "Alice")
        ht.put("age", 25)
        ht.put("city", "Moscow")
        
        assert ht.get("name") == "Alice"
        assert ht.get("age") == 25
        assert ht.get("city") == "Moscow"
        assert ht.get("country") is None
    
    def test_put_overwrite(self):
        ht = HashTable()
        
        ht.put("key", "value1")
        assert ht.get("key") == "value1"
        
        ht.put("key", "value2")
        assert ht.get("key") == "value2"
        assert len(ht) == 1
    
    def test_remove(self):
        ht = HashTable()
        
        ht.put("key1", "value1")
        ht.put("key2", "value2")
        
        assert len(ht) == 2
        
        removed = ht.remove("key1")
        assert removed == "value1"
        assert len(ht) == 1
        assert ht.get("key1") is None
        
        removed = ht.remove("nonexistent")
        assert removed is None
        assert len(ht) == 1
    
    def test_collision_handling(self):
        ht = HashTable()
        
        for i in range(10):
            ht.put(f"key{i}", f"value{i}")
        
        for i in range(10):
            assert ht.get(f"key{i}") == f"value{i}"
    
    def test_contains(self):
        ht = HashTable()
        
        ht.put("test", "value")
        
        assert "test" in ht
        assert "nonexistent" not in ht
    
    def test_len(self):
        ht = HashTable()
        
        assert len(ht) == 0
        
        for i in range(5):
            ht.put(f"key{i}", f"value{i}")
        
        assert len(ht) == 5
        
        ht.remove("key0")
        assert len(ht) == 4
    
    def test_load_factor(self):
        ht = HashTable()
        
        assert ht.load_factor() == 0.0
        
        ht.put("key1", "value1")
        assert ht.load_factor() == 1 / 128
        
        ht.put("key2", "value2")
        assert ht.load_factor() == 2 / 128
    
    def test_hash_function_type_check(self):
        ht = HashTable()
        
        assert ht._hash("test") >= 0
        
        with pytest.raises(TypeError):
            ht._hash(123)
        
        with pytest.raises(TypeError):
            ht._hash(None)
    
    def test_comprehensive_operations(self):
        ht = HashTable()
        
        items = [("a", 1), ("b", 2), ("c", 3), ("d", 4), ("e", 5)]
        
        for key, value in items:
            ht.put(key, value)
        
        for key, value in items:
            assert ht.get(key) == value
        
        assert ht.remove("b") == 2
        assert ht.remove("d") == 4
        
        assert ht.get("a") == 1
        assert ht.get("b") is None
        assert ht.get("c") == 3
        assert ht.get("d") is None
        assert ht.get("e") == 5
        
        assert len(ht) == 3
    
    def test_display_stats(self, capsys):
        ht = HashTable()
        
        ht.put("key1", "value1")
        ht.put("key2", "value2")
        
        ht.display_stats()
        captured = capsys.readouterr()
        assert "Hash Table Statistics:" in captured.out
        assert "Size: 128" in captured.out
        assert "Elements: 2" in captured.out
