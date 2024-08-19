#!/usr/bin/env python3
"""Simple helper function module."""


def index_range(page: int, page_size: int) -> tuple:
    """Simple helper function."""
    start_index = (page * page_size) - page_size
    end_index = page * page_size

    return (start_index, end_index)
