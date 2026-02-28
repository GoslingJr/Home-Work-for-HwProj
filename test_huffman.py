import unittest
import tempfile
import os
from huffman import encode, decode, encode_file, decode_file

class TestHuffman(unittest.TestCase):
    
    def test_encode_decode_simple(self):
        text = "hello world"
        encoded, table = encode(text)
        decoded = decode(encoded, table)
        self.assertEqual(text, decoded)
    
    def test_encode_decode_empty(self):
        text = ""
        encoded, table = encode(text)
        decoded = decode(encoded, table)
        self.assertEqual(text, decoded)
    
    def test_encode_decode_special_chars(self):
        text = "привет мир! 123 @#$"
        encoded, table = encode(text)
        decoded = decode(encoded, table)
        self.assertEqual(text, decoded)
    
    def test_encode_decode_repeated(self):
        text = "aaaaabbbbcccdde"
        encoded, table = encode(text)
        decoded = decode(encoded, table)
        self.assertEqual(text, decoded)
        
        original_bits = len(text) * 8
        compressed_bits = len(encoded)
        self.assertLess(compressed_bits, original_bits)
    
    def test_file_encode_decode(self):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            input_file = f.name
            f.write("Test content for file encoding. " * 10)
        
        encoded_file = input_file + ".huff"
        decoded_file = input_file + ".decoded.txt"
        
        try:
            encode_file(input_file, encoded_file)
            decode_file(encoded_file, decoded_file)
            
            with open(input_file, 'r', encoding='utf-8') as f1, \
                 open(decoded_file, 'r', encoding='utf-8') as f2:
                original = f1.read()
                decoded = f2.read()
            
            self.assertEqual(original, decoded)
            
        finally:
            for file in [input_file, encoded_file, decoded_file]:
                if os.path.exists(file):
                    os.remove(file)

if __name__ == '__main__':
    unittest.main()
