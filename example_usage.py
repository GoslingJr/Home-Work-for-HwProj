from src.hashtable import HashTable


def main():
    print("=== HashTable Example Usage ===")
    
    ht = HashTable()
    print("Created empty hash table")
    
    ht.put("name", "Alice")
    ht.put("age", 25)
    ht.put("city", "New York")
    ht.put("country", "USA")
    
    print("\nAdded 4 elements:")
    print(f"Table size: {len(ht)}")
    
    print("\nGetting values:")
    print(f"name: {ht.get('name')}")
    print(f"age: {ht.get('age')}")
    print(f"city: {ht.get('city')}")
    
    print("\nChecking keys:")
    print(f"'name' in table: {'name' in ht}")
    print(f"'salary' in table: {'salary' in ht}")
    
    print("\nUpdating 'age' to 26")
    ht.put("age", 26)
    print(f"New age: {ht.get('age')}")
    
    print("\nRemoving 'city'")
    removed = ht.remove("city")
    print(f"Removed value: {removed}")
    print(f"'city' in table after removal: {'city' in ht}")
    
    print("\nFinal statistics:")
    ht.display_stats()
    
    print(f"\nString representation: {ht}")
    
    print("\n=== Example completed ===")


if __name__ == "__main__":
    main()
