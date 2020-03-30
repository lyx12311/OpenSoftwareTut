from setuptools import setup

with open("OpenSoftwareTut/version.py", "r") as f:
    exec(f.read())

setup(name='OpenSoftwareTut',
      version=__version__,
      description='Tutorial to create an open-source software package!',
      url='https://github.com/lyx12311/OpenSoftwareTut',
      author='Yuxi(Lucy) Lu',
      author_email='lucylulu12311@gmail.com',
      license=' ',
      packages=['OpenSoftwareTut'],
      install_requires=['numpy'],
      zip_safe=False)
