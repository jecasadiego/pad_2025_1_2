from setuptools import setup, find_packages

setup(
    name='edu_pad',
    version='0.0.1',
    author='Juan Casadiego',
    author_email='juanescasa24@hotmail.com',
    description='A package for educational purposes',
    py_modules=['actividad1', 'actividad2'],
    install_requires=[
        'pandas',
        'openpyxl',
        'numpy',
        'requests',
        'beautifulsoup4',
    ]
)
