import setuptools

setuptools.setup(
    name="GuessingGameTwo",
    version="0.1",
    author="Carol Fazani",
    author_email="carolfazani.ds@gmail.com",
    description="Guessing Game Two Application",
    packages=setuptools.find_packages(),
    include_package_data=True,
    python_requires='>=3.6',
    install_requires=[
        'pygame'

    ],
    entry_points={
        'console_scripts': [
            'guessinggametwo = ggame.__main__:main',
        ]
    },
)