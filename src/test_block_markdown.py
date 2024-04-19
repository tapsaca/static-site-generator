import unittest
from block_markdown import block_to_block_type, markdown_to_blocks, code_to_html_node, heading_to_html_node, ordered_list_to_html_node, paragraph_to_html_node, quote_to_html_node
from leafnode import LeafNode
from parentnode import ParentNode

class TestBlockMarkdown(unittest.TestCase):
    def test_block_to_block_type(self):
        blocks = [
            "# heading",
            "######## actually a paragraph",
            "```code\nblock```",
            "```not a code block\nbut paragraph``",
            ">quote\n>another quote\n>and another",
            ">quote\nthis is not",
            "* list item\n* another list item",
            "- list item\n- another list item",
            "* list item\nnot a list item",
            "- list item\nnot a list item",
            "1. list item\n2. another list item",
            "2. list\n3. should start with 1.",
            "1. list item\n3. this should be 2."
        ]
        self.assertEqual(block_to_block_type(blocks[0]), "heading")
        self.assertEqual(block_to_block_type(blocks[1]), "paragraph")
        self.assertEqual(block_to_block_type(blocks[2]), "code")
        self.assertEqual(block_to_block_type(blocks[3]), "paragraph")
        self.assertEqual(block_to_block_type(blocks[4]), "quote")
        self.assertEqual(block_to_block_type(blocks[5]), "paragraph")
        self.assertEqual(block_to_block_type(blocks[6]), "unordered_list")
        self.assertEqual(block_to_block_type(blocks[7]), "unordered_list")
        self.assertEqual(block_to_block_type(blocks[8]), "paragraph")
        self.assertEqual(block_to_block_type(blocks[9]), "paragraph")
        self.assertEqual(block_to_block_type(blocks[10]), "ordered_list")
        self.assertEqual(block_to_block_type(blocks[11]), "paragraph")
        self.assertEqual(block_to_block_type(blocks[12]), "paragraph")

    def test_markdown_to_blocks(self):
        markdown = """# This is a heading

                    This is a paragraph of text. It has some **bold** and *italic* words inside of it.

                    
                    * This is a list item
                    * This is another list item

                    """
        self.assertEqual(
            markdown_to_blocks(markdown),
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is a list item\n* This is another list item"
            ]
        )
    
    def test_code_to_html_node(self):
        html_node = code_to_html_node("```code block```")
        self.assertEqual(
            html_node.to_html(),
            "<pre><code>code block</code></pre>"
        )
    
    def test_heading_to_html_node(self):
        heading_lvl_1 = heading_to_html_node("# This is a level **1** heading")
        heading_lvl_6 = heading_to_html_node("###### This is a level 6 heading")
        self.assertEqual(heading_lvl_1.to_html(), "<h1>This is a level <b>1</b> heading</h1>")
        self.assertEqual(heading_lvl_6.to_html(), "<h6>This is a level 6 heading</h6>")
    
    def test_ordered_list_to_html_node(self):
        markdown = """
                    1. Item 1
                    2. Item 2
                    3. Item 3
                    """
        html_node = ordered_list_to_html_node(markdown)
        self.assertEqual(
            html_node.to_html(),
            "<ol><li>Item 1</li><li>Item 2</li><li>Item 3</li></ol>"
        )
    
    def test_paragraph_to_html_node(self):
        html_node = paragraph_to_html_node("This is a paragraph of text. It has some **bold** and *italic* words inside of it.")
        self.assertEqual(
            html_node.to_html(),
            "<p>This is a paragraph of text. It has some <b>bold</b> and <i>italic</i> words inside of it.</p>"
        )
    
    def test_quote_to_html_node(self):
        markdown = """
                    >This is a
                    >block
                    >quote
                    """
        html_node = quote_to_html_node(markdown)
        print(html_node)
        self.assertEqual(
            html_node.to_html(),
            "<blockquote>This is a block quote</blockquote>"
        )
        
if __name__ == "__main__":
    unittest.main()