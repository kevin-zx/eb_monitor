# -*- coding: utf8 -*-
import threading
from store.store_mysql import StoreMysql


class eb_cookie_util(object):

    def __init__(self):
        self.threadlock = threading.Lock()
        self.cookie_list = {}
        self.db = StoreMysql(host="115.159.3.51", user="remote", password="Iknowthat", db="Tmall")
        pass

    def get(self, cookie_type):
        if cookie_type == "tmall":
            self.get_cookie(1)
        if cookie_type == "taobao":
            self.get_cookie(2)
        if cookie_type == "tmall_h5":
            self.get_cookie(3)
        if cookie_type == "JD":
            self.get_cookie(4)

    def get_cookie(self, cookie_type_id):
        cookie = ""
        self.threadLock.acquire()
        if(len(self.cookie_list[cookie_type_id])) < 0:
            self.init_cookie(cookie_type_id)
        else:
            cookie = self.cookie_list[cookie_type_id][0]
            self.cookie_list[cookie_type_id].remove(0)
        self.threadLock.release()
        return cookie

    def init_cookie(self, cookie_type_id):
        cookies = self.db.query("SELECT cookie_str FROM cookie_store WHERE type = {0} ORDER BY id DESC LIMIT 100".format(cookie_type_id))
        self.cookie_list[cookie_type_id] = []
        for cookie in cookies:
            self.cookie_list[cookie_type_id].append(cookie[0])


def main():
    ecu = eb_cookie_util()
    ecu.init_cookie()
    pass

if __name__ == '__main__':
    main()

