import csv
import argparse

class TNode(): 
    def __init__(self):
        # Init a trie node
        self.child_nodes = {} # Create child nodes dict
        self.leaf = False # Set leaf node property as false
  
class Trie():
    suggestSet=set()
    
    def __init__(self):
        # Creating the trie data structure
        self.root = TNode() # Create trie root node
        self.words = [] # Initialize a list of words
  
    def createTrie(self, keys):
        # Creates a trie with csv string data
        for key in keys: 
            self.insert(key) # Inserting a key into the trie
  
    def insert(self, key):
        # Inserts the key directly only if it doesn't exist
        # And marks it as leaf node

        node = self.root # Node is set to root
        for i in list(key): # Parse through each character of key
            if not node.child_nodes.get(i): # If not present in child_nodes
                node.child_nodes[i] = TNode() # Inserts new node

            node = node.child_nodes[i] # Sets 'node' to its child_nodes list
  
        node.leaf = True # Set node as leaf
  
    def search(self, key):
        # Searches the trie for exact match for key
        node = self.root # Set node to root
        success = True # Set success variable if search is successful
  
        for i in list(key): # Parse through the key list
            if not node.child_nodes.get(i): # If not found, set success to False
                success = False
                break

            node = node.child_nodes[i] # Traverse the child_nodes of current node

        return node and node.leaf and success

    def suggestRec(self, node, word):
        # Recursive tree traversal
        if node.leaf:
            self.words.append(word)

        for i,j in node.child_nodes.items():
            self.suggestRec(j, word + i)

    def autoSuggest(self, key):
        # Returns all the words in the trie whose common prefix is the given key
        node = self.root
        found = True
        temp = ''
        
        # Search for word in dictionary
        for i in list(key):
            if not node.child_nodes.get(i):
                found = False
                break

            temp += i
            node = node.child_nodes[i]
        
        # If word searched for is not found, print suggested words
        if not found:
            if len(key)>=1:
                self.autoSuggest(key[0:len(key)-1]) # Find suggestions with substrings of given key
            else:
                return 0
        elif node.leaf and not node.child_nodes: # If selected node is leaf and has no child_nodes,
            # Add it to suggestion set and return -1
            self.suggestSet.add(key)
            return -1

        self.suggestRec(node, temp)
        
        for i in self.words: # Add word list from that node level to suggestion set
                self.suggestSet.add(i)
        return 1

# Main Driver Code
if __name__ == "__main__":
    parser = argparse.ArgumentParser() # Open argument parser
    parser.add_argument("csvfile", help="Input the csv file name you want")
    parser.add_argument("word", help="Enter the word for suggestions")
    args = parser.parse_args() # Parse the two arguments

    keys = list()
    key = str(args.word.capitalize()) # Input second argument as key to search for
    
    with open(str(args.csvfile)) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',') # Open csv_reader with comma delimiter
        for row in csv_reader:
                keys.append(str(row[0].strip())) # Form keys list for the trie structure

    # Creating trie object
    trieObj = Trie()
    
    # Creating the trie structure
    trieObj.createTrie(keys)
    
    # Autocompleting the given key using trie
    comp = trieObj.autoSuggest(key)
    if len(trieObj.suggestSet)>=1: # Suggestions to be printed (if available)
        suggestList = list(trieObj.suggestSet)
        for i in range(len(suggestList[0:5])): # Max 5 suggestions to be printed
            print(suggestList[i])
