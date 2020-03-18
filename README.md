# MediaWiki to SharePoint

This is a simple script that will programatically send updates from MediaWiki to a SharePoint list for indexing. 

### Developing  

1. Clone the repo `git clone https://github.com/dtaivpp/mediawiki-to-sharepoint.git`
2. Create a .env file in the root of your project with the following lines:
    - `SHAREPOINT_USER="someuser@mail.com"`
    - `SHAREPOINT_PASS="APa55w0rd!!"`
3. Create a virtual environment (best practice but could be ignored) `python -m venv venv`
4. Source to that directory  
    - Windows: `.\venv\Scripts\Activate.ps1` (or .bat if you are using cmd)
    - Unix Base Systems: `source venv/bin/activate`
5. Install requirements.txt `python -m pip install -r requirements.txt`

#### Proposed Sharepoint List Format
| Site URL         | Title   | Contents  |
| ---------------- | ------- | --------- |
| http://agiwiki   | "Title" | "Content" |