from setuptools import setup

if __name__ == "__main__":
    setup(
        name='pytest-eradicate',
        description='pytest plugin to check for commented out code',
        long_description=open("README.md").read(),
        license="MIT license",
        version='0.0.2',
        author='Johan Bloemberg',
        author_email='johan.bloemberg@spilgames.com',
        url='https://github.com/spil-johan/pytest-eradicate',
        py_modules=['pytest_eradicate'],
        entry_points={'pytest11': ['eradicate = pytest_eradicate']},
        install_requires=['pytest-cache', 'pytest>=2.4.2', 'eradicate', ],
        classifiers=[
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4'
        ],
    )
