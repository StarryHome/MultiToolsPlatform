# -*- coding:utf-8 -*-
from __future__ import absolute_import
from Aw.celery_aw.celery import app


@app.task
def add(x, y):
    return x + y
