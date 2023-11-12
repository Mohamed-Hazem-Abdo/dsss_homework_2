from setuptools import setup, find_packages

setup(
    name='math_quiz',
    description='Math quiz game',
    url='https://github.com/Mohamed-Hazem-Abdo/dsss_homework_2',
    author='Mohamed Hazem',
    author_email='zeitherr99@gmail.com',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'math_quiz = math_quiz.math_quiz:main',
        ],
    },
)
