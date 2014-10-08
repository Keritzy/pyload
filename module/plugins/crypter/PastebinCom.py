# -*- coding: utf-8 -*-

from module.plugins.internal.SimpleCrypter import SimpleCrypter


class PastebinCom(SimpleCrypter):
    __name__ = "PastebinCom"
    __type__ = "crypter"
    __version__ = "0.02"

    __pattern__ = r'http://(?:www\.)?pastebin\.com/\w+'

    __description__ = """Pastebin.com decrypter plugin"""
    __license__ = "GPLv3"
    __authors__ = [("stickell", "l.stickell@yahoo.it")]


    LINK_PATTERN = r'<div class="de\d+">(https?://[^ <]+)(?:[^<]*)</div>'
    TITLE_PATTERN = r'<div class="paste_box_line1" title="([^"]+)">'
