#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/12/28
import logging
import logging.config

logging.config.fileConfig("logging.conf")
logger = logging.getLogger("save")

if __name__ == '__main__':
    pass