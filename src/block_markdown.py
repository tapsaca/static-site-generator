from inline_markdown import text_node_to_html_node, text_to_textnodes
from parentnode import ParentNode

def block_to_block_type(block: str):
    if block.startswith("# ") or block.startswith("## ") or block.startswith("### ") or block.startswith("#### ") or block.startswith("##### ") or block.startswith("###### "):
        return "heading"
    elif block.startswith("```") and block.endswith("```"):
        return "code"
    elif block.startswith(">"):
        for line in block.split("\n"):
            if not line.startswith(">"):
                return "paragraph"
        return "quote"
    elif block.startswith("* "):
        for line in block.split("\n"):
            if not line.startswith("* "):
                return "paragraph"
        return "unordered_list"
    elif block.startswith("- "):
        for line in block.split("\n"):
            if not line.startswith("- "):
                return "paragraph"
        return "unordered_list"
    elif block.startswith("1. "):
        lines = block.split("\n")
        for i in range(len(lines)):
            if not lines[i].startswith(f"{i + 1}. "):
                return "paragraph"
        return "ordered_list"
    return "paragraph"

def markdown_to_blocks(markdown: str):
    initial_blocks = markdown.split("\n\n")
    new_blocks = []
    for block in initial_blocks:
        new_block = block.strip()
        if len(new_block) != 0:
            new_blocks.append("\n".join(map(lambda b: b.strip(), new_block.split("\n"))))
    return new_blocks

def markdown_to_html_node(markdown: str):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == "code":
            children.append()
        elif block_type == "heading":
            children.append(heading_to_html_node(block))
        elif block_type == "paragraph":
            children.append(paragraph_to_html_node(block))
    return ParentNode("div", children)

def text_to_children(text: str):
    text_nodes = text_to_textnodes(text)
    children = []
    for node in text_nodes:
        children.append(text_node_to_html_node(node))
    return children

def code_to_html_node(block: str):
    children = text_to_children(block.strip("`"))
    return ParentNode("pre", [ParentNode("code", children)])

def heading_to_html_node(heading: str):
    level = len(heading) - len(heading.lstrip("#"))
    children = text_to_children(heading.lstrip("# "))
    return ParentNode(f"h{level}", children)

def paragraph_to_html_node(block: str):
    text = " ".join(block.split("\n"))
    children = text_to_children(text)
    return ParentNode("p", children)