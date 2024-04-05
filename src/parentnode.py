from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError('Missing tag')
        if self.children == None:
            raise ValueError('Missing children')
        child_nodes = ""
        for child_node in self.children:
            child_nodes += child_node.to_html()
        return f"<{self.tag}{self.props_to_html()}>{child_nodes}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"