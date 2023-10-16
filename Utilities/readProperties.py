import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+'\\Configuration\\config.ini',encoding='utf-8')

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url=(config.get('CommonInfo','baseURL'))
        return url

    @staticmethod
    def getUserEmail():
        username=(config.get('CommonInfo','email'))
        return username

    @staticmethod
    def getUserPwd():
        userpwd=(config.get('CommonInfo','password'))
        return userpwd



