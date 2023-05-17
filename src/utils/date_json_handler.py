import datetime

def date_handler(obj):
    """
    Custom JSON serializer for objects of type `datetime.datetime` and `datetime.date`.

    This function converts `datetime` and `date` objects to ISO 8601 format strings 
    which are JSON serializable. If the object is not of the correct type, it raises 
    a TypeError.

    Parameters:
    obj (object): The object to be serialized. It is expected to be a `datetime.datetime` 
                  or `datetime.date` object.

    Returns:
    str: The ISO 8601 formatted string representation of the date or datetime.

    Raises:
    TypeError: If the object is not of type `datetime.datetime` or `datetime.date`.

    Example:
    >>> date_handler(datetime.datetime(2023, 5, 17))
    '2023-05-17T00:00:00'
    >>> date_handler(datetime.date(2023, 5, 17))
    '2023-05-17'
    """
    if isinstance(obj, (datetime.datetime, datetime.date)):
        return obj.isoformat()
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")
