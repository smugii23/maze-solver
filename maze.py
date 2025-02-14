from cell import Cell


class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
    
    def _create_cells(self):
        self._cells = [[None] * self.num_cols for _ in range(self.num_rows)]
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                cell = Cell(self.win)
                self._cells[i][j] = cell
                self._draw_cell(i, j)


                