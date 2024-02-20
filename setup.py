"""
Jinja templates for Digital Marketplace apps.
"""
import re
import ast
import glob
import os
from setuptools import setup, find_packages


_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('digitalmarketplace_frontend_jinja/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(f.read().decode('utf-8')).group(1)))

components = []
directories = glob.glob("digitalmarketplace_frontend_jinja/**/**/*.html", recursive=True)
for directory in directories:
    components.append(os.path.relpath(os.path.dirname(directory), "digitalmarketplace_frontend_jinja") + "/*.html")

setup(
    name='ccs-digitalmarketplace-frontend-jinja',
    version=version,
    url='https://github.com/tim-s-ccs/ccs-digitalmarketplace-frontend-jinja',
    license='MIT',
    author='CCS',
    description='Jinja templates for Digital Marketplace apps.',
    long_description=__doc__,
    packages=find_packages(),
    package_data={'digitalmarketplace_frontend_jinja': components},
    include_package_data=True,
    install_requires=[
        'jinja2>3',
        'govuk-frontend-jinja>=2.8.0,<3',
        'ccs-digitalmarketplace-utils>=66.0.0rc1',
    ],
    python_requires=">=3.9,<3.12",
)
