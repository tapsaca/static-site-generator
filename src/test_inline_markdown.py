import unittest
from inline_markdown import extract_markdown_images, extract_markdown_links, split_nodes_delimiter, split_nodes_image, split_nodes_link, text_node_to_html_node, text_to_textnodes
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
    
    def test_split_nodes_image(self):
        node = TextNode(
            "This is text with an ![image](https://example.com/image.png) and another ![second image](https://example.net/second_image.png)",
            "text",
        )
        self.assertEqual(
            split_nodes_image([node]),
            [
                TextNode("This is text with an ", "text"),
                TextNode("image", "image", "https://example.com/image.png"),
                TextNode(" and another ", "text"),
                TextNode("second image", "image", "https://example.net/second_image.png")
            ]
        )

    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with an [link](https://example.com) and another [another](https://example.net)",
            "text",
        )
        self.assertEqual(
            split_nodes_link([node]),
            [
                TextNode("This is text with an ", "text"),
                TextNode("link", "link", "https://example.com"),
                TextNode(" and another ", "text"),
                TextNode("another", "link", "https://example.net")
            ]
        )

    def test_text_node_to_html(self):
        node = TextNode("italic text", "italic")
        self.assertEqual(repr(text_node_to_html_node(node)), repr(LeafNode("i", "italic text")))
    
    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://example.com/image.png) and a [link](https://example.net)"
        self.assertEqual(
            text_to_textnodes(text),
            [
                TextNode("This is ", "text"),
                TextNode("text", "bold"),
                TextNode(" with an ", "text"),
                TextNode("italic", "italic"),
                TextNode(" word and a ", "text"),
                TextNode("code block", "code"),
                TextNode(" and an ", "text"),
                TextNode("image", "image", "https://example.com/image.png"),
                TextNode(" and a ", "text"),
                TextNode("link", "link", "https://example.net"),
            ]
        )

if __name__ == "__main__":
    unittest.main()