try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
setup(
    description= 'My Project',
    author= 'Andrea Anaya',
    url= 'URL to get it at.',
    download_url= 'Where to download it.',
    author_email= 'My email.',
    version= '0.1',
    install_requires= ['nose'],
    packages= ['gothonweb'],
    scripts= ['bin/sample.py'],
    name= 'gothonweb'
)


    