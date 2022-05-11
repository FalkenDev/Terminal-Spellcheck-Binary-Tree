""" Trie Module """
from src.node import Node
from src.exceptions import SearchMiss
class Trie():
    """ Class Trie """
    def __init__(self):
        self.root = {}

    def insert(self, word):
        """
        Insert the words to trie, Using dictionary: key = char and Value = Node
        This method looks if the first letter is in self.root else create the node
        for the letter and insert it self.root
        """
        char_list = list(word)
        char = char_list[0].lower()
        if char not in self.root:
            new_node = Node(char)
            self.root[char] = new_node
        node_char = self.root.get(char)

        return self._insert(char_list, node_char)

    @classmethod
    def _insert(cls, char_list, node, counter = 1):
        """
        Insert the remaining letters if not in node.children dictionary
        and set the last letter of the word node to stop is True
        """
        char1 = char_list[counter]
        if char1 not in node:
            node[char1] = Node(char1)
        if len(char_list) == counter + 1:
            child_node = node[char1]
            child_node.stop = True
            return
        cls._insert(char_list, node[char1], counter + 1)

    def remove(self, word):
        """
        Remove method, using _find_word method to get the dict from the the previous
        dictionary where the last letter and node is.
        If the last node is not true, raise searchMiss else delete the node from dictionary.
        The other remainen letters go in to a for loop where
        """
        c_list = list(word)
        node_dict = self._find_word(word)
        length_list = len(c_list) - 1
        if node_dict[c_list[length_list]].stop is not True:
            raise SearchMiss

        if len(node_dict[c_list[length_list]].children) == 0:
            del node_dict[c_list[length_list]]
        else:
            node_dict[c_list[length_list]].stop = False

        word = word[:-1]

        for x in range(length_list, 0, -1):
            node_dict = self._find_word(word)
            if len(node_dict[c_list[x-1]].children) == 0:
                del node_dict[c_list[x-1]]

            word = word[:-1]
        return "Word has been removed"

    def find_word(self, word):
        """ Find word in wordlist method """
        last_dict = self._find_word(word)
        w_split = list(word)
        length = len(w_split) - 1
        if w_split[length] in last_dict and last_dict[w_split[length]].stop is True:
            return "word is spelled correctly"
        raise SearchMiss

    def _find_word(self, word):
        """
        Look the fist letter in word and then send the words node to
        method _find_word_recursion with char list.
        If char list is equal to 1 then retrun self.root (It's for remove function)
        """
        char_list = list(word)
        if char_list[0] not in self.root:
            raise SearchMiss
        if len(char_list) == 1:
            return self.root
        node_char = self.root.get(char_list[0])
        return self._find_word_recursion(char_list, node_char)

    @classmethod
    def _find_word_recursion(cls, char_list, node, counter = 1):
        """
        Rucursion to get to the last node and retrun the node.children.
        If char not in node.children raise SearchMiss
        """
        char = char_list[counter]
        if char not in node:
            raise SearchMiss
        if len(char_list) == (counter + 1):
            return node.children

        return cls._find_word_recursion(char_list, node.children.get(char), counter + 1)

    def print_prefix_search(self, prefix):
        """ Print the list with maximum 10 words that returns from prefix search """
        list_words = self.prefix_search(prefix)
        return_list_words = []
        counter = 0
        for word in list_words:
            if counter == 10:
                break
            counter += 1
            return_list_words.append(word)
            print(word)
        return return_list_words # For the test_trie

    def prefix_search(self, prefix):
        """
        Prefix search, Using _find_word method to get the dict from the the previous
        dictionary where the last letter and node is.
        Then send the node, prefix, and word_list to _prefix_search method which using recrusive.
        """
        word_list = []
        prev_node_dict = self._find_word(prefix)
        counter = len(prefix) - 1
        curr_node = prev_node_dict[prefix[counter]]
        prefix = prefix[:-1]
        self._prefix_search(curr_node, prefix, word_list)
        return word_list

    @classmethod
    def _prefix_search(cls, node, previous, word_list):
        """
        The method look if node.stop is true and then append the string with node letter.
        Then loop thorugh child nodes and call it's own method _prefix_search.
        If the loop is done it returns to next loop and start over with next node.
        """

        if node.stop is True:
            string = previous + node.char
            word_list.append(string)

        for child_key in node.children:
            cls._prefix_search(node.children[child_key], previous + node.char, word_list)

    def print(self):
        """ Print all the words in Trie object with using prefix_search as help. """
        whole_list = []
        for key in self.root:
            list_per_key = self.prefix_search(key)
            for word in list_per_key:
                whole_list.append(word)
        whole_list.sort()
        return whole_list
