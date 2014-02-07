#This file is part nereid_smtp module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.

from trytond.pool import Pool
from .routing import *


def register():
    Pool.register(
        WebSite,
        module='nereid_smtp', type_='model')
