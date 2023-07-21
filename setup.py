from setuptools import setup, find_packages

setup(
    name='claritygov',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests==2.31.0',
        'pytest==7.4.0'
    ],
    keywords=['claritygov', 'clarityapi', 'government', 'transparency'],
    license='Creative Commons Attribution 4.0 International Public License',
    description='Python API Client for ClarityGov, a free public developer API for accessing government legislative data in a standardized format.',
    author='ClarityGov',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: API Client',
        'License :: Creative Commons Attribution 4.0 International Public License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3'
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ]
)