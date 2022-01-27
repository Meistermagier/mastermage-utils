from setuptools import setup

setup(
    name="mastermage_utils",
    version="0.1.0",
    description="A package with Utilitiy tools that I use for my Physics Studies",
    author="Tom Ihro",
    author_email="tom.ihro@stud.uni-heidelberg.de",
    packages = ["mastermage_utils"],
    install_requires = ["numpy","matplotlib","orjson"],
    
    
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
    ],

    )