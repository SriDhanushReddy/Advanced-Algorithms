
"""
This code implements a search engine that takes in a list of pages and terms, and returns a list of pages containing the given terms.

The get_pages_from_file() function takes in a filename and returns a list of pages from the file.

The get_terms_from_file() function takes in a filename and returns a list of terms from the file.

The remove_html_tags() function takes in a string of text and removes all HTML tags from the string.

The get_stop_words() function returns a list of stop words.

The get_words_from_text() function takes in a string of text and returns a list of words from the string.

The get_words_from_webpage() function takes in a URL and returns a list of words from the webpage.

The get_links_from_webpage() function takes in a URL and returns a list of links from the webpage.

The search_engine() function takes in a list of pages and terms, and returns a list of pages containing the given terms.

The main() function tests the search engine.
"""

import sys
import re
import requests
from bs4 import BeautifulSoup

def get_links_from_webpage(url):
    """Returns a list of links from a webpage."""
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    return links

def get_pages_from_file(filename):
    """Returns a list of pages from a file."""
    pages = []
    filename = open(filename, "r", encoding="utf8")
    
    page = filename.read()
    
    pages_into_list = page.split("\n")
    pages = pages_into_list
    filename.close()
    return pages

def get_terms_from_file(filename):
    """Returns a list of terms from a file."""
    terms = []
    filename = open(filename, "r", encoding="utf8")
    
    term = filename.read()
    
    terms_into_list = term.split("\n")
    terms = terms_into_list
    filename.close()
    return terms

def remove_html_tags(text):
    """Remove html tags from a string"""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def get_stop_words():
    """Returns a list of stop words."""
    stop_words = ['a', 'or', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'was', 'were', 'will', 'with']
    return stop_words

def get_words_from_text(text):
    """Returns a list of words from a string of text."""
    text = remove_html_tags(text)
    text = text.lower()
    text = text.replace("'", "")
    text = re.sub(r'[^a-z0-9]', ' ', text)
    text = text.strip()
    words = text.split()
    stop_words = get_stop_words()
    for word in words:
        if word in stop_words:
            words.remove(word)
    return words

def get_words_from_webpage(url):
    """Returns a list of words from a webpage."""
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    words = get_words_from_text(text)
    return words

##################################################################################################################

class TrieNode:
    """Trie node."""

    def __init__(self, key):
        """Initialize this node."""
        # First initialize an empty list of children
        self.children = {}
        # Set the node's key
        self.key = key
        # Set the node's value
        # self.value = value
        self.urls = []
    
    def get_child(self, key):
        """Returns the child node with the given key."""
        return self.children.get(key)
    
    def add_child(self, key, child):
        """Adds a child node with the given key."""
        self.children[key] = child

##################################################################################################################
def add_word_to_trie(node, word, url):
    if word == '':
        node.urls.append(url)
        return
    first_letter, rest = word[0], word[1:]
    child = node.get_child(first_letter)
    if child == None:
        child = TrieNode(first_letter)
        node.add_child(first_letter, child)
    add_word_to_trie(child, rest, url)

def build_trie(urls):
    root = TrieNode('')
    for url in urls:
        words = get_words_from_webpage(url)
        for word in words:
            add_word_to_trie(root, word, url)
    return root

def get_node_from_trie(root, word):
    if word == '':
        return root
    first_letter, rest = word[0], word[1:]
    child = root.get_child(first_letter)
    if child == None:
        return None
    return get_node_from_trie(child, rest)

def get_urls_from_trie(root, word):
    node = get_node_from_trie(root, word)
    if node == None:
        return []
    return node.urls


def search_engine(pages, terms):
    """Returns a list of pages containing the given terms."""
    # TODO: Implement the search engine.
    result = []
    trie = build_trie(pages)
    for term in terms:
        found_urls = get_urls_from_trie(trie, term)
        result.extend(found_urls)
    d = {}
    for results in result:
        if results in d:
            d[results] += 1
        else:
            d[results] = 1
        #print (d)
    return d 

#########################################################################################################################################

def main():
    # TODO: Test the search engine.
    """Greetings"""
    print("\n")
    print ("Hello!\n")
    print("Welcome to CS600 Search Engine Model:10476150\n")
    
    """Take Input from the user for terms"""
    terms = input("Enter search terms: ")
    
    """Write input to file"""
    with open("terms.txt", "w") as f:
        for term in terms.split(" "):
            f.write(term + "\n")
    
    pages = get_pages_from_file("pages.txt")
    terms = get_terms_from_file("terms.txt")
    result = []
    result = search_engine(pages, terms)
    sorted_d = sorted(result.items(), key=lambda x: x[1], reverse=True)
    
    """Write sorted Dictionary to file"""
    with open('output.txt', 'w') as f:
        for sorted_ds in sorted_d:
            f.write(f"{sorted_ds}\n")
    
    """Display sorted pages to screen with the number of matches"""
    with open("output.txt") as f:
        sys.stdout.write(f.read())
    
    """Goodbye"""
    print ("Thanks for searching! Goodbye")
    
if __name__ == '__main__':
    main()