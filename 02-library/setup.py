from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

tests_require = [
  'pytest',
  'pytest-cov',
  'testfixtures',
  'numpy',
  'scipy',
  'sklearn'
]

setup(
  name='cs506',
  packages=['cs506'],
  version='0.0.1',
  description='Run some cs506 algorithms',
  install_requires=[],
  python_requires='>=3.6, <4',
  setup_requires=['pytest-runner'],
  tests_require=tests_require,
  extras_require={
    'test': tests_require,
  },
  long_description=long_description,
  long_description_content_type="text/markdown",
  license="Apache License 2.0",
  include_package_data=True,
  classifiers=[
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)