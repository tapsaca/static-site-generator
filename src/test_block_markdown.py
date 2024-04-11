import unittest
from block_markdown import block_to_block_type, markdown_to_blocks

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
        
if __name__ == "__main__":
    unittest.main()