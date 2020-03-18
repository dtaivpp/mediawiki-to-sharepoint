from shareplum import Site
from shareplum import Office365
from shareplum.site import Version


def _authenticate(_sharpoint_url: str, _username: str, _password: str):
    '''Returns Auth Cookie'''
    try:
        _cookie = Office365(_sharepoint_url, username=_username, password=_password).GetCookies()
        return _cookie
    except:
        raise Exception("Error Authenticating")

def _site_creation(_sharepoint_url: str, _username: str, _password: str):
    '''Returns Sharepoint Site Object'''
    _authcookie = authenticate(_sharepoint_url, _username, _password)

    try 
        _site = Site(_sharepoint_url, version=Version.v2016, authcookie=_authcookie)
        return _site
    except: 
        raise Exception("Unable to create site with provided token")

def create_list():
    pass

def get_list():
    pass

def get_list_items():
    pass

def upload_changes():
    pass

