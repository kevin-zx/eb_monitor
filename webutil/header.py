# -*- coding: utf-8 -*-


class header(object):
    """
    headers class, this class combine headers for webGeter
     headers( User_Agent = None, Cookie = None, Accept = None, Accept_Encoding = None, 
     Accept_Language = None,Connection = None, Host = None, Referer = None, 
     X_Requested_With = None, other = {})
     User_Agent,Cookie,Accept,etc. parameters is normal headers for request   
     if you have some other headers properties you can use other param to add them
    """
    headers = {}

    def __init__(self, user_agent=None, cookie=None, accept=None, accept_encoding=None, accept_language=None,
                 connection=None, host=None, referer=None, x_requested_with=None, other={}):
        """
        Constructor
        """
        self.set_header_item("User-Agent", user_agent)
        self.set_header_item("Cookie", cookie)
        self.set_header_item("Accept", accept)
        self.set_header_item("Accept-Encoding", accept_encoding)
        self.set_header_item("Accept-Language", accept_language)
        self.set_header_item("Connection", connection)
        self.set_header_item("Host", host)
        self.set_header_item("Referer", referer)
        self.set_header_item("X_Requested_With", x_requested_with)
        if other is None or len(other) == 0:
            return
        else:
            self.headers.update(other)
    
    def __str__(self):
        return self.headers.__str__()

    def set_header_item(self, item_name, item_value):
        if item_value is not None and item_name is not None:
            self.headers[item_name] = item_value
