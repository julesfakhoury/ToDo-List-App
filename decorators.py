
import logging
from flask import request, abort
from functools import wraps


def require_request_params(params):
    """
    Decorator to check that all required parameters are in the request.
    The required parameters are sent as arguments of the function.

    :param (list) params: list of required parameters

    :return: decorator
    """
    def decorator(f):
        @wraps(f)
        def inner(*args, **kwargs):
            data = request.values.to_dict()
            if not all(param in data for param in params):
                logging.error('missing parameter: this request requires all following parameters: {}'.format(params))
                return abort(400)
            return f(*args, **kwargs, **data)
        return inner
    return decorator
