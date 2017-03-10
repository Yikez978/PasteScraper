import requests
from bs4 import BeautifulSoup
from Site import Site
from Paste import Paste
from config import pastebin_sleeptime
from config import pastebin_url
from config import pastebin_blocked
from config import user_agent
import logging

class PastebinPaste(Paste):
    def __init__(self, id):
        self.logger = logging.getLogger(__name__)
        self.id = id
        self.url = 'http://pastebin.com/raw/' + self.id
        super(PastebinPaste, self).__init__()

class Pastebin(Site):
    def __init__(self):
        self.BASE_URL = pastebin_url
        self.PATH = "archive"
        self.sleep = pastebin_sleeptime
        self.user_agent = user_agent
        super(Pastebin, self).__init__()

    #get new paste IDs and add them to the queue
    #returns false if banned
    def get_paste_ids(self, lastID=None):
        #request archive
        self.logger.info('Retrieving Pastebin IDs from site')
        r = requests.get("{0}{1}".format(self.BASE_URL, self.PATH), headers={"User-Agent": self.user_agent})
        if pastebin_blocked in r.text:
            self.logger.error("Pastebin blocked your IP! Sleeping for 15 minutes. You might want to check your config and increase sleep time for the site")
            return False

        soup = BeautifulSoup(r.text, "html.parser")

        paths = [a.get('href') for a in (td.find('a') for td in soup.findAll('td')) if a] #get hrefs within tds
        paths = [item for item in paths if not "archive" in item] #remove some false positives
        paths = [item[1:].encode('ascii') for item in paths] #make it ascii, remove the slash

        self.logger.debug("Retrieved the following: : %s" % paths)
        self.logger.debug("Preparing to add to queue until we see paste %s" % lastID)
        for id in paths:
            paste = PastebinPaste(id)
            if lastID == paste.id:
                self.logger.debug("Breaking because we saw %s, which was on our last grab" %
                                  lastID)
                break
            paste.site = "pastebin"
            self.queue.add(paste)
            self.logger.debug("Found new ID %s (not %s)" % (id, lastID))

    def download_paste(self, paste_id):
        self.logger.debug("Downloading Pastebin ID %s" % paste_id)
        r = requests.get("{0}{1}".format(pastebin_url, paste_id), headers={"User-Agent": user_agent})
        return r.text
