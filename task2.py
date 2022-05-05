nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]


def flat_generator(some_list):
    for i in some_list:
        if isinstance(i, list):
            for item in i:
                yield item


for item in flat_generator(nested_list):
    print(item)

flat_list = [item for item in flat_generator(nested_list)]
print(flat_list)
