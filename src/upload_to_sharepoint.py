from shareplum import Site
from shareplum import Office365
from shareplum.site import Version
from settings import Sharepoint_Pass, Sharepoint_User, Sharepoint_Url

# Example
# https://shareplum.readthedocs.io/en/latest/tutorial.html#update-list-data


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

def  _list_doesnt_exist(site, list_name):
    sp_lists = site.get_list_collection()

    if sp_lists.get(list_name) == None:
        return True

    return False

def create_list():
    pass

def get_list():
    pass

def get_list_items():
    pass

def upload_changes():
    pass


if __name__=="__main__":
    # Use local variables for auth.
    SP_Site = _site_creation(Sharepoint_Url, Sharepoint_User, Sharepoint_Pass)
    List_Name = "WikiMedia"

    if _list_doesnt_exist(List_Name):
        create_list("WikiMedia")