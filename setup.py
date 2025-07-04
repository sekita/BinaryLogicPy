# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='BinaryLogicPy',
    version='2.0.0',
    py_modules=['binarylogicroutine'],
    description='This library is designed to easily simulate single-phase synchronous logic circuits using flip-flops (JKFF, RSFF, SRFF, DFF, TFF) in a text-based environment.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='SEKITA, Iwao',
    author_email='sekita@cs.k.tsukuba-tech.ac.jp',
    url='https://github.com/sekita/BinaryLogicPy',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
