# pylint: disable=missing-module-docstring
from flask import Response, request
def set_price_list():
    """web-scrap the product details from the given url add it the the database with the userId.
    Parameters:
        url (string): url of the product to be scrapped"""
    if request.method == 'POST':
        url=request.form.get('url')

        return Response(url),200
    return Response("invalid"),401
