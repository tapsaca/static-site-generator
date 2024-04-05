import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")
    
    def test_to_html_fails_with_no_value(self):
        node = LeafNode("p")
        self.assertRaises(ValueError, node.to_html)

    def test_to_html_with_no_tag(self):
        node = LeafNode(None, "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "This is a paragraph of text.")

    def test_to_html_with_props(self):
        node = node = LeafNode("a", "Click me!", {"href": "https://www.url.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.url.com">Click me!</a>')
    
    def test_repr(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(repr(node), "LeafNode(p, This is a paragraph of text., None)")

if __name__ == "__main__":
    unittest.main()