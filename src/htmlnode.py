

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children else []
        
        try:
            self.props = self.validate_props(props) if props else {}
        except ValueError as e:
            print(f"Error initializing HTMLNode: {e}")  # Provide informative feedback
            self.props = {}  # Fallback to an empty props dictionary
    
    def validate_props(self, props):
        valid_props = {}
        for key, value in props.items():
            if self.is_valid_attribute_name(key):
                valid_props[key] = value
            else:
                raise ValueError(f"Invalid attribute name: '{key}'. Attribute names should be alphanumeric or include dashes (-).")
        return valid_props
    
    def is_valid_attribute_name(self, name):
        # Example check: attribute names must be alphanumeric or include dashes
        return name.replace("-", "").isalnum()

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ""
        output = ""
        for key, value in self.props.items():
            if value is None:
                continue
            if isinstance(value, bool):
                if value:
                    output += f' {key}'
            else:
                output += f' {key}="{str(value)}"'
        return output 

    def __repr__(self):
        output = ""
        output += "tag: " + self.tag + " | " if self.tag is not None else "tag: is None | "
        output += "value: " + self.value + " | " if self.value is not None else "value: is None | "

        if self.children:
            output += "children: "
            for child in self.children:
                output += f"{str(child)}" + " | "
        else:
            output += "children: empty list | "
        
        output += "props: "
        for key,value in self.props.items():
            output += f" [key: {key}, value: {str(value)}]"
        return output