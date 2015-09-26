from setuptools import setup
from setuptools import find_packages


version = '0.1.0.dev0'

install_requires = [
    'acme=={0}'.format(version),
    'letsencrypt=={0}'.format(version),
    'mock<1.1.0',  # py26
    'python-augeas',
    'setuptools',  # pkg_resources
    'zope.component',
    'zope.interface',
]

setup(
    name='letsencrypt-apache',
    version=version,
    packages=find_packages(),
    install_requires=install_requires,
    entry_points={
        'letsencrypt.plugins': [
            'apache = letsencrypt_apache.configurator:ApacheConfigurator',
        ],
    },
    include_package_data=True,
)
