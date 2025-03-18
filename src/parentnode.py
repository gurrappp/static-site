
from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag = tag, value= None, children= children, props= props)

    def to_html(self):
        if not self.tag:
            raise ValueError("The object does not have a tag!")
        if not self.children:
            raise ValueError("The object does not have any children!")

        for child in self.children:
            if not child.value and child is LeafNode:
                raise ValueError(f"This child is missing a value : {str(child)}")

        output = f"<{self.tag}" 

        if self.props:
            for key, value in self.props.items():
                output += f' {key}="{value}"'
        output += ">"

        for child in self.children:
            output += child.to_html()

        output += f"</{self.tag}>"

        return output

        