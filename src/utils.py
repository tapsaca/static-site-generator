import re
from leafnode import LeafNode
from textnode import TextNode

def extract_markdown_images(text: str):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text: str):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def split_nodes_delimiter(old_nodes: list, delimiter: str, text_type: str):
    new_nodes = []
    for old_node in old_nodes:
        if not isinstance(old_node, TextNode):
            new_nodes.append(old_node)
        parts = old_node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError("Invalid markdown syntax")
        for i in range(len(parts)):
            if len(parts[i]) != 0:
                if i % 2 == 0:
                    new_nodes.append(TextNode(parts[i], "text"))
                else:
                    new_nodes.append(TextNode(parts[i], text_type))
    return new_nodes

def text_node_to_html_node(text_node: TextNode):
    if text_node.text_type == "text":
        return LeafNode(None, text_node.text)
    elif text_node.text_type == "bold":
        return LeafNode("b", text_node.text)
    elif text_node.text_type == "italic":
        return LeafNode("i", text_node.text)
    elif text_node.text_type == "code":
        return LeafNode("code", text_node.text)
    elif text_node.text_type == "link":
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == "image":
        return LeafNode("img", None, {"src": text_node.url, "alt": text_node.text})
    raise ValueError("Invalid text type")