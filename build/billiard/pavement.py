import sys
from paver.easy import *
from paver import doctools
from paver.setuputils import setup

PYCOMPILE_CACHES = ["*.pyc", "*$py.class"]

options(
        sphinx=Bunch(builddir=".build"),
)


def sphinx_builddir(options):
    return path("docs") / options.sphinx.builddir / "html"


@task
def clean_docs(options):
    sphinx_builddir(options).rmtree()


@task
@needs("clean_docs", "paver.doctools.html")
def html(options):
    destdir = path("Documentation")
    destdir.rmtree()
    builtdocs = sphinx_builddir(options)
    builtdocs.move(destdir)


@task
@needs("paver.doctools.html")
def qhtml(options):
    destdir = path("Documentation")
    builtdocs = sphinx_builddir(options)
    sh("rsync -az %s/ %s" % (builtdocs, destdir))


@task
@needs("clean_docs", "paver.doctools.html")
def ghdocs(options):
    builtdocs = sphinx_builddir(options)
    sh("git checkout gh-pages && \
            cp -r %s/* .    && \
            git commit . -m 'Rendered documentation for Github Pages.' && \
            git push origin gh-pages && \
            git checkout master" % builtdocs)


@task
@needs("clean_docs", "paver.doctools.html")
def upload_pypi_docs(options):
    builtdocs = path("docs") / options.builddir / "html"
    sh("%s setup.py upload_sphinx --upload-dir='%s'" % (
        sys.executable, builtdocs))


@task
@needs("upload_pypi_docs", "ghdocs")
def upload_docs(options):
    pass


@task
@cmdopts([
    ("noerror", "E", "Ignore errors"),
])
def flake8(options):
    noerror = getattr(options, "noerror", False)
    complexity = getattr(options, "complexity", 22)
    sh("""flake8 billiard | perl -mstrict -mwarnings -nle'
        my $ignore = m/too complex \((\d+)\)/ && $1 le %s;
        if (! $ignore) { print STDERR; our $FOUND_FLAKE = 1 }
    }{exit $FOUND_FLAKE;
        '""" % (complexity, ), ignore_error=noerror)


@task
@cmdopts([
    ("noerror", "E", "Ignore errors"),
])
def flakeplus(options):
    noerror = getattr(options, "noerror", False)
    sh("flakeplus billiard", ignore_error=noerror)


@task
@cmdopts([
    ("noerror", "E", "Ignore errors")
])
def flakes(options):
    flake8(options)
    flakeplus(options)


@task
def bump(options):
    sh("contrib/release/bump_version.py billiard/__init__.py")

@task
@cmdopts([
    ("coverage", "c", "Enable coverage"),
    ("verbose", "V", "Make more noise"),
])
def test(options):
    cmd = "nosetests"
    if getattr(options, "coverage", False):
        cmd += " --with-coverage3"
    if getattr(options, "verbose", False):
        cmd += " --verbosity=2"
    sh(cmd)


@task
@cmdopts([
    ("noerror", "E", "Ignore errors"),
])
def pep8(options):
    noerror = getattr(options, "noerror", False)
    return sh("""find . -name "*.py" | xargs pep8 | perl -nle'\
            print; $a=1 if $_}{exit($a)'""", ignore_error=noerror)


@task
def removepyc(options):
    sh("find . -type f -a \\( %s \\) | xargs rm" % (
        " -o ".join("-name '%s'" % (pat, ) for pat in PYCOMPILE_CACHES), ))


@task
@needs("removepyc")
def gitclean(options):
    sh("git clean -xdn")


@task
@needs("removepyc")
def gitcleanforce(options):
    sh("git clean -xdf")


@task
@needs("flakes", "test", "gitclean")
def releaseok(options):
    pass


@task
@needs("releaseok", "removepyc", "upload_docs")
def release(options):
    pass
