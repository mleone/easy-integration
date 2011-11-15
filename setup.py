from setuptools import setup, find_packages
 
setup(
    name='easy-integration',
    version='0.1',
    description='A simple API for easy, intuitive integration testing for python apps',
    author='Mike Leone',
    author_email='michael.leone@panopticdev.com',
    url='http://panopticdev.com',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License ::  MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools', 'splinter>=0.4', 'zope.testbrowser>=4.0.2'],
)
