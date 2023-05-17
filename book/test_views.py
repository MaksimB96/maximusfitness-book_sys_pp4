from django.test import TestCase

class TestViews(TestCase):

    def get_index(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "templates/index.html")

    def get_book(self):
        response = self.client.get("book-session/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "templates/book-session.html.html")


    def get_manage(self):
        response = self.client.get("manage-session/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "templates/manage-session.html")


    def get_delete(self):
        response = self.client.get("delete-session/<id>")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "templates/delete-session.html")


    def get_update(self):
        response = self.client.get("update-session/<id>")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "templates/update-session.html")
