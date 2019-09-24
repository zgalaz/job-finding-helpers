from setuptools import setup

setup(
    name='Job Finder Helpers',
    version=0.1,
    description='Useful job-finder helpers (searching and sending good fob offerings).',
    long_description=open('README.md').read(),
    author='Zoltán Galáž',
    author_email='xgalaz00@gmail.com',
    packages=['helpers'],
    license='MIT',
    install_requires=['requests', 'validators', 'pathlib', 'bs4', 'lxml', 'email_split ']
)
