from setuptools import setup

setup(
    name='cli',
    version='0.1',
    py_modules=['cli'],
    install_requires=[
        'Click',
        'requests',
        'beautifulsoup4',
    ],
    entry_points='''
        [console_scripts]
        cli=cli:cli
    ''',

)
