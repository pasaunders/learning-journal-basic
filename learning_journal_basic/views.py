"""View for our website."""

# from pyramid.response import Response
from pyramid.view import view_config
import io
import os

HERE = os.path.dirname(__file__)

list_template = [
    {'id': 5,
     'title': 'day 12',
     'creation_date': '12/20/2016',
     'body': "I'm not holding my end up. Claire's understanding of pyramid is way ahead of mine, and we don't have enough time to let me work through it myself. There's so much here, and I'm stuck cargo-culting my way through. I think I understnd how the templates are hooked up though, and the MVC format in python is making sense."},
    {'id': 4,
     'title': 'day 11',
     'creation_date': '12/19/2016',
     'body': """A few big lessons today. First: read my homework more carefully. I should have had my html set up properly already. Second, I need more practice, just in general. Third, get more sleep and better food. I've been in a fog all day and I'm not absorbing enough of the lessons."""},
    {'id': 3,
     'title': 'day 10',
     'creation_date': '12/16/2016',
     'body': """Today the big lesson was parametrizing my fixtures. It's really cool. I also learned that we need to read our assignments more literally. My group lost a ton of time trying to fix an issue that shouldn't have come up at all. Nick's talk about teamwork was really good. It made me really want to work on being a better teammate."""},
    {'id': 2,
     'title': 'day 9',
     'creation_date': '12/15/2016',
     'body': """The big event today was the PuPPy meetup. I'm glad I
     went, even though I had to cut work on the server project short of
     completion. After understanding a singly ordered list, a doubly
     ordered list wasn't too complicated. It was just a matter of
     implementing a 'prev' value to go with next, and updating a few
     methods to fix head and tail interactions. I think I like working
     with data structures. The server project is a huge thorn in my
     side. My syntax is weak, so I'm making a lot of small errors which
     take a lot of debugging time, which slows the process way down,
     which makes the next day's work harder. Getting another explanation
     of Composition in class was good. I think I understand it better,
     though not well enough for comfort yet. I know what it's for, just
     not how using it works."""},
    {'id': 1,
     'title': 'day 8',
     'creation_date': '12/14/2016',
     'body': """Coding is a lot easier after a good night's sleep and a hot meal. The biggest challenges today were communication with my teammates. I'm in a three person group and it's easy to get sidelined or left behind. The code review this morning was very helpful. It made it possible for my HTTP server group to keep our server open through a full run of tests. We finally got the server working (more or less) like we wanted this evening. With passing tests no less! I'm enjoying the data structures work the most though. I'm still not entirely clear on how composition works though. The examples in the class notes are two narrow-purpose. They don't actually do much to explain how to use composition ourselves. I need a more theoretical explanation, preferably with the chance to code along and get corrections."""},
]


@view_config(route_name='home', renderer='string')
def home_page(request):
    """Define location of home page."""
    # this is how to use a jinja template:
    return {'entry_list': list_template}
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
