import unittest
from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_eq_fails_if_text_not_equal(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("Is this a text node?", "bold")
        self.assertNotEqual(node, node2)
    
    def test_eq_fails_if_type_not_equal(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)
    
    def test_eq_fails_if_url_not_equal(self):
        node = TextNode("This is a text node", "bold", "http://url.com")
        node2 = TextNode("This is a text node", "bold", "http://url.net")
        self.assertNotEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("This is a text node", "bold")
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, None)")

if __name__ == "__main__":
    unittest.main()