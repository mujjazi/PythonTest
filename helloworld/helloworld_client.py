# -*- coding: utf-8 -*-

"""
    helloworld

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from helloworld.decorators import lazy_property
from helloworld.configuration import Configuration
from helloworld.controllers.helloworld_controller import HelloworldController


class HelloworldClient(object):

    config = Configuration

    @lazy_property
    def helloworld(self):
        return HelloworldController()


