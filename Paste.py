from re import match

import logging

from regexes import *

class Paste(object):

    def __init__(self):
        #body of text
        self.text = ""
        #metadata
        self.type = []
        self.site = ""

        # personal information
        self.emails = 0
        self.ssn = 0
        self.phone = 0

        # passwords, credentials, keys, api secrets
        self.password = 0
        self.userpass = 0
        self.hashes = 0
        self.cisco_hash = 0
        self.cisco_pass = 0
        self.pgp = 0
        self.ssh_key = 0
        self.google_api = 0
        self.honeypot = 0

        #hacker groups
        self.FFF = 0
        self.lulz = 0
        self.hackedby = 0
        self.anonymous = 0
        self.cicada = 0

        self.onions = 0

        self.irc = 0

        self.db = 0

        self.html = 0
        self.timestamp = 0
        self.blacklist = 0
        self.crash_reports = 0
        self.code_keywords = 0

    #search paste for interesting key words, and assign a score based on what was found
    def match(self):
        self.emails = list(set(regexes['email'].findall(self.text)))
        self.ssn = list(set(regexes['ssn'].findall(self.text)))
        self.phone = list(set(regexes['phone'].findall(self.text)))
        if self.emails or self.ssn or self.phone:
            self.type.append("PII")

        self.password = list(set(regexes['password'].findall(self.text)))
        self.userpass = list(set(regexes['userpass'].findall(self.text)))
        self.hashes = list(set(regexes['hash32'].findall(self.text)))
        if self.password or self.userpass or self.hashes:
            self.type.append("passwords")

        self.cisco_hash = list(set(regexes['cisco_hash'].findall(self.text)))
        self.cisco_pass = list(set(regexes['cisco_pass'].findall(self.text)))
        if self.cisco_pass or self.cisco_pass:
            self.type.append("cisco")

        self.pgp = list(set(regexes['pgp_private'].findall(self.text)))
        self.ssh_key = list(set(regexes['ssh_private'].findall(self.text)))
        self.google_api = list(set(regexes['google_api'].findall(self.text)))
        if self.pgp or self.ssh_key or self.google_api:
            self.type.append("key")

        self.honeypot = list(set(regexes['honeypot'].findall(self.text)))
        if self.honeypot:
            self.type.append("honeypot")

        self.FFF = list(set(regexes['FFF'].findall(self.text)))
        self.lulz = list(set(regexes['lulz'].findall(self.text)))
        self.hackedby = list(set(regexes['hackedby'].findall(self.text)))
        self.anonymous = list(set(regexes['anonymous'].findall(self.text)))
        self.cicada = list(set(regexes['cicada'].findall(self.text)))
        if self.FFF or self.lulz or self.hackedby or self.anonymous or self.cicada:
            self.type.append("hacker")

        self.onions = list(set(regexes['onions'].findall(self.text)))
        if self.onions:
            self.type.append("onion")

        self.irc = list(set(regexes['irc_channel'].findall(self.text))) #also finds hashtags and python comments :)
        self.irc = list(set(regexes['irc_server'].findall(self.text)))
        if self.irc:
            self.type.append("irc")

        for regex in regexes['db_keywords']:
            if regex.search(self.text):
                #logging.debug("Paste {0} matching database keyword: %s".format(self.id, regex.search(self.text)))
                self.db += 1
            #print("Match on %r" % regex)
        if self.db > 0:
            self.type.append("db")

        for item in regexes['html']:
            if item in self.text:
                #logging.debug("Paste {0} matching HTML keyword: {1]".format(self.id, item))
                self.html += 1

        self.timestamp = len(list(set(regexes['irc_channel'].findall(self.text))))

        for regex in regexes['blacklist']:
            if regex.search(self.text):
                #logging.debug("Paste {0} matching blacklist keyword: {1]".format(self.id, regex.search(self.text)))
                self.blacklist += 1

        for regex in regexes['crash_reports']:
            if regex.search(self.text):
                #logging.debug("Paste {0} matching crash_report keyword: {1]".format(self.id, regex.search(self.text)))
                self.crash_reports += 1

        for keyword in regexes['code']:
            if keyword in self.text:
                #logging.debug("Paste {0} matching code keyword: {1]".format(self.id, regex.search(self.text)))
                self.code_keywords += 1