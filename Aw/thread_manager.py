# -*- coding:utf-8 -*-
import threading


class ThreadManager(object):
    instance = None
    def __init__(self):
        self.thread_dict = {}

    @staticmethod
    def get_instance():
        if ThreadManager.instance is None:
            ThreadManager.instance = ThreadManager()
        return ThreadManager.instance

    @staticmethod
    def run(self, func_name, params, title):
        manager = ThreadManager.get_instance()
        if title not in manager.thread_dict:
            t = threading.Thread(target=func_name, args=params)
            manager.thread_dict[title] = t
        item = manager.thread_dict[title]
        item.setDadmon()
        item.join()
        item.start()

