import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    # def test_eq(self):
    #     node1 = HTMLNode()
    #     node2 = HTMLNode()

    #     node3 = HTMLNode("<p>", "test paragraph")
    #     node4 = HTMLNode("<p>", "test paragraph")
    #     print(node3)
    #     print(node4)
    #     self.assertEqual(node1, node2)
    #     self.assertEqual(node3, node4)
    
    def test_valid_input(self):
        test_tag = "<a>"
        test_value = "anchor tag"
        node = HTMLNode("<a>", "anchor tag")
        self.assertEqual(node.tag, test_tag)
        self.assertEqual(node.value, test_value)

    def test_props_to_html(self):
        node1 = HTMLNode(props= {
                            "href": "https://www.google.com",
                            "target": "_blank",
                        })
        output = node1.props_to_html()
        self.assertEqual(output, ' href="https://www.google.com" target="_blank"')

    def test_repr(self):
        node = HTMLNode("<h1>", "heading 1")
        self.assertEqual(repr(node), "tag: <h1> | value: heading 1 | children: empty list | props: ")
    
    def test_repr_with_all_attributes(self):
        node = HTMLNode(tag="div", value="test value", children=["child1", "child2"], props={"id": "my-id", "class": "my-class"})
        expected_output = "tag: div | value: test value | children: child1 | child2 | props:  [key: id, value: my-id] [key: class, value: my-class]"
        
        self.assertEqual(repr(node), expected_output)

if __name__ == "__main__":
    unittest.main()