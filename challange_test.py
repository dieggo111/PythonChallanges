import unittest
from challange import substitute_list_value

class TestChallange(unittest.TestCase):
    def test_substitute_list_value_1(self):
        self.assertEqual(
            substitute_list_value([0,1,2,3,[4,5,6,[7,8]]], 5, 'a'),
            [0,1,2,3,[4,'a',6,[7,8]]]
        )

    def test_substitute_list_value_2(self):
        self.assertEqual(
            substitute_list_value([[['f']], 'm', [22, [['a'], [54, [112]], 'd', [['s'], 8]]]], 8, 'z'),
            [[['f']], 'm', [22, [['a'], [54, [112]], 'd', [['s'], 'z']]]]
        )

    def test_substitute_list_value_3(self):
        self.assertEqual(
            substitute_list_value([0,[1],[2,[3,[4,[5,6]]]]], 5, 'a'),
            [0,[1],[2,[3,[4,['a',6]]]]]
        )

    def test_substitute_list_value_4(self):
        self.assertEqual(
            substitute_list_value([], 5, 'a'),
            [0,[1],[2,[3,[4,['a',6]]]]]
        )


if __name__ == '__main__':
    unittest.main()