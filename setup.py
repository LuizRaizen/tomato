from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='tomato',
    version='0.0.3',
    url='https://github.com/LuizRaizen/tomato.git',
    license='MIT License',
    author='Luiz R. Dererita',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='luizdererita02@gmail.com',
    keywords='Tomato',
    description=u'Text output customization and formatting tool.',
    packages=['tomato'],
    install_requires=[],)