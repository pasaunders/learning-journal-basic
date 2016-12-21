"""Initialize a response to a get request."""


from pyramid.config import Configurator


def main(global_config, **settings):
    """Return a Pyramid WSGI application."""
    config = Configurator(settings=settings)
    config.add_static_view(name='static', path='learning_journal_basic:static')
    config.include('pyramid_jinja2')
    config.include('.routes')
    # config.include('.views')
    config.scan()
    return config.make_wsgi_app()
