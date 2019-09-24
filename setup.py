from setuptools import setup

setup(
    name='Job Finding Helpers',
    version=0.1,
    description='Useful job-finding helpers (searching and sending good fob offerings).',
    long_description=open('README.md').read(),
    author='Zoltán Galáž',
    author_email='xgalaz00@gmail.com',
    packages=['helpers'],
    license='MIT',
    install_requires=['requests', 'validators', 'pathlib', 'bs4', 'lxml', 'email_split']
)
