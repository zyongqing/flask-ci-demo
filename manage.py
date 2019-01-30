import os
from app import create_app, celery

app = create_app(os.getenv('FLASK_CONFIG', 'default'))
celery = celery


@app.shell_context_processor
def make_shell_context():
    context = dict(app=app, celery=celery)
    return context


@app.cli.command()
def test():
    import unittest
    import sys
    tests = unittest.TestLoader().discover('tests')
    ret = not unittest.TextTestRunner(verbosity=2).run(tests).wasSuccessful()
    sys.exit(ret)


@app.cli.command()
def cov():
    import unittest
    import coverage
    import os
    import sys
    cov = coverage.coverage(branch=True, include='app/*')
    cov.start()
    tests = unittest.TestLoader().discover('tests')
    ret = not unittest.TextTestRunner(verbosity=2).run(tests).wasSuccessful()
    cov.stop()
    cov.save()
    print('Coverage Summary:')
    cov.report()
    basedir = os.path.abspath(os.path.dirname(__file__))
    covdir = os.path.join(basedir, 'htmlcov')
    cov.html_report(directory=covdir)
    cov.erase()
    sys.exit(ret)
