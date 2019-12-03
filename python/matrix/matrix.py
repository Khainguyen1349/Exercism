class Matrix(object):
    def __init__(self, matrix_string):
        line = matrix_string.split('\n')
        self.mat = [[int(num) for num in item.split(' ')] for item in line]

    def row(self, index):
        return list(self.mat[index-1])

    def column(self, index):
        return [col[index-1] for col in self.mat]
