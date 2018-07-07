# -*- coding: utf-8 -*-

"""Custom exception classes raised by the sfpl module."""


class NotOnHold(Exception):
    """Raised when a user tries to cancel a hold on a book they aren't holding."""

    def __init__(self, book):
        Exception.__init__(self, '{} is not on hold.'.format(self.book))


class InvalidSearchType(Exception):
    """Raised when a user passes an invalid search type for the Search class."""

    def __init__(self, _type):
        Exception.__init__(self, "{} is not a valid search type. Valid search types are 'keyword', 'title', 'author', 'subject', 'tag' and 'list'.".format(_type))


class NoBranchFound(Exception):
    """Raised when no matches are found for a user's branch search."""

    def __init__(self, branch):
        Exception.__init__(self, 'No matches found for {}.'.format(branch))


class NoUserFound(Exception):
    """Raised when no matches are found for a user's user search."""

    def __init__(self, user):
        Exception.__init__(self, 'No match found for {}'.format(user))


class LoginError(Exception):
    """Raised when a user's barcode and pin are rejected."""
    def __init__(self, msg):
        Exception.__init__(self, msg)


class HoldError(Exception):
    """Raised wheb a user's hold request is denied."""
    def __init__(self, msg):
        Exception.__init__(self, msg)


class NotLoggedIn(Exception):
    """Raised when an authentication token is rejected."""
    pass
