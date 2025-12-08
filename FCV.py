from typing import List, Tuple, Any, Union
from collections.abc import Sequence
import copy


class FrozenMatrix:
    
    def __init__(self, data: Union[List[List[Any]], Tuple[Tuple[Any, ...], ...], 'FrozenMatrix']):
        if isinstance(data, FrozenMatrix):
            self._data = data._data
            self._shape = data._shape
            self._hash = data._hash
            return
        
        if not isinstance(data, (list, tuple)):
            raise TypeError(f"Неверный тип данных: {type(data)}. Ожидается list или tuple.")
        
        if not all(isinstance(row, (list, tuple)) for row in data):
            raise TypeError("Все элементы должны быть списками или кортежами")
        
        first_len = len(data[0]) if data else 0
        if not all(len(row) == first_len for row in data):
            raise ValueError("Все строки матрицы должны иметь одинаковую длину")
        
        self._data = tuple(tuple(row) for row in data)
        self._shape = (len(data), first_len)
        self._hash = None  # Вычислится при первом вызове __hash__
    
    @property
    def shape(self) -> Tuple[int, int]:
        return self._shape
    
    def __getitem__(self, key: Union[int, Tuple[int, int], slice]) -> Any:
        if isinstance(key, tuple):
            if len(key) != 2:
                raise IndexError("Для матрицы нужны два индекса (строка, столбец)")
            row, col = key
            return self._data[row][col]
        elif isinstance(key, int):
            return self._data[key]
        elif isinstance(key, slice):
            return FrozenMatrix(self._data[key])
        else:
            raise TypeError(f"Неверный тип индекса: {type(key)}")
    
    def __repr__(self) -> str:
        return f"FrozenMatrix({list(list(row) for row in self._data)})"
    
    def __str__(self) -> str:
        if self._shape[0] == 0:
            return "FrozenMatrix([])"
        
        rows = []
        for row in self._data:
            row_str = "[ " + ", ".join(str(x) for x in row) + " ]"
            rows.append(row_str)
        
        return "FrozenMatrix([\n  " + ",\n  ".join(rows) + "\n])"
    
    def __len__(self) -> int:
        return self._shape[0]
    
    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, FrozenMatrix):
            return False
        
        if self._shape != other._shape:
            return False
        
        return self._data == other._data
    
    def __hash__(self) -> int:
        if self._hash is None:
            self._hash = hash((self._shape, self._data))
        return self._hash
    
    def __iter__(self):
        return iter(self._data)
    
    def transpose(self) -> 'FrozenMatrix':
        if self._shape[0] == 0 or self._shape[1] == 0:
            return self
        
        transposed = tuple(
            tuple(self._data[i][j] for i in range(self._shape[0]))
            for j in range(self._shape[1])
        )
        return FrozenMatrix(transposed)
    
    def flatten(self) -> Tuple[Any, ...]:
        return tuple(item for row in self._data for item in row)
    
    def to_list(self) -> List[List[Any]]:
        return [list(row) for row in self._data]
    
    def to_tuple(self) -> Tuple[Tuple[Any, ...], ...]:
        return self._data
    
    def copy(self) -> 'FrozenMatrix':
        return self
    
    def __add__(self, other: 'FrozenMatrix') -> 'FrozenMatrix':
        if not isinstance(other, FrozenMatrix):
            raise TypeError("Можно складывать только с другой FrozenMatrix")
        
        if self._shape != other._shape:
            raise ValueError("Матрицы должны быть одного размера для сложения")
        
        result = [
            [self._data[i][j] + other._data[i][j] for j in range(self._shape[1])]
            for i in range(self._shape[0])
        ]
        return FrozenMatrix(result)
    
    def __mul__(self, scalar: Union[int, float]) -> 'FrozenMatrix':
        if not isinstance(scalar, (int, float)):
            raise TypeError("Можно умножать только на число")
        
        result = [
            [self._data[i][j] * scalar for j in range(self._shape[1])]
            for i in range(self._shape[0])
        ]
        return FrozenMatrix(result)
    
    def __rmul__(self, scalar: Union[int, float]) -> 'FrozenMatrix':
        return self.__mul__(scalar)
    
    @classmethod
    def zeros(cls, rows: int, cols: int) -> 'FrozenMatrix':
        if rows < 0 or cols < 0:
            raise ValueError("Размеры матрицы не могут быть отрицательными")
        
        data = [[0] * cols for _ in range(rows)]
        return cls(data)
    
    @classmethod
    def identity(cls, n: int) -> 'FrozenMatrix':
        if n < 0:
            raise ValueError("Размер матрицы не может быть отрицательным")
        
        data = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        return cls(data)
    
    @classmethod
    def from_list_of_lists(cls, data: List[List[Any]]) -> 'FrozenMatrix':
        return cls(data)


