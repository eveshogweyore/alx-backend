#!/usr/bin/env python3
"""Simple helper function module."""


import csv
import math
from typing import List, Dict, Any
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get specific data from page in file
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        self.dataset()

        range = index_range(page, page_size)

        return self.__dataset[range[0]: range[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Use hypermedia pagination to retrieve data
        """
        self.hyper: Dict[str, Any] = {}

        data = self.get_page(page, page_size)
        pages = math.ceil(len(self.__dataset) / page_size)
        next_page = (page + 1) if len(data) > 0 else None
        prev_page = (page - 1) if page > 1 else None

        self.hyper['page_size'] = len(data)
        self.hyper['page'] = page
        self.hyper['data'] = data
        self.hyper['next_page'] = next_page
        self.hyper['prev_page'] = prev_page
        self.hyper['total_pages'] = pages

        return self.hyper
