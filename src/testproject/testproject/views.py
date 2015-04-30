from pyramid.view import view_config

import logging
log = logging.getLogger(__name__)

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    log.debug('TESTLOG')
    print  request.registry.settings['buildout_dir']
    return {'project': 'testproject'}
