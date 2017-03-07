import requests
import Paste
import time

from Pastebin import *
from QueueNG import *
import logging
from config import *
import os

class Site(object):

    def __init__(self):
        self.queue = QueueNG()

    def monitor(self):
        logging.info("Starting a new monitoring thread")

        #UNCOMMENT THIS
        self.get_paste_ids()

        # DEBUG: Test cases
        """
        test_paste_html = PastebinPaste("html")
        test_paste_bash = PastebinPaste("bash")
        test_paste_java = PastebinPaste("java")
        test_paste_blacklist = PastebinPaste("blacklist")
        test_paste_emails_creds = PastebinPaste("emailscreds")
        test_paste_onions_irc = PastebinPaste("onionsirc")
        test_paste_privkey = PastebinPaste("privkey")

        test_paste_html.site = "pastebin"
        test_paste_privkey.site = "pastebin"
        test_paste_bash.site = "pastebin"
        test_paste_java.site = "pastebin"
        test_paste_blacklist.site = "pastebin"
        test_paste_emails_creds.site = "pastebin"
        test_paste_onions_irc.site = "pastebin"
        """
        #test_paste_html.text =
        """
        <table border="0" cellspacing="0" width="290">
        <tbody>
        <tr>
        <td><strong>Name:</strong></td>
        <td>
        <p class="td">Isadora</p>
        </td>
        </tr>
        <tr>
        <td><strong>gender:</strong></td>
        <td>
        <p class="td">Female</p>
        </td>
        </tr>
        <tr>
        <td><strong>Age:</strong></td>
        <td>
        <p class="td">Twenty</p>
        </td>
        """

        #test_paste_bash.text =
        """
        #!/bin/sh
        rm /usr/share/info/dir
        for j in $( { for i in /usr/share/info/*.info /usr/share/info/*.gz; do echo "$i" | sed -r 's/-([0-9]+)\.gz$/\.gz/g'; done; } | uniq) ; do install-info "$j" /usr/share/info/dir; done
        """

        #test_paste_java.text =
        """
        import java.util.Scanner;
        public class mcmymcd {

        public static void main(String[] args) {
        // TODO Auto-generated method stub


        Scanner sc = new Scanner (System.in);
        String cadena = sc.nextLine ();
        String[] num = cadena.split(",");
        int mcd=Integer.parseInt(num[0]);
        int mcm=0;
        for (int i = 1; i < num.length; i++) {
            mcd = mcd(Integer.parseInt(num[i]),mcd);

        }

        for (int i = 0; i < num.length-1; i++) {
            mcm = mcm(Integer.parseInt(num[i]),Integer.parseInt(num[i+1]));
        }



        System.out.println("mcd = "+mcd);
        System.out.println("mcm = "+mcm);
        }
        }
        """

        #test_paste_blacklist.text =
        """border
        minecraft
        tuna
        carvings
        telephone
        whiteboard"""

        #test_paste_emails_creds.text =
        """   sanguinecarrion91186@yahoo.com:jason21
        lilisheree4u@yahoo.com:tiggelex
        angiemichael@yahoo.com:monsterangie
        servaasweijers@yahoo.com:examinanda
        indirageorge3@yahoo.com:maryjoe2710
        syukfenomena@yahoo.com:081089
        tehdoom@yahoo.com:timrocks
        bren21862@yahoo.com:bren
        lildevil-lildiva@yahoo.com:Aurther
        robertsont89@yahoo.com:kevin11606
        danijcbs@yahoo.com.br:daniel"""

        #test_paste_onions_irc.text =
        """asdjkj3jn2s.onion
        irc.freenode.net
        #security"""

        #test_paste_privkey.text =
        """
        -----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,4CA68B74C52A2C810E619898DFC596D8

rMqlDDQLyzLaF2xrjwRsiVsrTkWygx3/Dmr1rlCn5EBty5Ewi17UABQ4IQL1ZHom
h/xiL3fthSwqdSpJUfMgAi6OdWAh9ggi2kRFvf45T0MNhub6Rlmxhgix5gxiA0lS
G5y77FdXCl8joth2Q0+L3K39MRxga4rV5xvBzp5hDrJ+BBvZr0XMU9vFPl/aHa3u
m7mMRgJbSvS/KOwbv9jBFhnZsjRHmbWBoTfILQNNHnlhLqqgH0rN+jb3YWxSuFJB
LRc5kvGoP+p/cqEyOdiYkQn0YfU5G35emLkhQKYPgWy1hcJHdiwOjfvIkiugQThu
yGseNRontFoy2NzlFvxgpDp6waQO2Sdq6OKBniPx5p2nUy5seihoUKXtJQ5Nf+y6
KR73JfiXKqa3N6/QERXkxIiVZWrCcaYHml5t1EtlpnVyIn+EUfiIW4jA/sSKY9Jy
x7zhF+YmSXrWe2B8nE0IW5cR0Ua3jjqyePhzm3aS5/Lq7vKy0zRhPEVIuzyddBTO
vaqPLJ2fnF3kRRU3sevKpP08yeU2Oq6lF2hyXDPyObr+Zfq8UMn/uG7P5JgjjSw/
t7udi52JzkemNtfB8bIBTfbATNAzURXez5fBwyFQ+ZWRNfL8W4U9oKJyYPwRqEm/
pup8JxfbXJ1xVXEI4cWnJ3sopL1056UEzheMz2jNKTxPdMqpzj2Gi2G3DPH66tJg
VmSTskqknTMUisHSOBkkQgIwXZfUSbyhA+8zE80zr6DGQ3EyP86WExus4qkU4yfM
FMAPqzN/JWFoozbgbCWroZCshU6RSRu+hyDwagEP1XmP3GzFG3C5di37G/Jlfahb
xmnhgUE7+HuFhEtzPjT+/M81KqoxKjinxlDIuDOfqSeAec+Bn28C/ebpubRLeJmt
y7tpRx7JYHeWBcUFsHUPqXmBN+o2Flr1wbGTt/I66gAoDpOltJInJwQfEn1CUDL2
AY4F37HolJ2G10UTDTfZamVs/0kfbUH7hKJAvKjzvCWKRj1sa/BIjdaF0jTVFsUs
0kXbPjqQoXr8SMbu0sIhdgmsoBpuXLKYlLKE2g3FEmqUSBFbwKvX9rLC1fbOLSSF
s0KCJR4lnfkexD0n4SGVByEz/wmESt+6hD8ctK8VpxINWCgmATIIkeOnIH5spyd+
V+tvKIyiinCSCG3TylHXbJGDpdSAZqKl86CA9hD8jjG10A3eEo7h3l0Jt5+c2A0w
+fWi1Z+2gKOMSlWQ8hW8QfaR6pFnxnxTLGHXN1LY2NjP6axdCDWDRqMBmUbEAxUF
GylGFeELBnMbVC9yqrB387pWhhJmlr5osLOna4Xrx44Sj8nbvtF6UcPNSftpiQoE
XyZhWhtGkjdwN7rQ62oFKwPk2rROnVnN4Xgxf4CdcOZQeceIO6wAJwOXeyXNRJOw
NBKl9/L4wi0Af3fEG/8A6v+qsF9M4Wj78OC9BhNp/LymeLlVBBJJJdLP4RORv0XX
nDU7K23VWJzoyfURYCCVm4VjtmEbyZORDP1W1dpbuHEiH90VUQa6gPxBTXwl33+u
BB7fU+9X83T7Vm2DEmCNsTIuVHicj78GMY46wFye3JJPV9B/vK9Mn7TXeOkKicun
-----END RSA PRIVATE KEY-----
        """
        """
        self.queue.add(test_paste_privkey)
        self.queue.add(test_paste_onions_irc)
        self.queue.add(test_paste_emails_creds)
        self.queue.add(test_paste_blacklist)
        self.queue.add(test_paste_bash)
        self.queue.add(test_paste_html)
        self.queue.add(test_paste_java)
        """
        self.head = self.queue.peek()
        logging.debug("SEED set to %s" % self.head.id)

        #main loop
        while 1:
            logging.debug("Good morning!")
            #if we have items in the queue, process them
            while not self.queue.isEmpty():
                paste = self.queue.remove()

                paste.text = self.download_paste(paste.id)

                #logging.debug("------------------------------------------")
                #logging.debug(paste.text)
                #logging.debug("------------------------------------------")
                logging.debug("Sending paste {0} to matcher".format(paste.id))
                paste.match()
                if not paste.type:
                    logging.debug("Nothing interesting in paste {0}. Continuing".format(paste.id))
                    continue #paste is boring
                if paste.html >= threshhold_html:
                    logging.debug("Paste {0} was interesting, but reached HTML keyword threshhold".format(paste.id))
                    continue
                if paste.blacklist >= threshhold_blacklist:
                    logging.debug("Paste {0} was interesting, but reached blacklist keyword threshhold".format(paste.id))
                    continue
                if paste.crash_reports >= threshhold_crashreport:
                    logging.debug("Paste {0} was interesting, but reached crash report keyword threshhold".format(paste.id))
                    continue
                if paste.code_keywords >= threshhold_codekeyword:
                    logging.debug("Paste {0} was interesting, but reached code keyword threshhold".format(paste.id))
                    continue
                #paste is very interesting
                logging.info("Paste {0} from {1} has the following characteristics: {2}".format(paste.id, paste.site, paste.type))
                logging.debug("Saving paste {0} to file system".format(paste.id))

                # TODO: Logic for pastes with interesting keywords but has bad characteristics
                # (i.e. code but with API keys, HTML but with hashes, etc

                # MAKE SURE THIS WORKS ON LINUX
                folder = os.path.join("scraped_data", str(paste.site))
                if not os.path.exists(folder):
                    os.makedirs(folder)

                file = "{0}/{1}.txt".format(folder, paste.id)
                try:
                    with open(file, 'w') as paste_file:
                        if write_type_to_file:
                            paste_file.write("[*] {0}\n".format(paste.type))
                        paste_file.write(paste.text)
                        logging.debug("Wrote paste {0} to file system successfully".format(paste.id))
                except IOError as error:
                    logging.error("Error writing paste {0} to file {1}: Error code {3}".format(
                        paste.id, file, error))
                finally:
                    paste_file.close()

            #get new pastes. returns false if we got banned
            logging.debug("Searching for new pastes...")
            if self.get_paste_ids(lastID=self.head) == False:
                time.sleep(900)
            else:
                self.head = self.queue.peek()
                logging.debug("Setting watchpoint at %s" % self.head)
                logging.debug("Going to sleep")
                time.sleep(self.sleep)



#if __name__ == "__main__":
#    test = Site()
#    test.monitor()