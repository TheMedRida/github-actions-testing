
import unittest
from unittest.mock import patch

from main import app, get_mode, return_backwards_string


class TestMain(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_return_backwards_string(self):
        self.assertEqual(
            "gnirts tset ym si sihT",
            return_backwards_string("This is my test string")
        )

    def test_get_mode(self):
        with patch.dict("os.environ", {"MODE": "test"}):
            self.assertEqual("test", get_mode())

    def test_homepage(self):
        response = self.client.get("/")
        self.assertEqual(200, response.status_code)

    def test_reverse_interface(self):
        response = self.client.post(
            "/",
            data={"text": "hello"}
        )
        self.assertEqual(200, response.status_code)
        self.assertIn(b"olleh", response.data)


if __name__ == "__main__":
    unittest.main()
