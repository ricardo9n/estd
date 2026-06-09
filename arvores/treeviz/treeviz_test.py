import unittest

import treeviz


class DummyBinaryTree:
    def __init__(self, value=None, left=None, right=None):
        self._value = value
        self._left = left
        self._right = right

    def getRootVal(self):
        return self._value

    def getLeftChild(self):
        return self._left

    def getRightChild(self):
        return self._right


class DrawPublicApiTests(unittest.TestCase):
    def setUp(self):
        self.sample = [
            "A",
            ["B", ["F", [], []], ["G", [], []]],
            ["H", [], ["C", ["D", [], []], ["E", [], []]]],
        ]

    def test_draw_empty_tree_from_list(self):
        self.assertEqual(treeviz.draw([]), "<empty tree>")

    def test_draw_empty_tree_from_none(self):
        self.assertEqual(treeviz.draw(None), "<empty tree>")

    def test_draw_root_only_all_modes(self):
        tree = ["A", [], []]
        self.assertEqual(treeviz.draw(tree, mode="vertical"), "A")
        self.assertIn("A", treeviz.draw(tree, mode="side"))
        self.assertEqual(treeviz.draw(tree, mode="folder"), "A")

    def test_draw_vertical_contains_connectors(self):
        out = treeviz.draw(self.sample, mode="vertical")
        self.assertIn("A", out)
        self.assertIn("/", out)
        self.assertIn("\\", out)

    def test_draw_side_contains_unicode_connectors(self):
        out = treeviz.draw(self.sample, mode="side")
        self.assertIn("└──", out)
        self.assertIn("┌──", out)
        self.assertIn("│", out)
        self.assertIn("A", out)
        self.assertIn("B", out)

    def test_draw_folder_contains_unicode_connectors(self):
        out = treeviz.draw(self.sample, mode="folder")
        self.assertIn("├──", out)
        self.assertIn("└──", out)
        self.assertIn("│", out)
        self.assertIn("A", out)

    def test_draw_show_empty_folder(self):
        out = treeviz.draw(self.sample, mode="folder", show_empty=True)
        self.assertIn("∅", out)

    def test_draw_show_empty_side(self):
        only_right = ["A", [], ["B", [], []]]
        out = treeviz.draw(only_right, mode="side", show_empty=True)
        self.assertIn("∅", out)

    def test_draw_invalid_mode(self):
        with self.assertRaises(ValueError):
            treeviz.draw(self.sample, mode="invalid")

    def test_draw_unsupported_type(self):
        with self.assertRaises(TypeError):
            treeviz.draw(12345)

    def test_draw_with_long_labels(self):
        tree = ["root", ["node_15", [], []], ["while", [], []]]
        out = treeviz.draw(tree, mode="vertical")
        self.assertIn("root", out)
        self.assertIn("node_15", out)
        self.assertIn("while", out)

    def test_draw_with_numeric_labels(self):
        tree = ["100", ["20", [], []], ["3000", [], []]]
        out = treeviz.draw(tree, mode="vertical")
        self.assertIn("100", out)
        self.assertIn("20", out)
        self.assertIn("3000", out)

    def test_draw_only_left_chain(self):
        tree = ["A", ["B", ["C", ["D", [], []], []], []], []]
        out = treeviz.draw(tree, mode="vertical")
        self.assertIn("A", out)
        self.assertIn("B", out)
        self.assertIn("C", out)
        self.assertIn("D", out)

    def test_draw_only_right_chain(self):
        tree = ["A", [], ["B", [], ["C", [], ["D", [], []]]]]
        out = treeviz.draw(tree, mode="vertical")
        self.assertIn("A", out)
        self.assertIn("B", out)
        self.assertIn("C", out)
        self.assertIn("D", out)

    def test_draw_accepts_binarytree_duck_typing(self):
        bt = DummyBinaryTree(
            "*",
            DummyBinaryTree("+", DummyBinaryTree("7"), DummyBinaryTree("2")),
            DummyBinaryTree("4"),
        )
        out = treeviz.draw(bt, mode="folder")
        self.assertIn("*", out)
        self.assertIn("+", out)
        self.assertIn("4", out)


