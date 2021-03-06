# -*- coding: utf-8 -*-

from module.plugins.internal.SimpleCrypter import SimpleCrypter


class FilecloudIoFolder(SimpleCrypter):
    __name__ = "FilecloudIoFolder"
    __type__ = "crypter"
    __version__ = "0.02"

    __pattern__ = r'https?://(?:www\.)?(filecloud\.io|ifile\.it)/_\w+'

    __description__ = """Filecloud.io folder decrypter plugin"""
    __license__ = "GPLv3"
    __authors__ = [("Walter Purcaro", "vuolter@gmail.com")]


    LINK_PATTERN = r'href="(http://filecloud\.io/\w+)" title'
    TITLE_PATTERN = r'>(.+?) - filecloud\.io<'
