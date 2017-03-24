This project is a fork of Jordan Wright's Dumpmon for twitter.

I've done some rewrites, removed Twitter functionality, and will be monitoring additional keywords of interest to me
I also plan on monitoring some additional sites (Dumpmon currently monitors pastebin, pastie, and slexy). This code can be easily repurposed to constantly monitor anything for interesting characteristics

Work is still in progress

TODO LIST
* Logic to weigh interesting characteristics against uninteresting characteristics
* We are looking for pastes with LARGE NUMBERS of emails, hashes, and credentials.
    A paste with 3 hashes probably not interesting
    A paste with <word>:<word> only occuring a few times probably isnt interesting
* Ability to add regexes/keywords live
* Statistics


SIMILAR PROJECTS
* Dumpmon
* https://www.pastemonitor.com/
    Watches pastebin
* https://twitter.com/Pastebindorks
* https://twitter.com/PastebinLeaks
* https://www.troyhunt.com/introducing-paste-searches-and/
* https://www.corelan.be/index.php/2011/03/22/pastenum-pastebinpastie-enumeration-tool/
* http://www.reversecurity.com/2011/05/dangers-of-pastebin-sites.html
*   csrc [aT_]reversecurity.com

KNOWN ISSUES
* private keys match against hashes
* userpass: needs to exclude urls (http://)
