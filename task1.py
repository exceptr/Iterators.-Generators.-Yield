nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class FlatIterator:

    def __init__(self, some_list):
        self.some_list = some_list

    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        nested_list_new = []
        self.cursor += 1
        if self.cursor == 11:
            raise StopIteration
        for item in self.some_list:
            for i in item:
                nested_list_new.append(i)
        return nested_list_new[self.cursor]


for item in FlatIterator(nested_list):
    print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)