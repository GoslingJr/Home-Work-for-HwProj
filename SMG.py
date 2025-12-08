class MatrixError(Exception):
    pass

class MatrixDimensionError(MatrixError):
    pass

class MatrixMultiplicationError(MatrixDimensionError):
    pass

class MatrixAdditionError(MatrixDimensionError):
    pass

class NotSquareMatrixError(MatrixError):
    pass

class MatrixInversionError(MatrixError):
    pass


class Matrix:
    def __init__(self, data):
        if not data:
            raise ValueError("Матрица не может быть пустой")
        
        if not isinstance(data, (list, tuple)):
            raise TypeError(f"Ожидается list или tuple, получен {type(data)}")
        
        self._data = []
        first_row_len = None
        
        for i, row in enumerate(data):
            if not isinstance(row, (list, tuple)):
                raise TypeError(f"Строка {i} должна быть list или tuple")
            
            row_list = list(row)
            
            for j, element in enumerate(row_list):
                if not isinstance(element, (int, float)):
                    raise TypeError(f"Элемент [{i}][{j}] должен быть числом")
                row_list[j] = float(element)
            
            if first_row_len is None:
                first_row_len = len(row_list)
            elif len(row_list) != first_row_len:
                raise ValueError(f"Все строки должны иметь одинаковую длину")
            
            self._data.append(row_list)
        
        self._rows = len(self._data)
        self._cols = first_row_len if first_row_len is not None else 0
    
    @property
    def shape(self):
        return (self._rows, self._cols)
    
    @property
    def rows(self):
        return self._rows
    
    @property
    def cols(self):
        return self._cols
    
    @property
    def T(self):
        return self.transpose()
    
    def __getitem__(self, key):
        if isinstance(key, tuple):
            if len(key) != 2:
                raise IndexError("Для матрицы нужны два индекса")
            row, col = key
            return self._data[row][col]
        elif isinstance(key, int):
            return self._data[key]
        elif isinstance(key, slice):
            return Matrix(self._data[key])
        else:
            raise TypeError(f"Неверный тип индекса: {type(key)}")
    
    def __setitem__(self, key, value):
        if isinstance(key, tuple):
            if len(key) != 2:
                raise IndexError("Для матрицы нужны два индекса")
            row, col = key
            self._data[row][col] = float(value)
        elif isinstance(key, int):
            if isinstance(value, list):
                if len(value) != self._cols:
                    raise ValueError(f"Строка должна содержать {self._cols} элементов")
                self._data[key] = [float(x) for x in value]
            else:
                raise TypeError("Для установки строки нужно передать список")
        else:
            raise TypeError(f"Неверный тип индекса: {type(key)}")
    
    def __repr__(self):
        return f"Matrix({self._data})"
    
    def __str__(self):
        if self._rows == 0 or self._cols == 0:
            return "Matrix([])"
        
        col_widths = []
        for j in range(self._cols):
            max_width = 0
            for i in range(self._rows):
                width = len(f"{self._data[i][j]:.6g}")
                max_width = max(max_width, width)
            col_widths.append(max_width)
        
        lines = []
        for i in range(self._rows):
            row_str = "  "
            elements = []
            for j in range(self._cols):
                element = f"{self._data[i][j]:.6g}"
                elements.append(element.rjust(col_widths[j]))
            row_str += "  ".join(elements)
            lines.append(row_str)
        
        return "Matrix([\n" + "\n".join(lines) + "\n])"
    
    def __len__(self):
        return self._rows
    
    def __iter__(self):
        return iter(self._data)
    
    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False
        
        if self.shape != other.shape:
            return False
        
        for i in range(self._rows):
            for j in range(self._cols):
                if abs(self._data[i][j] - other._data[i][j]) > 1e-10:
                    return False
        
        return True
    
    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f"Можно складывать только матрицы. Получен {type(other)}")
        
        if self.shape != other.shape:
            raise MatrixAdditionError(f"Несовпадающие размеры: {self.shape} и {other.shape}")
        
        result = [
            [self._data[i][j] + other._data[i][j] for j in range(self._cols)]
            for i in range(self._rows)
        ]
        
        return Matrix(result)
    
    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f"Можно вычитать только матрицы. Получен {type(other)}")
        
        if self.shape != other.shape:
            raise MatrixAdditionError(f"Несовпадающие размеры: {self.shape} и {other.shape}")
        
        result = [
            [self._data[i][j] - other._data[i][j] for j in range(self._cols)]
            for i in range(self._rows)
        ]
        
        return Matrix(result)
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = [
                [self._data[i][j] * other for j in range(self._cols)]
                for i in range(self._rows)
            ]
            return Matrix(result)
        
        elif isinstance(other, Matrix):
            if self._cols != other._rows:
                raise MatrixMultiplicationError(
                    f"Несовместимые размеры для умножения: {self.shape} и {other.shape}"
                )
            
            result = []
            for i in range(self._rows):
                row = []
                for j in range(other._cols):
                    element = sum(
                        self._data[i][k] * other._data[k][j]
                        for k in range(self._cols)
                    )
                    row.append(element)
                result.append(row)
            
            return Matrix(result)
        
        else:
            raise TypeError(f"Неподдерживаемый тип для умножения: {type(other)}")
    
    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return self.__mul__(other)
        raise TypeError(f"Неподдерживаемый тип для умножения: {type(other)}")
    
    def __matmul__(self, other):
        return self.__mul__(other)
    
    def __pow__(self, power):
        if not isinstance(power, int) or power < 0:
            raise ValueError("Степень должна быть целым неотрицательным числом")
        
        if self._rows != self._cols:
            raise NotSquareMatrixError("Матрица должна быть квадратной для возведения в степень")
        
        if power == 0:
            return Matrix.identity(self._rows)
        
        result = self.copy()
        for _ in range(power - 1):
            result = result @ self
        
        return result
    
    def determinant(self):
        if self._rows != self._cols:
            raise NotSquareMatrixError("Определитель можно вычислить только для квадратной матрицы")
        
        return self._determinant_recursive(self._data)
    
    def _determinant_recursive(self, matrix):
        n = len(matrix)
        
        if n == 1:
            return matrix[0][0]
        if n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        
        det = 0.0
        for col in range(n):
            minor = []
            for i in range(1, n):
                row_minor = []
                for j in range(n):
                    if j != col:
                        row_minor.append(matrix[i][j])
                minor.append(row_minor)
            
            minor_det = self._determinant_recursive(minor)
            det += ((-1) ** col) * matrix[0][col] * minor_det
        
        return det
    
    def transpose(self):
        result = [
            [self._data[i][j] for i in range(self._rows)]
            for j in range(self._cols)
        ]
        return Matrix(result)
    
    def copy(self):
        import copy
        return Matrix(copy.deepcopy(self._data))
    
    def to_list(self):
        import copy
        return copy.deepcopy(self._data)
    
    @classmethod
    def zeros(cls, rows, cols):
        if rows <= 0 or cols <= 0:
            raise ValueError("Размеры должны быть положительными")
        
        data = [[0.0] * cols for _ in range(rows)]
        return cls(data)
    
    @classmethod
    def ones(cls, rows, cols):
        if rows <= 0 or cols <= 0:
            raise ValueError("Размеры должны быть положительными")
        
        data = [[1.0] * cols for _ in range(rows)]
        return cls(data)
    
    @classmethod
    def identity(cls, n):
        if n <= 0:
            raise ValueError("Размер должен быть положительным")
        
        data = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
        return cls(data)
    
    @classmethod
    def diagonal(cls, diag_values):
        n = len(diag_values)
        data = [[diag_values[i] if i == j else 0.0 for j in range(n)] for i in range(n)]
        return cls(data)


