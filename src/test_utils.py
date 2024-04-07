import unittest
from utils import extract_markdown_images, extract_markdown_links, split_nodes_delimiter, text_node_to_html_node
from leafnode import LeafNode
from textnode import TextNode

class TestUtils(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://url.com/image.png) and ![another](https://url.net/another.png)"
        self.assertEqual(
            extract_markdown_images(text),
            [
                ("image", "https://url.com/image.png"),
                ("another", "https://url.net/another.png")
            ]
        )
    
    def test_extract_markdown_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        self.assertEqual(
            extract_markdown_links(text),
            [
                ("link", "https://www.example.com"),
                ("another", "https://www.example.com/another")
            ]
        )

    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", "text")
        new_nodes = split_nodes_delimiter([node], "`", "code")
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is text with a ", "text"),
                TextNode("code block", "code"),
                TextNode(" word", "text"),
            ]
        )

    def test_text_node_to_html(self):
        node = TextNode("italic text", "italic")
        self.assertEqual(repr(text_node_to_html_node(node)), repr(LeafNode("i", "italic text")))

if __name__ == "__main__":
    unittest.main()