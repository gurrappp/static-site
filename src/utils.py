
from textnode import TextNode,TextType
from htmlnode import HTMLNode
from leafnode import LeafNode

def text_node_to_html_node(text_node):
    if not isinstance(text_node.text_type, TextType):
        raise Exception("Text node text_type is not of TextType enum!")
    
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text,{"href": f"{text_node.url}"})
        case TextType.IMAGE:
            return LeafNode("img", "",{"src": f"{text_node.url}", "alt": f"{text_node.text}"})

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    return