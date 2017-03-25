import setuptools

setuptools.setup(
    name="nbnavigator",
    version='0.0.1',
    url="https://github.com/data-8/nbnavigator",
    author="Andrew Linxie",
    description="Jupyter Extension for assignment navigation and fetching assignments",
    packages=setuptools.find_packages(),
    install_requires=[
        'notebook'
    ],
    package_data={'nbnavigator': ['static/*']},
)