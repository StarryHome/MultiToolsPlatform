# -*- coding:utf-8 -*-
from __future__ import absolute_import
from celery import Celery

app = Celery('celery_aw', include=['celery_aw.tasks'])

app.config_from_object('celery_aw.config')

if __name__ == '__main__':
    app.start()
