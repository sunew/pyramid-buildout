from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    print  request.registry.settings['buildout_dir']
    return {'project': 'testproject'}
