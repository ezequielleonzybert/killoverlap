from setuptools import setup, find_packages

setup(
    name='killoverlap',
    version='0.1.4',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'killoverlap=killoverlap:runner',
        ],
    },
    license='Apache License, Version 2.0',
    description='Merge all overlapping lines in an SVG drawing',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Ezequiel León Zybert',
    author_email='ezequielleonzybert@gmail.com',
    url='https://github.com/ezequielleonzybert/killoverlap',
    keywords=['python', 'svg', 'overlap','overlapping','merge','lines','outlines','join','overlapped'],
    install_requires=[
        'build123d'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)