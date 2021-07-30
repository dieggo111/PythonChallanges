from typing import Any, Sequence

class IndexObject:
    def __init__(self, position: int, new_value: Any) -> None:
        self.flatIndex = 0
        self.position = position
        self.new_value = new_value

    @property
    def match(self) -> bool:
        if self.position == self.flatIndex:
           return True
        return False


def substitute_list_value(original_list: Sequence[Any], position: int, new_value: Any) -> Sequence[Any]:
    """Substitute value at flattened index *position* with *new_value*

    Args:
        original_list (Sequence[Any])
        position (int)
        new_value (Any)

    Raises:
        TypeError

    Returns:
        Sequence[Any]
    """
    if not isinstance(original_list, Sequence) or not isinstance(position, int):
        raise TypeError
    indexObj = IndexObject(position, new_value)
    return loop_over_list(original_list, indexObj)


def loop_over_list(a_list: Sequence[Any], indexObj: IndexObject) -> Sequence[Any]:
    temp_list = a_list
    for index, elem in enumerate(a_list):
        if isinstance(elem, list):
            temp_list[index] = loop_over_list(elem, indexObj)
        if not isinstance(elem, list):
            if indexObj.match:
                temp_list[index] = indexObj.new_value
            indexObj.flatIndex += 1
    return temp_list


if __name__ == "__main__":
    # new_list = substitute_list_value([0,1,2,3,[4,5,6,[7,8]]], 5, 'a')
    # new_list = substitute_list_value([0,[1],[2,[3,[4,[5,6]]]]], 5, 'a')
    new_list = substitute_list_value([[['f']], 'm', [22, [['a'], [54, [112]], 'd', [['s'], 8]]]], 8, 'z')
    print(new_list)
    # expected = [0,[1],[2,[3,[4,['a',6]]]]]
    # expected = [0,[1],[2,[3,[4,['a',6]]]]]
    expected = [[['f']], 'm', [22, [['a'], [54, [112]], 'd', [['s'], 'z']]]]
    print(expected == new_list)