class ParseTreeTests(unittest.TestCase):
    def test_parse_tree_simple(self):
        tree = treeviz.parse_tree("A")
        self.assertEqual(tree, ("A", None, None))

    def test_parse_tree_nested(self):
        tree = treeviz.parse_tree("A(B(F,G),H(,C(D,E)))")
        expected = (
            "A",
            ("B", ("F", None, None), ("G", None, None)),
            ("H", None, ("C", ("D", None, None), ("E", None, None))),
        )
        self.assertEqual(tree, expected)

    def test_parse_tree_math(self):
        tree = treeviz.parse_tree("*(+(7,2),4)")
        expected = (
            "*",
            ("+", ("7", None, None), ("2", None, None)),
            ("4", None, None),
        )
        self.assertEqual(tree, expected)

    def test_parse_tree_with_outer_spaces(self):
        tree = treeviz.parse_tree("  A(B, C)  ")
        expected = ("A", ("B", None, None), ("C", None, None))
        self.assertEqual(tree, expected)

    def test_parse_tree_empty_text(self):
        with self.assertRaises(ValueError):
            treeviz.parse_tree("   ")

    def test_parse_tree_non_string(self):
        with self.assertRaises(TypeError):
            treeviz.parse_tree(42)

    def test_parse_tree_invalid_missing_comma(self):
        with self.assertRaises(ValueError):
            treeviz.parse_tree("A(B C)")

    def test_parse_tree_invalid_unclosed(self):
        with self.assertRaises(ValueError):
            treeviz.parse_tree("A(B,C")


