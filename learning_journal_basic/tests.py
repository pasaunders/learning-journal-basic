# import unittest
import pytest
from pyramid import testing


# class ViewTests(unittest.TestCase):
#     def setUp(self):
#         self.config = testing.setUp()

#     def tearDown(self):
#         testing.tearDown()

#     def test_my_view(self):
#         from .views import my_view
#         request = testing.DummyRequest()
#         info = my_view(request)
#         self.assertEqual(info['project'], 'learning_journal_basic')


# class FunctionalTests(unittest.TestCase):
#     def setUp(self):
#         from learning_journal_basic import main
#         app = main({})
#         from webtest import TestApp
#         self.testapp = TestApp(app)

#     def test_root(self):
#         res = self.testapp.get('/', status=200)
#         self.assertTrue(b'Pyramid' in res.body)

@pytest.fixture
def req():
    the_request = testing.DummyRequest()
    return the_request


def test_home_page_renders_file_data(req):
    """My home page view returns some data."""
    from .views import home_page
    response = home_page(req)
    assert "message_goes_here" in response


@pytest.fixture
def test():
    """Test app fixture."""
    from webtest import TestApp
    from learning_journal_basic import main
    app = main({})


def test_home_page_has_list(testapp):
    """Response is a get to homepage, expecting a 200 response."""
    response = testapp.get("/", status=200)
    inner_html = response.html
