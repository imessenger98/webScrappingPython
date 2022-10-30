# pylint: disable=missing-module-docstring
from flask import Response, request
from autoscraper import AutoScraper

def set_price_list():
    """web-scrap the product details from the given url add it the the database with the userId.
    Parameters:
        url (string): url of the product to be scrapped"""
    if request.method == 'POST':
        url=request.form.get('url')
        scrapper=AutoScraper()
        scrapper.load('amazonSearch')
        result=scrapper.get_result_similar(url,group_by_alias=True)
        print(type(result))
        print(result['title'],result['image'],result['price'])
        return Response("hey"),200
    return Response("invalid"),401
