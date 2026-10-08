class ApplicationError(Exception):
    """Base class for use-case level failures (not business-rule violations)."""


class TripNotFound(ApplicationError):      # BR6: the requested trip does not exist
    pass