from setuptools import setup, find_packages

setup(
    name='django-shortener',
    version='1.0dev',
    description='Django URL shortning application',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    classifiers = ['Frameword :: Django'],
)
