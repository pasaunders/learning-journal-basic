"""This is the routes for our website."""

def includeme(config):
    """The function adds routes to Pyramid's Configurator."""
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')