""" Test module to test trie.py and node.py """
import unittest
from src.trie import Trie
from src.exceptions import SearchMiss
# pylint: disable=protected-access

class TestTrie(unittest.TestCase):
    """ Test Trie class """
    def setUp(self):
        """ Init """
        self.trie = Trie()
        with open ("dictionary.txt", encoding="utf8") as file:
            for line in file:
                if line[-1:] == "\n":
                    self.trie.insert((line[:-1]))
                else:
                    self.trie.insert((line))

    def test_find_word_searchmiss(self):
        """ Test the find word returns a searchMiss when given a wrong word. """

        with self.assertRaises(SearchMiss):
            self.trie.find_word("hej")

    def test_find_word_returns_correct(self):
        """ Test find_word returns correct when given a correct word. """
        self.trie.find_word("zonal")
        self.assertEqual(self.trie.find_word("zonal"), "word is spelled correctly")

    def test_prefix_search_prints_correct(self):
        """ Test the prefix search prints correct answers. """
        correct_list = ["help","helped","helper","helpless","helping",
        "helpful","helpfulness","helpfully","helpmeet"]
        self.assertEqual(self.trie.print_prefix_search("help"), correct_list)

    def test_remove_correct_answer(self):
        """ Test remove so it gives searchmiss when using findword method. """
        self.trie.remove("zonal")
        with self.assertRaises(SearchMiss):
            self.trie.find_word("zonal")

    def test_remove_wrong_answer(self):
        """ Test the remove method it retruns a searchmiss when given a wrong word. """
        with self.assertRaises(SearchMiss):
            self.trie.remove("helploss")

    def test_print(self):
        """ Test if the print method prints 25402 times / the whole dictionary.txt """
        self.assertEqual(len(self.trie.print()), 25402)

    def test_find_word_returns_node_children(self):
        """ Test the _find_word method returns node children dictionary
        if still not is a full word ( Is for remove to work ) """
        self.assertIsInstance(self.trie._find_word("zona"), dict)
