# in questo documento troviamo tutte le funzioni utili per estrarre le feature dagli Url 



import requests as req
from datetime import datetime
from dateutil import parser
import tldextract
import re
from IPy import IP
from urllib.parse import urlparse 
from tld.exceptions import TldDomainNotFound
from tld.exceptions import TldBadUrl


#ritorna il numero di anni mancanti alla fine della registrazione del dominio 
def yearsFromExpiration(url):
    #bisogna controllare prima se l 'host name è un ip perchè mette un punto di troppo

    result = tldextract.extract(url)
    domain = result.domain +"."+result.suffix
    print("richiesta fatta al dominio "+domain)
    resp = req.get("https://www.whatsmydns.net/api/domain?q="+domain)
    json = resp.json()
    # expires is in ISO-8601 
    expires = json["data"]["expires"]
    
    if expires is None: 
        print ("data non disponibile")
        return None
    else:
        dateOfExpiration = datetime.fromisoformat(expires).date()
        now = datetime.now().date()
        yearsOnline = int(dateOfExpiration.strftime("%Y")) - int(now.strftime("%Y"))
        print("risultato--->",yearsOnline)
        return yearsOnline

def isIP(url):
    match = re.search(
        '(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.'
        '([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\/)|'  # IPv4
        '(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.'
        '([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\/)|'  # IPv4 with port
        '((0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\/)' # IPv4 in hexadecimal
        '(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}|'
        '([0-9]+(?:\.[0-9]+){3}:[0-9]+)|'
        '((?:(?:\d|[01]?\d\d|2[0-4]\d|25[0-5])\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d|\d)(?:\/\d{1,2})?)', url)  # Ipv6
    if match:
        return 1
    else:
        return 0

def urlLenght(url):
    if "http://" in url:
        url = url.replace('http://', '')
    if "https://" in url:
        url = url.replace('https://', '')
    return len(url)

def usingShortiningServ(url):
    match = re.search('shorte\.st|go2l\.ink|\/t\.co|cli\.gs|yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|lnkd\.in|db\.tt|qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|q\.gs|is\.gd|po\.st|bc\.vc|twitthis\.com|\/u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|tr\.im|link\.zip\.net|wgc7\.2\.vu|cutt\.ly',
                      url)
    if match:
        return 1
    else:
        return 0

    

def numberOfDash(url):
    if "http://" in url:
        url = url.replace('http://', '')
    if "https://" in url:
        url = url.replace('https://', '')
    return url.count("-")

def numberOfAt(url):
    if "http://" in url:
        url = url.replace('http://', '')
    if "https://" in url:
        url = url.replace('https://', '')
    return url.count("@")

def numberOfQM(url):
    if "http://" in url:
        url = url.replace('http://', '')
    if "https://" in url:
        url = url.replace('https://', '')
    return url.count("?")

def numberOfAmpersand(url):
    if "http://" in url:
        url = url.replace('http://', '')
    if "https://" in url:
        url = url.replace('https://', '')
    return url.count("&")

def numberOfVS(url):
    if "http://" in url:
        url = url.replace('http://', '')
    if "https://" in url:
        url = url.replace('https://', '')
    return url.count("∣")

def numberOfEqual(url):
    if "http://" in url:
        url = url.replace('http://', '')
    if "https://" in url:
        url = url.replace('https://', '')
    return url.count("=")

def numberOfUnderscore(url):
    if "http://" in url:
        url = url.replace('http://', '')
    if "https://" in url:
        url = url.replace('https://', '')
    return url.count("_")

def numberOfTilde(url):
    if "http://" in url:
        url = url.replace('http://', '')
    if "https://" in url:
        url = url.replace('https://', '')
    return url.count("˜")


def numberOfPercente(url):
    if "http://" in url:
        url = url.replace('http://', '')
    if "https://" in url:
        url = url.replace('https://', '')
    return url.count("%")

def numberOfAsterisc(url):
    if "http://" in url:
        url = url.replace('http://', '')
    if "https://" in url:
        url = url.replace('https://', '')
    return url.count("*")

def numberOfDollar(url):
    if "http://" in url:
        url = url.replace('http://', '')
    if "https://" in url:
        url = url.replace('https://', '')
    return url.count("$")

def numberOfSemiColons(url):
    if "http://" in url:
        url = url.replace('http://', '')
    if "https://" in url:
        url = url.replace('https://', '')
    return url.count(";")

def numberOfColons(url):
    if "http://" in url:
        url = url.replace('http://', '')
    if "https://" in url:
        url = url.replace('https://', '')
    return url.count(":")

#single quote
def numberOfSQ(url):
    if "http://" in url:
        url = url.replace('http://', '')
    if "https://" in url:
        url = url.replace('https://', '')
    return url.count("'")



def dashInDomOrSub(url):
    str= tldextract.extract(url).subdomain +"."+ tldextract.extract(url).domain
    if "-" in str:
        return 1
    else:
        return 0

def details(url):
    print("DOMAIN -->" +tldextract.extract(url).domain)
    print("SUBDOMAIN -->" +tldextract.extract(url).subdomain)
    print("SUFFIX -->" +tldextract.extract(url).suffix)

