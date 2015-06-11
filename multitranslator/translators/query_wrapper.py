import pycurl
import json
from urllib import urlencode
import cStringIO
from error_codes import *

hdr = cStringIO.StringIO()

class Buffer:
    """
    Store the response of a callback

    """
    def __init__(self):
        self.content = ''
    def callback(self, buf):
        """
        Stores buf

        :param buf: The response of an HTTP call
        :type buf: string

        """
        self.content = buf

class JSONBuffer(Buffer):
    """
    Store the JSON response of a callback and tries to dump it in a dictionary

    """
    def callback(self, buf):
        """
        Store buf and tries to load it in a dictionary.
        If the response can't be parsed, the content will be a void string

        :param buf:
        :type buf: JSON string

        """
        try:
            self.content = json.loads(buf)
        except:
            self.content = ''

def do_get(endpoint, params, headers, callback, con_timeout=10, timeout=10):
    """
    Perform an HTTP call using the GET method

    :param endpoint: The URL where the call is done
    :type endpoint: string
    :param params: The parameters that will be added in the URL
    :type params: dictionary, keys and values must be string
    :param headers: HTTP headers used for the call, for example, the content-type and the agent
    :type headers: List of string
    :param callback: The function that will receive the response
    :type callback: function
    :param con_timeout: Number of seconds to disconnect if the server doesn't respond
    :type con_timeout: int
    :param timeout: Number of seconds to disconnect if the connection is interrupted
    :type timeout: int
    :return: The response code of the call
    :rtype: int

    """
    try:
        c = pycurl.Curl()
        c.setopt(pycurl.URL, endpoint + urlencode(params))
        c.setopt(pycurl.CONNECTTIMEOUT, con_timeout)
        c.setopt(pycurl.TIMEOUT, timeout)
        c.setopt(pycurl.HTTPHEADER, headers)
        c.setopt(pycurl.HEADERFUNCTION, hdr.write)
        c.setopt(c.WRITEFUNCTION, callback)
        c.perform()
        response_code = c.getinfo(pycurl.HTTP_CODE)
        c.close()
        return response_code
    except:
        return TIMEOUT

def do_post(endpoint, postfields, headers, callback, encode=True, con_timeout=10, timeout=10):
    """
    Perform an HTTP call using the POST method

    :param endpoint: The URL where the call is done
    :type endpoint: string
    :param postfields: The post data that will be sent
    :type postfields: if encode is True: dictionary, keys and values must be string, else: string
    :param headers: HTTP headers used for the call, for example, the content-type and the agent
    :type headers: List of string
    :param callback: The function that will receive the response
    :type callback: function
    :param encode: Encode the post fields into the post data, otherwise, post fields are a unique string
    :type encode: bool
    :param con_timeout: Number of seconds to disconnect if the server doesn't respond
    :type con_timeout: int
    :param timeout: Number of seconds to disconnect if the connection is interrupted
    :type timeout: int
    :return: The response code of the call
    :rtype: int

    """
    try:
        c = pycurl.Curl()
        c.setopt(pycurl.URL, endpoint)
        c.setopt(pycurl.CONNECTTIMEOUT, con_timeout)
        c.setopt(pycurl.TIMEOUT, timeout)
        c.setopt(pycurl.HTTPHEADER, headers)
        c.setopt(pycurl.POST, 1)
        c.setopt(pycurl.POSTFIELDS, urlencode(postfields) if encode else postfields)
        c.setopt(c.HEADERFUNCTION, hdr.write)
        c.setopt(c.WRITEFUNCTION, callback)
        c.perform()
        response_code = c.getinfo(pycurl.HTTP_CODE)
        c.close()
        return response_code
    except:
        return TIMEOUT