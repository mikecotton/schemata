"""Routes configuration

The more specific and detailed routes should be defined first so they
may take precedent over the more generic routes. For more information
refer to the routes manual at http://routes.groovie.org/docs/
"""
from pylons import config
from routes import Mapper

def make_map():
    """Create, configure and return the routes Mapper"""
    map = Mapper(directory=config['pylons.paths']['controllers'],
                 always_scan=config['debug'])
    map.minimization = False

    # The ErrorController route (handles 404/500 error pages); it should
    # likely stay at the top, ensuring it can always be resolved
    map.connect('/error/{action}', controller='error')
    map.connect('/error/{action}/{id}', controller='error')

    # CUSTOM ROUTES HERE
    map.connect('/', controller='index', action='index')
#    map.connect('/newtable', controller='index', action='newtable')
    map.connect('/new_table', controller='index', action='new_table')
    map.connect('/tables', controller='tables', action='index')
    map.connect('/data_entry', controller='index', action='data_entry')
    map.connect('/display_data', controller='index', action='display_data')
    map.connect('/', controller='edit', action='index')
    map.connect('/csv/:file_name', controller='index', action='csv')
    map.connect('/{controller}/{action}')
    map.connect('/{controller}/{action}/{id}')

    return map
