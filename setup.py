"""

    Declare a Python package listlessview

    See

    * http://wiki.python.org/moin/Distutils/Tutorial

    * http://packages.python.org/distribute/setuptools.html#developer-s-

    * http://plone.org/products/plone/roadmap/247

"""

from setuptools import setup

setup(name = "listlessview",
    version = "0.1",
    description = "Provide listless folder view for Plone folders",
    author = "Mikko Ohtamaa",
    author_email = "mikko@opensourcehacker.com",
    url = "",
    install_requires = ["five.grok"],
    packages = ['listlessview'],
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    license="GPL2",
    include_package_data = True,
    entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
)