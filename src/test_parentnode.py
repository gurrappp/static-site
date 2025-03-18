import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_children_props(self):
        child_node = LeafNode("a","child",{"href": "https://www.google.com"})
        parent_node = ParentNode("code", [child_node])
        self.assertEqual(parent_node.to_html(),'<code><a href="https://www.google.com">child</a></code>')

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_children_text_tag(self):
        node = ParentNode(
                "p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],
            )

        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_without_children(self):
        with self.assertRaises(ValueError): ParentNode("div", children=None).to_html()
    
    def test_basic_parent_node(self):
        children = [LeafNode(None, "Hello"), LeafNode(None, "World")]
        parent = ParentNode("div", children)
        self.assertEqual(parent.to_html(), "<div>HelloWorld</div>")

    
        

if __name__ == "__main__":
    unittest.main()