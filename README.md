# scraping-best-sellers-from-glasses-shop

Web scraped the best selling glasses and their details using scrapy,from the website: https://www.glassesshop.com/bestsellers

Repository Link: https://github.com/Abishek-Suresh/scraping-best-sellers-from-glasses-shop

## Tools
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge)
![Scrapy](https://img.shields.io/badge/Scrapy-FFD43B?style=for-the-badge&logo=Scrapy)

## To install scrapy
    
    pip install scrapy
    
## To create a new project
    
    scrapy startproject glassesshop
    
## To generate spider
    
    scrapy gen spider gdp_debt www.glassesshop.com/bestsellers

## To Run the Spider

    scrapy crawl bestsellers

## Export output as CSV, Json, or XML

    scrapy crawl countries -o <filename.extension>