def httpsInDomOrSub(url):
    str= tldextract.extract(url).subdomain +"."+ tldextract.extract(url).domain
    if "https" in str:
        return 1
    else:
        return 0

#la durate in anni di quanto è vissuto il dominio
def ageOfDomain(url):
    result = tldextract.extract(url)
    domain = result.domain +"."+result.suffix
    print("richiesta fatta al dominio "+domain)
    resp = req.get("https://www.whatsmydns.net/api/domain?q="+domain)
    json = resp.json()
    # expires is in ISO-8601 
    created = json["data"]["created"]
    
    if created is None: 
        print ("data non disponibile")
        return None
    else:
        dateOfCreation = datetime.fromisoformat(created).date()
        now = datetime.now().date()
        yearsOnline = int(now.strftime("%Y")) - int(dateOfCreation.strftime("%Y"))
        return yearsOnline


def pageRank(url):
    serviceUrl = 'https://checkpagerank.net/check-page-rank.php'
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    
    data = {"name": "sandalychacosklep.com"}
 
    response = req.post(serviceUrl, headers=headers,data=data)
    print("Status Code", response.status_code)
    print(response.text)

    #extract useful information
    s = 'Google PageRank:</b></font> <font color="#000099"><b>'
    start = response.text.find(s) + len(s)
    end = response.text.find("/10", start)
    ran = response.text[start:end]
    print(ran)

#ritorna 1 se nella nel link è presente la porta 0 altrimenti
def port(url):
    newUrl = urlparse(url)
    if newUrl.port is None:
        return 0
    else:
        return 1

#controlla se nella path ci sono temini pericolosi come: 'txt’, ‘exe’, ‘js’ 

from re import search

def checkPath(url):
    newUrl = urlparse(url)
    if search(".txt",newUrl.path) or search(".js",newUrl.path) or search(".exe",newUrl.path):
        return 1
    else:
        return 0

#ritorna il numero di sottodomini 
def numberSub(url):
    sub = tldextract.extract(url).subdomain
    numberOfSub = sub.count(".") + 1
    return numberOfSub

#non fatto
from tld import get_tld
def checkTLD(url):
    tld = get_tld(url) 
    print("tld ="+tld)
    serviceUrl = "https://www.spamhaus.org/statistics/checktld/"
    response = req.get(serviceUrl+tld)
    print(response.text)

def lenghtDom(url):
    return len(tldextract.extract(url).domain)
    
def lenghtSub(url):
    return len(tldextract.extract(url).subdomain)

def lenghtPath(url):
    newUrl = urlparse(url)
    path = newUrl.path
    path = path.replace('/', '')
    return len(path)

def numberOfLetters(url):
    letters = sum(c.isalpha() for c in url)
    return letters

def numberOfDigits(url):
    numbers = sum(c.isdigit() for c in url)
    return numbers

def usingPunycode(url):
    if search("xn--",url):
        return 1
    else: 
        return 0

def suspiciousWords(url):
    match = re.search('PayPal|login|signin|bank|account|update|free|lucky|service|bonus|ebayisapi|webscrAlert|Bank|Bill|Billing|Card|Charge|Check|Client|Contact|Customer|Debit|Deposit|Email|Financial|Information|Invoice|Issue|Notice|Pay|Payment|Phone|Receipt|Record|Refund|Removal|Request|Reset|Security|Service|Statement|Subscription|Support|Technical|Transaction|Transfer|Verification|Warning|Web|Website|Access|Action|Activate|Address|Admin|Administrator|Advice|Alert|Api|App|Application|Attention|Authenticate|Authentication|Authorize|Authorized|Banking|Beneficiary|Bill|Billing|Block|Branch|Business|Buy|Cancel|Cancellation|Card|Care|Certificate|Change|Charge|Check|Client|Closed|Code|Commercial|Company|Contact|Contacts|Contacts|Contract|Copy|Corporate|Country|Credit|Currency|Customer|Data|Database|Date|Debit|Default|Deliver|Delivery|Department|Deposit|Description|Design|Device|Director|Disabled',url)
    if match:
        return 1
    else:
        return 0

def checkHttps(url):
    protocol = url[0:5]
    if "http" not in protocol:
        #allora questo particolare url non ha informazione riguardo il protocollo quindi ritorna Null
        return None
    elif "https" in protocol:
        return 1
    else:
        return 0


def getDomain(url):
    return tldextract.extract(url).domain +"."+tldextract.extract(url).suffix


def hasEmail(url):
    pattern = '[\w\.-]+@[\w\.-]+\.[\w\.-]+'
    if re.search(pattern, url):
        return 1
    return 0


def checkTLD(url):
    try:
        tld = get_tld(url)
        match = re.search("surf|ml|live|beauty|top|cn|fit|gq|cf|degree|xyz|ga|tk",tld)
        if match:
            return 1
        else:
            return 0
    except TldBadUrl: 
        return 0
    except TldDomainNotFound:
        #print("TldDomainNotFound -->",url)
        return 0