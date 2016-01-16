from __future__ import absolute_import

try:
    from collections import OrderedDict
except ImportError:
    from .packages.ordereddict import OrderedDict
    import collections
    collections.OrderedDict = OrderedDict

__doc__="""\
lyricsar is a tool for extracting lyrics from website.\
Unlike other tools, it focuses entirely on getting\
and fetching lyrics from website. lyricsar allows to\
obtain the exact lyrics from page.\
It includes a converter that can transform lyrics\
into other text formats (such as HTML).\
 """
__all__=['config','filetest','pagegetter','strprocess']
__package__=['plugin']

__title__ = 'lyricsar'
__version__ = '0.3.1'
__build__ = 0x000001
__author__ = 'Aniket patel '
__license__ = 'MIT'
__copyright__ = 'Copyright 2016 Aniket patel'
__docformat__ = 'restructuredtext'
