"""Dictionary related utility functions."""

__author__ = "730396639"

# Define your functions below

from csv import DictReader


def read_csv_rows(csv: str) -> list[dict[str, str]]:
    """Reading the CSV file and formatting it into a list of rows."""
    read: list[dict[str, str]] = []
    file_handle = open(csv, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        read.append(row)
    file_handle.close()   
    return read 


def column_values(table: list[dict[str, str]], column_name: str) -> list[str]:
    """Producing the values associated with a column name."""
    # empty list to store column values
    subject_age: list[str] = []
    i = 0
    # loop through row in the first parameter
    while i < len(table):
        column_value = table[i][column_name]
        # append the value associated with the key ("column") given as the second parameter to your list of column values
        subject_age.append(column_value)
        i += 1
    # return list of column values
    return subject_age


def columnar(rows: list[dict[str, str]]) -> dict[str, list[str]]:
    """Docstring."""
    dict_of_columns: dict = {}
    x: column_values
    i: int = 0
    # loop through each of the column names in the first row of the parameter
    while i < len(rows):
        row_value = rows[i]
        for key in column_values:
            dict_of_columns.append.key[row_value]
            i += 1
    # associate the column name with the list of its values in the dictionary you established
    return dict_of_columns
    

def head(a: dict[str, list[str]], b: int) -> dict[str, list[str]]:
    """Docstring."""
    c: dict[str, list[str]] = {"b", "d"}
    return c


def select(a: dict[str, list[str]], b: list[str]) -> dict[str, list[str]]:
    """Docstring."""
    c: dict[str, list[str]] = {"b", "d"}   
    return c


def concat(a: dict[str, list[str]], b: dict[str, list[str]]) -> dict[str, list[str]]:
    """Docstring."""
    c: dict[str, list[str]] = {"b", "d"}  
    return c