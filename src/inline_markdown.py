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
                    new_nodes.append(TextNode(parts[i], old_node.text_type))
                else:
                    new_nodes.append(TextNode(parts[i], text_type))
    return new_nodes

def split_nodes_image(old_nodes: list):
    new_nodes = []
    for old_node in old_nodes:
        if len(old_node.text) != 0:
            text = old_node.text
            images = extract_markdown_images(text)
            if len(images) != 0:
                for image in images:
                    parts = text.split(f"![{image[0]}]({image[1]})", 1)
                    if len(parts) != 2:
                        raise ValueError("Invalid markdown syntax")
                    if len(parts[0]) != 0:
                        new_nodes.append(TextNode(parts[0], "text"))
                    new_nodes.append(TextNode(image[0], "image", image[1]))
                    text = parts[1]
                if len(text) != 0:
                    new_nodes.append(TextNode(text, "text"))
            else:
                new_nodes.append(old_node)
    return new_nodes

def split_nodes_link(old_nodes: list):
    new_nodes = []
    for old_node in old_nodes:
        if len(old_node.text) != 0:
            text = old_node.text
            links = extract_markdown_links(text)
            if len(links) != 0:
                for link in links:
                    parts = text.split(f"[{link[0]}]({link[1]})", 1)
                    if len(parts) != 2:
                        raise ValueError("Invalid markdown syntax")
                    if len(parts[0]) != 0:
                        new_nodes.append(TextNode(parts[0], "text"))
                    new_nodes.append(TextNode(link[0], "link", link[1]))
                    text = parts[1]
                if len(text) != 0:
                    new_nodes.append(TextNode(text, "text"))
            else:
                new_nodes.append(old_node)
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
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise ValueError("Invalid text type")

def text_to_textnodes(text: str):
    textnodes = split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter([TextNode(text, "text")], "**", "bold"), "*", "italic"), "`", "code")
    return split_nodes_link(split_nodes_image(textnodes))