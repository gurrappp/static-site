import unittest

from textnode import TextNode,TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node,node2)

    def test_valid_input(self):
        testString = "textnode"
        enumValue = TextType.CODE
        url = "www.test.se"
        node = TextNode(testString, enumValue, url)
        self.assertEqual(testString, node.text)
        self.assertEqual(enumValue, node.text_type)
        self.assertEqual(url, node.url)
    
    def test_default_value(self):
        node = TextNode("string", TextType.BOLD)
        self.assertIsNone(node.url)
    
    def test_not_eq_enum(self):
        node1 = TextNode("test", TextType.CODE)
        node2 = TextNode("test", TextType.BOLD)
        self.assertNotEqual(node1, node2)
    
    def test_not_eq_text(self):
        node1 = TextNode("test1", TextType.CODE)
        node2 = TextNode("test2", TextType.CODE)
        self.assertNotEqual(node1, node2)
    

if __name__ == "__main__":
    unittest.main()