# soup

![soup picture](https://github.com/alexandriagroup/soup/raw/master/img/soup.jpg)

Extract the values requested from XML files using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).

## Usage

- Print the text for all the nodes ASIN

        soup 'ASIN' <file1> [<file2> ...]

- Print the text for multiple nodes

        soup 'ASIN','created_at' <file1> [<file2> ...]

- Print all the children in a given tag

        soup --children ItemAttributes <file> [<file2> ...]

- Print all the children and their values

        soup --children --values ItemAttributes <file> [<file2> ...]


## Installation

* With [poetry](https://poetry.eustace.io/):

        poetry install

* Manually:

        pip install beautifulsoup4
        cp soup/core.py <somepath>/soup


# Acknowledgement

Photo by Charles Koh on Unsplash.
