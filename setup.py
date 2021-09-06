from setuptools import find_packages, setup

def readme():
    with open('README.rst') as f:
        return f.read()


test_deps = []

extras = {
    'test': test_deps
}

# TODO: Authors add your emails!!!
authors = {
    "Luca Cappelletti":"luca.cappelletti1@unimi.it",
    "Tommaso Fontana":"tommaso.fontana@mail.polimi.it",
    "Vida Ravanmehr":"vida.ravanmehr@jax.org",
    "Peter Robinson":"peter.robinson@jax.org",
}

setup(
    name='grape',
    version='0.0.1',
    description='Rust/Python for high performance Graph Processing and Embedding.',
    long_description=readme(),
    url='https://github.com/monarch-initiative/embiggen',
    keywords='node2vec,word2vec,CBOW,SkipGram,GloVe',
    author=", ".join(list(authors.keys())),
    author_email=", ".join(list(authors.values())),
    license='MIT',
    python_requires='>3.6.0',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*', 'notebooks*']),
    install_requires=[
        "ensmallen>=0.6.1",
        "embiggen>=0.9.0"
    ],
    tests_require=test_deps,
    include_package_data=True,
    zip_safe=False,
    extras_require=extras,
)
