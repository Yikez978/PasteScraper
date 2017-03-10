import os
from re import match
import logging

from config import write_type_to_file
from regexes import *

class Paste(object):

    def __init__(self):
        self.logger = logging.getLogger(__name__)

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

        self.db = []

        self.html = []
        self.timestamp = 0
        self.blacklist = []
        self.crash_reports = []
        self.code_keywords = []

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
            match = regex.search(self.text)
            if match:
                self.db.append(match.group())
        if self.db:
            self.logger.debug("Paste {0} matching database keyword: {1}".format(self.id, self.db))
        if len(self.db) > 0:
            self.type.append("db")

        for item in regexes['html']:
            if item in self.text:
                self.html.append(item)
        if self.html:
            self.logger.debug("Paste {0} matching HTML keywords: {1}".format(self.id, self.html))


        self.timestamp = len(list(set(regexes['irc_channel'].findall(self.text))))

        for regex in regexes['blacklist']:
            match = regex.search(self.text)
            if match:
                self.blacklist.append(match.group())
        if self.blacklist:
            self.logger.debug("Paste {0} matching blacklist keywords {1}"
                              .format(self.id, self.blacklist))

        for regex in regexes['crash_reports']:
            match = regex.search(self.text)
            if match:
                self.crash_reports.append(match.group())
        if self.crash_reports:
            self.logger.debug("Paste {0} matching crash_report keywords {1}"
                                .format(self.id, self.crash_reports))


        for keyword in regexes['code']:
            if keyword in self.text:
                self.code_keywords.append(keyword)
        if self.code_keywords:
            self.logger.debug("Paste {0} matching code keywords {1}".format(self.id, self.code_keywords))

    def save(self):
        # MAKE SURE THIS WORKS ON LINUX
        folder = os.path.join("scraped_data", str(self.site))
        if not os.path.exists(folder):
            os.makedirs(folder)

        file = "{0}/{1}.txt".format(folder, self.id)
        try:
            with open(file, 'w') as paste_file:
                if write_type_to_file:
                    paste_file.write("[*] {0}\n".format(self.type))
                paste_file.write(self.text)
                self.logger.debug("Wrote paste {0} to file system successfully".format(self.id))
        except IOError as error:
            self.logger.error("Error writing paste {0} to file {1}: Error code {3}".format(
                self.id, file, error))
        finally:
            paste_file.close()
