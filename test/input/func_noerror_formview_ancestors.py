"""
Checks that Pylint does not complain about django FormViews
having too many ancestors
"""
#  pylint: disable=C0111,W5101
from django.views.generic import FormView


class SomeView(FormView):
    pass
