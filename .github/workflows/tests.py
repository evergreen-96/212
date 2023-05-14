import unittest
import requests

def get_status(url):
    try:
        status = requests.get(url)
        return status.status_code
    except:
        return 404


class TestCase(unittest.TestCase):
    def testCode(self):
        self.assertEqual(200, get_status('https://www.google.com/'))

if __name__ == '__main__':
    tests = TestCase()
    print(tests.testCode())