def inverse(matrix):
    if matrix.rows != matrix.cols:
        raise NotSquareMatrixError("Матрица должна быть квадратной")
    
    n = matrix.rows
    det = matrix.determinant()
    
    if abs(det) < 1e-12:
        raise MatrixInversionError("Матрица вырождена, обратной не существует")
    
    adjugate = []
    
    for i in range(n):
        adj_row = []
        for j in range(n):
            minor = []
            for row_idx in range(n):
                if row_idx == i:
                    continue
                minor_row = []
                for col_idx in range(n):
                    if col_idx == j:
                        continue
                    minor_row.append(matrix[row_idx, col_idx])
                minor.append(minor_row)
            
            minor_det = _determinant_recursive(minor)
            cofactor = ((-1) ** (i + j)) * minor_det
            adj_row.append(cofactor)
        
        adjugate.append(adj_row)
    
    adj_matrix = Matrix(adjugate).transpose()
    return adj_matrix * (1.0 / det)


def _determinant_recursive(matrix):
    n = len(matrix)
    
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0.0
    for col in range(n):
        minor = []
        for i in range(1, n):
            row_minor = []
            for j in range(n):
                if j != col:
                    row_minor.append(matrix[i][j])
            minor.append(row_minor)
        
        minor_det = _determinant_recursive(minor)
        det += ((-1) ** col) * matrix[0][col] * minor_det
    
    return det


def trace(matrix):
    if matrix.rows != matrix.cols:
        raise NotSquareMatrixError("Матрица должна быть квадратной")
    
    return sum(matrix[i, i] for i in range(matrix.rows))


