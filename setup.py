from setuptools import setup

setup(
    name='unwicked',
    version='0.1',
    description='Mock remains of wicked without doing anything',
    url='https://github.com/starzel/unwicked',
    author='Philip Bauer',
    author_email='bauer@starzel.de',
    license='GPL version 2',
    packages=['unwicked'],
    zip_safe=False,
    entry_points={'z3c.autoinclude.plugin': ['target = plone']},
    )
