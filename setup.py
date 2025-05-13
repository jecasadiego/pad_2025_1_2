from setuptools import setup, find_packages

setup(
    name='edu_pad',
    version='0.2.0',
    description='Scraper de libros con almacenamiento en CSV y SQLite',
    author='Juan Esteban Casadiego',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests',
        'beautifulsoup4',
        'selenium',
        'webdriver-manager',
        'tqdm',
    ],
    entry_points={
        'console_scripts': [
            'edu-pad-run=edu_pad.static.main:run'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.7',
)
