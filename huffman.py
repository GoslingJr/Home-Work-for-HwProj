import heapq
from collections import Counter
import pickle
import struct
import os

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_frequency_table(text):
    return Counter(text)

def build_huffman_tree(freq_table):
    heap = []
    for char, freq in freq_table.items():
        heapq.heappush(heap, Node(char, freq))
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        
        heapq.heappush(heap, merged)
    
    return heap[0] if heap else None

def build_coding_table(root):
    def traverse(node, code, table):
        if node.char is not None:
            table[node.char] = code
            return
        
        traverse(node.left, code + "0", table)
        traverse(node.right, code + "1", table)
    
    table = {}
    if root:
        traverse(root, "", table)
    return table

def encode(msg):
    if not msg:
        return "", {}
    
    freq_table = build_frequency_table(msg)
    root = build_huffman_tree(freq_table)
    coding_table = build_coding_table(root)
    
    encoded_bits = ''.join(coding_table[char] for char in msg)
    
    return encoded_bits, coding_table

def decode(encoded, table):
    if not encoded:
        return ""
    
    reverse_table = {code: char for char, code in table.items()}
    
    result = []
    current_code = ""
    
    for bit in encoded:
        current_code += bit
        if current_code in reverse_table:
            result.append(reverse_table[current_code])
            current_code = ""
    
    return ''.join(result)

def pad_encoded_bits(encoded_bits):
    padding = 8 - len(encoded_bits) % 8
    if padding != 8:
        encoded_bits += '0' * padding
    return encoded_bits, padding

def bits_to_bytes(bits):
    byte_array = bytearray()
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        byte_array.append(int(byte, 2))
    return bytes(byte_array)

def bytes_to_bits(byte_data, padding):
    bits = ''.join(f'{byte:08b}' for byte in byte_data)
    if padding != 0:
        bits = bits[:-padding]
    return bits

def encode_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    encoded_bits, coding_table = encode(text)
    
    padded_bits, padding = pad_encoded_bits(encoded_bits)
    encoded_bytes = bits_to_bytes(padded_bits)
    
    table_data = pickle.dumps(coding_table)
    table_size = len(table_data)
    
    with open(output_file, 'wb') as f:
        f.write(struct.pack('III', len(text), padding, table_size))
        f.write(table_data)
        f.write(encoded_bytes)
    
    original_size = os.path.getsize(input_file)
    compressed_size = 12 + table_size + len(encoded_bytes)
    
    print(f"Original size: {original_size} bytes")
    print(f"Compressed size: {compressed_size} bytes")
    print(f"Compression ratio: {original_size/compressed_size:.2f}x")

def decode_file(input_file, output_file):
    with open(input_file, 'rb') as f:
        header = f.read(12)
        if len(header) != 12:
            raise ValueError("Invalid file format")
        
        text_length, padding, table_size = struct.unpack('III', header)
        
        table_data = f.read(table_size)
        if len(table_data) != table_size:
            raise ValueError("Invalid table size")
        
        coding_table = pickle.loads(table_data)
        
        encoded_bytes = f.read()
    
    encoded_bits = bytes_to_bits(encoded_bytes, padding)
    decoded_text = decode(encoded_bits, coding_table)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(decoded_text)
    
    print(f"File decoded successfully. Restored {len(decoded_text)} characters.")

def encode_binary_file(input_file, output_file):
    with open(input_file, 'rb') as f:
        binary_data = f.read()
    
    text = ''.join(chr(byte) for byte in binary_data)
    
    encoded_bits, coding_table = encode(text)
    
    padded_bits, padding = pad_encoded_bits(encoded_bits)
    encoded_bytes = bits_to_bytes(padded_bits)
    
    table_data = pickle.dumps(coding_table)
    table_size = len(table_data)
    
    with open(output_file, 'wb') as f:
        f.write(struct.pack('III', len(binary_data), padding, table_size))
        f.write(table_data)
        f.write(encoded_bytes)
    
    print(f"Binary file encoded.")

def decode_binary_file(input_file, output_file):
    with open(input_file, 'rb') as f:
        header = f.read(12)
        if len(header) != 12:
            raise ValueError("Invalid file format")
        
        data_length, padding, table_size = struct.unpack('III', header)
        
        table_data = f.read(table_size)
        if len(table_data) != table_size:
            raise ValueError("Invalid table size")
        
        coding_table = pickle.loads(table_data)
        
        encoded_bytes = f.read()
    
    encoded_bits = bytes_to_bits(encoded_bytes, padding)
    decoded_text = decode(encoded_bits, coding_table)
    
    decoded_bytes = bytes(ord(char) for char in decoded_text)
    
    with open(output_file, 'wb') as f:
        f.write(decoded_bytes)
    
    print(f"Binary file decoded successfully.")

def test_example():
    print("=== Huffman Coding Test ===")
    
    text = "hello world"
    print(f"\nOriginal text: '{text}'")
    
    encoded, table = encode(text)
    print(f"Encoding table: {table}")
    print(f"Encoded bits: {encoded}")
    
    decoded = decode(encoded, table)
    print(f"Decoded text: '{decoded}'")
    print(f"Match: {text == decoded}")

if __name__ == "__main__":
    test_example()
