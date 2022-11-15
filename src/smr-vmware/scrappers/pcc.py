"""Scrap data from a VMWare PCC."""

class SmrScrapper:
    """SmrScrapper for VMWare PCC."""

    def __init__(self, url: str, username: str, password: str):
        self.url = url
        self.username = username
        self.password = password