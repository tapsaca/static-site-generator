import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", None, None, {"href": "https://www.url.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.url.com" target="_blank"')
    
    def test_props_to_html_with_single_prop(self):
        node = HTMLNode("a", None, None, {"href": "https://www.url.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.url.com"')
    
    def test_props_to_html_with_no_props(self):
        node = HTMLNode("a", None, None,)
        self.assertEqual(node.props_to_html(), "")
    
    def test_repr(self):
        node = HTMLNode("a", None, None, {"href": "https://www.url.com", "target": "_blank"})
        self.assertEqual(repr(node), "HTMLNode(a, None, None, {'href': 'https://www.url.com', 'target': '_blank'})")

if __name__ == "__main__":
    unittest.main()