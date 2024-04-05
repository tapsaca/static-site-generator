import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
    
    def test_to_html_with_props(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            {"style": "text-align:right"}
        )
        self.assertEqual(node.to_html(), '<p style="text-align:right"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')
    
    def test_to_html_with_parent_inside_another(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ]
                )
            ]
        )
        self.assertEqual(node.to_html(), "<div><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></div>")
    
    def test_repr(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text")
            ]
        )
        self.assertEqual(repr(node), f"ParentNode(p, [LeafNode(b, Bold text, None), LeafNode(None, Normal text, None)], None)")

if __name__ == "__main__":
    unittest.main()