class PrivateFunctionsTests(unittest.TestCase):
    def test_normalize_tree_from_list(self):
        tree = ["A", [], []]
        self.assertEqual(treeviz._normalize_tree(tree), ("A", None, None))

    def test_normalize_tree_from_tuple(self):
        tree = ("A", None, None)
        self.assertEqual(treeviz._normalize_tree(tree), ("A", None, None))

    def test_normalize_tree_from_string(self):
        tree = treeviz._normalize_tree("A(B,C)")
        self.assertEqual(tree, ("A", ("B", None, None), ("C", None, None)))

    def test_normalize_tree_invalid_type(self):
        with self.assertRaises(TypeError):
            treeviz._normalize_tree(object())

    def test_convert_from_list_empty(self):
        self.assertIsNone(treeviz._convert_from_list([]))

    def test_convert_from_list_invalid_type(self):
        with self.assertRaises(TypeError):
            treeviz._convert_from_list("not-a-list")

    def test_convert_from_list_invalid_len(self):
        with self.assertRaises(ValueError):
            treeviz._convert_from_list(["A", []])

    def test_is_binarytree_like(self):
        self.assertTrue(treeviz._is_binarytree_like(DummyBinaryTree("A")))
        self.assertFalse(treeviz._is_binarytree_like({}))

    def test_convert_from_binarytree(self):
        bt = DummyBinaryTree("A", DummyBinaryTree("B"), DummyBinaryTree("C"))
        self.assertEqual(
            treeviz._convert_from_binarytree(bt),
            ("A", ("B", None, None), ("C", None, None)),
        )

    def test_convert_from_binarytree_empty_pattern(self):
        bt = DummyBinaryTree(None, None, None)
        self.assertIsNone(treeviz._convert_from_binarytree(bt))

    def test_convert_from_binarytree_invalid(self):
        with self.assertRaises(TypeError):
            treeviz._convert_from_binarytree(object())

    def test_convert_binary_child_variants(self):
        self.assertIsNone(treeviz._convert_binary_child(None))
        self.assertIsNone(treeviz._convert_binary_child([]))
        self.assertEqual(treeviz._convert_binary_child(["A", [], []]), ("A", None, None))
        self.assertEqual(treeviz._convert_binary_child(("A", None, None)), ("A", None, None))

    def test_convert_binary_child_invalid(self):
        with self.assertRaises(TypeError):
            treeviz._convert_binary_child(3.14)

    def test_parse_tree_private_alias(self):
        self.assertEqual(treeviz._parse_tree("A"), ("A", None, None))

    def test_make_empty_node_and_marker(self):
        node = treeviz._make_empty_node()
        self.assertTrue(treeviz._is_empty_marker(node))

    def test_is_empty_marker_false(self):
        self.assertFalse(treeviz._is_empty_marker(("A", None, None)))

    def test_add_structural_empty_nodes_left_only(self):
        tree = ("A", ("B", None, None), None)
        out = treeviz._add_structural_empty_nodes(tree)
        self.assertEqual(out[0], "A")
        self.assertTrue(treeviz._is_empty_marker(out[2]))

    def test_add_structural_empty_nodes_right_only(self):
        tree = ("A", None, ("B", None, None))
        out = treeviz._add_structural_empty_nodes(tree)
        self.assertTrue(treeviz._is_empty_marker(out[1]))
        self.assertEqual(out[2][0], "B")

    def test_add_structural_empty_nodes_leaf_unchanged(self):
        tree = ("A", None, None)
        out = treeviz._add_structural_empty_nodes(tree)
        self.assertEqual(out, tree)

    def test_label_regular_and_empty_marker(self):
        self.assertEqual(treeviz._label("A"), "A")
        self.assertEqual(treeviz._label(treeviz._EMPTY_MARK), "∅")

    def test_build_ascii_vertical(self):
        tree = ("A", ("B", None, None), ("C", None, None))
        out = treeviz._build_ascii_vertical(tree)
        self.assertIn("A", out)
        self.assertIn("B", out)
        self.assertIn("C", out)

    def test_build_vertical_block_for_none(self):
        lines, width, height, root_pos = treeviz._build_vertical_block(None)
        self.assertEqual(lines, [""])
        self.assertEqual(width, 0)
        self.assertEqual(height, 1)
        self.assertEqual(root_pos, 0)

    def test_build_vertical_block_for_leaf(self):
        lines, width, height, root_pos = treeviz._build_vertical_block(("A", None, None))
        self.assertEqual(lines, ["A"])
        self.assertEqual(width, 1)
        self.assertEqual(height, 1)
        self.assertEqual(root_pos, 0)

    def test_build_ascii_side(self):
        tree = ("A", ("B", None, None), ("C", None, None))
        out = treeviz._build_ascii_side(tree)
        self.assertIn("└──", out)
        self.assertIn("┌──", out)
        self.assertIn("│", out)
        self.assertIn("A", out)

    def test_side_walk_none_does_not_change_lines(self):
        lines = ["x"]
        treeviz._side_walk(None, "", True, lines)
        self.assertEqual(lines, ["x"])

    def test_side_walk_adds_line(self):
        lines = []
        treeviz._side_walk(("A", None, None), "", True, lines)
        self.assertEqual(len(lines), 1)
        self.assertIn("A", lines[0])

    def test_build_ascii_folder_none(self):
        self.assertEqual(treeviz._build_ascii_folder(None), "<empty tree>")

    def test_build_ascii_folder(self):
        tree = ("A", ("B", None, None), ("C", None, None))
        out = treeviz._build_ascii_folder(tree)
        self.assertIn("A", out)
        self.assertIn("├──", out)
        self.assertIn("└──", out)

    def test_folder_children(self):
        left = ("L", None, None)
        right = ("R", None, None)
        self.assertEqual(treeviz._folder_children(left, None), [left])
        self.assertEqual(treeviz._folder_children(None, right), [right])
        self.assertEqual(treeviz._folder_children(left, right), [left, right])

    def test_folder_walk_none_does_not_change(self):
        lines = ["A"]
        treeviz._folder_walk(None, "", True, lines)
        self.assertEqual(lines, ["A"])

    def test_folder_walk_adds_line(self):
        lines = ["A"]
        treeviz._folder_walk(("B", None, None), "", True, lines)
        self.assertEqual(len(lines), 2)
        self.assertIn("B", lines[1])


if __name__ == "__main__":
    unittest.main(verbosity=2)
