import virtualenv, textwrap
output = virtualenv.create_bootstrap_script(textwrap.dedent("""
import os, subprocess, sys
def extend_parser(parser):
    parser.add_option(
        '--buildout_version',
        dest='buildout_version',
        default=None,
        help='Optional specification of zc.buildout version to use when bootstrapping')
def after_install(options, home_dir):
    if sys.platform == 'win32':
        bin = 'Scripts'
    else:
        bin = 'bin'
    # Install package example:
    #subprocess.call([join(home_dir, bin, 'easy_install'),
    #                 'MyPackage'])
    # Run script example:
    #subprocess.call([join(home_dir, bin, 'my-package-script'),
    #                 'setup', home_dir])
    if not os.path.exists(os.path.join(home_dir, 'buildout.cfg')):
        shutil.copy(os.path.join(home_dir, 'buildout.cfg.example'),
                    os.path.join(home_dir, 'buildout.cfg'))
    if os.path.exists('buildout-bootstrap.py'):
        logger.notify('')  # newline
        if options.buildout_version:
            logger.notify('Running buildout bootstrap; version specified = ' + str(options.buildout_version))
            subprocess.call([os.path.join(home_dir, bin, 'python'),
                            'buildout-bootstrap.py', '-v ' + options.buildout_version])
        else:
            logger.notify('Running buildout bootstrap; no version specified, using newest (check bin/buildout for version')
            subprocess.call([os.path.join(home_dir, bin, 'python'),
                            'buildout-bootstrap.py'])
        logger.notify('')  # newline
        logger.notify('updating setuptools')
        subprocess.call([os.path.join(home_dir, bin, 'easy_install'),
                        '-U', 'setuptools'])

def adjust_options(options, args):
    options.no_pip = True
"""))
f = open('bootstrap_virtualenv_.py', 'w').write(output)
