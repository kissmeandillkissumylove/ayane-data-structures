"""test AVL-tree module.
10.04.2023 https://github.com/kissmeandillkissumylove"""

import unittest
import AVL_tree


class TestAVLTree(unittest.TestCase):
	"""class with tests for AVLTree."""

	def setUp(self) -> None:
		"""create tree."""
		self.tree = AVL_tree.AVLTree()
		self.tree.insert([elt for elt in range(0, 100)])

	def test_get_root(self):
		self.assertIsNotNone(self.tree.get_root())


if __name__ == "__main__":
	unittest.main()
