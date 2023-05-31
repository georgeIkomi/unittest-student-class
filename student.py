from datetime import date, timedelta


class Student:
    """A student class as base for method testing"""

    # prepend property with underscore to indicate read-only fields
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today()
        self.naughty_list = False

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"
