# 2. Text Analysis with Constraints
#  Given a large paragraph of text, write a Python program that:
#  • Counts the frequency of each word, ignoring common stop words (the, is, at, on, in, and, 
# etc.).
#  • Allows efficient querying, for example:
#  • "Return the top 3 most frequent words starting with the prefix 'th'."
#  • Optimize for performance.

#  The approach uses a Trie data structure to store words and their frequencies.
#  This allows efficient insertion and querying of words based on prefixes.
#  The preprocessing step removes stop words and punctuation to focus on meaningful words.
#  During querying, a depth-first search (DFS) is used to traverse the Trie and collect results.
#  Results are sorted by frequency to return the most frequent words matching the prefix.

class TrieNode:
     """class to represent each node in the Trie."""
     def _init_(self):
          self.children = {}
          self.word_count = 0


class Trie:
     """Class to represent the Trie data structure."""
     def _init_(self):
          self.root = TrieNode()

     def insert(self, word):
          node = self.root
          for char in word:
                if char not in node.children:
                     node.children[char] = TrieNode()
                node = node.children[char]

          node.word_count += 1

     def query(self, prefix, top_n):
          def dfs(node, path, results):
                if node.word_count > 0:
                     results.append((path, node.word_count))
                for char, child in node.children.items():
                     dfs(child, path + char, results)

          node = self.root
          for char in prefix:
                if char not in node.children:
                     return []
                node = node.children[char]

          results = []
          dfs(node, prefix, results)
          # Sort results by frequency
          results.sort(key=lambda x: -x[1])
          return results[:top_n]

def preprocess_text(text, stop_words):
     words = text.lower().split()
     return [word.strip(".,!?") for word in words if word not in stop_words]

def main():
     # Sample stop words
     stop_words = {"the", "is", "at", "on", "in", "and", "a", "an", "of", "to"}
     text = """Sample text with some common words. like cricket, football, and basketball. cricket is a popular sport in many countries. also it is visible on cricbuzz."""
     words = preprocess_text(text, stop_words)
     trie = Trie()
     for word in words:
          trie.insert(word)

     # Example query
     prefix = "cri"
     top_n = 5
     print(trie.query(prefix, top_n))

if _name_ == "_main_":
   main()