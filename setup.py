try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='scify',
    version='0.0.1',
    description='Ethereum and Ethereum Classic abstraction layer',
    long_description=open('README.md').read(),
    author='Eric Somdahl',
    author_email='eric.somdahl@ethereumclassic.org',
    url='https://github.com/ericsomdahl/scify',
    packages=['scify'],
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: Apache 2.0',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
    ],
    install_requires=[
        'requests==2.9.1',
    ],
)
