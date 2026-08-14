class djikstra:
    def __init__(self,
                 size: [int, int],
                 start: [int, int],
                 end: [int, int],
                 list_wall: [[int, int]],
                 list_restriction: [int]
                 ) -> None:
        self.size = size
        self.start = start
        self.end = end
        self.list_wall = list_wall
        self.list_restriction = list_restriction





def print_tab(size: [int, int], start: [int, int], end: [int, int], list_wall: [[int, int]]):
    for row in range(size[0]):
        print('|', end='')
        for col in range(size[1]):
            if start == [row, col]:
                print('S|', end='')
            elif end == [row, col]:
                print('E|', end='')
            elif [row, col] in list_wall:
                print('X|', end='')
            else:
                print(' |', end='')
        print()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_tab([5, 3], start=[1, 2], end=[3, 2], list_wall=[[0, 0], [1, 1]])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
