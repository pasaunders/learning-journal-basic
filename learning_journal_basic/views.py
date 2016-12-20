"""View for our website."""

from pyramid.response import Response
import os

HERE = os.path.dirname(__file__)


def home_page(request):
    """Define location of home page."""
    imported_text = open(os.path.join(HERE, 'templates/main.html')).read()
    return Response(imported_text)


def edit_page(request):
    """Define location of edit journal entry."""
    imported_text = open(os.path.join(HERE, 'templates/edit.html')).read()
    return Response(imported_text)


def detail_page(request):
    """Define location of detail page."""
    imported_text = open(os.path.join(HERE, 'templates/detail.html')).read()
    return Response(imported_text)


def new_entry(request):
    """Define location of new entry."""
    imported_text = open(os.path.join(HERE, 'templates/new.html')).read()
    return Response(imported_text)


def includeme(config):
    """File to be include in init."""
    config.add_view(home_page, route_name='home')
    config.add_view(edit_page, route_name='edit')
    config.add_view(detail_page, route_name='detail')
    config.add_view(new_entry, route_name='new')