def random_matrix(rows, cols, min_val=0.0, max_val=1.0, seed=None):
    import random
    if seed is not None:
        random.seed(seed)
    
    data = [
        [random.uniform(min_val, max_val) for _ in range(cols)]
        for _ in range(rows)
    ]
    
    return Matrix(data)


def block_diag(*matrices):
    if not matrices:
        raise ValueError("Нужно передать хотя бы одну матрицу")
    
    total_rows = sum(m.rows for m in matrices)
    total_cols = sum(m.cols for m in matrices)
    
    result_data = [[0.0] * total_cols for _ in range(total_rows)]
    
    row_offset = 0
    col_offset = 0
    
    for matrix in matrices:
        for i in range(matrix.rows):
            for j in range(matrix.cols):
                result_data[row_offset + i][col_offset + j] = matrix[i, j]
        
        row_offset += matrix.rows
        col_offset += matrix.cols
    
    return Matrix(result_data)


def vstack(*matrices):
    if not matrices:
        raise ValueError("Нужно передать хотя бы одну матрицу")
    
    cols = matrices[0].cols
    if any(m.cols != cols for m in matrices):
        raise ValueError("Все матрицы должны иметь одинаковое количество столбцов")
    
    result_data = []
    for matrix in matrices:
        result_data.extend(matrix.to_list())
    
    return Matrix(result_data)


def hstack(*matrices):
    if not matrices:
        raise ValueError("Нужно передать хотя бы одну матрицу")
    
    rows = matrices[0].rows
    if any(m.rows != rows for m in matrices):
        raise ValueError("Все матрицы должны иметь одинаковое количество строк")
    
    result_data = []
    for i in range(rows):
        row = []
        for matrix in matrices:
            row.extend(matrix.to_list()[i])
        result_data.append(row)
    
    return Matrix(result_data)


def eye(n):
    return Matrix.identity(n)


def zeros(rows, cols):
    return Matrix.zeros(rows, cols)


def ones(rows, cols):
    return Matrix.ones(rows, cols)


if __name__ == "__main__":
    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ПАКЕТА ДЛЯ РАБОТЫ С МАТРИЦАМИ")
    print("=" * 60)
    
    print("\n1. Тестирование создания матриц...")
    A = Matrix([[1, 2, 3], [4, 5, 6]])
    B = Matrix([[7, 8, 9], [10, 11, 12]])
    print(f"A.shape = {A.shape}")
    print(f"A[0,1] = {A[0,1]}")
    
    print("\n2. Тестирование сложения и вычитания...")
    C = A + B
    D = B - A
    print(f"A + B[0,0] = {C[0,0]}")
    print(f"B - A[1,2] = {D[1,2]}")
    
    print("\n3. Тестирование умножения на скаляр...")
    E = A * 2
    print(f"A * 2[1,1] = {E[1,1]}")
    
    print("\n4. Тестирование умножения матриц...")
    F = Matrix([[1, 2], [3, 4], [5, 6]])
    G = Matrix([[7, 8], [9, 10]])
    H = F @ G
    print(f"F @ G[0,0] = {H[0,0]}")
    
    print("\n5. Тестирование определителя...")
    I = Matrix([[4, 7], [2, 6]])
    det_I = I.determinant()
    print(f"det([[4,7],[2,6]]) = {det_I}")
    
    print("\n6. Тестирование обратной матрицы...")
    try:
        I_inv = inverse(I)
        print(f"I @ I_inv = единичная матрица: {(I @ I_inv).to_list()}")
    except Exception as e:
        print(f"Ошибка: {e}")
    
    print("\n7. Тестирование итерирования...")
    print("Строки матрицы A:")
    for row in A:
        print(f"  {row}")
    
    print("\n8. Тестирование транспонирования...")
    A_T = A.T
    print(f"A.T.shape = {A_T.shape}")
    
    print("\n9. Тестирование возведения в степень...")
    J = Matrix([[1, 2], [3, 4]])
    J2 = J ** 2
    print(f"J^2 = {J2.to_list()}")
    
    print("\n10. Тестирование trace...")
    trace_J = trace(J)
    print(f"trace(J) = {trace_J}")
    
    print("\n11. Тестирование специальных матриц...")
    print(f"zeros(2,3) = {zeros(2,3)}")
    print(f"eye(3) = {eye(3)}")
    print(f"ones(2,2) = {ones(2,2)}")
    
    print("\n12. Тестирование случайной матрицы...")
    R = random_matrix(3, 3, seed=42)
    print(f"random_matrix(3,3) первые элементы: {R[0,0]:.3f}, {R[1,1]:.3f}")
    
    print("\n" + "=" * 60)
    print("ТЕСТИРОВАНИЕ ЗАВЕРШЕНО")
    print("=" * 60)