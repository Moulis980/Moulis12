import frappe

from frappe.tests.utils import FrappeTestCase


class TestHelpArticle(FrappeTestCase):

    def test_article_creation(self):
        article = frappe.get_doc({
            "doctype": "Help Article",
            "title": "My First Test1",
            "category": "Moulis",
            "published": 1,
            "content": "This is my first test article."
        })

        article.insert()

        self.assertEqual(article.title, "My First Test1")
        self.assertTrue(
            frappe.db.exists("Help Article", article.name)
        )
