# soup

Extract the values requested from XML files using **BeautifulSoup**.


## Usage

- Print the text for the first node ASIN in one file

    soup 'ASIN' <file>

- Print the texts for all the nodes ASIN in one file

    soup --all 'ASIN' <file>

- Print the texts for multiple nodes in one file

    soup --all 'ASIN','created_at' <file>

- Print all the children in a given tag

    soup --children ItemAttributes <file>