def demonstrate_frozen_matrix():
    
    print("=== Демонстрация FrozenMatrix ===\n")
    
    print("1. Создание матриц:")
    m1 = FrozenMatrix([[1, 2, 3], [4, 5, 6]])
    m2 = FrozenMatrix([[7, 8, 9], [10, 11, 12]])
    m3 = FrozenMatrix([[1, 2, 3], [4, 5, 6]]) 
    
    print(f"m1 = {m1}")
    print(f"m2 = {m2}")
    print(f"m3 = {m3}")
    print(f"m1.shape = {m1.shape}")
    print(f"m2.shape = {m2.shape}")
    
    print(f"\n2. Проверка равенства:")
    print(f"m1 == m2: {m1 == m2}")
    print(f"m1 == m3: {m1 == m3}")
    
    print(f"\n3. Хэширование:")
    print(f"hash(m1) = {hash(m1)}")
    print(f"hash(m2) = {hash(m2)}")
    print(f"hash(m3) = {hash(m3)} (должен совпадать с hash(m1))")
    
    print(f"\n4. Использование как ключа в словаре:")
    matrix_dict = {
        m1: "Первая матрица",
        m2: "Вторая матрица",
        m3: "Третья матрица (перезапишет первую)"
    }
    
    print("Содержимое словаря:")
    for key, value in matrix_dict.items():
        print(f"  {key} -> {value}")
    
    print(f"\n5. Использование как элемента множества:")
    matrix_set = {m1, m2, m3}
    print(f"Множество содержит {len(matrix_set)} элементов (m1 и m3 должны быть одинаковыми)")
    for mat in matrix_set:
        print(f"  {mat}")
    
    print(f"\n6. Доступ к элементам:")
    print(f"m1[0, 1] = {m1[0, 1]}")
    print(f"m1[1] = {m1[1]}")
    
    print(f"\n7. Транспонирование:")
    m1_t = m1.transpose()
    print(f"m1.transpose() = {m1_t}")
    print(f"m1_t.shape = {m1_t.shape}")
    
    print(f"\n8. Операции с матрицами:")
    print(f"m1 + m2 = {m1 + m2}")
    print(f"m1 * 3 = {m1 * 3}")
    print(f"2 * m1 = {2 * m1}")
    
    print(f"\n9. Статические методы создания:")
    zeros = FrozenMatrix.zeros(2, 3)
    identity = FrozenMatrix.identity(3)
    
    print(f"zeros(2, 3) = {zeros}")
    print(f"identity(3) = {identity}")
    
    print(f"\n10. Итерация по матрице:")
    print("Строки m1:")
    for i, row in enumerate(m1):
        print(f"  Строка {i}: {row}")
    
    print(f"\n11. Проверка неизменяемости:")
    print("Попытка изменить матрицу через to_list() и модификацию списка не изменяет оригинал")
    list_copy = m1.to_list()
    list_copy[0][0] = 999
    print(f"  Измененная копия: {list_copy}")
    print(f"  Оригинал m1: {m1}")
    print(f"  Оригинал не изменился: {m1[0, 0] == 1}")


def test_frozen_matrix():
    """Тестирование корректности работы FrozenMatrix."""
    
    print("\n=== Тестирование FrozenMatrix ===\n")
    
    tests_passed = 0
    tests_total = 0
    
    # Тест 1: Создание и равенство
    try:
        m1 = FrozenMatrix([[1, 2], [3, 4]])
        m2 = FrozenMatrix([[1, 2], [3, 4]])
        assert m1 == m2
        assert hash(m1) == hash(m2)
        print(" Тест 1: Создание и равенство - ПРОЙДЕН")
        tests_passed += 1
    except Exception as e:
        print(f" Тест 1: Создание и равенство - ПРОВАЛЕН: {e}")
    tests_total += 1
    
    # Тест 2: Использование в словаре
    try:
        m1 = FrozenMatrix([[1, 2], [3, 4]])
        m2 = FrozenMatrix([[5, 6], [7, 8]])
        d = {m1: "value1", m2: "value2"}
        assert d[m1] == "value1"
        assert d[m2] == "value2"
        print(" Тест 2: Использование в словаре - ПРОЙДЕН")
        tests_passed += 1
    except Exception as e:
        print(f" Тест 2: Использование в словаре - ПРОВАЛЕН: {e}")
    tests_total += 1
    
    # Тест 3: Использование в множестве
    try:
        m1 = FrozenMatrix([[1, 2], [3, 4]])
        m2 = FrozenMatrix([[1, 2], [3, 4]])
        m3 = FrozenMatrix([[5, 6], [7, 8]])
        s = {m1, m2, m3}
        assert len(s) == 2
        print(" Тест 3: Использование в множестве - ПРОЙДЕН")
        tests_passed += 1
    except Exception as e:
        print(f" Тест 3: Использование в множестве - ПРОЙДЕН: {e}")
    tests_total += 1
    
    # Тест 4: Неизменяемость
    try:
        m1 = FrozenMatrix([[1, 2], [3, 4]])
        # Попытка "изменить" через to_list
        lst = m1.to_list()
        lst[0][0] = 100
        assert m1[0, 0] == 1
        print(" Тест 4: Неизменяемость - ПРОЙДЕН")
        tests_passed += 1
    except Exception as e:
        print(f" Тест 4: Неизменяемость - ПРОВАЛЕН: {e}")
    tests_total += 1
    
    # Тест 5: Операции
    try:
        m1 = FrozenMatrix([[1, 2], [3, 4]])
        m2 = FrozenMatrix([[5, 6], [7, 8]])
        result = m1 + m2
        expected = FrozenMatrix([[6, 8], [10, 12]])
        assert result == expected
        print(" Тест 5: Операции - ПРОЙДЕН")
        tests_passed += 1
    except Exception as e:
        print(f" Тест 5: Операции - ПРОВАЛЕН: {e}")
    tests_total += 1
    
    print(f"\nРезультаты тестирования: {tests_passed}/{tests_total} тестов пройдено")
    
    if tests_passed == tests_total:
        print(" Все тесты пройдены успешно!")
    else:
        print(" Некоторые тесты не пройдены")


if __name__ == "__main__":
    demonstrate_frozen_matrix()
    
    test_frozen_matrix()