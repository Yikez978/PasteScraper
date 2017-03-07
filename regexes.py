import re

regexes = {
    #personal information
    'email': re.compile(r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}', re.I),
    'ssn' : re.compile(r'\d{3}-?\d{2}-?\d{4}'),
    'phone' : re.compile(r'((\(?\d{3}\)? ?)|(\d{3}-?))?\d{3}-?\d{4}', re.I),

    #passwords, credentials, keys, api secrets
    'password': re.compile(r'password', re.I),
    'userpass': re.compile(r'\w{3,}:\w{5,}', re.I), #matches username:password patterns
    'hash32': re.compile(r'[^<A-F\d]([A-F\d]{32})[^A-F\d]', re.I),
    'cisco_hash': re.compile(r'enable\s+secret', re.I),
    'cisco_pass': re.compile(r'enable\s+password', re.I),
    'pgp_private': re.compile(r'BEGIN PGP PRIVATE', re.I),
    'ssh_private': re.compile(r'BEGIN RSA PRIVATE', re.I),
    'google_api': re.compile(r'\W(AIza.{35})'),
    'honeypot': re.compile(r'<dionaea\.capture>', re.I),

    #keyworks based on hacker groups
    'FFF': re.compile(r'FBI\s*Friday', re.I),  # will need to work on this to not match CSS
    'lulz': re.compile(r'(lulzsec|antisec)', re.I),
    'hackedby': re.compile(r'(hacked\s*by)', re.I),
    'anonymous': re.compile(r'anonymous', re.I),
    'cicada': re.compile(r'anonymous', re.I),

    #onion sites
    'onions': re.compile(r'(.*?\.onion)', re.I),

    #irc channels
    'irc_server': re.compile(r'irc\.[a-z0-9]{2,12}\.[a-z]{2,3}', re.I),
    'irc_channel': re.compile(r'(\#[a-z]+\b)(?!;)', re.I),

    'db_keywords': [
		re.compile(r'((customers?|email|users?|members?|acc(?:oun)?ts?)([-_|/\s]?(address|name|id[^")a-zA-Z0-9_]|[-_:|/\\])))', re.I),
        re.compile(r'((\W?pass(wor)?d|hash)[\s|:])', re.I),
        re.compile(r'((\btarget|\bsite)\s*?:?\s*?(([a-z][\w-]+:/{1,3})?([-\w\s_/]+\.)*[\w=/?%]+))', re.I),  # very basic URL check - may be improved later
        re.compile(r'(my\s?sql[^i_\.]|sql\s*server)', re.I),
        re.compile(r'((host|target)[-_\s]+ip:)', re.I),
        re.compile(r'(data[-_\s]*base|\Wdb)', re.I),  # added the non-word char before db.. we'll see if that helps
        re.compile(r'(table\s*?:)', re.I),
        re.compile(r'((available|current)\s*(databases?|dbs?)\W)', re.I),
    ],
    'html': [
        #re.compile(r'(<.+?>)', re.I), #HTML tags
        'px;',
        'container',
        '.Text',
        ':hover',
        'scroll',
        'text',
        'Button',
        'toggle',
    ],
    'timestamp': re.compile(r'((\d{1,2}|\d{4})[:-]\d{1,2}[:-](\d{4}|\d{1,2}))', re.I),
    'blacklist': [
		re.compile(r'(select\s+.*?from|join|declare\s+.*?\s+as\s+|update.*?set|insert.*?into)', re.I),  # SQL
        re.compile(r'(define\(.*?\)|require_once\(.*?\))', re.I),  # PHP
        re.compile(r'(function.*?\(.*?\))', re.I),
        re.compile(r'(Configuration(\.Factory|\s*file))', re.I),
        re.compile(r'((border|background)-color)', re.I),  # Basic CSS (Will need to be improved)
        re.compile(r'(Traceback \(most recent call last\))', re.I),
        re.compile(r'(java\.(util|lang|io))', re.I),
        re.compile(r'(sqlserver\.jdbc)', re.I),
        re.compile(r'minecraft', re.I),
    ],
    # crash reports
    'crash_reports': [
        re.compile(r'faf\.fa\.proxies', re.I),
        re.compile(r'Technic Launcher is starting', re.I),
        re.compile(r'OTL logfile created on', re.I),
        re.compile(r'RO Game Client crashed!', re.I),
        re.compile(r'Selecting PSO2 Directory', re.I),
        re.compile(r'TDSS Rootkit', re.I),
        re.compile(r'SysInfoCrashReporterKey', re.I),
        re.compile(r'Current OS Full name: ', re.I),
        re.compile(r'Multi Theft Auto: ', re.I),
        re.compile(r'Initializing cgroup subsys cpuset', re.I),
        re.compile(r'Init vk network', re.I),
        re.compile(r'MediaTomb UPnP Server', re.I),
        re.compile(r'#EXTM3U\n#EXTINF:', re.I)
    ],

    #code
    'code': [
        'for(',
        'while(',
        '){',
        ') {',
        'if(',
        'else(',
        'for (',
        'while (',
        'if (',
        'else (',
        '++',
        ');',
        '==',
        'i=0;',
        'j=0;',
        '()',
        'jenkins',
        'unstable',
        'unknown',
        'Unknown',
        'func',
        'invoke',
        'Native',
        'u32(',
        'pointer',
    ]
}