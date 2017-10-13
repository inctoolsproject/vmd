# -*- coding: utf-8 -*-
class LineCallback(object):

    def __init__(self, callback):
        self.callback = callback

    def Pinverified(self, pin):
        self.callback("Masukkan Kode Pin '" + pin + "' Ke Smartphone-mu Dalam 2 Menit")

    def QrUrl(self, url):
        self.callback("Login Dengan Kode QR Dalam 2 Menit\n" + url)

    def default(self, str):
        self.callback(str)
