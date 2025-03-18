from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        if value is None:
            raise ValueError("value is required and cant be None!")
        super().__init__(tag= tag, value= value, children= [], props= props)

    def to_html(self):
        if self.value is None:
            raise ValueError("value is required and cant be None!")
        if self.tag is None:
            return str(self.value)
        output = f"<{self.tag}"
        if self.props:
            for key, value in self.props.items():
                output += f' {key}="{value}"'
        if self.tag == "img":
            output += " />"        
        else:
            output += f">{self.value}</{self.tag}>"
        return output

        
        
