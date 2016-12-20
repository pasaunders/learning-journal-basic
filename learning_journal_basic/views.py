"""View for our website."""

# from pyramid.response import Response
from pyramid.view import view_config
import io
import os

HERE = os.path.dirname(__file__)


@view_config(route_name='home', renderer='string')
def home_page(request):
    """Define location of home page."""
    # this is how to use a jinja template:
    list_template = ['data', 'for', 'the', 'template']
    return {'temp_list': list_template}
    # note that the dictionary's key is the name of the list i'm looping through in the .jinja2 file.
    # return Response(imported_text)


def edit_page(request):
    """Define location of edit journal entry."""
    imported_text = open(os.path.join(HERE, 'templates/edit.html')).read()
    return imported_text
    # return Response(imported_text)


def detail_page(request):
    """Define location of detail page."""
    imported_text = open(os.path.join(HERE, 'templates/detail.html')).read()
    return imported_text
    # return Response(imported_text)


def new_entry(request):
    """Define location of new entry."""
    imported_text = open(os.path.join(HERE, 'templates/new.html')).read()
    return imported_text
    # return Response(imported_text)
