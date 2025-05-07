from setuptools import setup, find_packages

setup(
    name='edu_pad',
    version='0.1',
    description='Scraper de libros con almacenamiento en CSV',
    author='Juan Esteban Casadiego',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests',
        'beautifulsoup4'
    ],
    entry_points={
        'console_scripts': [
            'edu-pad-run=edu_pad.static.main:run'
        ]
    },
)
