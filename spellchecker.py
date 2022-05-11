"""
Spellchecker module
"""
import sys
import inspect
from src.exceptions import SearchMiss
from src.trie import Trie

class SpellChecker:
    """ SpellChecker class """

    _OPTIONS = {
        "1": "find_word_in_wordlist",
        "2": "prefix_search",
        "3": "swap_file",
        "4": "print_all_words",
        "5": "remove_word",
        "6": "quit"
    }

    def __init__(self):
        """ Init Method """
        self.trie = Trie()

        with open ("dictionary.txt", encoding="utf8") as file:
            for line in file:
                if line[-1:] == "\n":
                    self.trie.insert((line[:-1]))
                else:
                    self.trie.insert((line))

    def _get_method(self, method_name):
        """
        Uses function getattr() to dynamically get value of an attribute.
        """
        return getattr(self, self._OPTIONS[method_name])

    def _print_menu(self):
        """
        Use docstring from methods to print options for the program.
        """
        menu = ""

        for key in sorted(self._OPTIONS):
            method = self._get_method(key)
            docstring = inspect.getdoc(method)

            menu += "{choice}: {explanation}\n".format(
                choice=key,
                explanation=docstring
            )

        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(menu)

    def find_word_in_wordlist(self):
        """ Check a word """
        word = input("Enter word to find: ")
        try:
            print(self.trie.find_word(word))
        except SearchMiss:
            print("word does not exist")
    def prefix_search(self):
        """ Get word suggestion. """
        prefix = input("Input 3 letters: ")
        try:
            self.trie.print_prefix_search(prefix)
            while "quit" not in prefix:
                new_prefix = input("Input next letter: " + prefix)
                if new_prefix == "quit":
                    break
                prefix += new_prefix
                self.trie.print_prefix_search(prefix)
        except SearchMiss:
            print("word does not exist")

    def swap_file(self):
        """ Change dictinary """
        file_name = input("Enter new file name: ")
        self.trie = Trie()
        with open (file_name, encoding="utf8") as file:
            for line in file:
                if line[-1:] == "\n":
                    self.trie.insert((line[:-1]))
                else:
                    self.trie.insert((line))
            print("Success!")

    def print_all_words(self):
        """ Print all words """
        whole_word_list = self.trie.print()
        for word in whole_word_list:
            print(word)
    def remove_word(self):
        """ Remove word """
        word = input("Delete word: ")
        try:
            print(self.trie.remove(word))
        except SearchMiss:
            print("word is missing")

    @staticmethod
    def quit():
        """ Exit """
        sys.exit()

    def main(self):
        """ Start method """
        while True:
            self._print_menu()
            choice = input("Enter menu selection:\n-> ")

            try:
                self._get_method(choice.lower())()
            except KeyError:
                print("Invalid choice!")

            input("\nPress any key to continue ...")

if __name__ == "__main__":
    s = SpellChecker()
    s.main()
