from setuptools import setup

setup(
    name='click_keyring',
    version='1.0.0',
    author='Eric McNiece',
    author_email='emcniece@gmail.com',
    packages=['click_keyring', 'click_keyring.test'],
    scripts=[],
    url='http://pypi.python.org/pypi/click_keyring/',
    license='LICENSE.txt',
    description='An easy way to use keyring in click CLI applications',
    long_description=open('README.md').read(),
    install_requires=[
        "click >= 7",
        "pytest",
    ],
    python_requires=">=3.0",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
