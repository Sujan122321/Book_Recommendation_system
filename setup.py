
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "Book_Recommendation_system"
AUTHOR_USER_NAME = "Sujan Shrestha"
SRC_REPO = "books_recommender"   # root folder name
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    author="Sujan Shrestha",
    description="A small local packages for ML based books recommendations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sujan122321/Book_Recommendation_system",
    author_email="suzanstha203@gmail.com",
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.12",
    install_requires=LIST_OF_REQUIREMENTS
)