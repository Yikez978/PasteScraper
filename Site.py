import logging
import requests
import Paste
import time
from QueueNG import *
from config import *
import os
from Pastebin import *

"""
Removes objects from the site's queue, and matches them against
a set of regexes for interesting characteristics. If the object
is considered "interesting" it is saved to disk
"""
class Site(object):

    def __init__(self):
        self.queue = QueueNG()
        self.logger = logging.getLogger(__name__)

    def monitor(self):
        self.logger.info("Starting a new monitoring thread")

        # PRODUCTION
        self.get_paste_ids()
        self.headID = self.queue.peek().id
        self.logger.debug("SEED set to %s" % self.headID)

        # DEBUG
        #example = PastebinPaste("abj43j4")
        #example.text = "test test"
        #self.queue.add(example)

        #main loop
        while 1:
            self.logger.debug("Good morning!")
            #if we have items in the queue, process them
            while not self.queue.isEmpty():
                paste = self.queue.remove()

                #paste.text = self.download_paste(paste.id)

                #self.logger.debug("Sending paste {0} to matcher".format(paste.id))
                paste.match()

                if not paste.type:
                    self.logger.debug("Nothing interesting in paste {0}. Continuing".format(paste.id))

                self.logger.info("Paste {0} from {1} has the following characteristics: {2}".format(paste.id, paste.site, paste.type))

                if len(paste.html) >= threshhold_html:
                    self.logger.debug("Paste {0} was interesting, but reached HTML keyword threshhold".format(paste.id))
                if len(paste.blacklist) >= threshhold_blacklist:
                    self.logger.debug("Paste {0} was interesting, but reached blacklist keyword threshhold".format(paste.id))
                if len(paste.crash_reports) >= threshhold_crashreport:
                    self.logger.debug("Paste {0} was interesting, but reached crash report keyword threshhold".format(paste.id))
                if len(paste.code_keywords) >= threshhold_codekeyword:
                    self.logger.debug("Paste {0} was interesting, but reached code keyword threshhold".format(paste.id))

                self.logger.debug("Paste {0} was interesting because of ".format(paste.id, paste.type))

                paste.save()

                # TODO: Logic for pastes with interesting keywords but has bad characteristics
                # (i.e. code but with API keys, HTML but with hashes, etc


            #get new pastes. returns false if we got banned
            self.logger.debug("Searching for new pastes...")
            if self.get_paste_ids(lastID=self.headID) == False:
                # not sure i need this line?
                #self.head = self.queue.peek().id
                time.sleep(900)
            else:
                self.headID = self.queue.peek().id
                self.logger.debug("Setting watchpoint at %s" % self.headID)
                self.logger.debug("Going to sleep")
                time.sleep(self.sleep)



#if __name__ == "__main__":
#    test = Site()
#    test.monitor()