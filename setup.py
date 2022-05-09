#!/usr/bin/env python
from setuptools import setup


setup_info = dict(
    name='utils',
    version=1.0,
    author='André Cerutti Franciscatto',
    author_email='andre@franciscatto.com',
    url='https://www.franciscatto.com/reposit%C3%B3rios-de-c%C3%B3digos',
    download_url='https://github.com/afmaster/utils.git',
    project_urls={
        'Documentation': 'https://github.com/afmaster/utils.git',
        'Source': 'https://github.com/afmaster/utils.git'
    },
    description='Tools for coding in python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],

    # Package info
    packages=['utils'],

    # Add _ prefix to the names of temporary build dirs
    options={'build': {'build_base': '_build'}, },
    zip_safe=True,
)


requirements = [
    'Brotli>=1.0.9',
    'cachetools>=5.0.0',
    'certifi>=2021.10.8',
    'cffi>=1.15.0',
    'charset-normalizer>=2.0.12',
    'configparser>=5.2.0',
    'cssselect>=1.1.0',
    'cssselect2>=0.6.0',
    'cssutils>=2.4.0',
    'email-to>=0.1.0',
    'fonttools>=4.33.3',
    'geographiclib>=1.52',
    'geopy>=2.2.0',
    'html5lib>=1.1',
    'idna>=3.3',
    'importlib-metadata>=4.11.3',
    'lxml>=4.8.0',
    'Markdown>=3.3.6',
    'Pillow>=9.1.0',
    'premailer>=3.10.0',
    'pycparser>=2.21',
    'pydyf>=0.1.2',
    'pyphen>=0.12.0',
    'requests>=2.27.1',
    'six>=1.16.0',
    'tinycss2>=1.1.1',
    'typing_extensions>=4.2.0',
    'urllib3>=1.26.9',
    'weasyprint>=54.3',
    'webencodings>=0.5.1',
    'zipp>=3.8.0',
    'zopfli>=0.2.1'
]

setup(**setup_info,
      install_requires=requirements)
