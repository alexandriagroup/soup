# soup

![soup picture](https://github.com/alexandriagroup/soup/raw/master/img/soup.jpg)

Extract the values requested from XML files using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).

## Usage

- Print the text for the first node ASIN in one file

        soup 'ASIN' <file>

- Print the texts for all the nodes ASIN in one file

        soup --all 'ASIN' <file>

- Print the texts for multiple nodes in one file

        soup --all 'ASIN','created_at' <file>

- Print all the children in a given tag

        soup --children ItemAttributes <file>


## Installation

* With [poetry](https://poetry.eustace.io/):

        poetry install

* Manually:

        pip install beautifulsoup4
        cp soup/core.py <somepath>/soup


# Acknowledgement

Photo by Charles Koh on Unsplash.
