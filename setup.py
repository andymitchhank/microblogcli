from io import open

from setuptools import find_packages, setup

with open('microblogcli/__init__.py', 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.strip().split('=')[1].strip(' \'"')
            break
    else:
        version = '0.0.1'

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

REQUIRES = []

setup(
    name='microblogcli',
    version=version,
    description='',
    long_description=readme,
    author='Andrew Henry',
    author_email='andymitchhank@users.noreply.github.com',
    maintainer='Andrew Henry',
    maintainer_email='andymitchhank@users.noreply.github.com',
    url='https://github.com/andymitchhank/microblogcli',
    license='MIT',

    keywords=[
        '',
    ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    install_requires=REQUIRES,
    tests_require=['coverage', 'pytest'],

    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'microblog = microblogcli.cli:cli',
        ],
    },
)
