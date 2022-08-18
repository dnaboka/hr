from setuptools import setup, find_packages

setup(
    name='hr',
    version='0.0.1',
    description='CLI user export utility',
    author='Dima Naboka',
    packages=find_packages('src'),
    package_dir={'':'src'},
    entry_points={'console_scripts':'hr=hr.cli:main'}
)
