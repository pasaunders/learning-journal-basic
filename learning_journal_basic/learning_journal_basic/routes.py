"""This is the routes for our website."""


def includeme(config):
    """The function adds routes to Pyramid's Configurator."""
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('new', '/journal/new-entry')
    config.add_route('detail', '/journal/1')
    config.add_route('edit', '/journal/1/edit-entry')
