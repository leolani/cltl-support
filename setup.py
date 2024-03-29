from setuptools import setup, find_namespace_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

with open("VERSION", "r") as fh:
    version = fh.read().strip()


setup(
    name='cltl.support',
    version=version,
    package_dir={'': 'src'},
    packages=find_namespace_packages(include=['cltl.*'], where='src'),
    data_files=[('VERSION', ['VERSION'])],
    url="https://github.com/leolani/cltl-support",
    license='MIT License',
    author='CLTL',
    author_email='t.baier@vu.nl',
    description='Utilities related to the Leolani application',
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.9',
    install_requires=['cltl.combot'],
)
