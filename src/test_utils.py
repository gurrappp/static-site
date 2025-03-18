import unittest
from utils import *
from textnode import TextNode,TextType



class TestUtils(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_image(self):
        node = TextNode("Description of image", TextType.IMAGE, "url/of/image.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")  # Image nodes have empty value
        self.assertEqual(html_node.props.get("src"), "url/of/image.jpg")
        self.assertEqual(html_node.props.get("alt"), "Description of image")

    def test_text_link(self):
        node = TextNode("link", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "link")
        self.assertEqual(html_node.props.get("href"),"https://www.google.com")
        self.assertEqual(html_node.to_html(), '<a href="https://www.google.com">link</a>')


if __name__ == "__main__":
    unittest.main()