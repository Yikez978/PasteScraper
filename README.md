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

MATCH IDEAS
* Get a better list of hacker groups
* Proxies?
* SQL injections/XSS (SQLI/XSS keywords). Maybe file inclusions
    * In addition to SQL keywords, maybe a match on id=<num>'
* "dox"
    * possible additional keywords: facebook, twitter, family,
* "greetz/greets"
* "compromise/dump/hack/target"
* ip addresses?
* mysql_connect (database connection strings)
* CREDIT CARDS
    * actual credit cards
    * "visa", "mastercard", "amex"
 * Bitcoin
    * Addresses
    * "BTC"


* Paste sites: Pastiebin, Slexy, Pastie, LodgeIt, YourPaste, Pastebay, FrubarPaste
Confirmed to be scraped by someone else
* None archived paste sites: Ghostbin, zerobin
    * Will require a rotating list of HTTP proxies to avoid being IP blocked. Another project for another day...
* LIST: https://inteltechniques.com/OSINT/pastebins.html (57 paste sites)
* LIST: https://blog.c22.cc/2012/02/28/quick-post-list-of-paste-sites/