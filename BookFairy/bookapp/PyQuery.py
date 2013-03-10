Last login: Thu Nov 15 17:25:37 on ttys005
Michelles-MacBook-Pro-2:~ michelleglauser$ cd ..
Michelles-MacBook-Pro-2:Users michelleglauser$ ls
Shared      michelleglauser
Michelles-MacBook-Pro-2:Users michelleglauser$ cd michelleglauser/
Michelles-MacBook-Pro-2:~ michelleglauser$ ls
Applications        Networking.txt      personal_chef.rb
Desktop         Pictures        personal_chef_final.rb
Documents       Public          projects
Downloads       RubyForBeginners.rb railsbridge
Google Drive        anna            ruby_fun
Guy.rb          cd          temp
HelloRubyTuesdays   ex12.txt        test_app
Library         ex13.txt        untitled text 2.txt
Movies          hello.rb        untitled text 3.txt
Music           jinja2          who_was_it
My Cubby        moviefiles.txt
Michelles-MacBook-Pro-2:~ michelleglauser$ cd Desktop/
Michelles-MacBook-Pro-2:Desktop michelleglauser$ python
Python 2.7.1 (r271:86832, Jun 16 2011, 16:59:05) 
[GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2335.15.00)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named requests
>>> pip install requests
  File "<stdin>", line 1
    pip install requests
              ^
SyntaxError: invalid syntax
>>> 
KeyboardInterrupt
>>> ^D
Michelles-MacBook-Pro-2:Desktop michelleglauser$ pip install requests
Downloading/unpacking requests
  Downloading requests-0.14.2.tar.gz (361kB): 361kB downloaded
  Running setup.py egg_info for package requests
    
    warning: no files found matching 'tests/*.'
Installing collected packages: requests
  Running setup.py install for requests
    
    warning: no files found matching 'tests/*.'
    error: could not create '/Library/Python/2.7/site-packages/requests': Permission denied
    Complete output from command /usr/bin/python -c "import setuptools;__file__='/var/folders/z_/0j8qytyj02dgmh8xjjgdvlk00000gn/T/pip-build/requests/setup.py';exec(compile(open(__file__).read().replace('\r\n', '\n'), __file__, 'exec'))" install --record /var/folders/z_/0j8qytyj02dgmh8xjjgdvlk00000gn/T/pip-UJHcYg-record/install-record.txt --single-version-externally-managed:
    running install

running build

running build_py

creating build

creating build/lib

creating build/lib/requests

copying requests/__init__.py -> build/lib/requests

copying requests/_oauth.py -> build/lib/requests

copying requests/adapters.py -> build/lib/requests

copying requests/api.py -> build/lib/requests

copying requests/async.py -> build/lib/requests

copying requests/auth.py -> build/lib/requests

copying requests/certs.py -> build/lib/requests

copying requests/compat.py -> build/lib/requests

copying requests/cookies.py -> build/lib/requests

copying requests/defaults.py -> build/lib/requests

copying requests/exceptions.py -> build/lib/requests

copying requests/hooks.py -> build/lib/requests

copying requests/models.py -> build/lib/requests

copying requests/safe_mode.py -> build/lib/requests

copying requests/sessions.py -> build/lib/requests

copying requests/status_codes.py -> build/lib/requests

copying requests/structures.py -> build/lib/requests

copying requests/utils.py -> build/lib/requests

creating build/lib/requests/packages

copying requests/packages/__init__.py -> build/lib/requests/packages

creating build/lib/requests/packages/urllib3

copying requests/packages/urllib3/__init__.py -> build/lib/requests/packages/urllib3

copying requests/packages/urllib3/_collections.py -> build/lib/requests/packages/urllib3

copying requests/packages/urllib3/connectionpool.py -> build/lib/requests/packages/urllib3

copying requests/packages/urllib3/exceptions.py -> build/lib/requests/packages/urllib3

copying requests/packages/urllib3/filepost.py -> build/lib/requests/packages/urllib3

copying requests/packages/urllib3/poolmanager.py -> build/lib/requests/packages/urllib3

copying requests/packages/urllib3/request.py -> build/lib/requests/packages/urllib3

copying requests/packages/urllib3/response.py -> build/lib/requests/packages/urllib3

copying requests/packages/urllib3/util.py -> build/lib/requests/packages/urllib3

creating build/lib/requests/packages/urllib3/packages

copying requests/packages/urllib3/packages/__init__.py -> build/lib/requests/packages/urllib3/packages

copying requests/packages/urllib3/packages/ordered_dict.py -> build/lib/requests/packages/urllib3/packages

copying requests/packages/urllib3/packages/six.py -> build/lib/requests/packages/urllib3/packages

creating build/lib/requests/packages/urllib3/packages/ssl_match_hostname

copying requests/packages/urllib3/packages/ssl_match_hostname/__init__.py -> build/lib/requests/packages/urllib3/packages/ssl_match_hostname

creating build/lib/requests/packages/oauthlib

copying requests/packages/oauthlib/__init__.py -> build/lib/requests/packages/oauthlib

copying requests/packages/oauthlib/common.py -> build/lib/requests/packages/oauthlib

creating build/lib/requests/packages/oauthlib/oauth1

copying requests/packages/oauthlib/oauth1/__init__.py -> build/lib/requests/packages/oauthlib/oauth1

creating build/lib/requests/packages/oauthlib/oauth1/rfc5849

copying requests/packages/oauthlib/oauth1/rfc5849/__init__.py -> build/lib/requests/packages/oauthlib/oauth1/rfc5849

copying requests/packages/oauthlib/oauth1/rfc5849/parameters.py -> build/lib/requests/packages/oauthlib/oauth1/rfc5849

copying requests/packages/oauthlib/oauth1/rfc5849/signature.py -> build/lib/requests/packages/oauthlib/oauth1/rfc5849

copying requests/packages/oauthlib/oauth1/rfc5849/utils.py -> build/lib/requests/packages/oauthlib/oauth1/rfc5849

creating build/lib/requests/packages/oauthlib/oauth2

copying requests/packages/oauthlib/oauth2/__init__.py -> build/lib/requests/packages/oauthlib/oauth2

creating build/lib/requests/packages/oauthlib/oauth2/draft25

copying requests/packages/oauthlib/oauth2/draft25/__init__.py -> build/lib/requests/packages/oauthlib/oauth2/draft25

copying requests/packages/oauthlib/oauth2/draft25/parameters.py -> build/lib/requests/packages/oauthlib/oauth2/draft25

copying requests/packages/oauthlib/oauth2/draft25/tokens.py -> build/lib/requests/packages/oauthlib/oauth2/draft25

copying requests/packages/oauthlib/oauth2/draft25/utils.py -> build/lib/requests/packages/oauthlib/oauth2/draft25

creating build/lib/requests/packages/chardet

copying requests/packages/chardet/__init__.py -> build/lib/requests/packages/chardet

copying requests/packages/chardet/big5freq.py -> build/lib/requests/packages/chardet

copying requests/packages/chardet/big5prober.py -> build/lib/requests/packages/chardet

copying requests/packages/chardet/chardistribution.py -> build/lib/requests/packages/chardet

copying requests/packages/chardet/charsetgroupprober.py -> build/lib/requests/packages/chardet

copying requests/packages/chardet/charsetprober.py -> build/lib/requests/packages/chardet

copying requests/packages/chardet/codingstatemachine.py -> build/lib/requests/packages/chardet

copying requests/packages/chardet/constants.py -> build/lib/requests/packages/chardet

copying requests/packages/chardet/escprober.py -> build/lib/requests/packages/chardet

copying requests/packages/chardet/escsm.py -> build/lib/requests/packages/chardet

copying requests/packages/chardet/eucjpprober.py -> build/lib/requests/packages/chardet

copying requests/packages/chardet/euckrfreq.py -> build/lib/requests/packages/chardet

copying requests/packages/chardet/euckrprober.py -> build/lib/requests/packages/chardet

copying requests/packages/chardet/euctwfreq.py -> build/lib/requests/packages/chardet

copying requests/packages/chardet/euctwprober.py -> build/lib/requests/packages/chardet

copying requests/packages/chardet/gb2312freq.py -> build/lib/requests/packages/chardet

copying requests/packages/chardet/gb2312prober.py -> build/lib/requests/packages/chardet

copying requests/packages/chardet/hebrewprober.py -> build/lib/requests/packages/chardet

copying requests/packages/chardet/jisfreq.py -> build/lib/requests/packages/chardet

copying requests/packages/chardet/jpcntx.py -> build/lib/requests/packages/chardet

copying requests/packages/chardet/langbulgarianmodel.py -> build/lib/requests/packages/chardet

copying requests/packages/chardet/langcyrillicmodel.py -> build/lib/requests/packages/chardet

copying requests/packages/chardet/langgreekmodel.py -> build/lib/requests/packages/chardet

copying requests/packages/chardet/langhebrewmodel.py -> build/lib/requests/packages/chardet

copying requests/packages/chardet/langhungarianmodel.py -> build/lib/requests/packages/chardet

copying requests/packages/chardet/langthaimodel.py -> build/lib/requests/packages/chardet

copying requests/packages/chardet/latin1prober.py -> build/lib/requests/packages/chardet

copying requests/packages/chardet/mbcharsetprober.py -> build/lib/requests/packages/chardet

copying requests/packages/chardet/mbcsgroupprober.py -> build/lib/requests/packages/chardet

copying requests/packages/chardet/mbcssm.py -> build/lib/requests/packages/chardet

copying requests/packages/chardet/sbcharsetprober.py -> build/lib/requests/packages/chardet

copying requests/packages/chardet/sbcsgroupprober.py -> build/lib/requests/packages/chardet

copying requests/packages/chardet/sjisprober.py -> build/lib/requests/packages/chardet

copying requests/packages/chardet/universaldetector.py -> build/lib/requests/packages/chardet

copying requests/packages/chardet/utf8prober.py -> build/lib/requests/packages/chardet

running egg_info

writing requests.egg-info/PKG-INFO

writing top-level names to requests.egg-info/top_level.txt

writing dependency_links to requests.egg-info/dependency_links.txt

warning: manifest_maker: standard file '-c' not found



reading manifest file 'requests.egg-info/SOURCES.txt'

reading manifest template 'MANIFEST.in'

warning: no files found matching 'tests/*.'

writing manifest file 'requests.egg-info/SOURCES.txt'

copying requests/cacert.pem -> build/lib/requests

running install_lib

creating /Library/Python/2.7/site-packages/requests

error: could not create '/Library/Python/2.7/site-packages/requests': Permission denied

----------------------------------------
Command /usr/bin/python -c "import setuptools;__file__='/var/folders/z_/0j8qytyj02dgmh8xjjgdvlk00000gn/T/pip-build/requests/setup.py';exec(compile(open(__file__).read().replace('\r\n', '\n'), __file__, 'exec'))" install --record /var/folders/z_/0j8qytyj02dgmh8xjjgdvlk00000gn/T/pip-UJHcYg-record/install-record.txt --single-version-externally-managed failed with error code 1 in /var/folders/z_/0j8qytyj02dgmh8xjjgdvlk00000gn/T/pip-build/requests
Storing complete log in /Users/michelleglauser/Library/Logs/pip.log
Michelles-MacBook-Pro-2:Desktop michelleglauser$ python
Python 2.7.1 (r271:86832, Jun 16 2011, 16:59:05) 
[GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2335.15.00)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named requests
>>> git clone git://github.com/kennethreitz/requests.git
  File "<stdin>", line 1
    git clone git://github.com/kennethreitz/requests.git
            ^
SyntaxError: invalid syntax
>>> 
KeyboardInterrupt
>>> ^D
Michelles-MacBook-Pro-2:Desktop michelleglauser$ git init
Reinitialized existing Git repository in /Users/michelleglauser/Desktop/.git/
Michelles-MacBook-Pro-2:Desktop michelleglauser$ git clone git://github.com/kennethreitz/requests.git
Cloning into 'requests'...
remote: Counting objects: 9014, done.
remote: Compressing objects: 100% (3051/3051), done.
remote: Total 9014 (delta 6161), reused 8717 (delta 5903)
Receiving objects: 100% (9014/9014), 1.64 MiB | 468 KiB/s, done.
Resolving deltas: 100% (6161/6161), done.
Michelles-MacBook-Pro-2:Desktop michelleglauser$ python setup.py install
python: can't open file 'setup.py': [Errno 2] No such file or directory
Michelles-MacBook-Pro-2:Desktop michelleglauser$ ls
14Nov2012LinkedIn.jpg
8GB Memory Card Back Up
BookFairy
Desktop
Dropbox
EMAIL20121013221755.JPG
Google Drive
Hackbright
JBookFairy
New Blog Design
Québec Pics
Resume Michelle Glauser 2012 HB.doc
Screen Recording 27.mov
Screen Shot 2012-09-13 at 9.29.47 AM.png
Screen Shot 2012-11-15 at 7.58.22 PM.png
Single Life.docx
Wedding
index.html
railsbridge
requests
■Michelle Glauser Resume 2012■.docx
■Michelle Glauser Resume 2012■.pdf
Michelles-MacBook-Pro-2:Desktop michelleglauser$ cd requests/
Michelles-MacBook-Pro-2:requests michelleglauser$ python setup.py install
running install
error: can't create or remove files in install directory

The following error occurred while trying to add or remove files in the
installation directory:

    [Errno 13] Permission denied: '/Library/Python/2.7/site-packages/test-easy-install-2586.write-test'

The installation directory you specified (via --install-dir, --prefix, or
the distutils default setting) was:

    /Library/Python/2.7/site-packages/

Perhaps your account does not have write access to this directory?  If the
installation directory is a system-owned directory, you may need to sign in
as the administrator or "root" account.  If you do not have administrative
access to this machine, you may wish to choose a different installation
directory, preferably one that is listed in your PYTHONPATH environment
variable.

For information on other options, you may wish to consult the
documentation at:

  http://packages.python.org/distribute/easy_install.html

Please make the appropriate changes for your system and try again.

Michelles-MacBook-Pro-2:requests michelleglauser$ easy_install requests
Traceback (most recent call last):
  File "/usr/bin/easy_install-2.7", line 10, in <module>
    load_entry_point('setuptools==0.6c12dev-r85381', 'console_scripts', 'easy_install')()
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/pkg_resources.py", line 318, in load_entry_point
    """Locate distribution `dist_spec` and run its `script_name` script"""
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/pkg_resources.py", line 2220, in load_entry_point
    
ImportError: Entry point ('console_scripts', 'easy_install') not found
Michelles-MacBook-Pro-2:requests michelleglauser$ . venv/bin/activate
-bash: venv/bin/activate: No such file or directory
Michelles-MacBook-Pro-2:requests michelleglauser$ virtualenv venv
New python executable in venv/bin/python
Installing setuptools............done.
Installing pip...............done.
Michelles-MacBook-Pro-2:requests michelleglauser$ . venv/bin/activate
(venv)Michelles-MacBook-Pro-2:requests michelleglauser$ pip install requests
Downloading/unpacking requests
  Downloading requests-0.14.2.tar.gz (361kB): 361kB downloaded
  Running setup.py egg_info for package requests
    
    warning: no files found matching 'tests/*.'
Installing collected packages: requests
  Running setup.py install for requests
    
    warning: no files found matching 'tests/*.'
Successfully installed requests
Cleaning up...
(venv)Michelles-MacBook-Pro-2:requests michelleglauser$ import requests
-bash: import: command not found
(venv)Michelles-MacBook-Pro-2:requests michelleglauser$ python
Python 2.7.1 (r271:86832, Jun 16 2011, 16:59:05) 
[GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2335.15.00)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests
>>> r = requests.get("https://convore.com/api/account/verify.json")
rTraceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "requests/api.py", line 65, in get
    return request('get', url, **kwargs)
  File "requests/safe_mode.py", line 39, in wrapped
    return function(method, url, **kwargs)
  File "requests/api.py", line 51, in request
    return session.request(method=method, url=url, **kwargs)
  File "requests/sessions.py", line 241, in request
    r.send(prefetch=prefetch)
  File "requests/models.py", line 643, in send
    raise SSLError(e)
requests.exceptions.SSLError: hostname 'convore.com' doesn't match either of '*.grove.io', 'grove.io'
>>> r = requests.get("http://sflib1.sfpl.org/search/X?SEARCH=A+Tree+Grows+in+Brooklyn+Betty+Smith&x=0&y=0&searchscope=3&p=&l=eng&m=a&Da=&Db=&SORT=D")
>>> r
<Response [200]>
>>> r.status_code
200
>>> r.headers['content-type]
  File "<stdin>", line 1
    r.headers['content-type]
                           ^
SyntaxError: EOL while scanning string literal
>>> r.headers['content-type']
'text/html; charset=UTF-8'
>>> r.content
'<html   dir="LTR">\n<head>\n<title>San Francisco Public Library                                              /Main</title>\n<base target="_self"/>\n<link rel="stylesheet" type="text/css" href="/scripts/ProStyles.css" />\n<link rel="stylesheet" type="text/css" href="/screens/styles.css" />\n<link rel="shortcut icon" type="ximage/icon" href="/screens/favicon.ico" />\n<script type="text/javascript" src="/scripts/common.js"></script>\n<script type="text/javascript" src="/scripts/features.js"></script>\n<script type="text/javascript" src="/scripts/webbridge.js"></script>\n<script type="text/javascript" src="/scripts/elcontent.js"></script>\n<script type="text/JavaScript">\n<!-- Hide the JS\nstartTimeout(6000000, "/");\n// -->\n</script>\n<noscript>\n<meta http-equiv="Refresh" content="6000;URL=/" />\n</noscript>\n\n<script type="text/javascript" src="/screens/sfplScripts.js"></script>\n</head>\n<body bgcolor="#FFFFFF;" onLoad="sfplScripts();" >\n<table align="center" cellpadding="0" cellspacing="0" border="0" \nsummary="This table structures page content.">\n<tr> \n<td colspan="2"> \n<!-- header image, language links, and top navigation -->\n<table class="navigationtable" cellpadding="0" cellspacing="0" border="0" \nsummary="Table containing primary navigation and language options">\n\n<tr class="headerrow">\n<td colspan="4">\n<a href="http://sfpl.org/" title="San Francisco Public Library home page">\n\n<img src="/screens/background_header.jpg" border="0" vspace="0" hspace="0"\nalt="Go to the San Francisco Public Library home page" \nwidth="950" height="79" /></a>\n<span class="fineprint" style="position: relative; top:-20px; left:250px;">\n<a href="http://sflib1.sfpl.org/search*spi">Espa&#241;ol</a>\n&nbsp;|&nbsp;\n<a href="http://sflib1.sfpl.org/search*cht">&#20013;&#25991;</a>\n</span>\n\n</td>\n</tr>              \n</table>\n\n<div align="center" class="navigationRow">\n<form>\n<a href="/search"><img src="/screens/startover.gif" alt="Start Over" border="0" /></a>\n<a href="/search~S3/X?NOSRCH=A+Tree+Grows+in+Brooklyn+Betty+Smith&searchscope=3&p=&l=eng&m=a&Da=&Db=&SORT=D&SUBKEY=A+Tree+Grows+in+Brooklyn+Betty+Smith"><img src="/screens/modify.gif" alt="Modify Search" border="0" /></a>\n<a href="http://csul.iii.com/search/X?A+Tree+Grows+in+Brooklyn+Betty+Smith&l=eng&m=a&Da=&Db=&SORT=D&backlink=http://sflib1.sfpl.org:80/search~S3?/XA+Tree+Grows+in+Brooklyn+Betty+Smith&searchscope=3&p=&l=eng&m=a&Da=&Db=&SORT=D/XA+Tree+Grows+in+Brooklyn+Betty+Smith&searchscope=3&p=&l=eng&m=a&Da=&Db=&SORT=D&SUBKEY=A+Tree+Grows+in+Brooklyn+Betty+Smith/1%2C2%2C2%2CB/browse"><img src="/screens/csul.gif "alt="Search Link+ Catalog" border="0"></a>\n<select name=HISTORY onChange="onSelectChange(this, \'~S3\')"><option value="">(Search History)</option>\n<OPTION VALUE="XA+Tree+Grows+in+Brooklyn+Betty+Smith&searchscope=3&p=&l=eng&m=a&Da=&Db=&SORT=D">Keyword: A Tree Grows in Brooklyn Betty Smith in Main Library\n<option value="+/search~S3/X?A+Tree+Grows+in+Brooklyn+Betty+Smith&searchscope=3&p=&l=eng&m=a&Da=&Db=&SORT=D&clear_history">(Clear Search History)</option>\n<option value="+/">(End Search Session)</option>\n</select>\n<noscript>\n<h2>Search history function requires JavaScript.</h2>\n</noscript>\n</form>\n</div>\n\n<span><center>\n<a href="" onClick="return createResourceWindow(\'/webbridge~S3/panel?returnurl=%2Fsearch~S3%3F%2FXA%2BTree%2BGrows%2Bin%2BBrooklyn%2BBetty%2BSmith%26searchscope%3D3%26p%3D%26l%3Deng%26m%3Da%26Da%3D%26Db%3D%26SORT%3DD%2FXA%2BTree%2BGrows%2Bin%2BBrooklyn%2BBetty%2BSmith%26searchscope%3D3%26p%3D%26l%3Deng%26m%3Da%26Da%3D%26Db%3D%26\');">\n<img src="/screens/resourcelink.gif" alt="Other Resources" border="0" /></a>\n</center></span>\n<!-- BEGIN BROWSE SCREEN TABLE -->\n<table align="center" width="100%" cellpadding="2" cellspacing="0" border="0" class="browseScreen">\n<!-- BEGIN SEARCH WIDGET -->\n<div align="center">\n<tr align="center" valign="middle">\n<td valign="middle" colspan="2">\n<div  class="browseSearchtool">\n<script type="text/JavaScript">\n<!-- Hide the JS\nvar savedScope;\nvar savedTag;\nvar savedSearch;\nvar sortButtonText = null;\nvar savedExactSearch = null;\nvar sortButtonEvent = null;\nvar sortExactBrowseURL = null;\nvar sortTypes = new Array();\nvar sortLabels = new Array();\nsortTypes[0] = "t";\nsortLabels[0] = "Title";\nsortTypes[1] = "a";\nsortLabels[1] = "Author";\nsortTypes[2] = "c";\nsortLabels[2] = "Year";\nsortTypes[3] = "r";\nsortLabels[3] = "Reverse Year";\nsortTypes[4] = "n";\nsortLabels[4] = "Call Number";\nsortTypes[5] = "m";\nsortLabels[5] = "Material Type";\nsortLabels[6] = "System Sorted";\nsortTypes[6] = "-";\nvar sortSelectedValue = "6";\nvar nonSortTags = "XYZprWw"\n// Unhide the JS -->\n</script>\n<form name="searchtool" target="_self" action="/search~S3/" method=\'POST\'>\n      <label for="searchtype" style="display:none;">SearchType</label> <select name="searchtype" id="searchtype" onChange="initSort()">\n        <option value="a"> Author</option>\n        <option value="t"> Title</option>\n        <option value="d"> Subject</option>\n        <option value="c"> Call No</option>\n        <option value="X" selected="selected"> Keyword</option>\n      </select>\n      &nbsp;\n      <label for="searcharg" style="display:none;">Search</label><input type="text" name="searcharg" id="searcharg" size="30" onchange=\'return searchtoolSubmitAction()\'maxlength="75" value="A Tree Grows in Brooklyn Betty Smith" />\n      &nbsp;\n      <label for="searchscope" style="display:none;">Search Scope</label><select name="searchscope" id="searchscope">\n        <option value="1"> View Entire Collection</option>\n        <option value="33"> Adult/Teen Materials</option>\n        <option value="4"> Anza</option>\n        <option value="5"> Bayview</option>\n        <option value="6"> Bernal Heights</option>\n        <option value="32"> Branch Bookmobile 1</option>\n        <option value="7"> Children\'s Bookmobile</option>\n        <option value="2"> Children\'s Materials Only</option>\n        <option value="8"> Chinatown</option>\n        <option value="9"> Eureka Valley</option>\n        <option value="10"> Excelsior</option>\n        <option value="11"> Glen Park</option>\n        <option value="12"> Golden Gate Valley</option>\n        <option value="13"> Ingleside</option>\n        <option value="14"> Library on Wheels</option>\n        <option value="3" selected="selected"> Main Library</option>\n        <option value="15"> Marina</option>\n        <option value="16"> Merced</option>\n        <option value="17"> Mission</option>\n        <option value="18"> Mission Bay</option>\n        <option value="19"> Noe Valley</option>\n        <option value="20"> North Beach</option>\n        <option value="21"> Oceanview</option>\n        <option value="22"> Ortega</option>\n        <option value="23"> Park</option>\n        <option value="24"> Parkside</option>\n        <option value="25"> Portola</option>\n        <option value="26"> Potrero</option>\n        <option value="27"> Presidio</option>\n        <option value="28"> Richmond</option>\n        <option value="29"> Sunset</option>\n        <option value="30"> Visitacion Valley</option>\n        <option value="31"> West Portal</option>\n        <option value="34"> Western Addition</option>\n      </select>\n      &nbsp;\n\n<span id="sort_cell">\n</span>\n\n<script type="text/JavaScript">\n<!-- Hide the JS\ninitSort();\n// Unhide the JS -->\n</script>\n      <input type="hidden" name="SORT" value="DZ" /><input type="hidden" name="extended" value="0" />      <input type="submit" name="SUBMIT" value="Search" onclick=\'return searchtoolSubmitAction();\' />\n<div>\n      <input type="checkbox" name="availlim" value="1"  /> <EM>Limit to available</EM><br/>\n</div>\n<div>\n      <input type="hidden" name="searchlimits" value="l=eng&m=a" />\n      <input type="hidden" name="searchorigarg" value="XA Tree Grows in Brooklyn Betty Smith&SORT=D" />\n</div>\n</form>\n<div>\n</div>\n<div  class="browseSearchtoolMessage">      <i>Limited to:</i> Language "English" <i> and</i> Material Type "BOOK" <i> and</i>  <i>2 results found. </i>Sorted by  <strong>relevance</strong>  | <a href="/search~S3/X?A+Tree+Grows+in+Brooklyn+Betty+Smith&searchscope=3&p=&l=eng&m=a&Da=&Db=&SORT=DX">date</a>  | <a href="/search~S3/X?A+Tree+Grows+in+Brooklyn+Betty+Smith&searchscope=3&p=&l=eng&m=a&Da=&Db=&SORT=AX">title</a> .\n</div>\n<div></div></div>\n\n</td>\n</tr>\n</div>\n<!-- END SEARCH WIDGET -->\n\n<!-- BEGIN BROWSE PAGER -->\n<!-- END BROWSE PAGER -->\n\n<style type="text/css">\n<!--\n#rategroup-9 { display: inline }\n#rateneed-9  { display: none }\n#rategroupMy-9 { display: none }\n#ratemy-9      { display: inline }\n#rategroup-8 { display: inline }\n#rateneed-8  { display: none }\n#rategroupMy-8 { display: none }\n#ratemy-8      { display: inline }\n#rategroup-7 { display: inline }\n#rateneed-7  { display: none }\n#rategroupMy-7 { display: none }\n#ratemy-7      { display: inline }\n#rategroup-6 { display: inline }\n#rateneed-6  { display: none }\n#rategroupMy-6 { display: none }\n#ratemy-6      { display: inline }\n#rategroup-5 { display: inline }\n#rateneed-5  { display: none }\n#rategroupMy-5 { display: none }\n#ratemy-5      { display: inline }\n#rategroup-4 { display: inline }\n#rateneed-4  { display: none }\n#rategroupMy-4 { display: none }\n#ratemy-4      { display: inline }\n#rategroup-3 { display: inline }\n#rateneed-3  { display: none }\n#rategroupMy-3 { display: none }\n#ratemy-3      { display: inline }\n#rategroup-2 { display: inline }\n#rateneed-2  { display: none }\n#rategroupMy-2 { display: none }\n#ratemy-2      { display: inline }\n#rategroup-1 { display: inline }\n#rateneed-1  { display: none }\n#rategroupMy-1 { display: none }\n#ratemy-1      { display: inline }\n#rategroup0 { display: inline }\n#rateneed0  { display: none }\n#rategroupMy0 { display: none }\n#ratemy0      { display: inline }\n#rategroup1 { display: inline }\n#rateneed1  { display: none }\n#rategroupMy1 { display: none }\n#ratemy1      { display: inline }\n#rategroup2 { display: inline }\n#rateneed2  { display: none }\n#rategroupMy2 { display: none }\n#ratemy2      { display: inline }\n-->\n</style>\n<!-- BEGIN BROWSE SCREEN LEFT CELL: BROWSELIST/BRIEFCIT AREA -->\n<tr><td>\n<table id="briefcit_table" align="center" border="0" bordercolor="339999" width="100%">\n<tr align="CENTER" valign="MIDDLE">\n<td colspan="5" class="browseSaveJump">\n<form method="POST" action="/search~S3?/XA+Tree+Grows+in+Brooklyn+Betty+Smith&searchscope=3&p=&l=eng&m=a&Da=&Db=&SORT=D/XA+Tree+Grows+in+Brooklyn+Betty+Smith&searchscope=3&p=&l=eng&m=a&Da=&Db=&SORT=D&SUBKEY=A+Tree+Grows+in+Brooklyn+Betty+Smith/1%2C2%2C2%2CB/browse" name="export_form" id="export_form" >\n<input type="hidden" name="jumpref" value="XA+Tree+Grows+in+Brooklyn+Betty+Smith">\n<input type="hidden" id="save_func" name="save_func" value=""/>\n<a href="#" onclick="process_save(0);" style="text-decoration:none">\n<img src="/screens/savemarked.gif" alt="Save marked records" border="0" /></a>\n<span name=\'save_page_btn1\' id=\'save_page_btn1\' style=\'visibility: visible\' ><a href="#" onclick="process_save(1);" style="text-decoration:none">\n<img src="/screens/saveallpage.gif" alt="Save all on page" border="0" /></a>\n</span>\n<span name=\'mylist_btn1\' id=\'mylist_btn1\' style=\'visibility: visible\' ><a href="#" onclick="save_to_mylist();">\n<img src="/screens/save-to-list.gif" alt="Save to List" border=0 /></a>\n</span>\n</td></tr>\n\n\n</td>\n</tr>\n<tr  class="browseHeader">\n<td align="center" class="browseHeaderData">\nKeyword (1-2 of 2)\n</td>\n</tr>\n<!-- Right Result rank 4 -->\n<tr  class="browseSuperEntry browseEntryRelGroup4"><td colspan="1"><img src="/screens/relevance2.gif" alt="">&nbsp;Relevant titles&nbsp;entries 1-1</td></tr>\n<tr class="briefCitRow">\n  <td>\n <table align="center" cellpadding="5" width="950">\n    <tr>\n      <td align="center" width="5%">\n        <strong>\n<a name=\'anchor_1\'></a> 1\t\t</strong>\n\n<br /><br />\n\n<img src="/screens/icon_bookbag.gif" border="0" alt="Select item / \xe9\x81\xb8\xe6\x93\x87\xe6\xad\xa4\xe9\xa0\x85 " width="23" height="34" />\n\n<input type="checkbox" \nname="save" value="b1243502" >\n      </td>\n      <td align="center" valign="top" width="15%">\n<a href="http://www.syndetics.com/index.aspx?isbn=9780061120077/index.html&client=sfpl&upc=&oclc=abl-ocm00000424&type=rn12" target="_parent"><img src="http://www.syndetics.com/index.aspx?isbn=9780061120077/SC.GIF&client=sfpl&upc=&oclc=abl-ocm00000424" border="0" alt="book jacket"></a>      </td>\n\t  <td align="left" valign="top" width="65%">\n\t  \t<table>\n\t\t\t<tr>\n\n\t\t\t\t<td>\n<!--{nohitmsg}-->\n\n\n<a href="/search~S3?/XA+Tree+Grows+in+Brooklyn+Betty+Smith&searchscope=3&p=&l=eng&m=a&Da=&Db=&SORT=D/XA+Tree+Grows+in+Brooklyn+Betty+Smith&searchscope=3&p=&l=eng&m=a&Da=&Db=&SORT=D&SUBKEY=A+Tree+Grows+in+Brooklyn+Betty+Smith/1%2C2%2C2%2CB/frameset&FF=XA+Tree+Grows+in+Brooklyn+Betty+Smith&searchscope=3&p=&l=eng&m=a&Da=&Db=&SORT=D&1%2C1%2C">A tree grows in Brooklyn : a novel / by Betty Smith.</a>\t\t\t\t</td>\n\t\t\t</tr>\n\t\t\t<tr>\n\t\t\t\t<td>\nSmith, Betty, 1896-1972.\t\t\t\t</td>\n\t\t\t</tr>\n\n\t\t\t<tr>\n\t\t\t\t<td>\nNew York : Harper & Brothers, [1943]\t\t\t\t</td>\n\t\t\t</tr>\n\t\t\t<tr>\n\t\t\t\t<td>\n3 p. l., 3-443, [1] p. ; 21 cm.\t\t\t\t</td>\n\t\t\t</tr>\n\t\t\t<tr>\n\n\t\t\t\t<td>\nF Smith Be\t\t\t\t</td>\n\t\t\t</tr>\n\t\t\t<tr>\n<tr>\n<td>\n&nbsp;</td>\n</tr>\n\n<td>\n\n<span id="rategroup1"><a href="/patroninfo~S3/0/redirect=/search~S3?/XA+Tree+Grows+in+Brooklyn+Betty+Smith&searchscope=3&p=&l=eng&m=a&Da=&Db=&SORT=D/XA+Tree+Grows+in+Brooklyn+Betty+Smith&searchscope=3&p=&l=eng&m=a&Da=&Db=&SORT=D&SUBKEY=A+Tree+Grows+in+Brooklyn+Betty+Smith/1%2C2%2C2%2CB/browse#anchor_1"><img src="/screens/rate_group.gif" border="0" title="Rated 4 stars out of 5 based on 3 ratings" /><img src="/screens/rate_group.gif" border="0" title="Rated 4 stars out of 5 based on 3 ratings" /><img src="/screens/rate_group.gif" border="0" title="Rated 4 stars out of 5 based on 3 ratings" /><img src="/screens/rate_group.gif" border="0" title="Rated 4 stars out of 5 based on 3 ratings" /><img src="/screens/rate_pad.gif" border="0" title="Rated 4 stars out of 5 based on 3 ratings" /></a>\n\n</span><span class="ratingslink_briefcit"><a href="/screens/ratings.html" title="Explanation of ratings">Ratings?</a></span>\n</td>\n</tr>\n</table>\n\n</td>\n<td align="center" valign="middle" width="15%">\n1943<br /><br />\n <img src="/screens/media_book.gif" alt="BOOK"><p class="detail">\n<a href="/search~S3?/XA+Tree+Grows+in+Brooklyn+Betty+Smith&searchscope=3&p=&l=eng&m=a&Da=&Db=&SORT=D/XA+Tree+Grows+in+Brooklyn+Betty+Smith&searchscope=3&p=&l=eng&m=a&Da=&Db=&SORT=D&SUBKEY=A+Tree+Grows+in+Brooklyn+Betty+Smith/1%2C2%2C2%2CB/frameset&FF=XA+Tree+Grows+in+Brooklyn+Betty+Smith&searchscope=3&p=&l=eng&m=a&Da=&Db=&SORT=D&1%2C1%2C"><img src="/screens/isitavailable.gif" alt="Is it available?" border="0" /></a></p>\n      </td>\n      </tr>\n    </table>\n  </td>\n\n</tr>\n<!--this is customized <screens/briefcit.html>-->\n<!--this is customized <screens/briefcit.html>-->\n<!-- Right Result rank 5 -->\n<tr  class="browseSuperEntry browseEntryRelGroup5"><td colspan="1"><img src="/screens/relevance1.gif" alt="">&nbsp;Other relevant titles&nbsp;entries 2-2</td></tr>\n<tr class="briefCitRow">\n  <td>\n <table align="center" cellpadding="5" width="950">\n    <tr>\n      <td align="center" width="5%">\n        <strong>\n<a name=\'anchor_2\'></a> 2\t\t</strong>\n\n<br /><br />\n\n<img src="/screens/icon_bookbag.gif" border="0" alt="Select item / \xe9\x81\xb8\xe6\x93\x87\xe6\xad\xa4\xe9\xa0\x85 " width="23" height="34" />\n\n<input type="checkbox" \nname="save" value="b2024786" >\n      </td>\n      <td align="center" valign="top" width="15%">\n<a href="http://www.syndetics.com/index.aspx?isbn=1592402100/index.html&client=sfpl&upc=9781592402106&oclc=ocm70707739+&type=rn12" target="_parent"><img src="http://www.syndetics.com/index.aspx?isbn=1592402100/SC.GIF&client=sfpl&upc=9781592402106&oclc=ocm70707739+" border="0" alt="book jacket"></a>      </td>\n\t  <td align="left" valign="top" width="65%">\n\t  \t<table>\n\t\t\t<tr>\n\n\t\t\t\t<td>\n<!--{nohitmsg}-->\n\n\n<a href="/search~S3?/XA+Tree+Grows+in+Brooklyn+Betty+Smith&searchscope=3&p=&l=eng&m=a&Da=&Db=&SORT=D/XA+Tree+Grows+in+Brooklyn+Betty+Smith&searchscope=3&p=&l=eng&m=a&Da=&Db=&SORT=D&SUBKEY=A+Tree+Grows+in+Brooklyn+Betty+Smith/1%2C2%2C2%2CB/frameset&FF=XA+Tree+Grows+in+Brooklyn+Betty+Smith&searchscope=3&p=&l=eng&m=a&Da=&Db=&SORT=D&2%2C2%2C">The book that changed my life : 71 remarkable writers celebrate the books that matter most to them /</a>\t\t\t\t</td>\n\t\t\t</tr>\n\t\t\t<tr>\n\t\t\t\t<td>\n\t\t\t\t</td>\n\t\t\t</tr>\n\n\t\t\t<tr>\n\t\t\t\t<td>\nNew York, N.Y. : Gotham Books, c2006.\t\t\t\t</td>\n\t\t\t</tr>\n\t\t\t<tr>\n\t\t\t\t<td>\nxvii, 197 p. ; 20 cm.\t\t\t\t</td>\n\t\t\t</tr>\n\t\t\t<tr>\n\n\t\t\t\t<td>\n028.8 B64434\t\t\t\t</td>\n\t\t\t</tr>\n\t\t\t<tr>\n<tr>\n<td>\n<a href="http://www.loc.gov/catdir/toc/ecip0617/2006023179.html" onclick="window.open(\'http://www.loc.gov/catdir/toc/ecip0617/2006023179.html\'); return false;">Digital Media</a><br />\n</td>\n</tr>\n\n<td>\n\n<span id="rategroup2"><a href="/patroninfo~S3/0/redirect=/search~S3?/XA+Tree+Grows+in+Brooklyn+Betty+Smith&searchscope=3&p=&l=eng&m=a&Da=&Db=&SORT=D/XA+Tree+Grows+in+Brooklyn+Betty+Smith&searchscope=3&p=&l=eng&m=a&Da=&Db=&SORT=D&SUBKEY=A+Tree+Grows+in+Brooklyn+Betty+Smith/1%2C2%2C2%2CB/browse#anchor_2"><img src="/screens/rate_no.gif" border="0" title="No one has rated this material" /></a>\n\n</span><span class="ratingslink_briefcit"><a href="/screens/ratings.html" title="Explanation of ratings">Ratings?</a></span>\n</td>\n</tr>\n</table>\n\n</td>\n<td align="center" valign="middle" width="15%">\nc2006<br /><br />\n <img src="/screens/media_book.gif" alt="BOOK"><p class="detail">\n<a href="/search~S3?/XA+Tree+Grows+in+Brooklyn+Betty+Smith&searchscope=3&p=&l=eng&m=a&Da=&Db=&SORT=D/XA+Tree+Grows+in+Brooklyn+Betty+Smith&searchscope=3&p=&l=eng&m=a&Da=&Db=&SORT=D&SUBKEY=A+Tree+Grows+in+Brooklyn+Betty+Smith/1%2C2%2C2%2CB/frameset&FF=XA+Tree+Grows+in+Brooklyn+Betty+Smith&searchscope=3&p=&l=eng&m=a&Da=&Db=&SORT=D&2%2C2%2C"><img src="/screens/isitavailable.gif" alt="Is it available?" border="0" /></a></p>\n      </td>\n      </tr>\n    </table>\n  </td>\n\n</tr>\n<!--this is customized <screens/briefcit.html>-->\n<!--this is customized <screens/briefcit.html>-->\n<tr align="CENTER" valign="MIDDLE">\n<td colspan="5" class="browseSaveJump">\n<a href="#" onclick="process_save(0);" style="text-decoration:none">\n<img src="/screens/savemarked.gif" alt="Save marked records" border="0" /></a>\n<span name=\'save_page_btn2\' id=\'save_page_btn2\' style=\'visibility: visible\' ><a href="#" onclick="process_save(1);" style="text-decoration:none">\n<img src="/screens/saveallpage.gif" alt="Save all on page" border="0" /></a>\n</span>\n<span name=\'mylist_btn2\' id=\'mylist_btn2\' style=\'visibility: visible\' ><a href="#" onclick="save_to_mylist();">\n<img src="/screens/save-to-list.gif" alt="Save to List" border=0 /></a>\n</span>\n</form>\n</td></tr>\n\n\n</td>\n</tr>\n</table>\n<!-- END BROWSELIST/BRIEFCIT AREA -->\n</td>\n<!-- END BROWSE SCREEN LEFT CELL -->\n\n<!-- BEGIN BROWSE SCREEN RIGHT CELL -->\n<td valign="top" width="0%">\n<div valign="top" rowspan="2"  class="browseResourceTable">\n\n<!-- BEGIN RESOURCE TABLE -->\n<table width="100%"  class="browseResourceTable" cellpadding="0" cellspacing="0" border="0">\n</table>\n<!-- END RESOURCE TABLE -->\n\n</div>\n\n</td>\n<!-- END BROWSE SCREEN RIGHT CELL -->\n</tr>\n\n<!-- BEGIN BOTTOM BROWSE PAGER -->\n<!-- END BOTTOM BROWSE PAGER -->\n</table>\n<!-- END BROWSE SCREEN TABLE -->\n<div align="center" class="navigationRow">\n<form>\n<a href="/search"><img src="/screens/startover.gif" alt="Start Over" border="0" /></a>\n<a href="/search~S3/X?NOSRCH=A+Tree+Grows+in+Brooklyn+Betty+Smith&searchscope=3&p=&l=eng&m=a&Da=&Db=&SORT=D&SUBKEY=A+Tree+Grows+in+Brooklyn+Betty+Smith"><img src="/screens/modify.gif" alt="Modify Search" border="0" /></a>\n<a href="http://csul.iii.com/search/X?A+Tree+Grows+in+Brooklyn+Betty+Smith&l=eng&m=a&Da=&Db=&SORT=D&backlink=http://sflib1.sfpl.org:80/search~S3?/XA+Tree+Grows+in+Brooklyn+Betty+Smith&searchscope=3&p=&l=eng&m=a&Da=&Db=&SORT=D/XA+Tree+Grows+in+Brooklyn+Betty+Smith&searchscope=3&p=&l=eng&m=a&Da=&Db=&SORT=D&SUBKEY=A+Tree+Grows+in+Brooklyn+Betty+Smith/1%2C2%2C2%2CB/browse"><img src="/screens/csul.gif "alt="Search Link+ Catalog" border="0"></a>\n<select name=HISTORY onChange="onSelectChange(this, \'~S3\')"><option value="">(Search History)</option>\n<OPTION VALUE="XA+Tree+Grows+in+Brooklyn+Betty+Smith&searchscope=3&p=&l=eng&m=a&Da=&Db=&SORT=D">Keyword: A Tree Grows in Brooklyn Betty Smith in Main Library\n<option value="+/search~S3/X?A+Tree+Grows+in+Brooklyn+Betty+Smith&searchscope=3&p=&l=eng&m=a&Da=&Db=&SORT=D&clear_history">(Clear Search History)</option>\n<option value="+/">(End Search Session)</option>\n</select>\n</form>\n</div>\n\n\n<div id="footer" class="fineprint" align="left">\n<img src="/screens/city_seal.gif" \nalt="City of San Francisco seal" width="44" height="44" \nstyle="float:left;margin:7px;" /> <br />\n<a href="http://sfpl.org/index.php?pg=2000034301" \ntarget="Resource_Window">Contact</a>&nbsp;|&nbsp;\n<a href="http://sfpl.org/index.php?pg=2000034401" \ntarget="Resource_Window">FAQ</a>&nbsp;|&nbsp;\n<a href="http://sfpl.org/index.php?pg=2000001701" \ntarget="Resource_Window">Ask A Librarian</a>&nbsp;|&nbsp;\n<a href="http://sfpl.org/index.php?pg=2000028601" \ntarget="Resource_Window">Articles &amp; Databases</a>&nbsp;|&nbsp;\n<a href="http://sfpl.org/index.php?pg=2000004401" \ntarget="Resource_Window">Suggest a Title </a>&nbsp;|&nbsp;\n<a href="http://sfpl.org/index.php?pg=2000031901"\ntarget="Resource_Window">Interlibrary Loan </a>\n<br />\nCopyright &copy; 2002-2012 San Francisco Public Library. All rights \nreserved.&nbsp;|&nbsp;\n<a href="http://sfpl.org/index.php?pg=2000001301" \ntarget="Resource_Window">Privacy policy</a>&nbsp;|&nbsp;Internet &amp; Computer \n<a href="http://sfpl.org/index.php?pg=2000377401">Help/</a><a href="http://sfpl.org/index.php?pg=2000004301">Rules</a>\t\t\n</div>\n\n\n</body>\n</html>\n'
>>> import pyquery
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named pyquery
>>> import pyquery from pyquery
  File "<stdin>", line 1
    import pyquery from pyquery
                      ^
SyntaxError: invalid syntax
>>> from pyquery import pyquery
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named pyquery
>>> from pyquery import PyQuery as pq
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named pyquery
>>> pip install pyquery
  File "<stdin>", line 1
    pip install pyquery
              ^
SyntaxError: invalid syntax
>>> r = requests.put("http://sflib1.sfpl.org/search/X?SEARCH=A+Tree+Grows+in+Brooklyn+Betty+Smith&x=0&y=0&searchscope=3&p=&l=eng&m=a&Da=&Db=&SORT=D", params="A T>>> r = requests.put("http://sflib1.sfpl.org/search/X?SEARCH=A+Tree+Grows+in+Broklyn+Betty+Smith&x=0&y=0&searchscope=3&p=&l=eng&m=a&Da=&Db=&SORT=D", params="A T
KeyboardInterrupt
>>> ^D
(venv)Michelles-MacBook-Pro-2:requests michelleglauser$ cd ..
(venv)Michelles-MacBook-Pro-2:Desktop michelleglauser$ mkdir Requests
mkdir: Requests: File exists
(venv)Michelles-MacBook-Pro-2:Desktop michelleglauser$ cd requests/
(venv)Michelles-MacBook-Pro-2:requests michelleglauser$ touch requirements.txt
(venv)Michelles-MacBook-Pro-2:requests michelleglauser$ less requirements.txt
(venv)Michelles-MacBook-Pro-2:requests michelleglauser$ pip install -r requirements.txt
Downloading/unpacking nose (from -r requirements.txt (line 1))
  Downloading nose-1.2.1.tar.gz (400kB): 400kB downloaded
  Running setup.py egg_info for package nose
    
    no previously-included directories found matching 'doc/.build'
Downloading/unpacking rudolf2 (from -r requirements.txt (line 2))
  Downloading rudolf2-0.3.tar.gz
  Running setup.py egg_info for package rudolf2
    
Installing collected packages: nose, rudolf2
  Running setup.py install for nose
    
    no previously-included directories found matching 'doc/.build'
    Installing nosetests script to /Users/michelleglauser/Desktop/requests/venv/bin
    Installing nosetests-2.7 script to /Users/michelleglauser/Desktop/requests/venv/bin
  Running setup.py install for rudolf2
    
Successfully installed nose rudolf2
Cleaning up...
(venv)Michelles-MacBook-Pro-2:requests michelleglauser$ . venv/bin/activate
(venv)Michelles-MacBook-Pro-2:requests michelleglauser$ python
Python 2.7.1 (r271:86832, Jun 16 2011, 16:59:05) 
[GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2335.15.00)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from pyquery import PyQuery
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named pyquery
>>> from pyquery import PyQuery as pq
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named pyquery
>>> 
KeyboardInterrupt
>>> ^D
(venv)Michelles-MacBook-Pro-2:requests michelleglauser$ deactivate
Michelles-MacBook-Pro-2:requests michelleglauser$ . venv/bin/activate
(venv)Michelles-MacBook-Pro-2:requests michelleglauser$ pip install -r requirements.txt
Requirement already satisfied (use --upgrade to upgrade): nose in ./venv/lib/python2.7/site-packages (from -r requirements.txt (line 1))
Requirement already satisfied (use --upgrade to upgrade): rudolf2 in ./venv/lib/python2.7/site-packages (from -r requirements.txt (line 2))
Cleaning up...
(venv)Michelles-MacBook-Pro-2:requests michelleglauser$ python
Python 2.7.1 (r271:86832, Jun 16 2011, 16:59:05) 
[GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2335.15.00)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from pyquery import PyQuery
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named pyquery
>>> 
KeyboardInterrupt
>>> ^D
(venv)Michelles-MacBook-Pro-2:requests michelleglauser$ python
Python 2.7.1 (r271:86832, Jun 16 2011, 16:59:05) 
[GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2335.15.00)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from pyquery import PyQuery
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named pyquery
>>> 
KeyboardInterrupt
>>> ^D
(venv)Michelles-MacBook-Pro-2:requests michelleglauser$ cd ..
(venv)Michelles-MacBook-Pro-2:Desktop michelleglauser$ cd BookFairy
(venv)Michelles-MacBook-Pro-2:BookFairy michelleglauser$ deactivate
Michelles-MacBook-Pro-2:BookFairy michelleglauser$ ls
BookFairy       import pyquery.py   venv
bookapp         manage.py
db          requirements.txt
Michelles-MacBook-Pro-2:BookFairy michelleglauser$ . venv/bin/activate
(venv)Michelles-MacBook-Pro-2:BookFairy michelleglauser$ python
Python 2.7.1 (r271:86832, Jun 16 2011, 16:59:05) 
[GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2335.15.00)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from pyquery import PyQuery
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named pyquery
>>> import requests
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named requests
>>> 
KeyboardInterrupt
>>> ^D
(venv)Michelles-MacBook-Pro-2:BookFairy michelleglauser$ cd ..
(venv)Michelles-MacBook-Pro-2:Desktop michelleglauser$ cd BookFairy/
(venv)Michelles-MacBook-Pro-2:BookFairy michelleglauser$ pip install pyquery
Downloading/unpacking pyquery
  Downloading pyquery-1.2.2.tar.gz
  Running setup.py egg_info for package pyquery
    /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/distutils/dist.py:267: UserWarning: Unknown distribution option: 'test_requires'
      warnings.warn(msg)
    
Downloading/unpacking lxml>=2.1 (from pyquery)
  Downloading lxml-3.0.1.tar.gz (3.2MB): 3.2MB downloaded
  Running setup.py egg_info for package lxml
    Building lxml version 3.0.1.
    Building without Cython.
    Using build configuration of libxslt 1.1.24
    
    warning: no previously-included files found matching '*.py'
    warning: no files found matching '*.txt' under directory 'src/lxml/tests'
Downloading/unpacking cssselect (from pyquery)
  Downloading cssselect-0.7.1.tar.gz
  Running setup.py egg_info for package cssselect
    
    no previously-included directories found matching 'docs/_build'
Installing collected packages: pyquery, lxml, cssselect
  Running setup.py install for pyquery
    /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/distutils/dist.py:267: UserWarning: Unknown distribution option: 'test_requires'
      warnings.warn(msg)
    
  Running setup.py install for lxml
    Building lxml version 3.0.1.
    Building without Cython.
    Using build configuration of libxslt 1.1.24
    building 'lxml.etree' extension
    llvm-gcc-4.2 -fno-strict-aliasing -fno-common -dynamic -g -Os -pipe -fno-common -fno-strict-aliasing -fwrapv -mno-fused-madd -DENABLE_DTRACE -DMACOSX -DNDEBUG -Wall -Wstrict-prototypes -Wshorten-64-to-32 -DNDEBUG -g -fwrapv -Os -Wall -Wstrict-prototypes -DENABLE_DTRACE -arch i386 -arch x86_64 -pipe -I/usr/include/libxml2 -I/Users/michelleglauser/Desktop/BookFairy/venv/build/lxml/src/lxml/includes -I/System/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7 -c src/lxml/lxml.etree.c -o build/temp.macosx-10.7-intel-2.7/src/lxml/lxml.etree.o -flat_namespace
    src/lxml/lxml.etree.c: In function ‘__pyx_pf_4lxml_5etree_4XSLT_18__call__’:
    src/lxml/lxml.etree.c:132608: warning: passing argument 1 of ‘__pyx_f_4lxml_5etree_12_XSLTContext__copy’ from incompatible pointer type
    src/lxml/lxml.etree.c: In function ‘__pyx_f_4lxml_5etree__copyXSLT’:
    src/lxml/lxml.etree.c:133997: warning: passing argument 1 of ‘__pyx_f_4lxml_5etree_12_XSLTContext__copy’ from incompatible pointer type
    src/lxml/lxml.etree.c: In function ‘__pyx_pf_4lxml_5etree_13XSLTExtension_2apply_templates’:
    src/lxml/lxml.etree.c:136661: warning: implicit declaration of function ‘xsltProcessOneNode’
    src/lxml/lxml.etree.c: In function ‘__pyx_f_4lxml_5etree__setNodeText’:
    src/lxml/lxml.etree.c:18219: warning: implicit conversion shortens 64-bit value into a 32-bit value
    src/lxml/lxml.etree.c: In function ‘__pyx_f_4lxml_5etree__mapTagsToQnameMatchArray’:
    src/lxml/lxml.etree.c:20501: warning: implicit conversion shortens 64-bit value into a 32-bit value
    src/lxml/lxml.etree.c:20561: warning: implicit conversion shortens 64-bit value into a 32-bit value
    src/lxml/lxml.etree.c: In function ‘__pyx_f_4lxml_5etree__receiveXSLTError’:
    src/lxml/lxml.etree.c:33738: warning: implicit conversion shortens 64-bit value into a 32-bit value
    src/lxml/lxml.etree.c:33747: warning: implicit conversion shortens 64-bit value into a 32-bit value
    src/lxml/lxml.etree.c:33821: warning: implicit conversion shortens 64-bit value into a 32-bit value
    src/lxml/lxml.etree.c:33830: warning: implicit conversion shortens 64-bit value into a 32-bit value
    src/lxml/lxml.etree.c: In function ‘__pyx_pf_4lxml_5etree_7_Attrib_38__contains__’:
    src/lxml/lxml.etree.c:54835: warning: implicit conversion shortens 64-bit value into a 32-bit value
    src/lxml/lxml.etree.c: In function ‘__pyx_f_4lxml_5etree_16_MultiTagMatcher_matchesType’:
    src/lxml/lxml.etree.c:56281: warning: implicit conversion shortens 64-bit value into a 32-bit value
    src/lxml/lxml.etree.c: In function ‘__pyx_f_4lxml_5etree__setupPythonUnicode’:
    src/lxml/lxml.etree.c:78941: warning: implicit conversion shortens 64-bit value into a 32-bit value
    src/lxml/lxml.etree.c: In function ‘__pyx_f_4lxml_5etree_18_FileReaderContext_copyToBuffer’:
    src/lxml/lxml.etree.c:80380: warning: implicit conversion shortens 64-bit value into a 32-bit value
    src/lxml/lxml.etree.c:80398: warning: implicit conversion shortens 64-bit value into a 32-bit value
    src/lxml/lxml.etree.c: In function ‘__pyx_f_4lxml_5etree__readFileParser’:
    src/lxml/lxml.etree.c:80823: warning: implicit conversion shortens 64-bit value into a 32-bit value
    src/lxml/lxml.etree.c: In function ‘__pyx_f_4lxml_5etree__local_resolver’:
    src/lxml/lxml.etree.c:81198: warning: implicit conversion shortens 64-bit value into a 32-bit value
    src/lxml/lxml.etree.c: In function ‘__pyx_f_4lxml_5etree_11_BaseParser__parseUnicodeDoc’:
    src/lxml/lxml.etree.c:85860: warning: implicit conversion shortens 64-bit value into a 32-bit value
    src/lxml/lxml.etree.c: In function ‘__pyx_f_4lxml_5etree_11_BaseParser__parseDoc’:
    src/lxml/lxml.etree.c:86260: warning: implicit conversion shortens 64-bit value into a 32-bit value
    src/lxml/lxml.etree.c:86316: warning: implicit conversion shortens 64-bit value into a 32-bit value
    src/lxml/lxml.etree.c: In function ‘__pyx_f_4lxml_5etree__convert_ns_prefixes’:
    src/lxml/lxml.etree.c:102254: warning: implicit conversion shortens 64-bit value into a 32-bit value
    src/lxml/lxml.etree.c: In function ‘__pyx_f_4lxml_5etree_9iterparse__read_more_events’:
    src/lxml/lxml.etree.c:107671: warning: implicit conversion shortens 64-bit value into a 32-bit value
    src/lxml/lxml.etree.c:107833: warning: implicit conversion shortens 64-bit value into a 32-bit value
    src/lxml/lxml.etree.c: In function ‘__pyx_pf_4lxml_5etree_4XSLT_18__call__’:
    src/lxml/lxml.etree.c:132608: warning: passing argument 1 of ‘__pyx_f_4lxml_5etree_12_XSLTContext__copy’ from incompatible pointer type
    src/lxml/lxml.etree.c: In function ‘__pyx_f_4lxml_5etree__convert_xslt_parameters’:
    src/lxml/lxml.etree.c:133776: warning: implicit conversion shortens 64-bit value into a 32-bit value
    src/lxml/lxml.etree.c:133799: warning: implicit conversion shortens 64-bit value into a 32-bit value
    src/lxml/lxml.etree.c: In function ‘__pyx_f_4lxml_5etree__copyXSLT’:
    src/lxml/lxml.etree.c:133997: warning: passing argument 1 of ‘__pyx_f_4lxml_5etree_12_XSLTContext__copy’ from incompatible pointer type
    src/lxml/lxml.etree.c: In function ‘__pyx_pf_4lxml_5etree_13XSLTExtension_2apply_templates’:
    src/lxml/lxml.etree.c:136661: warning: implicit declaration of function ‘xsltProcessOneNode’
    llvm-gcc-4.2 -Wl,-F. -bundle -undefined dynamic_lookup -Wl,-F. -arch i386 -arch x86_64 build/temp.macosx-10.7-intel-2.7/src/lxml/lxml.etree.o -lxslt -lexslt -lxml2 -lz -lm -o build/lib.macosx-10.7-intel-2.7/lxml/etree.so
    building 'lxml.objectify' extension
    llvm-gcc-4.2 -fno-strict-aliasing -fno-common -dynamic -g -Os -pipe -fno-common -fno-strict-aliasing -fwrapv -mno-fused-madd -DENABLE_DTRACE -DMACOSX -DNDEBUG -Wall -Wstrict-prototypes -Wshorten-64-to-32 -DNDEBUG -g -fwrapv -Os -Wall -Wstrict-prototypes -DENABLE_DTRACE -arch i386 -arch x86_64 -pipe -I/usr/include/libxml2 -I/Users/michelleglauser/Desktop/BookFairy/venv/build/lxml/src/lxml/includes -I/System/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7 -c src/lxml/lxml.objectify.c -o build/temp.macosx-10.7-intel-2.7/src/lxml/lxml.objectify.o -flat_namespace

    src/lxml/lxml.objectify.c: In function ‘__pyx_f_4lxml_9objectify__lookupChild’:
    src/lxml/lxml.objectify.c:5360: warning: implicit conversion shortens 64-bit value into a 32-bit value
    src/lxml/lxml.objectify.c: In function ‘__pyx_f_4lxml_9objectify__annotate_element’:
    src/lxml/lxml.objectify.c:19445: warning: implicit conversion shortens 64-bit value into a 32-bit value
    src/lxml/lxml.objectify.c: In function ‘__pyx_pf_4lxml_9objectify_10ObjectPath_6__call__’:
    src/lxml/lxml.objectify.c:23044: warning: implicit conversion shortens 64-bit value into a 32-bit value
    llvm-gcc-4.2 -Wl,-F. -bundle -undefined dynamic_lookup -Wl,-F. -arch i386 -arch x86_64 build/temp.macosx-10.7-intel-2.7/src/lxml/lxml.objectify.o -lxslt -lexslt -lxml2 -lz -lm -o build/lib.macosx-10.7-intel-2.7/lxml/objectify.so
    
    warning: no files found matching '*.txt' under directory 'src/lxml/tests'
  Running setup.py install for cssselect
    
    no previously-included directories found matching 'docs/_build'
Successfully installed pyquery lxml cssselect
Cleaning up...
(venv)Michelles-MacBook-Pro-2:BookFairy michelleglauser$ 
(venv)Michelles-MacBook-Pro-2:BookFairy michelleglauser$ pip install -r requirements.txt
Requirement already satisfied (use --upgrade to upgrade): Django==1.4.2 in ./venv/lib/python2.7/site-packages (from -r requirements.txt (line 1))
Requirement already satisfied (use --upgrade to upgrade): South==0.7.6 in ./venv/lib/python2.7/site-packages (from -r requirements.txt (line 2))
Requirement already satisfied (use --upgrade to upgrade): wsgiref==0.1.2 in /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7 (from -r requirements.txt (line 3))
Cleaning up...
(venv)Michelles-MacBook-Pro-2:BookFairy michelleglauser$ pip install pyquery
Requirement already satisfied (use --upgrade to upgrade): pyquery in ./venv/lib/python2.7/site-packages
Requirement already satisfied (use --upgrade to upgrade): lxml>=2.1 in ./venv/lib/python2.7/site-packages (from pyquery)
Requirement already satisfied (use --upgrade to upgrade): cssselect in ./venv/lib/python2.7/site-packages (from pyquery)
Cleaning up...
(venv)Michelles-MacBook-Pro-2:BookFairy michelleglauser$ import requests
-bash: import: command not found
(venv)Michelles-MacBook-Pro-2:BookFairy michelleglauser$ python
Python 2.7.1 (r271:86832, Jun 16 2011, 16:59:05) 
[GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2335.15.00)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named requests
>>> from pyquery import PyQuery as pq
import requests


>>> import requests
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named requests
>>> 
>>> 
>>> 
KeyboardInterrupt
>>> ^D
(venv)Michelles-MacBook-Pro-2:BookFairy michelleglauser$ python
Python 2.7.1 (r271:86832, Jun 16 2011, 16:59:05) 
[GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2335.15.00)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from pyquery import PyQuery as pq
>>> f = open("index.htmlm", 'r")
  File "<stdin>", line 1
    f = open("index.htmlm", 'r")
                               ^
SyntaxError: EOL while scanning string literal
>>> f = open("index.htmlm", 'r')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IOError: [Errno 2] No such file or directory: 'index.htmlm'
>>> f = open("index.html", 'r')
>>> jQuery = PyQuery(f.read())
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'PyQuery' is not defined
>>> from pyquery import PyQuery 
>>> jQuery = PyQuery(f.read())
>>> title = jQuery("title")
>>> title
[<title>]
>>> title.text()
'My title'
>>> title.html()
'My title'
>>> r = requests.get("http://sflib1.sfpl.org/search/X?SEARCH=A+Tree+Grows+in+Brooklyn+Betty+Smith&x=0&y=0&searchscope=3&p=&l=eng&m=a&Da=&Db=&SORT=D")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'requests' is not defined
>>> import requests
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named requests
>>> import requests
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named requests
>>> 
KeyboardInterrupt
>>> ^D
(venv)Michelles-MacBook-Pro-2:BookFairy michelleglauser$ pip install requests
Downloading/unpacking requests
  Downloading requests-0.14.2.tar.gz (361kB): 361kB downloaded
  Running setup.py egg_info for package requests
    
    warning: no files found matching 'tests/*.'
Installing collected packages: requests
  Running setup.py install for requests
    
    warning: no files found matching 'tests/*.'
Successfully installed requests
Cleaning up...
(venv)Michelles-MacBook-Pro-2:BookFairy michelleglauser$ python
Python 2.7.1 (r271:86832, Jun 16 2011, 16:59:05) 
[GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2335.15.00)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests
>>> r = requests.get("http://sflib1.sfpl.org/search/X?SEARCH=A+Tree+Grows+in+Brooklyn+Betty+Smith&x=0&y=0&searchscope=3&p=&l=eng&m=a&Da=&Db=&SORT=D")
jQ>>> jQuery = PyQuery(r.content)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'PyQuery' is not defined
>>> from pyquery import PyQuery
>>> r = requests.get("http://sflib1.sfpl.org/search/X?SEARCH=A+Tree+Grows+in+Brooklyn+Betty+Smith&x=0&y=0&searchscope=3&p=&l=eng&m=a&Da=&Db=&SORT=D")
j>>> jQuery = PyQuery(r.content)
>>> rows = jQuery("tr.briefCitRow")
>>> rows
[<tr.briefCitRow>, <tr.briefCitRow>]
>>> likelyBook = rows[0]
>>> likelyBook = jQuery(rows[0])
>>> likelyBook
[<tr.briefCitRow>]
>>> book = jQuery(likelyBook).children(">>> >>> 
>>> dir(file)
['__class__', '__delattr__', '__doc__', '__enter__', '__exit__', '__format__', '__getattribute__', '__hash__', '__init__', '__iter__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'close', 'closed', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'mode', 'name', 'newlines', 'next', 'read', 'readinto', 'readline', 'readlines', 'seek', 'softspace', 'tell', 'truncate', 'write', 'writelines', 'xreadlines']
>>> 
Last login: Tue Nov 27 09:17:17 on console
Michelles-MacBook-Pro-2:BookFairy michelleglauser$ python
Python 2.7.1 (r271:86832, Jun 16 2011, 16:59:05) 
[GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2335.15.00)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> gr_response = requests.get(http://www.goodreads.com/search?utf8=%E2%9C%93&q=atlas+shrugged+ayn+rand&search_type=books)
  File "<stdin>", line 1
    gr_response = requests.get(http://www.goodreads.com/search?utf8=%E2%9C%93&q=atlas+shrugged+ayn+rand&search_type=books)
                                   ^
SyntaxError: invalid syntax
>>> gr_url = http://www.goodreads.com/search?utf8=%E2%9C%93&q=atlas+shrugged+ayn+rand&search_type=books
  File "<stdin>", line 1
    gr_url = http://www.goodreads.com/search?utf8=%E2%9C%93&q=atlas+shrugged+ayn+rand&search_type=books
                 ^
SyntaxError: invalid syntax
>>> gr_url = "http://www.goodreads.com/search?utf8=%E2%9C%93&q=atlas+shrugged+ayn+rand&search_type=books"
>>> gr_response = requests.get(gr_url)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'requests' is not defined
>>> import requests
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named requests
>>> from pyquery import PyQuery
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named pyquery
>>> from pyquery import pq
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named pyquery
>>> from pyquery import PyQuery as pq
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named pyquery
>>> 
KeyboardInterrupt
>>> ^D
Michelles-MacBook-Pro-2:BookFairy michelleglauser$ . venv/bin/activate
(venv)Michelles-MacBook-Pro-2:BookFairy michelleglauser$ python
Python 2.7.1 (r271:86832, Jun 16 2011, 16:59:05) 
[GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2335.15.00)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests
>>> import pyquery import PyQuery as pq
  File "<stdin>", line 1
    import pyquery import PyQuery as pq
                        ^
SyntaxError: invalid syntax
>>> from pyquery import PyQuery as pq
>>> gr_response = requests.get(gr_url)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'gr_url' is not defined
>>> gr_url = "http://www.goodreads.com/search?utf8=%E2%9C%93&q=atlas+shrugged+ayn+rand&search_type=books"
>>> gr_response = requests.get(gr_url)
>>> pyed_gr_data = pq(gr_response.content)
>>> pyed_gr_data("rating").text()
>>> pyed_gr_data("minirating").text()
>>> a = pyed_gr_data("minirating").text()
>>> print a
None
>>> a = pyed_gr_data("span class").text()
>>> print a
None
>>> a = pyed_gr_data("span").text()
>>> print a
books (Goodreads search in 0.05s) Atlas Shrugged by Ayn Rand , Leonard Peikoff (Goodreads Author) (Introduction) Ayn Rand Leonard Peikoff (Goodreads Author) (Introduction) 3.69 avg rating — 119,424 ratings —
              published
             1957
            — 76 editions 3.69 avg rating — 119,424 ratings Want to Read savingâ¦ Want to Read Currently Reading Read Atlas Shrugged & The Fountainhead by Ayn Rand Ayn Rand 4.02 avg rating — 2,283 ratings —
              published
             1995
            — 3 editions 4.02 avg rating — 2,283 ratings Want to Read savingâ¦ Want to Read Currently Reading Read Essays on Ayn Rand's Atlas Shrugged by Robert Mayhew (Editor) Robert Mayhew (Editor) 3.89 avg rating — 18 ratings —
              published
             2009
            — 2 editions 3.89 avg rating — 18 ratings Want to Read savingâ¦ Want to Read Currently Reading Read Quicklet-Ayn Rand's Atlas Shrugged by Jason Malcolm Stewart (Goodreads Author) Jason Malcolm Stewart (Goodreads Author) 5.00 avg rating — 1 rating —
              published
             2012
            — 1 edition 5.00 avg rating — 1 rating Want to Read savingâ¦ Want to Read Currently Reading Read Ayn Rand's Atlas Shrugged: A Philosophical and Literary Companion by Edward Wayne Younkins Edward Wayne Younkins 3.86 avg rating — 7 ratings —
              published
             2007
            — 1 edition 3.86 avg rating — 7 ratings Want to Read savingâ¦ Want to Read Currently Reading Read Atlas Shrugged Part A: New Edition by Ayn Rand , Scott Brick (Read by) Ayn Rand Scott Brick (Read by) 4.00 avg rating — 84 ratings — 5 editions 4.00 avg rating — 84 ratings Want to Read savingâ¦ Want to Read Currently Reading Read Ayn Rand's Atlas Shrugged: A Philosophical and Literary Companion by Edward W. Younkins (Editor) Edward W. Younkins (Editor) 3.50 avg rating — 2 ratings —
              published
             2007
            — 2 editions 3.50 avg rating — 2 ratings Want to Read savingâ¦ Want to Read Currently Reading Read Atlas Shrugged by Andrew Bernstein , CliffsNotes , Ayn Rand Andrew Bernstein CliffsNotes Ayn Rand 4.12 avg rating — 41 ratings —
              published
             2000
            — 10 editions 4.12 avg rating — 41 ratings Want to Read savingâ¦ Want to Read Currently Reading Read Atlas Shrugged Part B: New Edition by Ayn Rand , Scott Brick (Narrator) Ayn Rand Scott Brick (Narrator) 3.93 avg rating — 28 ratings — 4 editions 3.93 avg rating — 28 ratings Want to Read savingâ¦ Want to Read Currently Reading Read Atlas Shrugged Part C: New Edition by Ayn Rand Ayn Rand 3.78 avg rating — 23 ratings — 4 editions 3.78 avg rating — 23 ratings Want to Read savingâ¦ Want to Read Currently Reading Read Novels by Ayn Rand: We the Living, Atlas Shrugged, the Fountainhead by Books LLC Books LLC 4.50 avg rating — 16 ratings —
              published
             2010
            — 1 edition 4.50 avg rating — 16 ratings Want to Read savingâ¦ Want to Read Currently Reading Read Atlas Shrugged (SparkNotes Literature Guides) by SparkNotes Editors , Ayn Rand , SparkNotes SparkNotes Editors Ayn Rand SparkNotes 4.25 avg rating — 8 ratings —
              published
             2003
            — 3 editions 4.25 avg rating — 8 ratings Want to Read savingâ¦ Want to Read Currently Reading Read Atlas Shrugged by Ayn Rand Ayn Rand 0.00 avg rating — 0 ratings —
              published
             1957
            — 1 edition 0.00 avg rating — 0 ratings Want to Read savingâ¦ Want to Read Currently Reading Read Why Businessmen Need Philosophy: The Capitalist's Guide to the Ideas Behind Ayn Rand's AtlasShrugged by Richard E. Ralston (Editor) , John A. Allison (Introduction) Richard E. Ralston (Editor) John A. Allison (Introduction) 4.08 avg rating — 12 ratings —
              published
             2011
            — 3 editions 4.08 avg rating — 12 ratings Want to Read savingâ¦ Want to Read Currently Reading Read Works by Ayn Rand (Book Guide): Ayn Rand Characters, Books by Ayn Rand, Novels by Ayn Rand, Plays by Ayn Rand, We the Living, Atlas Shrugged by Source Wikipedia Source Wikipedia 5.00 avg rating — 1 rating —
              published
             2010
            — 1 edition 5.00 avg rating — 1 rating Want to Read savingâ¦ Want to Read Currently Reading Read Articles on Novels by Ayn Rand, Including: The Fountainhead, Anthem (Novella), We the Living, Atlas Shrugged by Hephaestus Books Hephaestus Books 3.00 avg rating — 1 rating —
              published
             2011
            — 1 edition 3.00 avg rating — 1 rating Want to Read savingâ¦ Want to Read Currently Reading Read (63,594,326) (20,886,739) (1,284,728) (1,274,066) (1,011,448) (937,058) (884,426) (744,412) (561,798) (556,647) (436,827) (425,783) (412,276) (398,325) (385,283) (290,321) (283,966) (235,009) (214,918) (209,828) (178,252) (165,436) (164,380) (147,974) (136,909) (130,823) (125,319) (123,457) (118,967) (113,969) (107,930) (101,644) (93,384) (89,549) (88,748) (84,012) (77,522) (71,292) (63,001) (57,512) (52,305) (40,048) (30,880) (30,854) (3,146) (310) (299)
>>> a = pyed_gr_data("span.minirating").text()
>>> print a
3.69 avg rating — 119,424 ratings 4.02 avg rating — 2,283 ratings 3.89 avg rating — 18 ratings 5.00 avg rating — 1 rating 3.86 avg rating — 7 ratings 4.00 avg rating — 84 ratings 3.50 avg rating — 2 ratings 4.12 avg rating — 41 ratings 3.93 avg rating — 28 ratings 3.78 avg rating — 23 ratings 4.50 avg rating — 16 ratings 4.25 avg rating — 8 ratings 0.00 avg rating — 0 ratings 4.08 avg rating — 12 ratings 5.00 avg rating — 1 rating 3.00 avg rating — 1 rating
>>> a = pyed_gr_data("span.minirating").eq()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: eq() takes exactly 2 arguments (1 given)
>>> a = pyed_gr_data("span.minirating").eq(0)
>>> print a
<span class="minirating"><span class="stars"><img alt="3.69 of 5 stars" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.69 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.69 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.69 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/stars/red_star_66pct-a2f513494595fa112f4762672b33daef.png" title="3.69 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="3.69 of 5 stars" width="12"/></span> 3.69 avg rating &#8212; 119,424 ratings</span>
            &#8212;
              published
             1957
            &#8212;
            
>>> a = pyed_gr_data("span.minirating").text(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/michelleglauser/Desktop/BookFairy/venv/lib/python2.7/site-packages/pyquery/pyquery.py", line 964, in text
    tag.text = value
  File "lxml.etree.pyx", line 922, in lxml.etree._Element.text.__set__ (src/lxml/lxml.etree.c:40255)
  File "apihelpers.pxi", line 664, in lxml.etree._setNodeText (src/lxml/lxml.etree.c:18233)
  File "apihelpers.pxi", line 1337, in lxml.etree._utf8 (src/lxml/lxml.etree.c:23861)
TypeError: Argument must be bytes or unicode, got 'int'
>>> a = pyed_gr_data("span.stars").eq(0)
>>> print a
<span class="stars" id="starsstars_for_1_book_662" onmouseout="mouseOutStars('stars_for_1_book_662')"><a rel="nofollow"><img alt="didn't like it " class="star" height="15" id="starstars_for_1_book_662_0" onclick="submitStars('stars_for_1_book_662', 0, '/review/rate/662?rating=1&amp;wtr_button_id=1_book_662', 0);  return false;" onmouseover="checkStars('stars_for_1_book_662', 0)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="didn't like it" width="15"/></a><a rel="nofollow"><img alt="it was ok " class="star" height="15" id="starstars_for_1_book_662_1" onclick="submitStars('stars_for_1_book_662', 1, '/review/rate/662?rating=2&amp;wtr_button_id=1_book_662', 0);  return false;" onmouseover="checkStars('stars_for_1_book_662', 1)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was ok" width="15"/></a><a rel="nofollow"><img alt="liked it " class="star" height="15" id="starstars_for_1_book_662_2" onclick="submitStars('stars_for_1_book_662', 2, '/review/rate/662?rating=3&amp;wtr_button_id=1_book_662', 0);  return false;" onmouseover="checkStars('stars_for_1_book_662', 2)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="liked it" width="15"/></a><a rel="nofollow"><img alt="really liked it " class="star" height="15" id="starstars_for_1_book_662_3" onclick="submitStars('stars_for_1_book_662', 3, '/review/rate/662?rating=4&amp;wtr_button_id=1_book_662', 0);  return false;" onmouseover="checkStars('stars_for_1_book_662', 3)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="really liked it" width="15"/></a><a rel="nofollow"><img alt="it was amazing " class="star" height="15" id="starstars_for_1_book_662_4" onclick="submitStars('stars_for_1_book_662', 4, '/review/rate/662?rating=5&amp;wtr_button_id=1_book_662', 0);  return false;" onmouseover="checkStars('stars_for_1_book_662', 4)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was amazing" width="15"/></a></span>
>>> a = pyed_gr_data("span.minirating").eq(0)
>>> print a
<span class="minirating"/>
            &#8212;
              published
             1957
            &#8212;
            
>>> a = pyed_gr_data("span.minirating").eq(0)
>>> pyed_gr_data
[<html>]
>>> d = pyed_gr_data
>>> d
[<html>]
>>> type(d)
<class 'pyquery.pyquery.PyQuery'>
>>> dir(d)
['Fn', '__add__', '__call__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__dict__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__html__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', '__unicode__', '__weakref__', '_append', '_base_url', '_css_to_xpath', '_extend', '_filter_only', '_get_root', '_nextAll', '_parent', '_prevAll', '_translator', '_traverse', '_traverse_parent_topdown', 'addClass', 'after', 'append', 'appendTo', 'attr', 'base_url', 'before', 'children', 'clone', 'closest', 'count', 'css', 'each', 'empty', 'encoding', 'end', 'eq', 'extend', 'filter', 'find', 'fn', 'hasClass', 'height', 'hide', 'html', 'index', 'insert', 'insertAfter', 'insertBefore', 'is_', 'length', 'make_links_absolute', 'map', 'next', 'nextAll', 'not_', 'outerHtml', 'parent', 'parents', 'parser', 'pop', 'prepend', 'prependTo', 'prev', 'prevAll', 'remove', 'removeAttr', 'removeClass', 'replaceAll', 'replaceWith', 'reverse', 'root', 'show', 'siblings', 'size', 'sort', 'text', 'toggleClass', 'val', 'width', 'wrap', 'wrapAll']
>>> d.children
<bound method PyQuery.children of [<html>]>
>>> d.children()
[<head>, <body>]
>>> d.text
<bound method PyQuery.text of [<html>]>
>>> d.text()
u'Search results for "atlas shrugged ayn rand" (showing 1-16 of 16 books) [if lte IE 6]>\n    <link href="http://s.gr-assets.com/assets/ie6-4b79910cd43c47d41679e594015f7812.css" media="screen" rel="stylesheet" type="text/css" />\n\n    <script type="text/javascript">\n//<![CDATA[\n\n      try {\n        document.execCommand("BackgroundImageCache", false, true);\n      }\n      catch(err) {}\n\n//]]>\n</script>  <![endif] [if lt IE 9]>\n    <link href="http://s.gr-assets.com/assets/ie-eceebdfd8a734989e3084ce9e3e5b0d6.css" media="screen" rel="stylesheet" type="text/css" />\n  <![endif] [if lt IE 8]>\n    <link href="http://s.gr-assets.com/assets/common_images_ie-dada5b234de40a7e790683ee7a72e00c.css" media="screen" rel="stylesheet" type="text/css" />\n  <![endif] [if gte IE 8]><! <![endif] #searchButton {\n\t\tpadding-top: 5px;\n\t} register tour sign in setDefaultText(\'sitesearch_field\', \'Title / Author / ISBN\') Home My Books Friends Recommendations listopia giveaways popular goodreads voice ebooks fun trivia quizzes quotes community groups creative writing people events Explore GS_googleAddAdSenseService("ca-pub-7284881071421289")\n    GS_googleEnableAllServices() GA_googleAddAttr("sid", "270079165977cf67d29feef7b0b8d36d")\n            GA_googleAddAttr("shelf", "adult")\n            GA_googleAddAttr("shelf", "owned")\n            GA_googleAddAttr("shelf", "audio")\n            GA_googleAddAttr("shelf", "neverfinished")\n            GA_googleAddAttr("shelf", "economics")\n            GA_googleAddAttr("shelf", "literary")\n            GA_googleAddAttr("shelf", "novels")\n            GA_googleAddAttr("shelf", "capitalism")\n            GA_googleAddAttr("shelf", "scifi")\n            GA_googleAddAttr("shelf", "wishlist")\n            GA_googleAddAttr("shelf", "2012")\n            GA_googleAddAttr("shelf", "favorites")\n        GA_googleAddAttr("gtargeting", "bstqdj64n5") Search by Book Title, Author, or ISBN document.searchForm.search_query_main.focus(); all results books groups quotes events stories people listopia trivia current_tabs[776401595] = \'books\';\n\n  Event.observe(window, \'load\', function(e) {\n    // Switch to an anchored tab if specified in the URL\n    if (location.href.include(\'#\')) {\n      var tabID = location.href.split(\'#\')[1];\n      if (tabID != \'\' && $(tabID)) {\n        changeTab(tabID)\n      }\n    }\n  }) Showing 1-16 of  16 results for \'atlas shrugged ayn rand\' (Goodreads search in 0.05s) document.onclick = checkOpenSelects;\n\n  function submitShelfLink(unique_id, book_id, shelf_id, shelf_name, submit_form, exclusive) {\n    var checkbox_id = \'shelf_name_\' + unique_id + \'_\' + shelf_id;\n    var element = document.getElementById(checkbox_id)\n\n    var checked = element.checked\n    if (checked && exclusive) {\n      // can\'t uncheck a radio by clicking it!\n      return\n    }\n    if(document.getElementById("savingMessage")){\n      Element.show(\'savingMessage\')\n    }\n    var element_id = \'shelfInDropdownName_\' + unique_id + \'_\' + shelf_id;\n    Element.update(element_id, "saving...");\n    if (submit_form) {\n      Element.hide(\'shelfDropdown_\' + unique_id)\n      var form = document.getElementById(\'addBookForm\' + book_id)\n      if (form) {\n        form.shelf.value = shelf_name\n        form.onsubmit()\n      }\n    }\n    else {\n      var action = checked ? \'remove\' : \'\'\n      element.checked = !element.checked\n      new Ajax.Request(\'/shelf/add_to_shelf\', {asynchronous:true, evalScripts:true, onSuccess:function(request){shelfSubmitted(request, book_id, checkbox_id, element_id, unique_id, shelf_name)}, parameters:\'book_id=\' + book_id + \'&name=\' + shelf_name + \'&a=\' + action + \'&authenticity_token=\' + encodeURIComponent(\'55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4=\')})\n    }\n  }\n\n  function shelfSubmitted(request, book_id, checkbox_id, element_id, unique_id, shelf_name) {\n    Element.update(\'shelfListfalse_\' + book_id, request.responseText)\n    afterShelfSave(checkbox_id, element_id, unique_id, shelf_name.escapeHTML())\n  }\n\n  function refreshGroupBox(group_id, book_id) {\n    new Ajax.Updater(\'addGroupBooks\' + book_id + \'\', \'/group/add_book_box\', {asynchronous:true, evalScripts:true, onSuccess:function(request){refreshGroupBoxComplete(request, book_id);}, parameters:\'id=\' + group_id + \'&book_id=\' + book_id + \'&refresh=true\' + \'&authenticity_token=\' + encodeURIComponent(\'55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4=\')})\n  } Atlas Shrugged by Ayn Rand , Leonard Peikoff (Goodreads Author) (Introduction) \u2014\n              published\n             1957\n            \u2014 76 editions Want to Read saving\xe2\x80\xa6 Want to Read Currently Reading Read Rate this book Clear rating starRatings[ratingIndex++] = [ \'stars_for_1_book_662\', -1]; checkStars(\'stars_for_1_book_662\', -1); Atlas Shrugged & The Fountainhead by Ayn Rand 4.02 avg rating \u2014 2,283 ratings \u2014\n              published\n             1995\n            \u2014 3 editions Want to Read saving\xe2\x80\xa6 Want to Read Currently Reading Read Rate this book Clear rating starRatings[ratingIndex++] = [ \'stars_for_2_book_2115\', -1]; checkStars(\'stars_for_2_book_2115\', -1); Essays on Ayn Rand\'s Atlas Shrugged by Robert Mayhew (Editor) 3.89 avg rating \u2014 18 ratings \u2014\n              published\n             2009\n            \u2014 2 editions Want to Read saving\xe2\x80\xa6 Want to Read Currently Reading Read Rate this book Clear rating starRatings[ratingIndex++] = [ \'stars_for_3_book_6234337\', -1]; checkStars(\'stars_for_3_book_6234337\', -1); Quicklet-Ayn Rand\'s Atlas Shrugged by Jason Malcolm Stewart (Goodreads Author) 5.00 avg rating \u2014 1 rating \u2014\n              published\n             2012\n            \u2014 1 edition Want to Read saving\xe2\x80\xa6 Want to Read Currently Reading Read Rate this book Clear rating starRatings[ratingIndex++] = [ \'stars_for_4_book_13607666\', -1]; checkStars(\'stars_for_4_book_13607666\', -1); Ayn Rand\'s Atlas Shrugged: A Philosophical and Literary Companion by Edward Wayne Younkins 3.86 avg rating \u2014 7 ratings \u2014\n              published\n             2007\n            \u2014 1 edition Want to Read saving\xe2\x80\xa6 Want to Read Currently Reading Read Rate this book Clear rating starRatings[ratingIndex++] = [ \'stars_for_5_book_201237\', -1]; checkStars(\'stars_for_5_book_201237\', -1); Atlas Shrugged Part A: New Edition by Ayn Rand , Scott Brick (Read by) 4.00 avg rating \u2014 84 ratings \u2014 5 editions Want to Read saving\xe2\x80\xa6 Want to Read Currently Reading Read Rate this book Clear rating starRatings[ratingIndex++] = [ \'stars_for_6_book_5755462\', -1]; checkStars(\'stars_for_6_book_5755462\', -1); Ayn Rand\'s Atlas Shrugged: A Philosophical and Literary Companion by Edward W. Younkins (Editor) 3.50 avg rating \u2014 2 ratings \u2014\n              published\n             2007\n            \u2014 2 editions Want to Read saving\xe2\x80\xa6 Want to Read Currently Reading Read Rate this book Clear rating starRatings[ratingIndex++] = [ \'stars_for_7_book_831567\', -1]; checkStars(\'stars_for_7_book_831567\', -1); Atlas Shrugged by Andrew Bernstein , CliffsNotes , Ayn Rand 4.12 avg rating \u2014 41 ratings \u2014\n              published\n             2000\n            \u2014 10 editions Want to Read saving\xe2\x80\xa6 Want to Read Currently Reading Read Rate this book Clear rating starRatings[ratingIndex++] = [ \'stars_for_8_book_9364\', -1]; checkStars(\'stars_for_8_book_9364\', -1); Atlas Shrugged Part B: New Edition by Ayn Rand , Scott Brick (Narrator) 3.93 avg rating \u2014 28 ratings \u2014 4 editions Want to Read saving\xe2\x80\xa6 Want to Read Currently Reading Read Rate this book Clear rating starRatings[ratingIndex++] = [ \'stars_for_9_book_5430955\', -1]; checkStars(\'stars_for_9_book_5430955\', -1); Atlas Shrugged Part C: New Edition by Ayn Rand 3.78 avg rating \u2014 23 ratings \u2014 4 editions Want to Read saving\xe2\x80\xa6 Want to Read Currently Reading Read Rate this book Clear rating starRatings[ratingIndex++] = [ \'stars_for_10_book_5141345\', -1]; checkStars(\'stars_for_10_book_5141345\', -1); Novels by Ayn Rand: We the Living, Atlas Shrugged, the Fountainhead by Books LLC 4.50 avg rating \u2014 16 ratings \u2014\n              published\n             2010\n            \u2014 1 edition Want to Read saving\xe2\x80\xa6 Want to Read Currently Reading Read Rate this book Clear rating starRatings[ratingIndex++] = [ \'stars_for_11_book_9017523\', -1]; checkStars(\'stars_for_11_book_9017523\', -1); Atlas Shrugged (SparkNotes Literature Guides) by SparkNotes Editors , Ayn Rand , SparkNotes 4.25 avg rating \u2014 8 ratings \u2014\n              published\n             2003\n            \u2014 3 editions Want to Read saving\xe2\x80\xa6 Want to Read Currently Reading Read Rate this book Clear rating starRatings[ratingIndex++] = [ \'stars_for_12_book_181147\', -1]; checkStars(\'stars_for_12_book_181147\', -1); Atlas Shrugged by Ayn Rand 0.00 avg rating \u2014 0 ratings \u2014\n              published\n             1957\n            \u2014 1 edition Want to Read saving\xe2\x80\xa6 Want to Read Currently Reading Read Rate this book Clear rating starRatings[ratingIndex++] = [ \'stars_for_13_book_16135783\', -1]; checkStars(\'stars_for_13_book_16135783\', -1); Why Businessmen Need Philosophy: The Capitalist\'s Guide to the Ideas Behind Ayn Rand\'s AtlasShrugged by Richard E. Ralston (Editor) , John A. Allison (Introduction) 4.08 avg rating \u2014 12 ratings \u2014\n              published\n             2011\n            \u2014 3 editions Want to Read saving\xe2\x80\xa6 Want to Read Currently Reading Read Rate this book Clear rating starRatings[ratingIndex++] = [ \'stars_for_14_book_9577604\', -1]; checkStars(\'stars_for_14_book_9577604\', -1); Works by Ayn Rand (Book Guide): Ayn Rand Characters, Books by Ayn Rand, Novels by Ayn Rand, Plays by Ayn Rand, We the Living, Atlas Shrugged by Source Wikipedia 5.00 avg rating \u2014 1 rating \u2014\n              published\n             2010\n            \u2014 1 edition Want to Read saving\xe2\x80\xa6 Want to Read Currently Reading Read Rate this book Clear rating starRatings[ratingIndex++] = [ \'stars_for_15_book_9935187\', -1]; checkStars(\'stars_for_15_book_9935187\', -1); Articles on Novels by Ayn Rand, Including: The Fountainhead, Anthem (Novella), We the Living, Atlas Shrugged by Hephaestus Books 3.00 avg rating \u2014 1 rating \u2014\n              published\n             2011\n            \u2014 1 edition Want to Read saving\xe2\x80\xa6 Want to Read Currently Reading Read Rate this book Clear rating starRatings[ratingIndex++] = [ \'stars_for_16_book_12716520\', -1]; checkStars(\'stars_for_16_book_12716520\', -1); Manually add a book Import books GA_googleAddSlot("ca-pub-7284881071421289", "Search") GA_googleFetchAds() GA_googleFillSlot("Search") Related Shelves to-read (63,594,326) currently-reading (20,886,739) favorites (1,284,728) fiction (1,274,066) fantasy (1,011,448) own (937,058) wishlist (884,426) 2012 (744,412) owned (561,798) books-i-own (556,647) kindle (436,827) library (425,783) wish-list (412,276) classics (398,325) to-buy (385,283) 2011 (290,321) science-fiction (283,966) adult (235,009) sci-fi (214,918) i-own (209,828) favourites (178,252) novels (165,436) literature (164,380) novel (147,974) philosophy (136,909) audiobook (130,823) book-club (125,319) adult-fiction (123,457) classic (118,967) audio (113,969) abandoned (107,930) general-fiction (101,644) unfinished (93,384) politics (89,549) american (88,748) all-time-favorites (84,012) dystopian (77,522) dystopia (71,292) literary-fiction (63,001) literary (57,512) never-finished (52,305) political (40,048) classic-literature (30,880) economics (30,854) capitalism (3,146) objectivism (310) ayn-rand (299) More shelves... var pageOptions = {\n    \'pubId\' : \'pub-7284881071421289\',\n    \'query\' : \'atlas shrugged ayn rand buy books\',\n    \'channel\' : \'4204718441\',\n    \'hl\' : \'en\'\n  };\n\n  var adblock1 = {\n    \'container\' : \'adcontainer1\',\n    \'colorTitleLink\' : \'#666600\',\n    \'colorDomainLink\' : \'#215625\'\n  };\n\n  var adblock2 = {\n    \'container\' : \'adcontainer2\',\n    \'colorTitleLink\' : \'#666600\',\n    \'colorDomainLink\' : \'#215625\'\n  };\n\n  new google.ads.search.Ads(pageOptions, adblock1, adblock2); \xa9 2012 Goodreads Inc about us advertise author program jobs api our blog terms privacy help close Welcome back. Just a moment while we sign you in to your Goodreads account. function loadFacebookScripts() {\n    \n  }\n\n  window._fb_app_id = \'2415071772\';\n\n  window._gr_session = \'false\'\n  window._no_gr_account = \'false\'\n  window._suppress_auto_login = ""\n\n  window.fbAsyncInit = function() {\n    GR_Facebook.initialize();\n    loadFacebookScripts();\n  };\n\n  (function(d){\n     var js, id = \'facebook-jssdk\', ref = d.getElementsByTagName(\'script\')[0];\n     if (d.getElementById(id)) {return;}\n     js = d.createElement(\'script\'); js.id = id; js.async = true;\n     js.src = "//connect.facebook.net/en_US/all.js";\n     ref.parentNode.insertBefore(js, ref);\n   }(document)); //<![CDATA[\n\n    var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");\n    document.write(unescape("%3Cscript src=\'" + gaJsHost + "google-analytics.com/ga.js\' type=\'text/javascript\'%3E%3C/script%3E"));\n\n//]]> //<![CDATA[\n\n    try {\n      var pageTracker = _gat._createTracker("UA-968618-1");\n      pageTracker._setCustomVar(1, "User Status", "signed_out", 2);\n      pageTracker._trackPageview();\n    }\n    catch(err) {}\n\n//]]> //<![CDATA[\n\n    _qoptions={\n    qacct:"p-0dUe_kJAjvkoY"\n    };\n\n//]]> //<![CDATA[\n\n    document.write(unescape("%3Cscript src=\'" + (document.location.protocol == "https:" ? "https://sb" : "http://b") + ".scorecardresearch.com/beacon.js\' %3E%3C/script%3E"));\n\n//]]> //<![CDATA[\n\n    COMSCORE.beacon({\n      c1:2,\n      c2:6035830,\n      c3:"",\n      c4:"",\n      c5:"",\n      c6:"",\n      c15:""\n    });\n\n//]]>'
>>> dir(d)
['Fn', '__add__', '__call__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__dict__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__html__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', '__unicode__', '__weakref__', '_append', '_base_url', '_css_to_xpath', '_extend', '_filter_only', '_get_root', '_nextAll', '_parent', '_prevAll', '_translator', '_traverse', '_traverse_parent_topdown', 'addClass', 'after', 'append', 'appendTo', 'attr', 'base_url', 'before', 'children', 'clone', 'closest', 'count', 'css', 'each', 'empty', 'encoding', 'end', 'eq', 'extend', 'filter', 'find', 'fn', 'hasClass', 'height', 'hide', 'html', 'index', 'insert', 'insertAfter', 'insertBefore', 'is_', 'length', 'make_links_absolute', 'map', 'next', 'nextAll', 'not_', 'outerHtml', 'parent', 'parents', 'parser', 'pop', 'prepend', 'prependTo', 'prev', 'prevAll', 'remove', 'removeAttr', 'removeClass', 'replaceAll', 'replaceWith', 'reverse', 'root', 'show', 'siblings', 'size', 'sort', 'text', 'toggleClass', 'val', 'width', 'wrap', 'wrapAll']
>>> d.html
<bound method PyQuery.html of [<html>]>
>>> d.html()
u'<head><meta name="google-site-verification" content="PfFjeZ9OK1RrUrKlmAPn_iZJ_vgHaZO1YQ-QlG2VsJs"/><title>Search results for "atlas shrugged ayn rand" (showing 1-16 of 16 books)</title><meta name="description" content="Search results for atlas shrugged ayn rand: Atlas Shrugged, Atlas Shrugged &amp; The Fountainhead, Essays on Ayn Rand\'s Atlas Shrugged, Quicklet-Ayn Rand\'s A..."/><meta name="verify-v1" content="cEf8XOH0pulh1aYQeZ1gkXHsQ3dMPSyIGGYqmF53690="/><meta name="apple-itunes-app" content="app-id=355833469"/><link href="http://s.gr-assets.com/assets/goodreads-4db08e118d7ff1c08adc9db069c433f3.css" media="screen" rel="stylesheet" type="text/css"/><script src="http://s.gr-assets.com/assets/application-2f2a647aee98bd5a09abb63a7ed24da2.js" type="text/javascript"/><meta content="authenticity_token" name="csrf-param"/><meta content="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4=" name="csrf-token"/><meta name="robots" content="noindex"/><!--[if lte IE 6]>\n    <link href="http://s.gr-assets.com/assets/ie6-4b79910cd43c47d41679e594015f7812.css" media="screen" rel="stylesheet" type="text/css" />\n\n    <script type="text/javascript">\n//<![CDATA[\n\n      try {\n        document.execCommand("BackgroundImageCache", false, true);\n      }\n      catch(err) {}\n\n//]]>\n</script>  <![endif]--><!--[if lt IE 9]>\n    <link href="http://s.gr-assets.com/assets/ie-eceebdfd8a734989e3084ce9e3e5b0d6.css" media="screen" rel="stylesheet" type="text/css" />\n  <![endif]--><!--[if lt IE 8]>\n    <link href="http://s.gr-assets.com/assets/common_images_ie-dada5b234de40a7e790683ee7a72e00c.css" media="screen" rel="stylesheet" type="text/css" />\n  <![endif]--><!--[if gte IE 8]><!--><link href="http://s.gr-assets.com/assets/common_images-f0478bd9a9b956ca6aab1e98bddd8b69.css" media="screen" rel="stylesheet" type="text/css"/><!--<![endif]--><style type="text/css" media="screen">\n\t#searchButton {\n\t\tpadding-top: 5px;\n\t}\n</style><link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="Goodreads"/></head><body><div class="content">\n  \n\n    <div class="uitext" id="siteheader">\n<div class="mainContent">\n<ul class="nav" id="usernav"><li>\n<strong>\n<a href="/user/new" class="navlink" rel="nofollow">register</a>\n</strong>\n</li>\n<li>\n<a href="/about/how_it_works" class="navlink" rel="nofollow">tour</a>\n</li>\n<li>\n<a href="/user/sign_in?returnurl=%2Fsearch%3Futf8%3D%25E2%259C%2593%26q%3Datlas%2Bshrugged%2Bayn%2Brand%26search_type%3Dbooks" class="navlink" rel="nofollow">sign in</a>\n</li>\n</ul><div id="logo">\n<a href="/">\n<img alt="Goodreads: Book reviews, recommendations, and discussion" border="0" src="http://s.gr-assets.com/assets/layout/goodreads_logo_140-d09dedbb00ba4219b00b356d39a980a8.png"/></a>\n</div>\n<div id="sitesearch">\n<form accept-charset="UTF-8" action="/search" method="get" name="headerSearchForm"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/></div>\n<div class="auto_complete_field_wrapper">\n<input id="sitesearch_field" name="query" type="text"/><script type="text/javascript" charset="utf-8">\n          setDefaultText(\'sitesearch_field\', \'Title / Author / ISBN\')\n        </script><div id="sitesearch_autocomplete"/>\n<img alt="Loading-trans" class="loading" id="sitesearch_field_loading" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif" style="display: none"/></div>\n<a class="submitLink" href="#" onclick="clearDefaultText(\'sitesearch_field\', \'Title / Author / ISBN\'); document.headerSearchForm.submit(); return false;"><img alt="search" src="http://s.gr-assets.com/assets/layout/magnifying_glass-06024a120abc83578b9c0b45241ee394.png" title="Title / Author / ISBN" width="16"/></a>\n</form>\n</div>\n\n<ul class="nav" id="sitenav"><li>\n<a href="/" class="navlink">Home</a>\n</li>\n<li>\n<a href="/review/list" class="navlink" rel="nofollow">My Books</a>\n</li>\n<li>\n<a href="/friend" class="navlink" rel="nofollow">Friends</a>\n</li>\n<li>\n<a href="/recommendations" class="navlink" rel="nofollow">Recommendations</a>\n</li>\n<li class="withsubnav">\n<div class="subnav">\n<ul class="content"><li>\n<a href="/list" title="Popular lists of books">listopia</a>\n</li>\n<li>\n<a href="/giveaway" title="Free book giveaways">giveaways</a>\n</li>\n<li>\n<a href="/book/popular_by_date/2012/11" title="Popular New Releases">popular</a>\n</li>\n<li>\n<a href="/voice">goodreads voice</a>\n</li>\n<li>\n<a href="/ebooks">ebooks</a>\n</li>\n</ul><ul class="content"><li>\n<b>\nfun\n</b>\n</li>\n<li>\n<a href="/trivia">trivia</a>\n</li>\n<li>\n<a href="/quizzes">quizzes</a>\n</li>\n<li>\n<a href="/quotes">quotes</a>\n</li>\n</ul><ul class="content"><li>\n<b>\ncommunity\n</b>\n</li>\n<li>\n<a href="/group">groups</a>\n</li>\n<li>\n<a href="/story">creative writing</a>\n</li>\n<li>\n<a href="/user/online_now" rel="nofollow">people</a>\n</li>\n<li>\n<a href="/event">events</a>\n</li>\n</ul></div>\n<a href="/book" class="navlink" title="Explore books">Explore</a>\n<a class="subnavlink inlineblock" href="#" onclick="HeaderNav.toggleSubnav({target: this}); return false;">\xa0</a>\n</li>\n</ul></div>\n</div>\n\n\n  \n\n  <div class="mainContentContainer ">\n    \n    <div class="mainContent">\n      \n\n\n<script type="text/javascript" src="http://partner.googleadservices.com/gampad/google_service.js">\n</script><script type="text/javascript">\n    GS_googleAddAdSenseService("ca-pub-7284881071421289")\n    GS_googleEnableAllServices()\n</script><script type="text/javascript">\n    GA_googleAddAttr("sid", "270079165977cf67d29feef7b0b8d36d")\n            GA_googleAddAttr("shelf", "adult")\n            GA_googleAddAttr("shelf", "owned")\n            GA_googleAddAttr("shelf", "audio")\n            GA_googleAddAttr("shelf", "neverfinished")\n            GA_googleAddAttr("shelf", "economics")\n            GA_googleAddAttr("shelf", "literary")\n            GA_googleAddAttr("shelf", "novels")\n            GA_googleAddAttr("shelf", "capitalism")\n            GA_googleAddAttr("shelf", "scifi")\n            GA_googleAddAttr("shelf", "wishlist")\n            GA_googleAddAttr("shelf", "2012")\n            GA_googleAddAttr("shelf", "favorites")\n        GA_googleAddAttr("gtargeting", "bstqdj64n5")\n</script><div class="mainContentFloat">\n        <div id="flashContainer">\n\n</div>\n        \n\n<div class="leftContainer">\n  <form accept-charset="UTF-8" action="/search" class="stacked" method="get" name="searchForm" style="width: 100%"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/></div>\n    <h1>\n    Search by Book Title, Author, or ISBN\n</h1>\n<div class="greyText" style="padding-bottom: 10px">\n  <input type="text" name="q" size="55" value="atlas shrugged ayn rand" id="search_query_main" style=""/><input type="hidden" name="search_type" value="books"/></div>\n<input class="button smallButton" style="margin-top: 2px" type="submit" value="search"/><div class="clear"/>\n\n</form>\n  <script type="text/javascript">\n    document.searchForm.search_query_main.focus();\n  </script><div>\n    <div class="tabs mediumTabs">\n        <a href="/search?q=atlas+shrugged+ayn+rand&amp;search%5Bsource%5D=goodreads&amp;search_type=all_results&amp;tab=all_results" class=" tab" id="all_resultsLink">all results</a>\n        <span class=" selectedTab" id="booksLink" url="{:q=&gt;&quot;atlas shrugged ayn rand&quot;, :search_type=&gt;&quot;books&quot;, :&quot;search[source]&quot;=&gt;&quot;goodreads&quot;, :&quot;search[field]&quot;=&gt;nil, :tab=&gt;&quot;books&quot;}">books</span>\n        <a href="/search?q=atlas+shrugged+ayn+rand&amp;search%5Bsource%5D=goodreads&amp;search_type=groups&amp;tab=groups" class=" tab" id="groupsLink">groups</a>\n        <a href="/search?q=atlas+shrugged+ayn+rand&amp;search%5Bsource%5D=goodreads&amp;search_type=quotes&amp;tab=quotes" class=" tab" id="quotesLink">quotes</a>\n        <a href="/search?q=atlas+shrugged+ayn+rand&amp;search%5Bsource%5D=goodreads&amp;search_type=events&amp;tab=events" class=" tab" id="eventsLink">events</a>\n        <a href="/search?q=atlas+shrugged+ayn+rand&amp;search%5Bsource%5D=goodreads&amp;search_type=stories&amp;tab=stories" class=" tab" id="storiesLink">stories</a>\n        <a href="/search?q=atlas+shrugged+ayn+rand&amp;search%5Bsource%5D=goodreads&amp;search_type=people&amp;tab=people" class=" tab" id="peopleLink">people</a>\n        <a href="/search?q=atlas+shrugged+ayn+rand&amp;search%5Bsource%5D=goodreads&amp;search_type=lists&amp;tab=lists" class=" tab" id="listsLink">listopia</a>\n        <a href="/search?q=atlas+shrugged+ayn+rand&amp;search%5Bsource%5D=goodreads&amp;search_type=trivia&amp;tab=trivia" class=" tab" id="triviaLink">trivia</a>\n<div class="clear"> </div></div><script type="text/javascript" charset="utf-8">\n  current_tabs[776401595] = \'books\';\n\n  Event.observe(window, \'load\', function(e) {\n    // Switch to an anchored tab if specified in the URL\n    if (location.href.include(\'#\')) {\n      var tabID = location.href.split(\'#\')[1];\n      if (tabID != \'\' &amp;&amp; $(tabID)) {\n        changeTab(tabID)\n      }\n    }\n  })\n</script></div>\n\n\n    <div id="adcontainer1"/>\n\n    <h3 class="searchSubNavContainer">Showing 1-16 of  16 results for \'atlas shrugged ayn rand\' <span class="smallText"> (Goodreads search in 0.05s)</span></h3>\n\n\n  \t  \t\t\n<script type="text/javascript" charset="utf-8">\n  document.onclick = checkOpenSelects;\n\n  function submitShelfLink(unique_id, book_id, shelf_id, shelf_name, submit_form, exclusive) {\n    var checkbox_id = \'shelf_name_\' + unique_id + \'_\' + shelf_id;\n    var element = document.getElementById(checkbox_id)\n\n    var checked = element.checked\n    if (checked &amp;&amp; exclusive) {\n      // can\'t uncheck a radio by clicking it!\n      return\n    }\n    if(document.getElementById("savingMessage")){\n      Element.show(\'savingMessage\')\n    }\n    var element_id = \'shelfInDropdownName_\' + unique_id + \'_\' + shelf_id;\n    Element.update(element_id, "saving...");\n    if (submit_form) {\n      Element.hide(\'shelfDropdown_\' + unique_id)\n      var form = document.getElementById(\'addBookForm\' + book_id)\n      if (form) {\n        form.shelf.value = shelf_name\n        form.onsubmit()\n      }\n    }\n    else {\n      var action = checked ? \'remove\' : \'\'\n      element.checked = !element.checked\n      new Ajax.Request(\'/shelf/add_to_shelf\', {asynchronous:true, evalScripts:true, onSuccess:function(request){shelfSubmitted(request, book_id, checkbox_id, element_id, unique_id, shelf_name)}, parameters:\'book_id=\' + book_id + \'&amp;name=\' + shelf_name + \'&amp;a=\' + action + \'&amp;authenticity_token=\' + encodeURIComponent(\'55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4=\')})\n    }\n  }\n\n  function shelfSubmitted(request, book_id, checkbox_id, element_id, unique_id, shelf_name) {\n    Element.update(\'shelfListfalse_\' + book_id, request.responseText)\n    afterShelfSave(checkbox_id, element_id, unique_id, shelf_name.escapeHTML())\n  }\n\n  function refreshGroupBox(group_id, book_id) {\n    new Ajax.Updater(\'addGroupBooks\' + book_id + \'\', \'/group/add_book_box\', {asynchronous:true, evalScripts:true, onSuccess:function(request){refreshGroupBoxComplete(request, book_id);}, parameters:\'id=\' + group_id + \'&amp;book_id=\' + book_id + \'&amp;refresh=true\' + \'&amp;authenticity_token=\' + encodeURIComponent(\'55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4=\')})\n  }\n</script><table cellspacing="0" cellpadding="0" border="0" width="100%" class="tableList"><tr itemscope="" itemtype="http://schema.org/Book"><td width="5%" valign="top">\n      <a name="662"/>\n      <a href="/book/show/662.Atlas_Shrugged" title="Atlas Shrugged">\n          <img alt="Atlas Shrugged" class="bookSmallImg" src="http://d.gr-assets.com/books/1347633289s/662.jpg"/></a>    </td>\n    <td width="100%" valign="top">\n      <a href="/book/show/662.Atlas_Shrugged" class="bookTitle" itemprop="url">\n        <span itemprop="name">Atlas Shrugged</span>\n</a>      <br/><span class="by smallText">by</span>\n<span itemprop="author" itemscope="" itemtype="http://schema.org/Person">\n<a href="http://www.goodreads.com/author/show/432.Ayn_Rand" class="authorName" itemprop="url"><span itemprop="name">Ayn Rand</span></a>, \n<a href="http://www.goodreads.com/author/show/1421.Leonard_Peikoff" class="authorName" itemprop="url"><span itemprop="name">Leonard Peikoff</span></a> <span class="greyText">(Goodreads Author)</span> <span class="authorName greyText smallText role">(Introduction)</span>\n</span>\n\n        <br/><span class="greyText smallText uitext">\n          <span class="minirating"/>\n            \u2014\n              published\n             1957\n            \u2014\n            <a href="/work/editions/817219-atlas-shrugged" class="greyText" rel="nofollow">76 editions</a>\n        </span>\n        \n\n\n    </td>\n\n      <td width="130px">\n          <div class="wtrButtonContainer wtrSignedOut" id="1_book_662">\n<div class="wtrUp wtrLeft">\n<form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="book_id" name="book_id" type="hidden" value="662"/><input id="name" name="name" type="hidden" value="to-read"/><input id="unique_id" name="unique_id" type="hidden" value="1_book_662"/><input id="wtr_new" name="wtr_new" type="hidden" value="true"/><button class="wtrToRead" type="submit">\n<span class="progressTrigger">Want to Read</span>\n<span class="progressIndicator">saving\xe2\x80\xa6</span>\n</button>\n</form>\n\n</div>\n\n<div class="wtrDivider"/>\n<div class="wtrRight">\n<button class="wtrShelfButton wtrUp">\n<img alt="pick shelf" src="http://s.gr-assets.com/assets/wtr_button/books-0866015891eb128cdc57e550383532a0.png"/></button>\n<div class="wtrShelfMenu">\n<ul class="wtrExclusiveShelves"><li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="1_book_662"/><input id="book_id" name="book_id" type="hidden" value="662"/><button class="wtrExclusiveShelf" name="name" type="submit" value="to-read">\n<span class="progressTrigger">Want to Read</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="1_book_662"/><input id="book_id" name="book_id" type="hidden" value="662"/><button class="wtrExclusiveShelf" name="name" type="submit" value="currently-reading">\n<span class="progressTrigger">Currently Reading</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="1_book_662"/><input id="book_id" name="book_id" type="hidden" value="662"/><button class="wtrExclusiveShelf" name="name" type="submit" value="read">\n<span class="progressTrigger">Read</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n</ul></div>\n</div>\n\n<div class="ratingStars wtrRating">\n<form accept-charset="UTF-8" action="/review/rate/662.Atlas_Shrugged" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<button class="greyText uitext myRating" disabled="disabled" name="button" type="submit">Rate this book</button>\n<div class="clearRating uitext">Clear rating</div>\n<input id="rating" name="rating" type="hidden" value="0"/><input id="wtr_button_id" name="wtr_button_id" type="hidden" value="1_book_662"/></form>\n\n<span class="stars" id="starsstars_for_1_book_662" onmouseout="mouseOutStars(\'stars_for_1_book_662\')"><a rel="nofollow"><img alt="didn\'t like it " class="star" height="15" id="starstars_for_1_book_662_0" onclick="submitStars(\'stars_for_1_book_662\', 0, \'/review/rate/662?rating=1&amp;wtr_button_id=1_book_662\', 0);  return false;" onmouseover="checkStars(\'stars_for_1_book_662\', 0)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="didn\'t like it" width="15"/></a><a rel="nofollow"><img alt="it was ok " class="star" height="15" id="starstars_for_1_book_662_1" onclick="submitStars(\'stars_for_1_book_662\', 1, \'/review/rate/662?rating=2&amp;wtr_button_id=1_book_662\', 0);  return false;" onmouseover="checkStars(\'stars_for_1_book_662\', 1)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was ok" width="15"/></a><a rel="nofollow"><img alt="liked it " class="star" height="15" id="starstars_for_1_book_662_2" onclick="submitStars(\'stars_for_1_book_662\', 2, \'/review/rate/662?rating=3&amp;wtr_button_id=1_book_662\', 0);  return false;" onmouseover="checkStars(\'stars_for_1_book_662\', 2)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="liked it" width="15"/></a><a rel="nofollow"><img alt="really liked it " class="star" height="15" id="starstars_for_1_book_662_3" onclick="submitStars(\'stars_for_1_book_662\', 3, \'/review/rate/662?rating=4&amp;wtr_button_id=1_book_662\', 0);  return false;" onmouseover="checkStars(\'stars_for_1_book_662\', 3)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="really liked it" width="15"/></a><a rel="nofollow"><img alt="it was amazing " class="star" height="15" id="starstars_for_1_book_662_4" onclick="submitStars(\'stars_for_1_book_662\', 4, \'/review/rate/662?rating=5&amp;wtr_button_id=1_book_662\', 0);  return false;" onmouseover="checkStars(\'stars_for_1_book_662\', 4)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was amazing" width="15"/></a></span><script language="javascript" type="text/javascript">starRatings[ratingIndex++] = [ \'stars_for_1_book_662\', -1]; checkStars(\'stars_for_1_book_662\', -1);</script></div>\n\n</div>\n\n      </td>\n\n  </tr><tr itemscope="" itemtype="http://schema.org/Book"><td width="5%" valign="top">\n      <a name="2115"/>\n      <a href="/book/show/2115.Atlas_Shrugged_The_Fountainhead" title="Atlas Shrugged &amp; The Fountainhead">\n          <img alt="Atlas Shrugged &amp; The Founta..." class="bookSmallImg" src="http://d.gr-assets.com/books/1159932401s/2115.jpg"/></a>    </td>\n    <td width="100%" valign="top">\n      <a href="/book/show/2115.Atlas_Shrugged_The_Fountainhead" class="bookTitle" itemprop="url">\n        <span itemprop="name">Atlas Shrugged &amp; The Fountainhead</span>\n</a>      <br/><span class="by smallText">by</span>\n<span itemprop="author" itemscope="" itemtype="http://schema.org/Person">\n<a href="http://www.goodreads.com/author/show/432.Ayn_Rand" class="authorName" itemprop="url"><span itemprop="name">Ayn Rand</span></a>\n</span>\n\n        <br/><span class="greyText smallText uitext">\n          <span class="minirating"><span class="stars"><img alt="4.02 of 5 stars" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.02 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.02 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.02 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.02 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/stars/red_star_33pct-69a219b6d79a91503f292bf5ac039d6b.png" title="4.02 of 5 stars" width="12"/></span> 4.02 avg rating \u2014 2,283 ratings</span>\n            \u2014\n              published\n             1995\n            \u2014\n            <a href="/work/editions/817229-atlas-shrugged-the-fountainhead" class="greyText" rel="nofollow">3 editions</a>\n        </span>\n        \n\n\n    </td>\n\n      <td width="130px">\n          <div class="wtrButtonContainer wtrSignedOut" id="2_book_2115">\n<div class="wtrUp wtrLeft">\n<form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="book_id" name="book_id" type="hidden" value="2115"/><input id="name" name="name" type="hidden" value="to-read"/><input id="unique_id" name="unique_id" type="hidden" value="2_book_2115"/><input id="wtr_new" name="wtr_new" type="hidden" value="true"/><button class="wtrToRead" type="submit">\n<span class="progressTrigger">Want to Read</span>\n<span class="progressIndicator">saving\xe2\x80\xa6</span>\n</button>\n</form>\n\n</div>\n\n<div class="wtrDivider"/>\n<div class="wtrRight">\n<button class="wtrShelfButton wtrUp">\n<img alt="pick shelf" src="http://s.gr-assets.com/assets/wtr_button/books-0866015891eb128cdc57e550383532a0.png"/></button>\n<div class="wtrShelfMenu">\n<ul class="wtrExclusiveShelves"><li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="2_book_2115"/><input id="book_id" name="book_id" type="hidden" value="2115"/><button class="wtrExclusiveShelf" name="name" type="submit" value="to-read">\n<span class="progressTrigger">Want to Read</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="2_book_2115"/><input id="book_id" name="book_id" type="hidden" value="2115"/><button class="wtrExclusiveShelf" name="name" type="submit" value="currently-reading">\n<span class="progressTrigger">Currently Reading</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="2_book_2115"/><input id="book_id" name="book_id" type="hidden" value="2115"/><button class="wtrExclusiveShelf" name="name" type="submit" value="read">\n<span class="progressTrigger">Read</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n</ul></div>\n</div>\n\n<div class="ratingStars wtrRating">\n<form accept-charset="UTF-8" action="/review/rate/2115.Atlas_Shrugged_The_Fountainhead" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<button class="greyText uitext myRating" disabled="disabled" name="button" type="submit">Rate this book</button>\n<div class="clearRating uitext">Clear rating</div>\n<input id="rating" name="rating" type="hidden" value="0"/><input id="wtr_button_id" name="wtr_button_id" type="hidden" value="2_book_2115"/></form>\n\n<span class="stars" id="starsstars_for_2_book_2115" onmouseout="mouseOutStars(\'stars_for_2_book_2115\')"><a rel="nofollow"><img alt="didn\'t like it " class="star" height="15" id="starstars_for_2_book_2115_0" onclick="submitStars(\'stars_for_2_book_2115\', 0, \'/review/rate/2115?rating=1&amp;wtr_button_id=2_book_2115\', 0);  return false;" onmouseover="checkStars(\'stars_for_2_book_2115\', 0)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="didn\'t like it" width="15"/></a><a rel="nofollow"><img alt="it was ok " class="star" height="15" id="starstars_for_2_book_2115_1" onclick="submitStars(\'stars_for_2_book_2115\', 1, \'/review/rate/2115?rating=2&amp;wtr_button_id=2_book_2115\', 0);  return false;" onmouseover="checkStars(\'stars_for_2_book_2115\', 1)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was ok" width="15"/></a><a rel="nofollow"><img alt="liked it " class="star" height="15" id="starstars_for_2_book_2115_2" onclick="submitStars(\'stars_for_2_book_2115\', 2, \'/review/rate/2115?rating=3&amp;wtr_button_id=2_book_2115\', 0);  return false;" onmouseover="checkStars(\'stars_for_2_book_2115\', 2)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="liked it" width="15"/></a><a rel="nofollow"><img alt="really liked it " class="star" height="15" id="starstars_for_2_book_2115_3" onclick="submitStars(\'stars_for_2_book_2115\', 3, \'/review/rate/2115?rating=4&amp;wtr_button_id=2_book_2115\', 0);  return false;" onmouseover="checkStars(\'stars_for_2_book_2115\', 3)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="really liked it" width="15"/></a><a rel="nofollow"><img alt="it was amazing " class="star" height="15" id="starstars_for_2_book_2115_4" onclick="submitStars(\'stars_for_2_book_2115\', 4, \'/review/rate/2115?rating=5&amp;wtr_button_id=2_book_2115\', 0);  return false;" onmouseover="checkStars(\'stars_for_2_book_2115\', 4)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was amazing" width="15"/></a></span><script language="javascript" type="text/javascript">starRatings[ratingIndex++] = [ \'stars_for_2_book_2115\', -1]; checkStars(\'stars_for_2_book_2115\', -1);</script></div>\n\n</div>\n\n      </td>\n\n  </tr><tr itemscope="" itemtype="http://schema.org/Book"><td width="5%" valign="top">\n      <a name="6234337"/>\n      <a href="/book/show/6234337-essays-on-ayn-rand-s-atlas-shrugged" title="Essays on Ayn Rand\'s Atlas Shrugged">\n          <img alt="Essays on Ayn Rand\'s Atlas ..." class="bookSmallImg" src="http://d.gr-assets.com/books/1348746577s/6234337.jpg"/></a>    </td>\n    <td width="100%" valign="top">\n      <a href="/book/show/6234337-essays-on-ayn-rand-s-atlas-shrugged" class="bookTitle" itemprop="url">\n        <span itemprop="name">Essays on Ayn Rand\'s Atlas Shrugged</span>\n</a>      <br/><span class="by smallText">by</span>\n<span itemprop="author" itemscope="" itemtype="http://schema.org/Person">\n<a href="http://www.goodreads.com/author/show/1422.Robert_Mayhew" class="authorName" itemprop="url"><span itemprop="name">Robert Mayhew</span></a> <span class="authorName greyText smallText role">(Editor)</span>\n</span>\n\n        <br/><span class="greyText smallText uitext">\n          <span class="minirating"><span class="stars"><img alt="3.89 of 5 stars" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.89 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.89 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.89 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/stars/red_star_66pct-a2f513494595fa112f4762672b33daef.png" title="3.89 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="3.89 of 5 stars" width="12"/></span> 3.89 avg rating \u2014 18 ratings</span>\n            \u2014\n              published\n             2009\n            \u2014\n            <a href="/work/editions/6416993-essays-on-ayn-rand-s-atlas-shrugged" class="greyText" rel="nofollow">2 editions</a>\n        </span>\n        \n\n\n    </td>\n\n      <td width="130px">\n          <div class="wtrButtonContainer wtrSignedOut" id="3_book_6234337">\n<div class="wtrUp wtrLeft">\n<form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="book_id" name="book_id" type="hidden" value="6234337"/><input id="name" name="name" type="hidden" value="to-read"/><input id="unique_id" name="unique_id" type="hidden" value="3_book_6234337"/><input id="wtr_new" name="wtr_new" type="hidden" value="true"/><button class="wtrToRead" type="submit">\n<span class="progressTrigger">Want to Read</span>\n<span class="progressIndicator">saving\xe2\x80\xa6</span>\n</button>\n</form>\n\n</div>\n\n<div class="wtrDivider"/>\n<div class="wtrRight">\n<button class="wtrShelfButton wtrUp">\n<img alt="pick shelf" src="http://s.gr-assets.com/assets/wtr_button/books-0866015891eb128cdc57e550383532a0.png"/></button>\n<div class="wtrShelfMenu">\n<ul class="wtrExclusiveShelves"><li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="3_book_6234337"/><input id="book_id" name="book_id" type="hidden" value="6234337"/><button class="wtrExclusiveShelf" name="name" type="submit" value="to-read">\n<span class="progressTrigger">Want to Read</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="3_book_6234337"/><input id="book_id" name="book_id" type="hidden" value="6234337"/><button class="wtrExclusiveShelf" name="name" type="submit" value="currently-reading">\n<span class="progressTrigger">Currently Reading</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="3_book_6234337"/><input id="book_id" name="book_id" type="hidden" value="6234337"/><button class="wtrExclusiveShelf" name="name" type="submit" value="read">\n<span class="progressTrigger">Read</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n</ul></div>\n</div>\n\n<div class="ratingStars wtrRating">\n<form accept-charset="UTF-8" action="/review/rate/6234337-essays-on-ayn-rand-s-atlas-shrugged" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<button class="greyText uitext myRating" disabled="disabled" name="button" type="submit">Rate this book</button>\n<div class="clearRating uitext">Clear rating</div>\n<input id="rating" name="rating" type="hidden" value="0"/><input id="wtr_button_id" name="wtr_button_id" type="hidden" value="3_book_6234337"/></form>\n\n<span class="stars" id="starsstars_for_3_book_6234337" onmouseout="mouseOutStars(\'stars_for_3_book_6234337\')"><a rel="nofollow"><img alt="didn\'t like it " class="star" height="15" id="starstars_for_3_book_6234337_0" onclick="submitStars(\'stars_for_3_book_6234337\', 0, \'/review/rate/6234337?rating=1&amp;wtr_button_id=3_book_6234337\', 0);  return false;" onmouseover="checkStars(\'stars_for_3_book_6234337\', 0)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="didn\'t like it" width="15"/></a><a rel="nofollow"><img alt="it was ok " class="star" height="15" id="starstars_for_3_book_6234337_1" onclick="submitStars(\'stars_for_3_book_6234337\', 1, \'/review/rate/6234337?rating=2&amp;wtr_button_id=3_book_6234337\', 0);  return false;" onmouseover="checkStars(\'stars_for_3_book_6234337\', 1)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was ok" width="15"/></a><a rel="nofollow"><img alt="liked it " class="star" height="15" id="starstars_for_3_book_6234337_2" onclick="submitStars(\'stars_for_3_book_6234337\', 2, \'/review/rate/6234337?rating=3&amp;wtr_button_id=3_book_6234337\', 0);  return false;" onmouseover="checkStars(\'stars_for_3_book_6234337\', 2)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="liked it" width="15"/></a><a rel="nofollow"><img alt="really liked it " class="star" height="15" id="starstars_for_3_book_6234337_3" onclick="submitStars(\'stars_for_3_book_6234337\', 3, \'/review/rate/6234337?rating=4&amp;wtr_button_id=3_book_6234337\', 0);  return false;" onmouseover="checkStars(\'stars_for_3_book_6234337\', 3)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="really liked it" width="15"/></a><a rel="nofollow"><img alt="it was amazing " class="star" height="15" id="starstars_for_3_book_6234337_4" onclick="submitStars(\'stars_for_3_book_6234337\', 4, \'/review/rate/6234337?rating=5&amp;wtr_button_id=3_book_6234337\', 0);  return false;" onmouseover="checkStars(\'stars_for_3_book_6234337\', 4)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was amazing" width="15"/></a></span><script language="javascript" type="text/javascript">starRatings[ratingIndex++] = [ \'stars_for_3_book_6234337\', -1]; checkStars(\'stars_for_3_book_6234337\', -1);</script></div>\n\n</div>\n\n      </td>\n\n  </tr><tr itemscope="" itemtype="http://schema.org/Book"><td width="5%" valign="top">\n      <a name="13607666"/>\n      <a href="/book/show/13607666-quicklet-ayn-rand-s-atlas-shrugged" title="Quicklet-Ayn Rand\'s Atlas Shrugged">\n          <img alt="Quicklet-Ayn Rand\'s Atlas S..." class="bookSmallImg" src="http://www.goodreads.com/assets/nocover/60x80.png"/></a>    </td>\n    <td width="100%" valign="top">\n      <a href="/book/show/13607666-quicklet-ayn-rand-s-atlas-shrugged" class="bookTitle" itemprop="url">\n        <span itemprop="name">Quicklet-Ayn Rand\'s Atlas Shrugged</span>\n</a>      <br/><span class="by smallText">by</span>\n<span itemprop="author" itemscope="" itemtype="http://schema.org/Person">\n<a href="http://www.goodreads.com/author/show/2990982.Jason_Malcolm_Stewart" class="authorName" itemprop="url"><span itemprop="name">Jason Malcolm Stewart</span></a> <span class="greyText">(Goodreads Author)</span>\n</span>\n\n        <br/><span class="greyText smallText uitext">\n          <span class="minirating"><span class="stars"><img alt="5.0 of 5 stars" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="5.0 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="5.0 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="5.0 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="5.0 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="5.0 of 5 stars" width="12"/></span> 5.00 avg rating \u2014 1 rating</span>\n            \u2014\n              published\n             2012\n            \u2014\n            <a href="/work/editions/19203737-quicklet-ayn-rand-s-atlas-shrugged" class="greyText" rel="nofollow">1 edition</a>\n        </span>\n        \n\n\n    </td>\n\n      <td width="130px">\n          <div class="wtrButtonContainer wtrSignedOut" id="4_book_13607666">\n<div class="wtrUp wtrLeft">\n<form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="book_id" name="book_id" type="hidden" value="13607666"/><input id="name" name="name" type="hidden" value="to-read"/><input id="unique_id" name="unique_id" type="hidden" value="4_book_13607666"/><input id="wtr_new" name="wtr_new" type="hidden" value="true"/><button class="wtrToRead" type="submit">\n<span class="progressTrigger">Want to Read</span>\n<span class="progressIndicator">saving\xe2\x80\xa6</span>\n</button>\n</form>\n\n</div>\n\n<div class="wtrDivider"/>\n<div class="wtrRight">\n<button class="wtrShelfButton wtrUp">\n<img alt="pick shelf" src="http://s.gr-assets.com/assets/wtr_button/books-0866015891eb128cdc57e550383532a0.png"/></button>\n<div class="wtrShelfMenu">\n<ul class="wtrExclusiveShelves"><li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="4_book_13607666"/><input id="book_id" name="book_id" type="hidden" value="13607666"/><button class="wtrExclusiveShelf" name="name" type="submit" value="to-read">\n<span class="progressTrigger">Want to Read</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="4_book_13607666"/><input id="book_id" name="book_id" type="hidden" value="13607666"/><button class="wtrExclusiveShelf" name="name" type="submit" value="currently-reading">\n<span class="progressTrigger">Currently Reading</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="4_book_13607666"/><input id="book_id" name="book_id" type="hidden" value="13607666"/><button class="wtrExclusiveShelf" name="name" type="submit" value="read">\n<span class="progressTrigger">Read</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n</ul></div>\n</div>\n\n<div class="ratingStars wtrRating">\n<form accept-charset="UTF-8" action="/review/rate/13607666-quicklet-ayn-rand-s-atlas-shrugged" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<button class="greyText uitext myRating" disabled="disabled" name="button" type="submit">Rate this book</button>\n<div class="clearRating uitext">Clear rating</div>\n<input id="rating" name="rating" type="hidden" value="0"/><input id="wtr_button_id" name="wtr_button_id" type="hidden" value="4_book_13607666"/></form>\n\n<span class="stars" id="starsstars_for_4_book_13607666" onmouseout="mouseOutStars(\'stars_for_4_book_13607666\')"><a rel="nofollow"><img alt="didn\'t like it " class="star" height="15" id="starstars_for_4_book_13607666_0" onclick="submitStars(\'stars_for_4_book_13607666\', 0, \'/review/rate/13607666?rating=1&amp;wtr_button_id=4_book_13607666\', 0);  return false;" onmouseover="checkStars(\'stars_for_4_book_13607666\', 0)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="didn\'t like it" width="15"/></a><a rel="nofollow"><img alt="it was ok " class="star" height="15" id="starstars_for_4_book_13607666_1" onclick="submitStars(\'stars_for_4_book_13607666\', 1, \'/review/rate/13607666?rating=2&amp;wtr_button_id=4_book_13607666\', 0);  return false;" onmouseover="checkStars(\'stars_for_4_book_13607666\', 1)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was ok" width="15"/></a><a rel="nofollow"><img alt="liked it " class="star" height="15" id="starstars_for_4_book_13607666_2" onclick="submitStars(\'stars_for_4_book_13607666\', 2, \'/review/rate/13607666?rating=3&amp;wtr_button_id=4_book_13607666\', 0);  return false;" onmouseover="checkStars(\'stars_for_4_book_13607666\', 2)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="liked it" width="15"/></a><a rel="nofollow"><img alt="really liked it " class="star" height="15" id="starstars_for_4_book_13607666_3" onclick="submitStars(\'stars_for_4_book_13607666\', 3, \'/review/rate/13607666?rating=4&amp;wtr_button_id=4_book_13607666\', 0);  return false;" onmouseover="checkStars(\'stars_for_4_book_13607666\', 3)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="really liked it" width="15"/></a><a rel="nofollow"><img alt="it was amazing " class="star" height="15" id="starstars_for_4_book_13607666_4" onclick="submitStars(\'stars_for_4_book_13607666\', 4, \'/review/rate/13607666?rating=5&amp;wtr_button_id=4_book_13607666\', 0);  return false;" onmouseover="checkStars(\'stars_for_4_book_13607666\', 4)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was amazing" width="15"/></a></span><script language="javascript" type="text/javascript">starRatings[ratingIndex++] = [ \'stars_for_4_book_13607666\', -1]; checkStars(\'stars_for_4_book_13607666\', -1);</script></div>\n\n</div>\n\n      </td>\n\n  </tr><tr itemscope="" itemtype="http://schema.org/Book"><td width="5%" valign="top">\n      <a name="201237"/>\n      <a href="/book/show/201237.Ayn_Rand_s_Atlas_Shrugged" title="Ayn Rand\'s Atlas Shrugged: A Philosophical and Literary Companion">\n          <img alt="Ayn Rand\'s Atlas Shrugged: ..." class="bookSmallImg" src="http://d.gr-assets.com/books/1266494900s/201237.jpg"/></a>    </td>\n    <td width="100%" valign="top">\n      <a href="/book/show/201237.Ayn_Rand_s_Atlas_Shrugged" class="bookTitle" itemprop="url">\n        <span itemprop="name">Ayn Rand\'s Atlas Shrugged: A Philosophical and Literary Companion</span>\n</a>      <br/><span class="by smallText">by</span>\n<span itemprop="author" itemscope="" itemtype="http://schema.org/Person">\n<a href="http://www.goodreads.com/author/show/117359.Edward_Wayne_Younkins" class="authorName" itemprop="url"><span itemprop="name">Edward Wayne Younkins</span></a>\n</span>\n\n        <br/><span class="greyText smallText uitext">\n          <span class="minirating"><span class="stars"><img alt="3.86 of 5 stars" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.86 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.86 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.86 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/stars/red_star_66pct-a2f513494595fa112f4762672b33daef.png" title="3.86 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="3.86 of 5 stars" width="12"/></span> 3.86 avg rating \u2014 7 ratings</span>\n            \u2014\n              published\n             2007\n            \u2014\n            <a href="/work/editions/194705-ayn-rand-s-atlas-shrugged-a-philosophical-and-literary-companion" class="greyText" rel="nofollow">1 edition</a>\n        </span>\n        \n\n\n    </td>\n\n      <td width="130px">\n          <div class="wtrButtonContainer wtrSignedOut" id="5_book_201237">\n<div class="wtrUp wtrLeft">\n<form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="book_id" name="book_id" type="hidden" value="201237"/><input id="name" name="name" type="hidden" value="to-read"/><input id="unique_id" name="unique_id" type="hidden" value="5_book_201237"/><input id="wtr_new" name="wtr_new" type="hidden" value="true"/><button class="wtrToRead" type="submit">\n<span class="progressTrigger">Want to Read</span>\n<span class="progressIndicator">saving\xe2\x80\xa6</span>\n</button>\n</form>\n\n</div>\n\n<div class="wtrDivider"/>\n<div class="wtrRight">\n<button class="wtrShelfButton wtrUp">\n<img alt="pick shelf" src="http://s.gr-assets.com/assets/wtr_button/books-0866015891eb128cdc57e550383532a0.png"/></button>\n<div class="wtrShelfMenu">\n<ul class="wtrExclusiveShelves"><li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="5_book_201237"/><input id="book_id" name="book_id" type="hidden" value="201237"/><button class="wtrExclusiveShelf" name="name" type="submit" value="to-read">\n<span class="progressTrigger">Want to Read</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="5_book_201237"/><input id="book_id" name="book_id" type="hidden" value="201237"/><button class="wtrExclusiveShelf" name="name" type="submit" value="currently-reading">\n<span class="progressTrigger">Currently Reading</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="5_book_201237"/><input id="book_id" name="book_id" type="hidden" value="201237"/><button class="wtrExclusiveShelf" name="name" type="submit" value="read">\n<span class="progressTrigger">Read</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n</ul></div>\n</div>\n\n<div class="ratingStars wtrRating">\n<form accept-charset="UTF-8" action="/review/rate/201237.Ayn_Rand_s_Atlas_Shrugged" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<button class="greyText uitext myRating" disabled="disabled" name="button" type="submit">Rate this book</button>\n<div class="clearRating uitext">Clear rating</div>\n<input id="rating" name="rating" type="hidden" value="0"/><input id="wtr_button_id" name="wtr_button_id" type="hidden" value="5_book_201237"/></form>\n\n<span class="stars" id="starsstars_for_5_book_201237" onmouseout="mouseOutStars(\'stars_for_5_book_201237\')"><a rel="nofollow"><img alt="didn\'t like it " class="star" height="15" id="starstars_for_5_book_201237_0" onclick="submitStars(\'stars_for_5_book_201237\', 0, \'/review/rate/201237?rating=1&amp;wtr_button_id=5_book_201237\', 0);  return false;" onmouseover="checkStars(\'stars_for_5_book_201237\', 0)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="didn\'t like it" width="15"/></a><a rel="nofollow"><img alt="it was ok " class="star" height="15" id="starstars_for_5_book_201237_1" onclick="submitStars(\'stars_for_5_book_201237\', 1, \'/review/rate/201237?rating=2&amp;wtr_button_id=5_book_201237\', 0);  return false;" onmouseover="checkStars(\'stars_for_5_book_201237\', 1)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was ok" width="15"/></a><a rel="nofollow"><img alt="liked it " class="star" height="15" id="starstars_for_5_book_201237_2" onclick="submitStars(\'stars_for_5_book_201237\', 2, \'/review/rate/201237?rating=3&amp;wtr_button_id=5_book_201237\', 0);  return false;" onmouseover="checkStars(\'stars_for_5_book_201237\', 2)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="liked it" width="15"/></a><a rel="nofollow"><img alt="really liked it " class="star" height="15" id="starstars_for_5_book_201237_3" onclick="submitStars(\'stars_for_5_book_201237\', 3, \'/review/rate/201237?rating=4&amp;wtr_button_id=5_book_201237\', 0);  return false;" onmouseover="checkStars(\'stars_for_5_book_201237\', 3)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="really liked it" width="15"/></a><a rel="nofollow"><img alt="it was amazing " class="star" height="15" id="starstars_for_5_book_201237_4" onclick="submitStars(\'stars_for_5_book_201237\', 4, \'/review/rate/201237?rating=5&amp;wtr_button_id=5_book_201237\', 0);  return false;" onmouseover="checkStars(\'stars_for_5_book_201237\', 4)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was amazing" width="15"/></a></span><script language="javascript" type="text/javascript">starRatings[ratingIndex++] = [ \'stars_for_5_book_201237\', -1]; checkStars(\'stars_for_5_book_201237\', -1);</script></div>\n\n</div>\n\n      </td>\n\n  </tr><tr itemscope="" itemtype="http://schema.org/Book"><td width="5%" valign="top">\n      <a name="5755462"/>\n      <a href="/book/show/5755462-atlas-shrugged-part-a" title="Atlas Shrugged Part A: New Edition">\n          <img alt="Atlas Shrugged Part A: New ..." class="bookSmallImg" src="http://d.gr-assets.com/books/1348463450s/5755462.jpg"/></a>    </td>\n    <td width="100%" valign="top">\n      <a href="/book/show/5755462-atlas-shrugged-part-a" class="bookTitle" itemprop="url">\n        <span itemprop="name">Atlas Shrugged Part A: New Edition</span>\n</a>      <br/><span class="by smallText">by</span>\n<span itemprop="author" itemscope="" itemtype="http://schema.org/Person">\n<a href="http://www.goodreads.com/author/show/432.Ayn_Rand" class="authorName" itemprop="url"><span itemprop="name">Ayn Rand</span></a>, \n<a href="http://www.goodreads.com/author/show/44554.Scott_Brick" class="authorName" itemprop="url"><span itemprop="name">Scott Brick</span></a> <span class="authorName greyText smallText role">(Read by)</span>\n</span>\n\n        <br/><span class="greyText smallText uitext">\n          <span class="minirating"><span class="stars"><img alt="4.0 of 5 stars" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.0 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.0 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.0 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.0 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="4.0 of 5 stars" width="12"/></span> 4.00 avg rating \u2014 84 ratings</span>\n            \u2014\n            <a href="/work/editions/21836607-atlas-shrugged-part-a-new-edition" class="greyText" rel="nofollow">5 editions</a>\n        </span>\n        \n\n\n    </td>\n\n      <td width="130px">\n          <div class="wtrButtonContainer wtrSignedOut" id="6_book_5755462">\n<div class="wtrUp wtrLeft">\n<form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="book_id" name="book_id" type="hidden" value="5755462"/><input id="name" name="name" type="hidden" value="to-read"/><input id="unique_id" name="unique_id" type="hidden" value="6_book_5755462"/><input id="wtr_new" name="wtr_new" type="hidden" value="true"/><button class="wtrToRead" type="submit">\n<span class="progressTrigger">Want to Read</span>\n<span class="progressIndicator">saving\xe2\x80\xa6</span>\n</button>\n</form>\n\n</div>\n\n<div class="wtrDivider"/>\n<div class="wtrRight">\n<button class="wtrShelfButton wtrUp">\n<img alt="pick shelf" src="http://s.gr-assets.com/assets/wtr_button/books-0866015891eb128cdc57e550383532a0.png"/></button>\n<div class="wtrShelfMenu">\n<ul class="wtrExclusiveShelves"><li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="6_book_5755462"/><input id="book_id" name="book_id" type="hidden" value="5755462"/><button class="wtrExclusiveShelf" name="name" type="submit" value="to-read">\n<span class="progressTrigger">Want to Read</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="6_book_5755462"/><input id="book_id" name="book_id" type="hidden" value="5755462"/><button class="wtrExclusiveShelf" name="name" type="submit" value="currently-reading">\n<span class="progressTrigger">Currently Reading</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="6_book_5755462"/><input id="book_id" name="book_id" type="hidden" value="5755462"/><button class="wtrExclusiveShelf" name="name" type="submit" value="read">\n<span class="progressTrigger">Read</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n</ul></div>\n</div>\n\n<div class="ratingStars wtrRating">\n<form accept-charset="UTF-8" action="/review/rate/5755462-atlas-shrugged-part-a" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<button class="greyText uitext myRating" disabled="disabled" name="button" type="submit">Rate this book</button>\n<div class="clearRating uitext">Clear rating</div>\n<input id="rating" name="rating" type="hidden" value="0"/><input id="wtr_button_id" name="wtr_button_id" type="hidden" value="6_book_5755462"/></form>\n\n<span class="stars" id="starsstars_for_6_book_5755462" onmouseout="mouseOutStars(\'stars_for_6_book_5755462\')"><a rel="nofollow"><img alt="didn\'t like it " class="star" height="15" id="starstars_for_6_book_5755462_0" onclick="submitStars(\'stars_for_6_book_5755462\', 0, \'/review/rate/5755462?rating=1&amp;wtr_button_id=6_book_5755462\', 0);  return false;" onmouseover="checkStars(\'stars_for_6_book_5755462\', 0)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="didn\'t like it" width="15"/></a><a rel="nofollow"><img alt="it was ok " class="star" height="15" id="starstars_for_6_book_5755462_1" onclick="submitStars(\'stars_for_6_book_5755462\', 1, \'/review/rate/5755462?rating=2&amp;wtr_button_id=6_book_5755462\', 0);  return false;" onmouseover="checkStars(\'stars_for_6_book_5755462\', 1)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was ok" width="15"/></a><a rel="nofollow"><img alt="liked it " class="star" height="15" id="starstars_for_6_book_5755462_2" onclick="submitStars(\'stars_for_6_book_5755462\', 2, \'/review/rate/5755462?rating=3&amp;wtr_button_id=6_book_5755462\', 0);  return false;" onmouseover="checkStars(\'stars_for_6_book_5755462\', 2)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="liked it" width="15"/></a><a rel="nofollow"><img alt="really liked it " class="star" height="15" id="starstars_for_6_book_5755462_3" onclick="submitStars(\'stars_for_6_book_5755462\', 3, \'/review/rate/5755462?rating=4&amp;wtr_button_id=6_book_5755462\', 0);  return false;" onmouseover="checkStars(\'stars_for_6_book_5755462\', 3)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="really liked it" width="15"/></a><a rel="nofollow"><img alt="it was amazing " class="star" height="15" id="starstars_for_6_book_5755462_4" onclick="submitStars(\'stars_for_6_book_5755462\', 4, \'/review/rate/5755462?rating=5&amp;wtr_button_id=6_book_5755462\', 0);  return false;" onmouseover="checkStars(\'stars_for_6_book_5755462\', 4)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was amazing" width="15"/></a></span><script language="javascript" type="text/javascript">starRatings[ratingIndex++] = [ \'stars_for_6_book_5755462\', -1]; checkStars(\'stars_for_6_book_5755462\', -1);</script></div>\n\n</div>\n\n      </td>\n\n  </tr><tr itemscope="" itemtype="http://schema.org/Book"><td width="5%" valign="top">\n      <a name="831567"/>\n      <a href="/book/show/831567.Ayn_Rand_s_Atlas_Shrugged" title="Ayn Rand\'s Atlas Shrugged: A Philosophical and Literary Companion">\n          <img alt="Ayn Rand\'s Atlas Shrugged: ..." class="bookSmallImg" src="http://d.gr-assets.com/books/1266654752s/831567.jpg"/></a>    </td>\n    <td width="100%" valign="top">\n      <a href="/book/show/831567.Ayn_Rand_s_Atlas_Shrugged" class="bookTitle" itemprop="url">\n        <span itemprop="name">Ayn Rand\'s Atlas Shrugged: A Philosophical and Literary Companion</span>\n</a>      <br/><span class="by smallText">by</span>\n<span itemprop="author" itemscope="" itemtype="http://schema.org/Person">\n<a href="http://www.goodreads.com/author/show/432722.Edward_W_Younkins" class="authorName" itemprop="url"><span itemprop="name">Edward W. Younkins</span></a> <span class="authorName greyText smallText role">(Editor)</span>\n</span>\n\n        <br/><span class="greyText smallText uitext">\n          <span class="minirating"><span class="stars"><img alt="3.5 of 5 stars" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.5 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.5 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.5 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/stars/red_star_66pct-a2f513494595fa112f4762672b33daef.png" title="3.5 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="3.5 of 5 stars" width="12"/></span> 3.50 avg rating \u2014 2 ratings</span>\n            \u2014\n              published\n             2007\n            \u2014\n            <a href="/work/editions/817220-ayn-rand-s-atlas-shrugged-a-philosophical-and-literary-companion" class="greyText" rel="nofollow">2 editions</a>\n        </span>\n        \n\n\n    </td>\n\n      <td width="130px">\n          <div class="wtrButtonContainer wtrSignedOut" id="7_book_831567">\n<div class="wtrUp wtrLeft">\n<form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="book_id" name="book_id" type="hidden" value="831567"/><input id="name" name="name" type="hidden" value="to-read"/><input id="unique_id" name="unique_id" type="hidden" value="7_book_831567"/><input id="wtr_new" name="wtr_new" type="hidden" value="true"/><button class="wtrToRead" type="submit">\n<span class="progressTrigger">Want to Read</span>\n<span class="progressIndicator">saving\xe2\x80\xa6</span>\n</button>\n</form>\n\n</div>\n\n<div class="wtrDivider"/>\n<div class="wtrRight">\n<button class="wtrShelfButton wtrUp">\n<img alt="pick shelf" src="http://s.gr-assets.com/assets/wtr_button/books-0866015891eb128cdc57e550383532a0.png"/></button>\n<div class="wtrShelfMenu">\n<ul class="wtrExclusiveShelves"><li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="7_book_831567"/><input id="book_id" name="book_id" type="hidden" value="831567"/><button class="wtrExclusiveShelf" name="name" type="submit" value="to-read">\n<span class="progressTrigger">Want to Read</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="7_book_831567"/><input id="book_id" name="book_id" type="hidden" value="831567"/><button class="wtrExclusiveShelf" name="name" type="submit" value="currently-reading">\n<span class="progressTrigger">Currently Reading</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="7_book_831567"/><input id="book_id" name="book_id" type="hidden" value="831567"/><button class="wtrExclusiveShelf" name="name" type="submit" value="read">\n<span class="progressTrigger">Read</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n</ul></div>\n</div>\n\n<div class="ratingStars wtrRating">\n<form accept-charset="UTF-8" action="/review/rate/831567.Ayn_Rand_s_Atlas_Shrugged" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<button class="greyText uitext myRating" disabled="disabled" name="button" type="submit">Rate this book</button>\n<div class="clearRating uitext">Clear rating</div>\n<input id="rating" name="rating" type="hidden" value="0"/><input id="wtr_button_id" name="wtr_button_id" type="hidden" value="7_book_831567"/></form>\n\n<span class="stars" id="starsstars_for_7_book_831567" onmouseout="mouseOutStars(\'stars_for_7_book_831567\')"><a rel="nofollow"><img alt="didn\'t like it " class="star" height="15" id="starstars_for_7_book_831567_0" onclick="submitStars(\'stars_for_7_book_831567\', 0, \'/review/rate/831567?rating=1&amp;wtr_button_id=7_book_831567\', 0);  return false;" onmouseover="checkStars(\'stars_for_7_book_831567\', 0)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="didn\'t like it" width="15"/></a><a rel="nofollow"><img alt="it was ok " class="star" height="15" id="starstars_for_7_book_831567_1" onclick="submitStars(\'stars_for_7_book_831567\', 1, \'/review/rate/831567?rating=2&amp;wtr_button_id=7_book_831567\', 0);  return false;" onmouseover="checkStars(\'stars_for_7_book_831567\', 1)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was ok" width="15"/></a><a rel="nofollow"><img alt="liked it " class="star" height="15" id="starstars_for_7_book_831567_2" onclick="submitStars(\'stars_for_7_book_831567\', 2, \'/review/rate/831567?rating=3&amp;wtr_button_id=7_book_831567\', 0);  return false;" onmouseover="checkStars(\'stars_for_7_book_831567\', 2)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="liked it" width="15"/></a><a rel="nofollow"><img alt="really liked it " class="star" height="15" id="starstars_for_7_book_831567_3" onclick="submitStars(\'stars_for_7_book_831567\', 3, \'/review/rate/831567?rating=4&amp;wtr_button_id=7_book_831567\', 0);  return false;" onmouseover="checkStars(\'stars_for_7_book_831567\', 3)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="really liked it" width="15"/></a><a rel="nofollow"><img alt="it was amazing " class="star" height="15" id="starstars_for_7_book_831567_4" onclick="submitStars(\'stars_for_7_book_831567\', 4, \'/review/rate/831567?rating=5&amp;wtr_button_id=7_book_831567\', 0);  return false;" onmouseover="checkStars(\'stars_for_7_book_831567\', 4)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was amazing" width="15"/></a></span><script language="javascript" type="text/javascript">starRatings[ratingIndex++] = [ \'stars_for_7_book_831567\', -1]; checkStars(\'stars_for_7_book_831567\', -1);</script></div>\n\n</div>\n\n      </td>\n\n  </tr><tr itemscope="" itemtype="http://schema.org/Book"><td width="5%" valign="top">\n      <a name="9364"/>\n      <a href="/book/show/9364.Atlas_Shrugged" title="Atlas Shrugged">\n          <img alt="Atlas Shrugged" class="bookSmallImg" src="http://d.gr-assets.com/books/1348366796s/9364.jpg"/></a>    </td>\n    <td width="100%" valign="top">\n      <a href="/book/show/9364.Atlas_Shrugged" class="bookTitle" itemprop="url">\n        <span itemprop="name">Atlas Shrugged</span>\n</a>      <br/><span class="by smallText">by</span>\n<span itemprop="author" itemscope="" itemtype="http://schema.org/Person">\n<a href="http://www.goodreads.com/author/show/1423.Andrew_Bernstein" class="authorName" itemprop="url"><span itemprop="name">Andrew Bernstein</span></a>, \n<a href="http://www.goodreads.com/author/show/3899673.CliffsNotes" class="authorName" itemprop="url"><span itemprop="name">CliffsNotes</span></a>, <a href="http://www.goodreads.com/author/show/432.Ayn_Rand" class="authorName" itemprop="url"><span itemprop="name">Ayn Rand</span></a>\n</span>\n\n        <br/><span class="greyText smallText uitext">\n          <span class="minirating"><span class="stars"><img alt="4.12 of 5 stars" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.12 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.12 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.12 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.12 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/stars/red_star_33pct-69a219b6d79a91503f292bf5ac039d6b.png" title="4.12 of 5 stars" width="12"/></span> 4.12 avg rating \u2014 41 ratings</span>\n            \u2014\n              published\n             2000\n            \u2014\n            <a href="/work/editions/12225-atlas-shrugged-cliffs-notes" class="greyText" rel="nofollow">10 editions</a>\n        </span>\n        \n\n\n    </td>\n\n      <td width="130px">\n          <div class="wtrButtonContainer wtrSignedOut" id="8_book_9364">\n<div class="wtrUp wtrLeft">\n<form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="book_id" name="book_id" type="hidden" value="9364"/><input id="name" name="name" type="hidden" value="to-read"/><input id="unique_id" name="unique_id" type="hidden" value="8_book_9364"/><input id="wtr_new" name="wtr_new" type="hidden" value="true"/><button class="wtrToRead" type="submit">\n<span class="progressTrigger">Want to Read</span>\n<span class="progressIndicator">saving\xe2\x80\xa6</span>\n</button>\n</form>\n\n</div>\n\n<div class="wtrDivider"/>\n<div class="wtrRight">\n<button class="wtrShelfButton wtrUp">\n<img alt="pick shelf" src="http://s.gr-assets.com/assets/wtr_button/books-0866015891eb128cdc57e550383532a0.png"/></button>\n<div class="wtrShelfMenu">\n<ul class="wtrExclusiveShelves"><li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="8_book_9364"/><input id="book_id" name="book_id" type="hidden" value="9364"/><button class="wtrExclusiveShelf" name="name" type="submit" value="to-read">\n<span class="progressTrigger">Want to Read</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="8_book_9364"/><input id="book_id" name="book_id" type="hidden" value="9364"/><button class="wtrExclusiveShelf" name="name" type="submit" value="currently-reading">\n<span class="progressTrigger">Currently Reading</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="8_book_9364"/><input id="book_id" name="book_id" type="hidden" value="9364"/><button class="wtrExclusiveShelf" name="name" type="submit" value="read">\n<span class="progressTrigger">Read</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n</ul></div>\n</div>\n\n<div class="ratingStars wtrRating">\n<form accept-charset="UTF-8" action="/review/rate/9364.Atlas_Shrugged" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<button class="greyText uitext myRating" disabled="disabled" name="button" type="submit">Rate this book</button>\n<div class="clearRating uitext">Clear rating</div>\n<input id="rating" name="rating" type="hidden" value="0"/><input id="wtr_button_id" name="wtr_button_id" type="hidden" value="8_book_9364"/></form>\n\n<span class="stars" id="starsstars_for_8_book_9364" onmouseout="mouseOutStars(\'stars_for_8_book_9364\')"><a rel="nofollow"><img alt="didn\'t like it " class="star" height="15" id="starstars_for_8_book_9364_0" onclick="submitStars(\'stars_for_8_book_9364\', 0, \'/review/rate/9364?rating=1&amp;wtr_button_id=8_book_9364\', 0);  return false;" onmouseover="checkStars(\'stars_for_8_book_9364\', 0)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="didn\'t like it" width="15"/></a><a rel="nofollow"><img alt="it was ok " class="star" height="15" id="starstars_for_8_book_9364_1" onclick="submitStars(\'stars_for_8_book_9364\', 1, \'/review/rate/9364?rating=2&amp;wtr_button_id=8_book_9364\', 0);  return false;" onmouseover="checkStars(\'stars_for_8_book_9364\', 1)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was ok" width="15"/></a><a rel="nofollow"><img alt="liked it " class="star" height="15" id="starstars_for_8_book_9364_2" onclick="submitStars(\'stars_for_8_book_9364\', 2, \'/review/rate/9364?rating=3&amp;wtr_button_id=8_book_9364\', 0);  return false;" onmouseover="checkStars(\'stars_for_8_book_9364\', 2)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="liked it" width="15"/></a><a rel="nofollow"><img alt="really liked it " class="star" height="15" id="starstars_for_8_book_9364_3" onclick="submitStars(\'stars_for_8_book_9364\', 3, \'/review/rate/9364?rating=4&amp;wtr_button_id=8_book_9364\', 0);  return false;" onmouseover="checkStars(\'stars_for_8_book_9364\', 3)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="really liked it" width="15"/></a><a rel="nofollow"><img alt="it was amazing " class="star" height="15" id="starstars_for_8_book_9364_4" onclick="submitStars(\'stars_for_8_book_9364\', 4, \'/review/rate/9364?rating=5&amp;wtr_button_id=8_book_9364\', 0);  return false;" onmouseover="checkStars(\'stars_for_8_book_9364\', 4)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was amazing" width="15"/></a></span><script language="javascript" type="text/javascript">starRatings[ratingIndex++] = [ \'stars_for_8_book_9364\', -1]; checkStars(\'stars_for_8_book_9364\', -1);</script></div>\n\n</div>\n\n      </td>\n\n  </tr><tr itemscope="" itemtype="http://schema.org/Book"><td width="5%" valign="top">\n      <a name="5430955"/>\n      <a href="/book/show/5430955-atlas-shrugged-part-b" title="Atlas Shrugged Part B: New Edition">\n          <img alt="Atlas Shrugged Part B: New ..." class="bookSmallImg" src="http://d.gr-assets.com/books/1348469426s/5430955.jpg"/></a>    </td>\n    <td width="100%" valign="top">\n      <a href="/book/show/5430955-atlas-shrugged-part-b" class="bookTitle" itemprop="url">\n        <span itemprop="name">Atlas Shrugged Part B: New Edition</span>\n</a>      <br/><span class="by smallText">by</span>\n<span itemprop="author" itemscope="" itemtype="http://schema.org/Person">\n<a href="http://www.goodreads.com/author/show/432.Ayn_Rand" class="authorName" itemprop="url"><span itemprop="name">Ayn Rand</span></a>, \n<a href="http://www.goodreads.com/author/show/44554.Scott_Brick" class="authorName" itemprop="url"><span itemprop="name">Scott Brick</span></a> <span class="authorName greyText smallText role">(Narrator)</span>\n</span>\n\n        <br/><span class="greyText smallText uitext">\n          <span class="minirating"><span class="stars"><img alt="3.93 of 5 stars" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.93 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.93 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.93 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/stars/red_star_66pct-a2f513494595fa112f4762672b33daef.png" title="3.93 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="3.93 of 5 stars" width="12"/></span> 3.93 avg rating \u2014 28 ratings</span>\n            \u2014\n            <a href="/work/editions/21836608-atlas-shrugged-part-b-new-edition" class="greyText" rel="nofollow">4 editions</a>\n        </span>\n        \n\n\n    </td>\n\n      <td width="130px">\n          <div class="wtrButtonContainer wtrSignedOut" id="9_book_5430955">\n<div class="wtrUp wtrLeft">\n<form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="book_id" name="book_id" type="hidden" value="5430955"/><input id="name" name="name" type="hidden" value="to-read"/><input id="unique_id" name="unique_id" type="hidden" value="9_book_5430955"/><input id="wtr_new" name="wtr_new" type="hidden" value="true"/><button class="wtrToRead" type="submit">\n<span class="progressTrigger">Want to Read</span>\n<span class="progressIndicator">saving\xe2\x80\xa6</span>\n</button>\n</form>\n\n</div>\n\n<div class="wtrDivider"/>\n<div class="wtrRight">\n<button class="wtrShelfButton wtrUp">\n<img alt="pick shelf" src="http://s.gr-assets.com/assets/wtr_button/books-0866015891eb128cdc57e550383532a0.png"/></button>\n<div class="wtrShelfMenu">\n<ul class="wtrExclusiveShelves"><li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="9_book_5430955"/><input id="book_id" name="book_id" type="hidden" value="5430955"/><button class="wtrExclusiveShelf" name="name" type="submit" value="to-read">\n<span class="progressTrigger">Want to Read</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="9_book_5430955"/><input id="book_id" name="book_id" type="hidden" value="5430955"/><button class="wtrExclusiveShelf" name="name" type="submit" value="currently-reading">\n<span class="progressTrigger">Currently Reading</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="9_book_5430955"/><input id="book_id" name="book_id" type="hidden" value="5430955"/><button class="wtrExclusiveShelf" name="name" type="submit" value="read">\n<span class="progressTrigger">Read</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n</ul></div>\n</div>\n\n<div class="ratingStars wtrRating">\n<form accept-charset="UTF-8" action="/review/rate/5430955-atlas-shrugged-part-b" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<button class="greyText uitext myRating" disabled="disabled" name="button" type="submit">Rate this book</button>\n<div class="clearRating uitext">Clear rating</div>\n<input id="rating" name="rating" type="hidden" value="0"/><input id="wtr_button_id" name="wtr_button_id" type="hidden" value="9_book_5430955"/></form>\n\n<span class="stars" id="starsstars_for_9_book_5430955" onmouseout="mouseOutStars(\'stars_for_9_book_5430955\')"><a rel="nofollow"><img alt="didn\'t like it " class="star" height="15" id="starstars_for_9_book_5430955_0" onclick="submitStars(\'stars_for_9_book_5430955\', 0, \'/review/rate/5430955?rating=1&amp;wtr_button_id=9_book_5430955\', 0);  return false;" onmouseover="checkStars(\'stars_for_9_book_5430955\', 0)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="didn\'t like it" width="15"/></a><a rel="nofollow"><img alt="it was ok " class="star" height="15" id="starstars_for_9_book_5430955_1" onclick="submitStars(\'stars_for_9_book_5430955\', 1, \'/review/rate/5430955?rating=2&amp;wtr_button_id=9_book_5430955\', 0);  return false;" onmouseover="checkStars(\'stars_for_9_book_5430955\', 1)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was ok" width="15"/></a><a rel="nofollow"><img alt="liked it " class="star" height="15" id="starstars_for_9_book_5430955_2" onclick="submitStars(\'stars_for_9_book_5430955\', 2, \'/review/rate/5430955?rating=3&amp;wtr_button_id=9_book_5430955\', 0);  return false;" onmouseover="checkStars(\'stars_for_9_book_5430955\', 2)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="liked it" width="15"/></a><a rel="nofollow"><img alt="really liked it " class="star" height="15" id="starstars_for_9_book_5430955_3" onclick="submitStars(\'stars_for_9_book_5430955\', 3, \'/review/rate/5430955?rating=4&amp;wtr_button_id=9_book_5430955\', 0);  return false;" onmouseover="checkStars(\'stars_for_9_book_5430955\', 3)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="really liked it" width="15"/></a><a rel="nofollow"><img alt="it was amazing " class="star" height="15" id="starstars_for_9_book_5430955_4" onclick="submitStars(\'stars_for_9_book_5430955\', 4, \'/review/rate/5430955?rating=5&amp;wtr_button_id=9_book_5430955\', 0);  return false;" onmouseover="checkStars(\'stars_for_9_book_5430955\', 4)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was amazing" width="15"/></a></span><script language="javascript" type="text/javascript">starRatings[ratingIndex++] = [ \'stars_for_9_book_5430955\', -1]; checkStars(\'stars_for_9_book_5430955\', -1);</script></div>\n\n</div>\n\n      </td>\n\n  </tr><tr itemscope="" itemtype="http://schema.org/Book"><td width="5%" valign="top">\n      <a name="5141345"/>\n      <a href="/book/show/5141345-atlas-shrugged-part-c" title="Atlas Shrugged Part C: New Edition">\n          <img alt="Atlas Shrugged Part C: New ..." class="bookSmallImg" src="http://d.gr-assets.com/books/1348467302s/5141345.jpg"/></a>    </td>\n    <td width="100%" valign="top">\n      <a href="/book/show/5141345-atlas-shrugged-part-c" class="bookTitle" itemprop="url">\n        <span itemprop="name">Atlas Shrugged Part C: New Edition</span>\n</a>      <br/><span class="by smallText">by</span>\n<span itemprop="author" itemscope="" itemtype="http://schema.org/Person">\n<a href="http://www.goodreads.com/author/show/432.Ayn_Rand" class="authorName" itemprop="url"><span itemprop="name">Ayn Rand</span></a>\n</span>\n\n        <br/><span class="greyText smallText uitext">\n          <span class="minirating"><span class="stars"><img alt="3.78 of 5 stars" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.78 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.78 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.78 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/stars/red_star_66pct-a2f513494595fa112f4762672b33daef.png" title="3.78 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="3.78 of 5 stars" width="12"/></span> 3.78 avg rating \u2014 23 ratings</span>\n            \u2014\n            <a href="/work/editions/21836609-atlas-shrugged-part-c-new-edition" class="greyText" rel="nofollow">4 editions</a>\n        </span>\n        \n\n\n    </td>\n\n      <td width="130px">\n          <div class="wtrButtonContainer wtrSignedOut" id="10_book_5141345">\n<div class="wtrUp wtrLeft">\n<form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="book_id" name="book_id" type="hidden" value="5141345"/><input id="name" name="name" type="hidden" value="to-read"/><input id="unique_id" name="unique_id" type="hidden" value="10_book_5141345"/><input id="wtr_new" name="wtr_new" type="hidden" value="true"/><button class="wtrToRead" type="submit">\n<span class="progressTrigger">Want to Read</span>\n<span class="progressIndicator">saving\xe2\x80\xa6</span>\n</button>\n</form>\n\n</div>\n\n<div class="wtrDivider"/>\n<div class="wtrRight">\n<button class="wtrShelfButton wtrUp">\n<img alt="pick shelf" src="http://s.gr-assets.com/assets/wtr_button/books-0866015891eb128cdc57e550383532a0.png"/></button>\n<div class="wtrShelfMenu">\n<ul class="wtrExclusiveShelves"><li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="10_book_5141345"/><input id="book_id" name="book_id" type="hidden" value="5141345"/><button class="wtrExclusiveShelf" name="name" type="submit" value="to-read">\n<span class="progressTrigger">Want to Read</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="10_book_5141345"/><input id="book_id" name="book_id" type="hidden" value="5141345"/><button class="wtrExclusiveShelf" name="name" type="submit" value="currently-reading">\n<span class="progressTrigger">Currently Reading</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="10_book_5141345"/><input id="book_id" name="book_id" type="hidden" value="5141345"/><button class="wtrExclusiveShelf" name="name" type="submit" value="read">\n<span class="progressTrigger">Read</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n</ul></div>\n</div>\n\n<div class="ratingStars wtrRating">\n<form accept-charset="UTF-8" action="/review/rate/5141345-atlas-shrugged-part-c" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<button class="greyText uitext myRating" disabled="disabled" name="button" type="submit">Rate this book</button>\n<div class="clearRating uitext">Clear rating</div>\n<input id="rating" name="rating" type="hidden" value="0"/><input id="wtr_button_id" name="wtr_button_id" type="hidden" value="10_book_5141345"/></form>\n\n<span class="stars" id="starsstars_for_10_book_5141345" onmouseout="mouseOutStars(\'stars_for_10_book_5141345\')"><a rel="nofollow"><img alt="didn\'t like it " class="star" height="15" id="starstars_for_10_book_5141345_0" onclick="submitStars(\'stars_for_10_book_5141345\', 0, \'/review/rate/5141345?rating=1&amp;wtr_button_id=10_book_5141345\', 0);  return false;" onmouseover="checkStars(\'stars_for_10_book_5141345\', 0)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="didn\'t like it" width="15"/></a><a rel="nofollow"><img alt="it was ok " class="star" height="15" id="starstars_for_10_book_5141345_1" onclick="submitStars(\'stars_for_10_book_5141345\', 1, \'/review/rate/5141345?rating=2&amp;wtr_button_id=10_book_5141345\', 0);  return false;" onmouseover="checkStars(\'stars_for_10_book_5141345\', 1)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was ok" width="15"/></a><a rel="nofollow"><img alt="liked it " class="star" height="15" id="starstars_for_10_book_5141345_2" onclick="submitStars(\'stars_for_10_book_5141345\', 2, \'/review/rate/5141345?rating=3&amp;wtr_button_id=10_book_5141345\', 0);  return false;" onmouseover="checkStars(\'stars_for_10_book_5141345\', 2)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="liked it" width="15"/></a><a rel="nofollow"><img alt="really liked it " class="star" height="15" id="starstars_for_10_book_5141345_3" onclick="submitStars(\'stars_for_10_book_5141345\', 3, \'/review/rate/5141345?rating=4&amp;wtr_button_id=10_book_5141345\', 0);  return false;" onmouseover="checkStars(\'stars_for_10_book_5141345\', 3)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="really liked it" width="15"/></a><a rel="nofollow"><img alt="it was amazing " class="star" height="15" id="starstars_for_10_book_5141345_4" onclick="submitStars(\'stars_for_10_book_5141345\', 4, \'/review/rate/5141345?rating=5&amp;wtr_button_id=10_book_5141345\', 0);  return false;" onmouseover="checkStars(\'stars_for_10_book_5141345\', 4)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was amazing" width="15"/></a></span><script language="javascript" type="text/javascript">starRatings[ratingIndex++] = [ \'stars_for_10_book_5141345\', -1]; checkStars(\'stars_for_10_book_5141345\', -1);</script></div>\n\n</div>\n\n      </td>\n\n  </tr><tr itemscope="" itemtype="http://schema.org/Book"><td width="5%" valign="top">\n      <a name="9017523"/>\n      <a href="/book/show/9017523-novels-by-ayn-rand" title="Novels by Ayn Rand: We the Living, Atlas Shrugged, the Fountainhead">\n          <img alt="Novels by Ayn Rand: We the ..." class="bookSmallImg" src="http://d.gr-assets.com/books/1348368069s/9017523.jpg"/></a>    </td>\n    <td width="100%" valign="top">\n      <a href="/book/show/9017523-novels-by-ayn-rand" class="bookTitle" itemprop="url">\n        <span itemprop="name">Novels by Ayn Rand: We the Living, Atlas Shrugged, the Fountainhead</span>\n</a>      <br/><span class="by smallText">by</span>\n<span itemprop="author" itemscope="" itemtype="http://schema.org/Person">\n<a href="http://www.goodreads.com/author/show/4340042.Books_LLC" class="authorName" itemprop="url"><span itemprop="name">Books LLC</span></a>\n</span>\n\n        <br/><span class="greyText smallText uitext">\n          <span class="minirating"><span class="stars"><img alt="4.5 of 5 stars" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.5 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.5 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.5 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.5 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/stars/red_star_66pct-a2f513494595fa112f4762672b33daef.png" title="4.5 of 5 stars" width="12"/></span> 4.50 avg rating \u2014 16 ratings</span>\n            \u2014\n              published\n             2010\n            \u2014\n            <a href="/work/editions/13895034-novels-by-ayn-rand-we-the-living-atlas-shrugged-the-fountainhead" class="greyText" rel="nofollow">1 edition</a>\n        </span>\n        \n\n\n    </td>\n\n      <td width="130px">\n          <div class="wtrButtonContainer wtrSignedOut" id="11_book_9017523">\n<div class="wtrUp wtrLeft">\n<form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="book_id" name="book_id" type="hidden" value="9017523"/><input id="name" name="name" type="hidden" value="to-read"/><input id="unique_id" name="unique_id" type="hidden" value="11_book_9017523"/><input id="wtr_new" name="wtr_new" type="hidden" value="true"/><button class="wtrToRead" type="submit">\n<span class="progressTrigger">Want to Read</span>\n<span class="progressIndicator">saving\xe2\x80\xa6</span>\n</button>\n</form>\n\n</div>\n\n<div class="wtrDivider"/>\n<div class="wtrRight">\n<button class="wtrShelfButton wtrUp">\n<img alt="pick shelf" src="http://s.gr-assets.com/assets/wtr_button/books-0866015891eb128cdc57e550383532a0.png"/></button>\n<div class="wtrShelfMenu">\n<ul class="wtrExclusiveShelves"><li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="11_book_9017523"/><input id="book_id" name="book_id" type="hidden" value="9017523"/><button class="wtrExclusiveShelf" name="name" type="submit" value="to-read">\n<span class="progressTrigger">Want to Read</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="11_book_9017523"/><input id="book_id" name="book_id" type="hidden" value="9017523"/><button class="wtrExclusiveShelf" name="name" type="submit" value="currently-reading">\n<span class="progressTrigger">Currently Reading</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="11_book_9017523"/><input id="book_id" name="book_id" type="hidden" value="9017523"/><button class="wtrExclusiveShelf" name="name" type="submit" value="read">\n<span class="progressTrigger">Read</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n</ul></div>\n</div>\n\n<div class="ratingStars wtrRating">\n<form accept-charset="UTF-8" action="/review/rate/9017523-novels-by-ayn-rand" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<button class="greyText uitext myRating" disabled="disabled" name="button" type="submit">Rate this book</button>\n<div class="clearRating uitext">Clear rating</div>\n<input id="rating" name="rating" type="hidden" value="0"/><input id="wtr_button_id" name="wtr_button_id" type="hidden" value="11_book_9017523"/></form>\n\n<span class="stars" id="starsstars_for_11_book_9017523" onmouseout="mouseOutStars(\'stars_for_11_book_9017523\')"><a rel="nofollow"><img alt="didn\'t like it " class="star" height="15" id="starstars_for_11_book_9017523_0" onclick="submitStars(\'stars_for_11_book_9017523\', 0, \'/review/rate/9017523?rating=1&amp;wtr_button_id=11_book_9017523\', 0);  return false;" onmouseover="checkStars(\'stars_for_11_book_9017523\', 0)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="didn\'t like it" width="15"/></a><a rel="nofollow"><img alt="it was ok " class="star" height="15" id="starstars_for_11_book_9017523_1" onclick="submitStars(\'stars_for_11_book_9017523\', 1, \'/review/rate/9017523?rating=2&amp;wtr_button_id=11_book_9017523\', 0);  return false;" onmouseover="checkStars(\'stars_for_11_book_9017523\', 1)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was ok" width="15"/></a><a rel="nofollow"><img alt="liked it " class="star" height="15" id="starstars_for_11_book_9017523_2" onclick="submitStars(\'stars_for_11_book_9017523\', 2, \'/review/rate/9017523?rating=3&amp;wtr_button_id=11_book_9017523\', 0);  return false;" onmouseover="checkStars(\'stars_for_11_book_9017523\', 2)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="liked it" width="15"/></a><a rel="nofollow"><img alt="really liked it " class="star" height="15" id="starstars_for_11_book_9017523_3" onclick="submitStars(\'stars_for_11_book_9017523\', 3, \'/review/rate/9017523?rating=4&amp;wtr_button_id=11_book_9017523\', 0);  return false;" onmouseover="checkStars(\'stars_for_11_book_9017523\', 3)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="really liked it" width="15"/></a><a rel="nofollow"><img alt="it was amazing " class="star" height="15" id="starstars_for_11_book_9017523_4" onclick="submitStars(\'stars_for_11_book_9017523\', 4, \'/review/rate/9017523?rating=5&amp;wtr_button_id=11_book_9017523\', 0);  return false;" onmouseover="checkStars(\'stars_for_11_book_9017523\', 4)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was amazing" width="15"/></a></span><script language="javascript" type="text/javascript">starRatings[ratingIndex++] = [ \'stars_for_11_book_9017523\', -1]; checkStars(\'stars_for_11_book_9017523\', -1);</script></div>\n\n</div>\n\n      </td>\n\n  </tr><tr itemscope="" itemtype="http://schema.org/Book"><td width="5%" valign="top">\n      <a name="181147"/>\n      <a href="/book/show/181147.Atlas_Shrugged" title="Atlas Shrugged">\n          <img alt="Atlas Shrugged (SparkNotes ..." class="bookSmallImg" src="http://d.gr-assets.com/books/1328853108s/181147.jpg"/></a>    </td>\n    <td width="100%" valign="top">\n      <a href="/book/show/181147.Atlas_Shrugged" class="bookTitle" itemprop="url">\n        <span itemprop="name">Atlas Shrugged (SparkNotes Literature Guides)</span>\n</a>      <br/><span class="by smallText">by</span>\n<span itemprop="author" itemscope="" itemtype="http://schema.org/Person">\n<a href="http://www.goodreads.com/author/show/6460726.SparkNotes_Editors" class="authorName" itemprop="url"><span itemprop="name">SparkNotes Editors</span></a>, \n<a href="http://www.goodreads.com/author/show/432.Ayn_Rand" class="authorName" itemprop="url"><span itemprop="name">Ayn Rand</span></a>, <a href="http://www.goodreads.com/author/show/2904509.SparkNotes" class="authorName" itemprop="url"><span itemprop="name">SparkNotes</span></a>\n</span>\n\n        <br/><span class="greyText smallText uitext">\n          <span class="minirating"><span class="stars"><img alt="4.25 of 5 stars" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.25 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.25 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.25 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.25 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/stars/red_star_33pct-69a219b6d79a91503f292bf5ac039d6b.png" title="4.25 of 5 stars" width="12"/></span> 4.25 avg rating \u2014 8 ratings</span>\n            \u2014\n              published\n             2003\n            \u2014\n            <a href="/work/editions/175035-spark-notes-atlas-shrugged-sparknotes-literature-guides" class="greyText" rel="nofollow">3 editions</a>\n        </span>\n        \n\n\n    </td>\n\n      <td width="130px">\n          <div class="wtrButtonContainer wtrSignedOut" id="12_book_181147">\n<div class="wtrUp wtrLeft">\n<form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="book_id" name="book_id" type="hidden" value="181147"/><input id="name" name="name" type="hidden" value="to-read"/><input id="unique_id" name="unique_id" type="hidden" value="12_book_181147"/><input id="wtr_new" name="wtr_new" type="hidden" value="true"/><button class="wtrToRead" type="submit">\n<span class="progressTrigger">Want to Read</span>\n<span class="progressIndicator">saving\xe2\x80\xa6</span>\n</button>\n</form>\n\n</div>\n\n<div class="wtrDivider"/>\n<div class="wtrRight">\n<button class="wtrShelfButton wtrUp">\n<img alt="pick shelf" src="http://s.gr-assets.com/assets/wtr_button/books-0866015891eb128cdc57e550383532a0.png"/></button>\n<div class="wtrShelfMenu">\n<ul class="wtrExclusiveShelves"><li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="12_book_181147"/><input id="book_id" name="book_id" type="hidden" value="181147"/><button class="wtrExclusiveShelf" name="name" type="submit" value="to-read">\n<span class="progressTrigger">Want to Read</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="12_book_181147"/><input id="book_id" name="book_id" type="hidden" value="181147"/><button class="wtrExclusiveShelf" name="name" type="submit" value="currently-reading">\n<span class="progressTrigger">Currently Reading</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="12_book_181147"/><input id="book_id" name="book_id" type="hidden" value="181147"/><button class="wtrExclusiveShelf" name="name" type="submit" value="read">\n<span class="progressTrigger">Read</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n</ul></div>\n</div>\n\n<div class="ratingStars wtrRating">\n<form accept-charset="UTF-8" action="/review/rate/181147.Atlas_Shrugged" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<button class="greyText uitext myRating" disabled="disabled" name="button" type="submit">Rate this book</button>\n<div class="clearRating uitext">Clear rating</div>\n<input id="rating" name="rating" type="hidden" value="0"/><input id="wtr_button_id" name="wtr_button_id" type="hidden" value="12_book_181147"/></form>\n\n<span class="stars" id="starsstars_for_12_book_181147" onmouseout="mouseOutStars(\'stars_for_12_book_181147\')"><a rel="nofollow"><img alt="didn\'t like it " class="star" height="15" id="starstars_for_12_book_181147_0" onclick="submitStars(\'stars_for_12_book_181147\', 0, \'/review/rate/181147?rating=1&amp;wtr_button_id=12_book_181147\', 0);  return false;" onmouseover="checkStars(\'stars_for_12_book_181147\', 0)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="didn\'t like it" width="15"/></a><a rel="nofollow"><img alt="it was ok " class="star" height="15" id="starstars_for_12_book_181147_1" onclick="submitStars(\'stars_for_12_book_181147\', 1, \'/review/rate/181147?rating=2&amp;wtr_button_id=12_book_181147\', 0);  return false;" onmouseover="checkStars(\'stars_for_12_book_181147\', 1)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was ok" width="15"/></a><a rel="nofollow"><img alt="liked it " class="star" height="15" id="starstars_for_12_book_181147_2" onclick="submitStars(\'stars_for_12_book_181147\', 2, \'/review/rate/181147?rating=3&amp;wtr_button_id=12_book_181147\', 0);  return false;" onmouseover="checkStars(\'stars_for_12_book_181147\', 2)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="liked it" width="15"/></a><a rel="nofollow"><img alt="really liked it " class="star" height="15" id="starstars_for_12_book_181147_3" onclick="submitStars(\'stars_for_12_book_181147\', 3, \'/review/rate/181147?rating=4&amp;wtr_button_id=12_book_181147\', 0);  return false;" onmouseover="checkStars(\'stars_for_12_book_181147\', 3)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="really liked it" width="15"/></a><a rel="nofollow"><img alt="it was amazing " class="star" height="15" id="starstars_for_12_book_181147_4" onclick="submitStars(\'stars_for_12_book_181147\', 4, \'/review/rate/181147?rating=5&amp;wtr_button_id=12_book_181147\', 0);  return false;" onmouseover="checkStars(\'stars_for_12_book_181147\', 4)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was amazing" width="15"/></a></span><script language="javascript" type="text/javascript">starRatings[ratingIndex++] = [ \'stars_for_12_book_181147\', -1]; checkStars(\'stars_for_12_book_181147\', -1);</script></div>\n\n</div>\n\n      </td>\n\n  </tr><tr itemscope="" itemtype="http://schema.org/Book"><td width="5%" valign="top">\n      <a name="16135783"/>\n      <a href="/book/show/16135783-atlas-shrugged" title="Atlas Shrugged">\n          <img alt="Atlas Shrugged" class="bookSmallImg" src="http://www.goodreads.com/assets/nocover/60x80.png"/></a>    </td>\n    <td width="100%" valign="top">\n      <a href="/book/show/16135783-atlas-shrugged" class="bookTitle" itemprop="url">\n        <span itemprop="name">Atlas Shrugged</span>\n</a>      <br/><span class="by smallText">by</span>\n<span itemprop="author" itemscope="" itemtype="http://schema.org/Person">\n<a href="http://www.goodreads.com/author/show/432.Ayn_Rand" class="authorName" itemprop="url"><span itemprop="name">Ayn Rand</span></a>\n</span>\n\n        <br/><span class="greyText smallText uitext">\n          <span class="minirating"><span class="stars"><img alt="0.0 of 5 stars" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="0.0 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="0.0 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="0.0 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="0.0 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="0.0 of 5 stars" width="12"/></span> 0.00 avg rating \u2014 0 ratings</span>\n            \u2014\n              published\n             1957\n            \u2014\n            <a href="/work/editions/21963920-atlas-shrugged" class="greyText" rel="nofollow">1 edition</a>\n        </span>\n        \n\n\n    </td>\n\n      <td width="130px">\n          <div class="wtrButtonContainer wtrSignedOut" id="13_book_16135783">\n<div class="wtrUp wtrLeft">\n<form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="book_id" name="book_id" type="hidden" value="16135783"/><input id="name" name="name" type="hidden" value="to-read"/><input id="unique_id" name="unique_id" type="hidden" value="13_book_16135783"/><input id="wtr_new" name="wtr_new" type="hidden" value="true"/><button class="wtrToRead" type="submit">\n<span class="progressTrigger">Want to Read</span>\n<span class="progressIndicator">saving\xe2\x80\xa6</span>\n</button>\n</form>\n\n</div>\n\n<div class="wtrDivider"/>\n<div class="wtrRight">\n<button class="wtrShelfButton wtrUp">\n<img alt="pick shelf" src="http://s.gr-assets.com/assets/wtr_button/books-0866015891eb128cdc57e550383532a0.png"/></button>\n<div class="wtrShelfMenu">\n<ul class="wtrExclusiveShelves"><li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="13_book_16135783"/><input id="book_id" name="book_id" type="hidden" value="16135783"/><button class="wtrExclusiveShelf" name="name" type="submit" value="to-read">\n<span class="progressTrigger">Want to Read</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="13_book_16135783"/><input id="book_id" name="book_id" type="hidden" value="16135783"/><button class="wtrExclusiveShelf" name="name" type="submit" value="currently-reading">\n<span class="progressTrigger">Currently Reading</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="13_book_16135783"/><input id="book_id" name="book_id" type="hidden" value="16135783"/><button class="wtrExclusiveShelf" name="name" type="submit" value="read">\n<span class="progressTrigger">Read</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n</ul></div>\n</div>\n\n<div class="ratingStars wtrRating">\n<form accept-charset="UTF-8" action="/review/rate/16135783-atlas-shrugged" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<button class="greyText uitext myRating" disabled="disabled" name="button" type="submit">Rate this book</button>\n<div class="clearRating uitext">Clear rating</div>\n<input id="rating" name="rating" type="hidden" value="0"/><input id="wtr_button_id" name="wtr_button_id" type="hidden" value="13_book_16135783"/></form>\n\n<span class="stars" id="starsstars_for_13_book_16135783" onmouseout="mouseOutStars(\'stars_for_13_book_16135783\')"><a rel="nofollow"><img alt="didn\'t like it " class="star" height="15" id="starstars_for_13_book_16135783_0" onclick="submitStars(\'stars_for_13_book_16135783\', 0, \'/review/rate/16135783?rating=1&amp;wtr_button_id=13_book_16135783\', 0);  return false;" onmouseover="checkStars(\'stars_for_13_book_16135783\', 0)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="didn\'t like it" width="15"/></a><a rel="nofollow"><img alt="it was ok " class="star" height="15" id="starstars_for_13_book_16135783_1" onclick="submitStars(\'stars_for_13_book_16135783\', 1, \'/review/rate/16135783?rating=2&amp;wtr_button_id=13_book_16135783\', 0);  return false;" onmouseover="checkStars(\'stars_for_13_book_16135783\', 1)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was ok" width="15"/></a><a rel="nofollow"><img alt="liked it " class="star" height="15" id="starstars_for_13_book_16135783_2" onclick="submitStars(\'stars_for_13_book_16135783\', 2, \'/review/rate/16135783?rating=3&amp;wtr_button_id=13_book_16135783\', 0);  return false;" onmouseover="checkStars(\'stars_for_13_book_16135783\', 2)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="liked it" width="15"/></a><a rel="nofollow"><img alt="really liked it " class="star" height="15" id="starstars_for_13_book_16135783_3" onclick="submitStars(\'stars_for_13_book_16135783\', 3, \'/review/rate/16135783?rating=4&amp;wtr_button_id=13_book_16135783\', 0);  return false;" onmouseover="checkStars(\'stars_for_13_book_16135783\', 3)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="really liked it" width="15"/></a><a rel="nofollow"><img alt="it was amazing " class="star" height="15" id="starstars_for_13_book_16135783_4" onclick="submitStars(\'stars_for_13_book_16135783\', 4, \'/review/rate/16135783?rating=5&amp;wtr_button_id=13_book_16135783\', 0);  return false;" onmouseover="checkStars(\'stars_for_13_book_16135783\', 4)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was amazing" width="15"/></a></span><script language="javascript" type="text/javascript">starRatings[ratingIndex++] = [ \'stars_for_13_book_16135783\', -1]; checkStars(\'stars_for_13_book_16135783\', -1);</script></div>\n\n</div>\n\n      </td>\n\n  </tr><tr itemscope="" itemtype="http://schema.org/Book"><td width="5%" valign="top">\n      <a name="9577604"/>\n      <a href="/book/show/9577604-why-businessmen-need-philosophy" title="Why Businessmen Need Philosophy: The Capitalist\'s Guide to the Ideas Behind Ayn Rand\'s AtlasShrugged">\n          <img alt="Why Businessmen Need Philos..." class="bookSmallImg" src="http://d.gr-assets.com/books/1347770922s/9577604.jpg"/></a>    </td>\n    <td width="100%" valign="top">\n      <a href="/book/show/9577604-why-businessmen-need-philosophy" class="bookTitle" itemprop="url">\n        <span itemprop="name">Why Businessmen Need Philosophy: The Capitalist\'s Guide to the Ideas Behind Ayn Rand\'s AtlasShrugged</span>\n</a>      <br/><span class="by smallText">by</span>\n<span itemprop="author" itemscope="" itemtype="http://schema.org/Person">\n<a href="http://www.goodreads.com/author/show/89107.Richard_E_Ralston" class="authorName" itemprop="url"><span itemprop="name">Richard E. Ralston</span></a> <span class="authorName greyText smallText role">(Editor)</span>, \n<a href="http://www.goodreads.com/author/show/5145756.John_A_Allison" class="authorName" itemprop="url"><span itemprop="name">John A. Allison</span></a> <span class="authorName greyText smallText role">(Introduction)</span>\n</span>\n\n        <br/><span class="greyText smallText uitext">\n          <span class="minirating"><span class="stars"><img alt="4.08 of 5 stars" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.08 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.08 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.08 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.08 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/stars/red_star_33pct-69a219b6d79a91503f292bf5ac039d6b.png" title="4.08 of 5 stars" width="12"/></span> 4.08 avg rating \u2014 12 ratings</span>\n            \u2014\n              published\n             2011\n            \u2014\n            <a href="/work/editions/14464481-why-businessmen-need-philosophy-the-capitalist-s-guide-to-the-ideas-beh" class="greyText" rel="nofollow">3 editions</a>\n        </span>\n        \n\n\n    </td>\n\n      <td width="130px">\n          <div class="wtrButtonContainer wtrSignedOut" id="14_book_9577604">\n<div class="wtrUp wtrLeft">\n<form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="book_id" name="book_id" type="hidden" value="9577604"/><input id="name" name="name" type="hidden" value="to-read"/><input id="unique_id" name="unique_id" type="hidden" value="14_book_9577604"/><input id="wtr_new" name="wtr_new" type="hidden" value="true"/><button class="wtrToRead" type="submit">\n<span class="progressTrigger">Want to Read</span>\n<span class="progressIndicator">saving\xe2\x80\xa6</span>\n</button>\n</form>\n\n</div>\n\n<div class="wtrDivider"/>\n<div class="wtrRight">\n<button class="wtrShelfButton wtrUp">\n<img alt="pick shelf" src="http://s.gr-assets.com/assets/wtr_button/books-0866015891eb128cdc57e550383532a0.png"/></button>\n<div class="wtrShelfMenu">\n<ul class="wtrExclusiveShelves"><li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="14_book_9577604"/><input id="book_id" name="book_id" type="hidden" value="9577604"/><button class="wtrExclusiveShelf" name="name" type="submit" value="to-read">\n<span class="progressTrigger">Want to Read</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="14_book_9577604"/><input id="book_id" name="book_id" type="hidden" value="9577604"/><button class="wtrExclusiveShelf" name="name" type="submit" value="currently-reading">\n<span class="progressTrigger">Currently Reading</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="14_book_9577604"/><input id="book_id" name="book_id" type="hidden" value="9577604"/><button class="wtrExclusiveShelf" name="name" type="submit" value="read">\n<span class="progressTrigger">Read</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n</ul></div>\n</div>\n\n<div class="ratingStars wtrRating">\n<form accept-charset="UTF-8" action="/review/rate/9577604-why-businessmen-need-philosophy" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<button class="greyText uitext myRating" disabled="disabled" name="button" type="submit">Rate this book</button>\n<div class="clearRating uitext">Clear rating</div>\n<input id="rating" name="rating" type="hidden" value="0"/><input id="wtr_button_id" name="wtr_button_id" type="hidden" value="14_book_9577604"/></form>\n\n<span class="stars" id="starsstars_for_14_book_9577604" onmouseout="mouseOutStars(\'stars_for_14_book_9577604\')"><a rel="nofollow"><img alt="didn\'t like it " class="star" height="15" id="starstars_for_14_book_9577604_0" onclick="submitStars(\'stars_for_14_book_9577604\', 0, \'/review/rate/9577604?rating=1&amp;wtr_button_id=14_book_9577604\', 0);  return false;" onmouseover="checkStars(\'stars_for_14_book_9577604\', 0)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="didn\'t like it" width="15"/></a><a rel="nofollow"><img alt="it was ok " class="star" height="15" id="starstars_for_14_book_9577604_1" onclick="submitStars(\'stars_for_14_book_9577604\', 1, \'/review/rate/9577604?rating=2&amp;wtr_button_id=14_book_9577604\', 0);  return false;" onmouseover="checkStars(\'stars_for_14_book_9577604\', 1)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was ok" width="15"/></a><a rel="nofollow"><img alt="liked it " class="star" height="15" id="starstars_for_14_book_9577604_2" onclick="submitStars(\'stars_for_14_book_9577604\', 2, \'/review/rate/9577604?rating=3&amp;wtr_button_id=14_book_9577604\', 0);  return false;" onmouseover="checkStars(\'stars_for_14_book_9577604\', 2)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="liked it" width="15"/></a><a rel="nofollow"><img alt="really liked it " class="star" height="15" id="starstars_for_14_book_9577604_3" onclick="submitStars(\'stars_for_14_book_9577604\', 3, \'/review/rate/9577604?rating=4&amp;wtr_button_id=14_book_9577604\', 0);  return false;" onmouseover="checkStars(\'stars_for_14_book_9577604\', 3)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="really liked it" width="15"/></a><a rel="nofollow"><img alt="it was amazing " class="star" height="15" id="starstars_for_14_book_9577604_4" onclick="submitStars(\'stars_for_14_book_9577604\', 4, \'/review/rate/9577604?rating=5&amp;wtr_button_id=14_book_9577604\', 0);  return false;" onmouseover="checkStars(\'stars_for_14_book_9577604\', 4)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was amazing" width="15"/></a></span><script language="javascript" type="text/javascript">starRatings[ratingIndex++] = [ \'stars_for_14_book_9577604\', -1]; checkStars(\'stars_for_14_book_9577604\', -1);</script></div>\n\n</div>\n\n      </td>\n\n  </tr><tr itemscope="" itemtype="http://schema.org/Book"><td width="5%" valign="top">\n      <a name="9935187"/>\n      <a href="/book/show/9935187-works-by-ayn-rand-book-guide" title="Works by Ayn Rand (Book Guide): Ayn Rand Characters, Books by Ayn Rand, Novels by Ayn Rand, Plays by Ayn Rand, We the Living, Atlas Shrugged">\n          <img alt="Works by Ayn Rand (Book Gui..." class="bookSmallImg" src="http://d.gr-assets.com/books/1347935031s/9935187.jpg"/></a>    </td>\n    <td width="100%" valign="top">\n      <a href="/book/show/9935187-works-by-ayn-rand-book-guide" class="bookTitle" itemprop="url">\n        <span itemprop="name">Works by Ayn Rand (Book Guide): Ayn Rand Characters, Books by Ayn Rand, Novels by Ayn Rand, Plays by Ayn Rand, We the Living, Atlas Shrugged</span>\n</a>      <br/><span class="by smallText">by</span>\n<span itemprop="author" itemscope="" itemtype="http://schema.org/Person">\n<a href="http://www.goodreads.com/author/show/5153555.Source_Wikipedia" class="authorName" itemprop="url"><span itemprop="name">Source Wikipedia</span></a>\n</span>\n\n        <br/><span class="greyText smallText uitext">\n          <span class="minirating"><span class="stars"><img alt="5.0 of 5 stars" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="5.0 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="5.0 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="5.0 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="5.0 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="5.0 of 5 stars" width="12"/></span> 5.00 avg rating \u2014 1 rating</span>\n            \u2014\n              published\n             2010\n            \u2014\n            <a href="/work/editions/14828345-works-by-ayn-rand-book-guide-ayn-rand-characters-books-by-ayn-rand" class="greyText" rel="nofollow">1 edition</a>\n        </span>\n        \n\n\n    </td>\n\n      <td width="130px">\n          <div class="wtrButtonContainer wtrSignedOut" id="15_book_9935187">\n<div class="wtrUp wtrLeft">\n<form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="book_id" name="book_id" type="hidden" value="9935187"/><input id="name" name="name" type="hidden" value="to-read"/><input id="unique_id" name="unique_id" type="hidden" value="15_book_9935187"/><input id="wtr_new" name="wtr_new" type="hidden" value="true"/><button class="wtrToRead" type="submit">\n<span class="progressTrigger">Want to Read</span>\n<span class="progressIndicator">saving\xe2\x80\xa6</span>\n</button>\n</form>\n\n</div>\n\n<div class="wtrDivider"/>\n<div class="wtrRight">\n<button class="wtrShelfButton wtrUp">\n<img alt="pick shelf" src="http://s.gr-assets.com/assets/wtr_button/books-0866015891eb128cdc57e550383532a0.png"/></button>\n<div class="wtrShelfMenu">\n<ul class="wtrExclusiveShelves"><li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="15_book_9935187"/><input id="book_id" name="book_id" type="hidden" value="9935187"/><button class="wtrExclusiveShelf" name="name" type="submit" value="to-read">\n<span class="progressTrigger">Want to Read</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="15_book_9935187"/><input id="book_id" name="book_id" type="hidden" value="9935187"/><button class="wtrExclusiveShelf" name="name" type="submit" value="currently-reading">\n<span class="progressTrigger">Currently Reading</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="15_book_9935187"/><input id="book_id" name="book_id" type="hidden" value="9935187"/><button class="wtrExclusiveShelf" name="name" type="submit" value="read">\n<span class="progressTrigger">Read</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n</ul></div>\n</div>\n\n<div class="ratingStars wtrRating">\n<form accept-charset="UTF-8" action="/review/rate/9935187-works-by-ayn-rand-book-guide" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<button class="greyText uitext myRating" disabled="disabled" name="button" type="submit">Rate this book</button>\n<div class="clearRating uitext">Clear rating</div>\n<input id="rating" name="rating" type="hidden" value="0"/><input id="wtr_button_id" name="wtr_button_id" type="hidden" value="15_book_9935187"/></form>\n\n<span class="stars" id="starsstars_for_15_book_9935187" onmouseout="mouseOutStars(\'stars_for_15_book_9935187\')"><a rel="nofollow"><img alt="didn\'t like it " class="star" height="15" id="starstars_for_15_book_9935187_0" onclick="submitStars(\'stars_for_15_book_9935187\', 0, \'/review/rate/9935187?rating=1&amp;wtr_button_id=15_book_9935187\', 0);  return false;" onmouseover="checkStars(\'stars_for_15_book_9935187\', 0)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="didn\'t like it" width="15"/></a><a rel="nofollow"><img alt="it was ok " class="star" height="15" id="starstars_for_15_book_9935187_1" onclick="submitStars(\'stars_for_15_book_9935187\', 1, \'/review/rate/9935187?rating=2&amp;wtr_button_id=15_book_9935187\', 0);  return false;" onmouseover="checkStars(\'stars_for_15_book_9935187\', 1)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was ok" width="15"/></a><a rel="nofollow"><img alt="liked it " class="star" height="15" id="starstars_for_15_book_9935187_2" onclick="submitStars(\'stars_for_15_book_9935187\', 2, \'/review/rate/9935187?rating=3&amp;wtr_button_id=15_book_9935187\', 0);  return false;" onmouseover="checkStars(\'stars_for_15_book_9935187\', 2)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="liked it" width="15"/></a><a rel="nofollow"><img alt="really liked it " class="star" height="15" id="starstars_for_15_book_9935187_3" onclick="submitStars(\'stars_for_15_book_9935187\', 3, \'/review/rate/9935187?rating=4&amp;wtr_button_id=15_book_9935187\', 0);  return false;" onmouseover="checkStars(\'stars_for_15_book_9935187\', 3)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="really liked it" width="15"/></a><a rel="nofollow"><img alt="it was amazing " class="star" height="15" id="starstars_for_15_book_9935187_4" onclick="submitStars(\'stars_for_15_book_9935187\', 4, \'/review/rate/9935187?rating=5&amp;wtr_button_id=15_book_9935187\', 0);  return false;" onmouseover="checkStars(\'stars_for_15_book_9935187\', 4)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was amazing" width="15"/></a></span><script language="javascript" type="text/javascript">starRatings[ratingIndex++] = [ \'stars_for_15_book_9935187\', -1]; checkStars(\'stars_for_15_book_9935187\', -1);</script></div>\n\n</div>\n\n      </td>\n\n  </tr><tr itemscope="" itemtype="http://schema.org/Book"><td width="5%" valign="top">\n      <a name="12716520"/>\n      <a href="/book/show/12716520-articles-on-novels-by-ayn-rand-including" title="Articles on Novels by Ayn Rand, Including: The Fountainhead, Anthem (Novella), We the Living, Atlas Shrugged">\n          <img alt="Articles on Novels by Ayn R..." class="bookSmallImg" src="http://d.gr-assets.com/books/1348641370s/12716520.jpg"/></a>    </td>\n    <td width="100%" valign="top">\n      <a href="/book/show/12716520-articles-on-novels-by-ayn-rand-including" class="bookTitle" itemprop="url">\n        <span itemprop="name">Articles on Novels by Ayn Rand, Including: The Fountainhead, Anthem (Novella), We the Living, Atlas Shrugged</span>\n</a>      <br/><span class="by smallText">by</span>\n<span itemprop="author" itemscope="" itemtype="http://schema.org/Person">\n<a href="http://www.goodreads.com/author/show/5167894.Hephaestus_Books" class="authorName" itemprop="url"><span itemprop="name">Hephaestus Books</span></a>\n</span>\n\n        <br/><span class="greyText smallText uitext">\n          <span class="minirating"><span class="stars"><img alt="3.0 of 5 stars" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.0 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.0 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.0 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="3.0 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="3.0 of 5 stars" width="12"/></span> 3.00 avg rating \u2014 1 rating</span>\n            \u2014\n              published\n             2011\n            \u2014\n            <a href="/work/editions/17851307-articles-on-novels-by-ayn-rand-including-the-fountainhead-anthem-nov" class="greyText" rel="nofollow">1 edition</a>\n        </span>\n        \n\n\n    </td>\n\n      <td width="130px">\n          <div class="wtrButtonContainer wtrSignedOut" id="16_book_12716520">\n<div class="wtrUp wtrLeft">\n<form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="book_id" name="book_id" type="hidden" value="12716520"/><input id="name" name="name" type="hidden" value="to-read"/><input id="unique_id" name="unique_id" type="hidden" value="16_book_12716520"/><input id="wtr_new" name="wtr_new" type="hidden" value="true"/><button class="wtrToRead" type="submit">\n<span class="progressTrigger">Want to Read</span>\n<span class="progressIndicator">saving\xe2\x80\xa6</span>\n</button>\n</form>\n\n</div>\n\n<div class="wtrDivider"/>\n<div class="wtrRight">\n<button class="wtrShelfButton wtrUp">\n<img alt="pick shelf" src="http://s.gr-assets.com/assets/wtr_button/books-0866015891eb128cdc57e550383532a0.png"/></button>\n<div class="wtrShelfMenu">\n<ul class="wtrExclusiveShelves"><li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="16_book_12716520"/><input id="book_id" name="book_id" type="hidden" value="12716520"/><button class="wtrExclusiveShelf" name="name" type="submit" value="to-read">\n<span class="progressTrigger">Want to Read</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="16_book_12716520"/><input id="book_id" name="book_id" type="hidden" value="12716520"/><button class="wtrExclusiveShelf" name="name" type="submit" value="currently-reading">\n<span class="progressTrigger">Currently Reading</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<input id="unique_id" name="unique_id" type="hidden" value="16_book_12716520"/><input id="book_id" name="book_id" type="hidden" value="12716520"/><button class="wtrExclusiveShelf" name="name" type="submit" value="read">\n<span class="progressTrigger">Read</span>\n<img alt="saving\xe2\x80\xa6" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>\n</form>\n\n</li>\n</ul></div>\n</div>\n\n<div class="ratingStars wtrRating">\n<form accept-charset="UTF-8" action="/review/rate/12716520-articles-on-novels-by-ayn-rand-including" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="\u2713"/><input name="authenticity_token" type="hidden" value="55xyUYaIFfAnaRwJAU3ckhDqDcq+6vQzHIh803ezWT4="/></div>\n<button class="greyText uitext myRating" disabled="disabled" name="button" type="submit">Rate this book</button>\n<div class="clearRating uitext">Clear rating</div>\n<input id="rating" name="rating" type="hidden" value="0"/><input id="wtr_button_id" name="wtr_button_id" type="hidden" value="16_book_12716520"/></form>\n\n<span class="stars" id="starsstars_for_16_book_12716520" onmouseout="mouseOutStars(\'stars_for_16_book_12716520\')"><a rel="nofollow"><img alt="didn\'t like it " class="star" height="15" id="starstars_for_16_book_12716520_0" onclick="submitStars(\'stars_for_16_book_12716520\', 0, \'/review/rate/12716520?rating=1&amp;wtr_button_id=16_book_12716520\', 0);  return false;" onmouseover="checkStars(\'stars_for_16_book_12716520\', 0)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="didn\'t like it" width="15"/></a><a rel="nofollow"><img alt="it was ok " class="star" height="15" id="starstars_for_16_book_12716520_1" onclick="submitStars(\'stars_for_16_book_12716520\', 1, \'/review/rate/12716520?rating=2&amp;wtr_button_id=16_book_12716520\', 0);  return false;" onmouseover="checkStars(\'stars_for_16_book_12716520\', 1)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was ok" width="15"/></a><a rel="nofollow"><img alt="liked it " class="star" height="15" id="starstars_for_16_book_12716520_2" onclick="submitStars(\'stars_for_16_book_12716520\', 2, \'/review/rate/12716520?rating=3&amp;wtr_button_id=16_book_12716520\', 0);  return false;" onmouseover="checkStars(\'stars_for_16_book_12716520\', 2)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="liked it" width="15"/></a><a rel="nofollow"><img alt="really liked it " class="star" height="15" id="starstars_for_16_book_12716520_3" onclick="submitStars(\'stars_for_16_book_12716520\', 3, \'/review/rate/12716520?rating=4&amp;wtr_button_id=16_book_12716520\', 0);  return false;" onmouseover="checkStars(\'stars_for_16_book_12716520\', 3)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="really liked it" width="15"/></a><a rel="nofollow"><img alt="it was amazing " class="star" height="15" id="starstars_for_16_book_12716520_4" onclick="submitStars(\'stars_for_16_book_12716520\', 4, \'/review/rate/12716520?rating=5&amp;wtr_button_id=16_book_12716520\', 0);  return false;" onmouseover="checkStars(\'stars_for_16_book_12716520\', 4)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was amazing" width="15"/></a></span><script language="javascript" type="text/javascript">starRatings[ratingIndex++] = [ \'stars_for_16_book_12716520\', -1]; checkStars(\'stars_for_16_book_12716520\', -1);</script></div>\n\n</div>\n\n      </td>\n\n  </tr></table><br/><div style="float: right">\n  \t  \n\n  \t</div>\n      <div id="adcontainer2"/>\n  \t<br/><br/><br/><br/></div>\n\n<div class="rightContainer">\n  <br/><a href="/book/new?book%5Btitle%5D=atlas+shrugged+ayn+rand" class="actionLinkLite" rel="nofollow">Manually add a book</a><br/><a href="/review/import" class="actionLinkLite" rel="nofollow">Import books</a><br/><br/><script language="JavaScript">\n    GA_googleAddSlot("ca-pub-7284881071421289", "Search")\n  </script><script language="JavaScript">\n    GA_googleFetchAds()\n  </script><script language="JavaScript">\n    GA_googleFillSlot("Search")\n  </script><div id="self_serve_ads"/>\n  \t<br/><div class=" clearFloats bigBox"><div class="h2Container gradientHeaderContainer"><h2 class="brownBackground"><a href="/shelf/top_shelves">Related Shelves</a></h2></div><div class="bigBoxBody"><div class="bigBoxContent containerWithHeaderContent">\n            <a href="/shelf/show/to-read" class="actionLinkLite" style="font-size: 1.1em">to-read</a> <span class="greyText smallText">(63,594,326)</span><br/><a href="/shelf/show/currently-reading" class="actionLinkLite" style="font-size: 1.1em">currently-reading</a> <span class="greyText smallText">(20,886,739)</span><br/><a href="/shelf/show/favorites" class="actionLinkLite" style="font-size: 1.1em">favorites</a> <span class="greyText smallText">(1,284,728)</span><br/><a href="/shelf/show/fiction" class="actionLinkLite" style="font-size: 1.1em">fiction</a> <span class="greyText smallText">(1,274,066)</span><br/><a href="/shelf/show/fantasy" class="actionLinkLite" style="font-size: 1.1em">fantasy</a> <span class="greyText smallText">(1,011,448)</span><br/><a href="/shelf/show/own" class="actionLinkLite" style="font-size: 1.1em">own</a> <span class="greyText smallText">(937,058)</span><br/><a href="/shelf/show/wishlist" class="actionLinkLite" style="font-size: 1.1em">wishlist</a> <span class="greyText smallText">(884,426)</span><br/><a href="/shelf/show/2012" class="actionLinkLite" style="font-size: 1.1em">2012</a> <span class="greyText smallText">(744,412)</span><br/><a href="/shelf/show/owned" class="actionLinkLite" style="font-size: 1.1em">owned</a> <span class="greyText smallText">(561,798)</span><br/><a href="/shelf/show/books-i-own" class="actionLinkLite" style="font-size: 1.1em">books-i-own</a> <span class="greyText smallText">(556,647)</span><br/><a href="/shelf/show/kindle" class="actionLinkLite" style="font-size: 1.1em">kindle</a> <span class="greyText smallText">(436,827)</span><br/><a href="/shelf/show/library" class="actionLinkLite" style="font-size: 1.1em">library</a> <span class="greyText smallText">(425,783)</span><br/><a href="/shelf/show/wish-list" class="actionLinkLite" style="font-size: 1.1em">wish-list</a> <span class="greyText smallText">(412,276)</span><br/><a href="/shelf/show/classics" class="actionLinkLite" style="font-size: 1.1em">classics</a> <span class="greyText smallText">(398,325)</span><br/><a href="/shelf/show/to-buy" class="actionLinkLite" style="font-size: 1.1em">to-buy</a> <span class="greyText smallText">(385,283)</span><br/><a href="/shelf/show/2011" class="actionLinkLite" style="font-size: 1.1em">2011</a> <span class="greyText smallText">(290,321)</span><br/><a href="/shelf/show/science-fiction" class="actionLinkLite" style="font-size: 1.1em">science-fiction</a> <span class="greyText smallText">(283,966)</span><br/><a href="/shelf/show/adult" class="actionLinkLite" style="font-size: 1.1em">adult</a> <span class="greyText smallText">(235,009)</span><br/><a href="/shelf/show/sci-fi" class="actionLinkLite" style="font-size: 1.1em">sci-fi</a> <span class="greyText smallText">(214,918)</span><br/><a href="/shelf/show/i-own" class="actionLinkLite" style="font-size: 1.1em">i-own</a> <span class="greyText smallText">(209,828)</span><br/><a href="/shelf/show/favourites" class="actionLinkLite" style="font-size: 1.1em">favourites</a> <span class="greyText smallText">(178,252)</span><br/><a href="/shelf/show/novels" class="actionLinkLite" style="font-size: 1.1em">novels</a> <span class="greyText smallText">(165,436)</span><br/><a href="/shelf/show/literature" class="actionLinkLite" style="font-size: 1.1em">literature</a> <span class="greyText smallText">(164,380)</span><br/><a href="/shelf/show/novel" class="actionLinkLite" style="font-size: 1.1em">novel</a> <span class="greyText smallText">(147,974)</span><br/><a href="/shelf/show/philosophy" class="actionLinkLite" style="font-size: 1.1em">philosophy</a> <span class="greyText smallText">(136,909)</span><br/><a href="/shelf/show/audiobook" class="actionLinkLite" style="font-size: 1.1em">audiobook</a> <span class="greyText smallText">(130,823)</span><br/><a href="/shelf/show/book-club" class="actionLinkLite" style="font-size: 1.1em">book-club</a> <span class="greyText smallText">(125,319)</span><br/><a href="/shelf/show/adult-fiction" class="actionLinkLite" style="font-size: 1.1em">adult-fiction</a> <span class="greyText smallText">(123,457)</span><br/><a href="/shelf/show/classic" class="actionLinkLite" style="font-size: 1.1em">classic</a> <span class="greyText smallText">(118,967)</span><br/><a href="/shelf/show/audio" class="actionLinkLite" style="font-size: 1.1em">audio</a> <span class="greyText smallText">(113,969)</span><br/><a href="/shelf/show/abandoned" class="actionLinkLite" style="font-size: 1.1em">abandoned</a> <span class="greyText smallText">(107,930)</span><br/><a href="/shelf/show/general-fiction" class="actionLinkLite" style="font-size: 1.1em">general-fiction</a> <span class="greyText smallText">(101,644)</span><br/><a href="/shelf/show/unfinished" class="actionLinkLite" style="font-size: 1.1em">unfinished</a> <span class="greyText smallText">(93,384)</span><br/><a href="/shelf/show/politics" class="actionLinkLite" style="font-size: 1.1em">politics</a> <span class="greyText smallText">(89,549)</span><br/><a href="/shelf/show/american" class="actionLinkLite" style="font-size: 1.1em">american</a> <span class="greyText smallText">(88,748)</span><br/><a href="/shelf/show/all-time-favorites" class="actionLinkLite" style="font-size: 1.1em">all-time-favorites</a> <span class="greyText smallText">(84,012)</span><br/><a href="/shelf/show/dystopian" class="actionLinkLite" style="font-size: 1.1em">dystopian</a> <span class="greyText smallText">(77,522)</span><br/><a href="/shelf/show/dystopia" class="actionLinkLite" style="font-size: 1.1em">dystopia</a> <span class="greyText smallText">(71,292)</span><br/><a href="/shelf/show/literary-fiction" class="actionLinkLite" style="font-size: 1.1em">literary-fiction</a> <span class="greyText smallText">(63,001)</span><br/><a href="/shelf/show/literary" class="actionLinkLite" style="font-size: 1.1em">literary</a> <span class="greyText smallText">(57,512)</span><br/><a href="/shelf/show/never-finished" class="actionLinkLite" style="font-size: 1.1em">never-finished</a> <span class="greyText smallText">(52,305)</span><br/><a href="/shelf/show/political" class="actionLinkLite" style="font-size: 1.1em">political</a> <span class="greyText smallText">(40,048)</span><br/><a href="/shelf/show/classic-literature" class="actionLinkLite" style="font-size: 1.1em">classic-literature</a> <span class="greyText smallText">(30,880)</span><br/><a href="/shelf/show/economics" class="actionLinkLite" style="font-size: 1.1em">economics</a> <span class="greyText smallText">(30,854)</span><br/><a href="/shelf/show/capitalism" class="actionLinkLite" style="font-size: 1.1em">capitalism</a> <span class="greyText smallText">(3,146)</span><br/><a href="/shelf/show/objectivism" class="actionLinkLite" style="font-size: 1.1em">objectivism</a> <span class="greyText smallText">(310)</span><br/><a href="/shelf/show/ayn-rand" class="actionLinkLite" style="font-size: 1.1em">ayn-rand</a> <span class="greyText smallText">(299)</span><br/><a href="/shelf/top_shelves" class="actionLink" style="float: right">More shelves...</a>\n<div class="clear"/></div></div><div class="bigBoxBottom"/></div>\n\n\n\n\n\n\n\n\n</div>\n\n  <script src="http://www.google.com/adsense/search/ads.js" type="text/javascript"/><script type="text/javascript" charset="utf-8">\n  var pageOptions = {\n    \'pubId\' : \'pub-7284881071421289\',\n    \'query\' : \'atlas shrugged ayn rand buy books\',\n    \'channel\' : \'4204718441\',\n    \'hl\' : \'en\'\n  };\n\n  var adblock1 = {\n    \'container\' : \'adcontainer1\',\n    \'colorTitleLink\' : \'#666600\',\n    \'colorDomainLink\' : \'#215625\'\n  };\n\n  var adblock2 = {\n    \'container\' : \'adcontainer2\',\n    \'colorTitleLink\' : \'#666600\',\n    \'colorDomainLink\' : \'#215625\'\n  };\n\n  new google.ads.search.Ads(pageOptions, adblock1, adblock2);\n  </script></div>\n      <div class="clear"/>\n    </div>\n    <div class="clear"/>\n  </div>\n\n  <div class="clear"/>\n  <div class="footerContainer">\n    <div class="footer">\n      <div class="copyright">\n        \xa9 2012 Goodreads Inc\n      </div>\n      <div class="adminLinksContainer">\n        <ul class="adminLinks"><li>\n            <a href="/about/us" class="first" rel="nofollow">about us</a>\n          </li>\n          <li>\n            <a href="/advertisers" rel="nofollow">advertise</a>\n          </li>\n          <li>\n            <a href="/author/program" rel="nofollow">author program</a>\n          </li>\n          <li>\n            <a href="/jobs" rel="nofollow">jobs</a>\n          </li>\n          <li>\n            <a href="/api" rel="nofollow">api</a>\n          </li>\n          <li>\n            <a href="/blog">our blog</a>\n          </li>\n          <li>\n            <a href="/about/terms" rel="nofollow">terms</a>\n          </li>\n          <li>\n            <a href="/about/privacy" rel="nofollow">privacy</a>\n          </li>\n          <li>\n            <a href="/help" class="last" rel="nofollow">help</a>\n          </li>\n        </ul><br/><br/></div>\n    </div>\n  </div>\n</div><div id="overlay" style="display:none" onclick="Lightbox.hideBox(\'dropout\')"/><div id="box" style="display:none">\n\t<img id="close" src="/assets/close.gif" onclick="Lightbox.hideBox(\'dropout\')" alt="Close" title="Close this window"/><div id="boxContents"/>\n\t<div id="boxContentsLeftovers" style="display:none"/>\n\t<a class="right actionLinkLite smallText greyText" href="#" id="lightBoxRightClose" onclick="Lightbox.hideBox(\'dropout\'); return false;" style="padding:10px">close</a>\n\t<div class="clear"/>\n</div><div id="fbSigninNotification" style="display:none;">\n    <p>Welcome back. Just a moment while we sign you in to your Goodreads account.</p>\n    <img alt="Login_animation" src="http://s.gr-assets.com/assets/facebook/login_animation-1e8a0fcfab132f98bfe58ff081c643c5.gif"/></div><script type="text/javascript" src="http://bookads2.goodreads.com/ad?gtargeting=bstqdj64n5&amp;n=3&amp;p=search&amp;sid=270079165977cf67d29feef7b0b8d36d&amp;uid=false">\n    </script><div id="fb-root"/><script type="text/javascript">\n  function loadFacebookScripts() {\n    \n  }\n\n  window._fb_app_id = \'2415071772\';\n\n  window._gr_session = \'false\'\n  window._no_gr_account = \'false\'\n  window._suppress_auto_login = ""\n\n  window.fbAsyncInit = function() {\n    GR_Facebook.initialize();\n    loadFacebookScripts();\n  };\n\n  (function(d){\n     var js, id = \'facebook-jssdk\', ref = d.getElementsByTagName(\'script\')[0];\n     if (d.getElementById(id)) {return;}\n     js = d.createElement(\'script\'); js.id = id; js.async = true;\n     js.src = "//connect.facebook.net/en_US/all.js";\n     ref.parentNode.insertBefore(js, ref);\n   }(document));\n</script><script type="text/javascript">\n//&lt;![CDATA[\n\n    var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");\n    document.write(unescape("%3Cscript src=\'" + gaJsHost + "google-analytics.com/ga.js\' type=\'text/javascript\'%3E%3C/script%3E"));\n\n//]]&gt;\n</script><script type="text/javascript">\n//&lt;![CDATA[\n\n    try {\n      var pageTracker = _gat._createTracker("UA-968618-1");\n      pageTracker._setCustomVar(1, "User Status", "signed_out", 2);\n      pageTracker._trackPageview();\n    }\n    catch(err) {}\n\n//]]&gt;\n</script><script type="text/javascript">\n//&lt;![CDATA[\n\n    _qoptions={\n    qacct:"p-0dUe_kJAjvkoY"\n    };\n\n//]]&gt;\n</script><script type="text/javascript" src="http://edge.quantserve.com/quant.js"/><noscript>\n  <img src="http://pixel.quantserve.com/pixel/p-0dUe_kJAjvkoY.gif" style="display: none;" border="0" height="1" width="1" alt="Quantcast"/></noscript><script type="text/javascript">\n//&lt;![CDATA[\n\n    document.write(unescape("%3Cscript src=\'" + (document.location.protocol == "https:" ? "https://sb" : "http://b") + ".scorecardresearch.com/beacon.js\' %3E%3C/script%3E"));\n\n//]]&gt;\n</script><script type="text/javascript">\n//&lt;![CDATA[\n\n    COMSCORE.beacon({\n      c1:2,\n      c2:6035830,\n      c3:"",\n      c4:"",\n      c5:"",\n      c6:"",\n      c15:""\n    });\n\n//]]&gt;\n</script><noscript>\n    <img src="http://b.scorecardresearch.com/b?c1=2&amp;c2=6035830&amp;c3=&amp;c4=&amp;c5=&amp;c6=&amp;c15=&amp;cv=1.3&amp;cj=1" style="display:none" width="0" height="0" alt=""/></noscript></body>'
>>> dir(d)
['Fn', '__add__', '__call__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__dict__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__html__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', '__unicode__', '__weakref__', '_append', '_base_url', '_css_to_xpath', '_extend', '_filter_only', '_get_root', '_nextAll', '_parent', '_prevAll', '_translator', '_traverse', '_traverse_parent_topdown', 'addClass', 'after', 'append', 'appendTo', 'attr', 'base_url', 'before', 'children', 'clone', 'closest', 'count', 'css', 'each', 'empty', 'encoding', 'end', 'eq', 'extend', 'filter', 'find', 'fn', 'hasClass', 'height', 'hide', 'html', 'index', 'insert', 'insertAfter', 'insertBefore', 'is_', 'length', 'make_links_absolute', 'map', 'next', 'nextAll', 'not_', 'outerHtml', 'parent', 'parents', 'parser', 'pop', 'prepend', 'prependTo', 'prev', 'prevAll', 'remove', 'removeAttr', 'removeClass', 'replaceAll', 'replaceWith', 'reverse', 'root', 'show', 'siblings', 'size', 'sort', 'text', 'toggleClass', 'val', 'width', 'wrap', 'wrapAll']
>>> d('div')
[<div.content>, <div#siteheader.uitext>, <div.mainContent>, <div#logo>, <div#sitesearch>, <div>, <div.auto_complete_field_wrapper>, <div#sitesearch_autocomplete>, <div.subnav>, <div.mainContentContainer.>, <div.mainContent>, <div.mainContentFloat>, <div#flashContainer>, <div.leftContainer>, <div>, <div.greyText>, <div.clear>, <div>, <div.tabs.mediumTabs>, <div.clear>, <div#adcontainer1>, <div#1_book_662.wtrButtonContainer.wtrSignedOut>, <div.wtrUp.wtrLeft>, <div>, <div.wtrDivider>, <div.wtrRight>, <div.wtrShelfMenu>, <div>, <div>, <div>, <div.ratingStars.wtrRating>, <div>, <div.clearRating.uitext>, <div#2_book_2115.wtrButtonContainer.wtrSignedOut>, <div.wtrUp.wtrLeft>, <div>, <div.wtrDivider>, <div.wtrRight>, <div.wtrShelfMenu>, <div>, <div>, <div>, <div.ratingStars.wtrRating>, <div>, <div.clearRating.uitext>, <div#3_book_6234337.wtrButtonContainer.wtrSignedOut>, <div.wtrUp.wtrLeft>, <div>, <div.wtrDivider>, <div.wtrRight>, <div.wtrShelfMenu>, <div>, <div>, <div>, <div.ratingStars.wtrRating>, <div>, <div.clearRating.uitext>, <div#4_book_13607666.wtrButtonContainer.wtrSignedOut>, <div.wtrUp.wtrLeft>, <div>, <div.wtrDivider>, <div.wtrRight>, <div.wtrShelfMenu>, <div>, <div>, <div>, <div.ratingStars.wtrRating>, <div>, <div.clearRating.uitext>, <div#5_book_201237.wtrButtonContainer.wtrSignedOut>, <div.wtrUp.wtrLeft>, <div>, <div.wtrDivider>, <div.wtrRight>, <div.wtrShelfMenu>, <div>, <div>, <div>, <div.ratingStars.wtrRating>, <div>, <div.clearRating.uitext>, <div#6_book_5755462.wtrButtonContainer.wtrSignedOut>, <div.wtrUp.wtrLeft>, <div>, <div.wtrDivider>, <div.wtrRight>, <div.wtrShelfMenu>, <div>, <div>, <div>, <div.ratingStars.wtrRating>, <div>, <div.clearRating.uitext>, <div#7_book_831567.wtrButtonContainer.wtrSignedOut>, <div.wtrUp.wtrLeft>, <div>, <div.wtrDivider>, <div.wtrRight>, <div.wtrShelfMenu>, <div>, <div>, <div>, <div.ratingStars.wtrRating>, <div>, <div.clearRating.uitext>, <div#8_book_9364.wtrButtonContainer.wtrSignedOut>, <div.wtrUp.wtrLeft>, <div>, <div.wtrDivider>, <div.wtrRight>, <div.wtrShelfMenu>, <div>, <div>, <div>, <div.ratingStars.wtrRating>, <div>, <div.clearRating.uitext>, <div#9_book_5430955.wtrButtonContainer.wtrSignedOut>, <div.wtrUp.wtrLeft>, <div>, <div.wtrDivider>, <div.wtrRight>, <div.wtrShelfMenu>, <div>, <div>, <div>, <div.ratingStars.wtrRating>, <div>, <div.clearRating.uitext>, <div#10_book_5141345.wtrButtonContainer.wtrSignedOut>, <div.wtrUp.wtrLeft>, <div>, <div.wtrDivider>, <div.wtrRight>, <div.wtrShelfMenu>, <div>, <div>, <div>, <div.ratingStars.wtrRating>, <div>, <div.clearRating.uitext>, <div#11_book_9017523.wtrButtonContainer.wtrSignedOut>, <div.wtrUp.wtrLeft>, <div>, <div.wtrDivider>, <div.wtrRight>, <div.wtrShelfMenu>, <div>, <div>, <div>, <div.ratingStars.wtrRating>, <div>, <div.clearRating.uitext>, <div#12_book_181147.wtrButtonContainer.wtrSignedOut>, <div.wtrUp.wtrLeft>, <div>, <div.wtrDivider>, <div.wtrRight>, <div.wtrShelfMenu>, <div>, <div>, <div>, <div.ratingStars.wtrRating>, <div>, <div.clearRating.uitext>, <div#13_book_16135783.wtrButtonContainer.wtrSignedOut>, <div.wtrUp.wtrLeft>, <div>, <div.wtrDivider>, <div.wtrRight>, <div.wtrShelfMenu>, <div>, <div>, <div>, <div.ratingStars.wtrRating>, <div>, <div.clearRating.uitext>, <div#14_book_9577604.wtrButtonContainer.wtrSignedOut>, <div.wtrUp.wtrLeft>, <div>, <div.wtrDivider>, <div.wtrRight>, <div.wtrShelfMenu>, <div>, <div>, <div>, <div.ratingStars.wtrRating>, <div>, <div.clearRating.uitext>, <div#15_book_9935187.wtrButtonContainer.wtrSignedOut>, <div.wtrUp.wtrLeft>, <div>, <div.wtrDivider>, <div.wtrRight>, <div.wtrShelfMenu>, <div>, <div>, <div>, <div.ratingStars.wtrRating>, <div>, <div.clearRating.uitext>, <div#16_book_12716520.wtrButtonContainer.wtrSignedOut>, <div.wtrUp.wtrLeft>, <div>, <div.wtrDivider>, <div.wtrRight>, <div.wtrShelfMenu>, <div>, <div>, <div>, <div.ratingStars.wtrRating>, <div>, <div.clearRating.uitext>, <div>, <div#adcontainer2>, <div.rightContainer>, <div#self_serve_ads>, <div..clearFloats.bigBox>, <div.h2Container.gradientHeaderContainer>, <div.bigBoxBody>, <div.bigBoxContent.containerWithHeaderContent>, <div.clear>, <div.bigBoxBottom>, <div.clear>, <div.clear>, <div.clear>, <div.footerContainer>, <div.footer>, <div.copyright>, <div.adminLinksContainer>, <div#overlay>, <div#box>, <div#boxContents>, <div#boxContentsLeftovers>, <div.clear>, <div#fbSigninNotification>, <div#fb-root>]
>>> d('.minirating')
[<span.minirating>, <span.minirating>, <span.minirating>, <span.minirating>, <span.minirating>, <span.minirating>, <span.minirating>, <span.minirating>, <span.minirating>, <span.minirating>, <span.minirating>, <span.minirating>, <span.minirating>, <span.minirating>, <span.minirating>, <span.minirating>]
>>> d('.minirating').eq(0)
[<span.minirating>]
>>> d('.minirating').eq(1)
[<span.minirating>]
>>> d('.minirating').eq(0).html()
>>> d('.minirating').eq(0)
[<span.minirating>]
>>> d('.minirating')[0]
<Element span at 0x10e7e3950>
>>> d('.minirating')[0].html()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'HtmlElement' object has no attribute 'html'
>>> d('.minirating').eq(0)
[<span.minirating>]
>>> type(d('.minirating').eq(0))
<class 'pyquery.pyquery.PyQuery'>
>>> dir(d('.minirating').eq(0))
['Fn', '__add__', '__call__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__dict__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__html__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', '__unicode__', '__weakref__', '_append', '_base_url', '_css_to_xpath', '_extend', '_filter_only', '_get_root', '_nextAll', '_parent', '_prevAll', '_translator', '_traverse', '_traverse_parent_topdown', 'addClass', 'after', 'append', 'appendTo', 'attr', 'base_url', 'before', 'children', 'clone', 'closest', 'count', 'css', 'each', 'empty', 'encoding', 'end', 'eq', 'extend', 'filter', 'find', 'fn', 'hasClass', 'height', 'hide', 'html', 'index', 'insert', 'insertAfter', 'insertBefore', 'is_', 'length', 'make_links_absolute', 'map', 'next', 'nextAll', 'not_', 'outerHtml', 'parent', 'parents', 'parser', 'pop', 'prepend', 'prependTo', 'prev', 'prevAll', 'remove', 'removeAttr', 'removeClass', 'replaceAll', 'replaceWith', 'reverse', 'root', 'show', 'siblings', 'size', 'sort', 'text', 'toggleClass', 'val', 'width', 'wrap', 'wrapAll']
>>> d('.minirating').eq(0).text
<bound method PyQuery.text of [<span.minirating>]>
>>> d('.minirating').eq(0).text()
''
>>> d('.minirating').eq(0).attr
<flexible_element attr>
>>> d('.minirating').eq(0).attr()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/michelleglauser/Desktop/BookFairy/venv/lib/python2.7/site-packages/pyquery/pyquery.py", line 97, in __call__
    return self.pget(instance, *args, **kwargs)
  File "/Users/michelleglauser/Desktop/BookFairy/venv/lib/python2.7/site-packages/pyquery/pyquery.py", line 654, in attr
    raise ValueError('Invalid arguments %s %s' % (args, kwargs))
ValueError: Invalid arguments () {}
>>> d('.minirating').eq(0).children
<bound method PyQuery.children of [<span.minirating>]>
>>> d('.minirating').eq(0).children()
[]
>>> d('.minirating').eq(0).text()
''
>>> d('.minirating').eq(0).html()
>>> d('.minirating').eq(1)
[<span.minirating>]
>>> d('.minirating').eq(2)
[<span.minirating>]
>>> d('.minirating')
[<span.minirating>, <span.minirating>, <span.minirating>, <span.minirating>, <span.minirating>, <span.minirating>, <span.minirating>, <span.minirating>, <span.minirating>, <span.minirating>, <span.minirating>, <span.minirating>, <span.minirating>, <span.minirating>, <span.minirating>, <span.minirating>]
>>> type(d('.minirating'))
<class 'pyquery.pyquery.PyQuery'>
>>> d('.minirating').contents()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'PyQuery' object has no attribute 'contents'
>>> d('.minirating').eq(0)
[<span.minirating>]
>>> d('.minirating').eq(0).contents()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'PyQuery' object has no attribute 'contents'
>>> d('.minirating').eq(0)
[<span.minirating>]
>>> d('.minirating').contents()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'PyQuery' object has no attribute 'contents'
>>> d('.minirating').text()
u'4.02 avg rating \u2014 2,283 ratings 3.89 avg rating \u2014 18 ratings 5.00 avg rating \u2014 1 rating 3.86 avg rating \u2014 7 ratings 4.00 avg rating \u2014 84 ratings 3.50 avg rating \u2014 2 ratings 4.12 avg rating \u2014 41 ratings 3.93 avg rating \u2014 28 ratings 3.78 avg rating \u2014 23 ratings 4.50 avg rating \u2014 16 ratings 4.25 avg rating \u2014 8 ratings 0.00 avg rating \u2014 0 ratings 4.08 avg rating \u2014 12 ratings 5.00 avg rating \u2014 1 rating 3.00 avg rating \u2014 1 rating'
>>> url = "http://sflib1.sfpl.org/search/X?SEARCH=A+Tree+Grows+in+Brooklyn&x=0&y=0&searchscope=1&p=&l=eng&m=a&Da=&Db=&SORT=D"
>>> response = requests.get(url)                                                                                   >>> print response
<Response [200]>
>>> data = pq(response.content)
>>> print data
<html dir="LTR"><head><title>San Francisco Public Library                                     /All Locations</title><base target="_self"/><link rel="stylesheet" type="text/css" href="/scripts/ProStyles.css"/><link rel="stylesheet" type="text/css" href="/screens/styles.css"/><link rel="shortcut icon" type="ximage/icon" href="/screens/favicon.ico"/><script type="text/javascript" src="/scripts/common.js"/><script type="text/javascript" src="/scripts/features.js"/><script type="text/javascript" src="/scripts/webbridge.js"/><script type="text/javascript" src="/scripts/elcontent.js"/><script type="text/JavaScript">
&lt;!-- Hide the JS
startTimeout(6000000, "/");
// --&gt;
</script></head><body><noscript>
<meta http-equiv="Refresh" content="6000;URL=/"/></noscript>

<script type="text/javascript" src="/screens/sfplScripts.js"/><table align="center" cellpadding="0" cellspacing="0" border="0" summary="This table structures page content."><tr><td colspan="2"> 
<!-- header image, language links, and top navigation -->
<table class="navigationtable" cellpadding="0" cellspacing="0" border="0" summary="Table containing primary navigation and language options"><tr class="headerrow"><td colspan="4">
<a href="http://sfpl.org/" title="San Francisco Public Library home page">

<img src="/screens/background_header.jpg" border="0" vspace="0" hspace="0" alt="Go to the San Francisco Public Library home page" width="950" height="79"/></a>
<span class="fineprint" style="position: relative; top:-20px; left:250px;">
<a href="http://sflib1.sfpl.org/search*spi">Espa&#241;ol</a>
&#160;|&#160;
<a href="http://sflib1.sfpl.org/search*cht">&#20013;&#25991;</a>
</span>

</td>
</tr></table><div align="center" class="navigationRow">
<form>
<a href="/search"><img src="/screens/startover.gif" alt="Start Over" border="0"/></a>
<a href="/search~S1/X?NOSRCH=A+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D&amp;SUBKEY=A+Tree+Grows+in+Brooklyn"><img src="/screens/modify.gif" alt="Modify Search" border="0"/></a>
<a href="http://csul.iii.com/search/X?A+Tree+Grows+in+Brooklyn&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D&amp;backlink=http://sflib1.sfpl.org:80/search~S1?/XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D/XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D&amp;SUBKEY=A+Tree+Grows+in+Brooklyn/1%2C5%2C5%2CB/browse"><img src="/screens/csul.gif " alt="Search Link+ Catalog" border="0"/></a>
<select name="HISTORY" onchange="onSelectChange(this, '~S1')"><option value="">(Search History)</option><option value="XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D">Keyword: A Tree Grows in Brooklyn in View Entire Collection
</option><option value="+/search~S1/X?A+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D&amp;clear_history">(Clear Search History)</option><option value="+/">(End Search Session)</option></select><noscript>
<h2>Search history function requires JavaScript.</h2>
</noscript>
</form>
</div>

<span><center>
<a href="" onclick="return createResourceWindow('/webbridge~S1/panel?returnurl=%2Fsearch~S1%3F%2FXA%2BTree%2BGrows%2Bin%2BBrooklyn%26searchscope%3D1%26p%3D%26l%3Deng%26m%3Da%26Da%3D%26Db%3D%26SORT%3DD%2FXA%2BTree%2BGrows%2Bin%2BBrooklyn%26searchscope%3D1%26p%3D%26l%3Deng%26m%3Da%26Da%3D%26Db%3D%26SORT%3DD%26SUBKEY%3DA%2BTree%2BG');">
<img src="/screens/resourcelink.gif" alt="Other Resources" border="0"/></a>
</center></span>
<!-- BEGIN BROWSE SCREEN TABLE -->
<table align="center" width="100%" cellpadding="2" cellspacing="0" border="0" class="browseScreen"><!-- BEGIN SEARCH WIDGET --><div align="center">
<tr align="center" valign="middle"><td valign="middle" colspan="2">
<div class="browseSearchtool">
<script type="text/JavaScript">
&lt;!-- Hide the JS
var savedScope;
var savedTag;
var savedSearch;
var sortButtonText = null;
var savedExactSearch = null;
var sortButtonEvent = null;
var sortExactBrowseURL = null;
var sortTypes = new Array();
var sortLabels = new Array();
sortTypes[0] = "t";
sortLabels[0] = "Title";
sortTypes[1] = "a";
sortLabels[1] = "Author";
sortTypes[2] = "c";
sortLabels[2] = "Year";
sortTypes[3] = "r";
sortLabels[3] = "Reverse Year";
sortTypes[4] = "n";
sortLabels[4] = "Call Number";
sortTypes[5] = "m";
sortLabels[5] = "Material Type";
sortLabels[6] = "System Sorted";
sortTypes[6] = "-";
var sortSelectedValue = "6";
var nonSortTags = "XYZprWw"
// Unhide the JS --&gt;
</script><form name="searchtool" target="_self" action="/search~S1/" method="POST">
      <label for="searchtype" style="display:none;">SearchType</label> <select name="searchtype" id="searchtype" onchange="initSort()"><option value="a"> Author</option><option value="t"> Title</option><option value="d"> Subject</option><option value="c"> Call No</option><option value="X" selected="selected"> Keyword</option></select>
      &#160;
      <label for="searcharg" style="display:none;">Search</label><input type="text" name="searcharg" id="searcharg" size="30" onchange="return searchtoolSubmitAction()" maxlength="75" value="A Tree Grows in Brooklyn"/>
      &#160;
      <label for="searchscope" style="display:none;">Search Scope</label><select name="searchscope" id="searchscope"><option value="1" selected="selected"> View Entire Collection</option><option value="33"> Adult/Teen Materials</option><option value="4"> Anza</option><option value="5"> Bayview</option><option value="6"> Bernal Heights</option><option value="32"> Branch Bookmobile 1</option><option value="7"> Children's Bookmobile</option><option value="2"> Children's Materials Only</option><option value="8"> Chinatown</option><option value="9"> Eureka Valley</option><option value="10"> Excelsior</option><option value="11"> Glen Park</option><option value="12"> Golden Gate Valley</option><option value="13"> Ingleside</option><option value="14"> Library on Wheels</option><option value="3"> Main Library</option><option value="15"> Marina</option><option value="16"> Merced</option><option value="17"> Mission</option><option value="18"> Mission Bay</option><option value="19"> Noe Valley</option><option value="20"> North Beach</option><option value="21"> Oceanview</option><option value="22"> Ortega</option><option value="23"> Park</option><option value="24"> Parkside</option><option value="25"> Portola</option><option value="26"> Potrero</option><option value="27"> Presidio</option><option value="28"> Richmond</option><option value="29"> Sunset</option><option value="30"> Visitacion Valley</option><option value="31"> West Portal</option><option value="34"> Western Addition</option></select>
      &#160;

<span id="sort_cell">
</span>

<script type="text/JavaScript">
&lt;!-- Hide the JS
initSort();
// Unhide the JS --&gt;
</script><input type="hidden" name="SORT" value="DZ"/><input type="hidden" name="extended" value="0"/><input type="submit" name="SUBMIT" value="Search" onclick="return searchtoolSubmitAction();"/><div>
      <input type="checkbox" name="availlim" value="1"/><em>Limit to available</em><br/></div>
<div>
      <input type="hidden" name="searchlimits" value="l=eng&amp;m=a"/><input type="hidden" name="searchorigarg" value="XA Tree Grows in Brooklyn&amp;SORT=D"/></div>
</form>
<div>
</div>
<div class="browseSearchtoolMessage">      <i>Limited to:</i> Language "English" <i> and</i> Material Type "BOOK" <i> and</i>  <i>5 results found. </i>Sorted by  <strong>relevance</strong>  | <a href="/search~S1/X?A+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=DX">date</a>  | <a href="/search~S1/X?A+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=AX">title</a> .
</div>
<div/></div>

</td>
</tr></div>
<!-- END SEARCH WIDGET -->

<!-- BEGIN BROWSE PAGER -->
<!-- END BROWSE PAGER -->

<style type="text/css">
&lt;!--
#rategroup-6 { display: inline }
#rateneed-6  { display: none }
#rategroupMy-6 { display: none }
#ratemy-6      { display: inline }
#rategroup-5 { display: inline }
#rateneed-5  { display: none }
#rategroupMy-5 { display: none }
#ratemy-5      { display: inline }
#rategroup-4 { display: inline }
#rateneed-4  { display: none }
#rategroupMy-4 { display: none }
#ratemy-4      { display: inline }
#rategroup-3 { display: inline }
#rateneed-3  { display: none }
#rategroupMy-3 { display: none }
#ratemy-3      { display: inline }
#rategroup-2 { display: inline }
#rateneed-2  { display: none }
#rategroupMy-2 { display: none }
#ratemy-2      { display: inline }
#rategroup-1 { display: inline }
#rateneed-1  { display: none }
#rategroupMy-1 { display: none }
#ratemy-1      { display: inline }
#rategroup0 { display: inline }
#rateneed0  { display: none }
#rategroupMy0 { display: none }
#ratemy0      { display: inline }
#rategroup1 { display: inline }
#rateneed1  { display: none }
#rategroupMy1 { display: none }
#ratemy1      { display: inline }
#rategroup2 { display: inline }
#rateneed2  { display: none }
#rategroupMy2 { display: none }
#ratemy2      { display: inline }
#rategroup3 { display: inline }
#rateneed3  { display: none }
#rategroupMy3 { display: none }
#ratemy3      { display: inline }
#rategroup4 { display: inline }
#rateneed4  { display: none }
#rategroupMy4 { display: none }
#ratemy4      { display: inline }
#rategroup5 { display: inline }
#rateneed5  { display: none }
#rategroupMy5 { display: none }
#ratemy5      { display: inline }
--&gt;
</style><!-- BEGIN BROWSE SCREEN LEFT CELL: BROWSELIST/BRIEFCIT AREA --><tr><td>
<table id="briefcit_table" align="center" border="0" bordercolor="339999" width="100%"><tr align="CENTER" valign="MIDDLE"><td colspan="5" class="browseSaveJump">
<form method="POST" action="/search~S1?/XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D/XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D&amp;SUBKEY=A+Tree+Grows+in+Brooklyn/1%2C5%2C5%2CB/browse" name="export_form" id="export_form">
<input type="hidden" name="jumpref" value="XA+Tree+Grows+in+Brooklyn"/><input type="hidden" id="save_func" name="save_func" value=""/><a href="#" onclick="process_save(0);" style="text-decoration:none">
<img src="/screens/savemarked.gif" alt="Save marked records" border="0"/></a>
<span name="save_page_btn1" id="save_page_btn1" style="visibility: visible"><a href="#" onclick="process_save(1);" style="text-decoration:none">
<img src="/screens/saveallpage.gif" alt="Save all on page" border="0"/></a>
</span>
<span name="mylist_btn1" id="mylist_btn1" style="visibility: visible"><a href="#" onclick="save_to_mylist();">
<img src="/screens/save-to-list.gif" alt="Save to List" border="0"/></a>
</span>
</form></td></tr><tr class="browseHeader"><td align="center" class="browseHeaderData">
Keyword (1-5 of 5)
</td>
</tr><!-- Right Result rank 1 --><tr class="browseSuperEntry browseEntryRelGroup1"><td colspan="1"><img src="/screens/relevance5.gif" alt=""/>&#160;Most relevant titles&#160;entries 1-1</td></tr><tr class="briefCitRow"><td>
 <table align="center" cellpadding="5" width="950"><tr><td align="center" width="5%">
        <strong>
<a name="anchor_1"/> 1      </strong>

<br/><br/><img src="/screens/icon_bookbag.gif" border="0" alt="Select item / &#233;&#129;&#184;&#230;&#147;&#135;&#230;&#173;&#164;&#233;&#160;&#133; " width="23" height="34"/><input type="checkbox" name="save" value="b1243502"/></td>
      <td align="center" valign="top" width="15%">
<a href="http://www.syndetics.com/index.aspx?isbn=9780061120077/index.html&amp;client=sfpl&amp;upc=&amp;oclc=abl-ocm00000424&amp;type=rn12" target="_parent"><img src="http://www.syndetics.com/index.aspx?isbn=9780061120077/SC.GIF&amp;client=sfpl&amp;upc=&amp;oclc=abl-ocm00000424" border="0" alt="book jacket"/></a>      </td>
      <td align="left" valign="top" width="65%">
        <table><tr><td>
<!--{nohitmsg}-->


<a href="/search~S1?/XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D/XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D&amp;SUBKEY=A+Tree+Grows+in+Brooklyn/1%2C5%2C5%2CB/frameset&amp;FF=XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D&amp;1%2C1%2C">A tree grows in Brooklyn : a novel / by Betty Smith.</a>           </td>
            </tr><tr><td>
Smith, Betty, 1896-1972.                </td>
            </tr><tr><td>
New York : Harper &amp; Brothers, [1943]                </td>
            </tr><tr><td>
3 p. l., 3-443, [1] p. ; 21 cm.             </td>
            </tr><tr><td>
F Smith Be              </td>
            </tr><tr/><tr><td>
&#160;</td>
</tr><td>

<span id="rategroup1"><a href="/patroninfo~S1/0/redirect=/search~S1?/XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D/XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D&amp;SUBKEY=A+Tree+Grows+in+Brooklyn/1%2C5%2C5%2CB/browse#anchor_1"><img src="/screens/rate_group.gif" border="0" title="Rated 4 stars out of 5 based on 3 ratings"/><img src="/screens/rate_group.gif" border="0" title="Rated 4 stars out of 5 based on 3 ratings"/><img src="/screens/rate_group.gif" border="0" title="Rated 4 stars out of 5 based on 3 ratings"/><img src="/screens/rate_group.gif" border="0" title="Rated 4 stars out of 5 based on 3 ratings"/><img src="/screens/rate_pad.gif" border="0" title="Rated 4 stars out of 5 based on 3 ratings"/></a>

</span><span class="ratingslink_briefcit"><a href="/screens/ratings.html" title="Explanation of ratings">Ratings?</a></span>
</td>

</table></td>
<td align="center" valign="middle" width="15%">
1943<br/><br/><img src="/screens/media_book.gif" alt="BOOK"/><p class="detail">
<a href="/search~S1?/XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D/XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D&amp;SUBKEY=A+Tree+Grows+in+Brooklyn/1%2C5%2C5%2CB/frameset&amp;FF=XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D&amp;1%2C1%2C"><img src="/screens/isitavailable.gif" alt="Is it available?" border="0"/></a></p>
      </td>
      </tr></table></td>

</tr><!--this is customized <screens/briefcit.html>--><!--this is customized <screens/briefcit.html>--><!-- Right Result rank 3 --><tr class="browseSuperEntry browseEntryRelGroup3"><td colspan="1"><img src="/screens/relevance3.gif" alt=""/>&#160;Very relevant titles&#160;entries 2-4</td></tr><tr class="briefCitRow"><td>
 <table align="center" cellpadding="5" width="950"><tr><td align="center" width="5%">
        <strong>
<a name="anchor_2"/> 2      </strong>

<br/><br/><img src="/screens/icon_bookbag.gif" border="0" alt="Select item / &#233;&#129;&#184;&#230;&#147;&#135;&#230;&#173;&#164;&#233;&#160;&#133; " width="23" height="34"/><input type="checkbox" name="save" value="b2291280"/></td>
      <td align="center" valign="top" width="15%">
<a href="http://www.syndetics.com/index.aspx?isbn=9780307264770/index.html&amp;client=sfpl&amp;upc=&amp;oclc=ocn232980279&amp;type=rn12" target="_parent"><img src="http://www.syndetics.com/index.aspx?isbn=9780307264770/SC.GIF&amp;client=sfpl&amp;upc=&amp;oclc=ocn232980279" border="0" alt="book jacket"/></a>      </td>
      <td align="left" valign="top" width="65%">
        <table><tr><td>
<!--{nohitmsg}-->


<a href="/search~S1?/XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D/XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D&amp;SUBKEY=A+Tree+Grows+in+Brooklyn/1%2C5%2C5%2CB/frameset&amp;FF=XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D&amp;2%2C2%2C">Kazan on directing / Elia Kazan.</a>               </td>
            </tr><tr><td>
Kazan, Elia.                </td>
            </tr><tr><td>
New York : Alfred A. Knopf, 2009.               </td>
            </tr><tr><td>
xxiii, 341 p. : ill. ; 25 cm.               </td>
            </tr><tr><td>
791.4302 K189k              </td>
            </tr><tr/><tr><td>
<a href="http://www.loc.gov/catdir/enhancements/fy0912/2008048345-b.html" onclick="window.open('http://www.loc.gov/catdir/enhancements/fy0912/2008048345-b.html'); return false;">Digital Media</a><br/></td></tr><tr><td>
<a href="/search~S1?/XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D/XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D&amp;SUBKEY=A+Tree+Grows+in+Brooklyn/1%2C5%2C5%2CB/frameset&amp;FF=XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D&amp;2%2C2%2C">More...</a></td></tr><td>

<span id="rategroup2"><a href="/patroninfo~S1/0/redirect=/search~S1?/XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D/XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D&amp;SUBKEY=A+Tree+Grows+in+Brooklyn/1%2C5%2C5%2CB/browse#anchor_2"><img src="/screens/rate_no.gif" border="0" title="No one has rated this material"/></a>

</span><span class="ratingslink_briefcit"><a href="/screens/ratings.html" title="Explanation of ratings">Ratings?</a></span>
</td>

</table></td>
<td align="center" valign="middle" width="15%">
2009<br/><br/><img src="/screens/media_book.gif" alt="BOOK"/><p class="detail">
<a href="/search~S1?/XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D/XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D&amp;SUBKEY=A+Tree+Grows+in+Brooklyn/1%2C5%2C5%2CB/frameset&amp;FF=XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D&amp;2%2C2%2C"><img src="/screens/isitavailable.gif" alt="Is it available?" border="0"/></a></p>
      </td>
      </tr></table></td>

</tr><!--this is customized <screens/briefcit.html>--><!--this is customized <screens/briefcit.html>--><tr class="briefCitRow"><td>
 <table align="center" cellpadding="5" width="950"><tr><td align="center" width="5%">
        <strong>
<a name="anchor_3"/> 3      </strong>

<br/><br/><img src="/screens/icon_bookbag.gif" border="0" alt="Select item / &#233;&#129;&#184;&#230;&#147;&#135;&#230;&#173;&#164;&#233;&#160;&#133; " width="23" height="34"/><input type="checkbox" name="save" value="b2310487"/></td>
      <td align="center" valign="top" width="15%">
<a href="http://www.syndetics.com/index.aspx?isbn=9781557837363/index.html&amp;client=sfpl&amp;upc=&amp;oclc=ocn279258930&amp;type=rn12" target="_parent"><img src="http://www.syndetics.com/index.aspx?isbn=9781557837363/SC.GIF&amp;client=sfpl&amp;upc=&amp;oclc=ocn279258930" border="0" alt="book jacket"/></a>      </td>
      <td align="left" valign="top" width="65%">
        <table><tr><td>
<!--{nohitmsg}-->


<a href="/search~S1?/XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D/XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D&amp;SUBKEY=A+Tree+Grows+in+Brooklyn/1%2C5%2C5%2CB/frameset&amp;FF=XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D&amp;3%2C3%2C">Broadway musicals, show by show / by Stanley Green.</a>            </td>
            </tr><tr><td>
Green, Stanley.             </td>
            </tr><tr><td>
New York : Applause Theatre &amp; Cinema Books, 2008.               </td>
            </tr><tr><td>
xxv, 443 p. : ill. ; 23 cm.             </td>
            </tr><tr><td>
782.7 ZG826b 2008               </td>
            </tr><tr/><tr><td>
&#160;</td>
</tr><td>

<span id="rategroup3"><a href="/patroninfo~S1/0/redirect=/search~S1?/XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D/XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D&amp;SUBKEY=A+Tree+Grows+in+Brooklyn/1%2C5%2C5%2CB/browse#anchor_3"><img src="/screens/rate_no.gif" border="0" title="No one has rated this material"/></a>

</span><span class="ratingslink_briefcit"><a href="/screens/ratings.html" title="Explanation of ratings">Ratings?</a></span>
</td>

</table></td>
<td align="center" valign="middle" width="15%">
2008<br/><br/><img src="/screens/media_book.gif" alt="BOOK"/><p class="detail">
<a href="/search~S1?/XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D/XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D&amp;SUBKEY=A+Tree+Grows+in+Brooklyn/1%2C5%2C5%2CB/frameset&amp;FF=XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D&amp;3%2C3%2C"><img src="/screens/isitavailable.gif" alt="Is it available?" border="0"/></a></p>
      </td>
      </tr></table></td>

</tr><!--this is customized <screens/briefcit.html>--><!--this is customized <screens/briefcit.html>--><tr class="briefCitRow"><td>
 <table align="center" cellpadding="5" width="950"><tr><td align="center" width="5%">
        <strong>
<a name="anchor_4"/> 4      </strong>

<br/><br/><img src="/screens/icon_bookbag.gif" border="0" alt="Select item / &#233;&#129;&#184;&#230;&#147;&#135;&#230;&#173;&#164;&#233;&#160;&#133; " width="23" height="34"/><input type="checkbox" name="save" value="b2024786"/></td>
      <td align="center" valign="top" width="15%">
<a href="http://www.syndetics.com/index.aspx?isbn=1592402100/index.html&amp;client=sfpl&amp;upc=9781592402106&amp;oclc=ocm70707739+&amp;type=rn12" target="_parent"><img src="http://www.syndetics.com/index.aspx?isbn=1592402100/SC.GIF&amp;client=sfpl&amp;upc=9781592402106&amp;oclc=ocm70707739+" border="0" alt="book jacket"/></a>      </td>
      <td align="left" valign="top" width="65%">
        <table><tr><td>
<!--{nohitmsg}-->


<a href="/search~S1?/XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D/XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D&amp;SUBKEY=A+Tree+Grows+in+Brooklyn/1%2C5%2C5%2CB/frameset&amp;FF=XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D&amp;4%2C4%2C">The book that changed my life : 71 remarkable writers celebrate the books that matter most to them /</a>               </td>
            </tr><tr><td>
                </td>
            </tr><tr><td>
New York, N.Y. : Gotham Books, c2006.               </td>
            </tr><tr><td>
xvii, 197 p. ; 20 cm.               </td>
            </tr><tr><td>
028.8 B64434                </td>
            </tr><tr/><tr><td>
<a href="http://www.loc.gov/catdir/toc/ecip0617/2006023179.html" onclick="window.open('http://www.loc.gov/catdir/toc/ecip0617/2006023179.html'); return false;">Digital Media</a><br/></td>
</tr><td>

<span id="rategroup4"><a href="/patroninfo~S1/0/redirect=/search~S1?/XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D/XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D&amp;SUBKEY=A+Tree+Grows+in+Brooklyn/1%2C5%2C5%2CB/browse#anchor_4"><img src="/screens/rate_no.gif" border="0" title="No one has rated this material"/></a>

</span><span class="ratingslink_briefcit"><a href="/screens/ratings.html" title="Explanation of ratings">Ratings?</a></span>
</td>

</table></td>
<td align="center" valign="middle" width="15%">
c2006<br/><br/><img src="/screens/media_book.gif" alt="BOOK"/><p class="detail">
<a href="/search~S1?/XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D/XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D&amp;SUBKEY=A+Tree+Grows+in+Brooklyn/1%2C5%2C5%2CB/frameset&amp;FF=XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D&amp;4%2C4%2C"><img src="/screens/isitavailable.gif" alt="Is it available?" border="0"/></a></p>
      </td>
      </tr></table></td>

</tr><!--this is customized <screens/briefcit.html>--><!--this is customized <screens/briefcit.html>--><!-- Right Result rank 5 --><tr class="browseSuperEntry browseEntryRelGroup5"><td colspan="1"><img src="/screens/relevance1.gif" alt=""/>&#160;Other relevant titles&#160;entries 5-5</td></tr><tr class="briefCitRow"><td>
 <table align="center" cellpadding="5" width="950"><tr><td align="center" width="5%">
        <strong>
<a name="anchor_5"/> 5      </strong>

<br/><br/><img src="/screens/icon_bookbag.gif" border="0" alt="Select item / &#233;&#129;&#184;&#230;&#147;&#135;&#230;&#173;&#164;&#233;&#160;&#133; " width="23" height="34"/><input type="checkbox" name="save" value="b2482307"/></td>
      <td align="center" valign="top" width="15%">
<a href="http://www.syndetics.com/index.aspx?isbn=9781593720469/index.html&amp;client=sfpl&amp;upc=&amp;oclc=ocn705568292&amp;type=rn12" target="_parent"><img src="http://www.syndetics.com/index.aspx?isbn=9781593720469/SC.GIF&amp;client=sfpl&amp;upc=&amp;oclc=ocn705568292" border="0" alt="book jacket"/></a>      </td>
      <td align="left" valign="top" width="65%">
        <table><tr><td>
<!--{nohitmsg}-->


<a href="/search~S1?/XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D/XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D&amp;SUBKEY=A+Tree+Grows+in+Brooklyn/1%2C5%2C5%2CB/frameset&amp;FF=XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D&amp;5%2C5%2C">BAM : the complete works / edited by Steven Serafin.</a>           </td>
            </tr><tr><td>
                </td>
            </tr><tr><td>
New York : Brooklyn Academy of Music in association with The Quantuck Lane Press : Distributed by W.W. Norton &amp; Co., c2011.             </td>
            </tr><tr><td>
382 p. : ill. (some col.) ; 32 cm.              </td>
            </tr><tr><td>
711.558 B2194               </td>
            </tr><tr/><tr><td>
<a href="http://bvbr.bib-bvb.de:8991/F?func=service&amp;doc_library=BVB01&amp;doc_number=024591210&amp;line_number=0001&amp;func_code=DB_RECORDS&amp;service_type=MEDIA" onclick="window.open('http://bvbr.bib-bvb.de:8991/F?func=service&amp;doc_library=BVB01&amp;doc_number=024591210&amp;line_number=0001&amp;func_code=DB_RECORDS&amp;service_type=MEDIA'); return false;">Digital Media</a><br/></td>
</tr><td>

<span id="rategroup5"><a href="/patroninfo~S1/0/redirect=/search~S1?/XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D/XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D&amp;SUBKEY=A+Tree+Grows+in+Brooklyn/1%2C5%2C5%2CB/browse#anchor_5"><img src="/screens/rate_no.gif" border="0" title="No one has rated this material"/></a>

</span><span class="ratingslink_briefcit"><a href="/screens/ratings.html" title="Explanation of ratings">Ratings?</a></span>
</td>

</table></td>
<td align="center" valign="middle" width="15%">
c2011<br/><br/><img src="/screens/media_book.gif" alt="BOOK"/><p class="detail">
<a href="/search~S1?/XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D/XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D&amp;SUBKEY=A+Tree+Grows+in+Brooklyn/1%2C5%2C5%2CB/frameset&amp;FF=XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D&amp;5%2C5%2C"><img src="/screens/isitavailable.gif" alt="Is it available?" border="0"/></a></p>
      </td>
      </tr></table></td>

</tr><!--this is customized <screens/briefcit.html>--><!--this is customized <screens/briefcit.html>--><tr align="CENTER" valign="MIDDLE"><td colspan="5" class="browseSaveJump">
<a href="#" onclick="process_save(0);" style="text-decoration:none">
<img src="/screens/savemarked.gif" alt="Save marked records" border="0"/></a>
<span name="save_page_btn2" id="save_page_btn2" style="visibility: visible"><a href="#" onclick="process_save(1);" style="text-decoration:none">
<img src="/screens/saveallpage.gif" alt="Save all on page" border="0"/></a>
</span>
<span name="mylist_btn2" id="mylist_btn2" style="visibility: visible"><a href="#" onclick="save_to_mylist();">
<img src="/screens/save-to-list.gif" alt="Save to List" border="0"/></a>
</span>

</td></tr></table><!-- END BROWSELIST/BRIEFCIT AREA --></td>
<!-- END BROWSE SCREEN LEFT CELL -->

<!-- BEGIN BROWSE SCREEN RIGHT CELL -->
<td valign="top" width="0%">
<div valign="top" rowspan="2" class="browseResourceTable">

<!-- BEGIN RESOURCE TABLE -->
<table width="100%" class="browseResourceTable" cellpadding="0" cellspacing="0" border="0"/><!-- END RESOURCE TABLE --></div>

</td>
<!-- END BROWSE SCREEN RIGHT CELL -->
</tr><!-- BEGIN BOTTOM BROWSE PAGER --><!-- END BOTTOM BROWSE PAGER --></table><!-- END BROWSE SCREEN TABLE --><div align="center" class="navigationRow">
<form>
<a href="/search"><img src="/screens/startover.gif" alt="Start Over" border="0"/></a>
<a href="/search~S1/X?NOSRCH=A+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D&amp;SUBKEY=A+Tree+Grows+in+Brooklyn"><img src="/screens/modify.gif" alt="Modify Search" border="0"/></a>
<a href="http://csul.iii.com/search/X?A+Tree+Grows+in+Brooklyn&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D&amp;backlink=http://sflib1.sfpl.org:80/search~S1?/XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D/XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D&amp;SUBKEY=A+Tree+Grows+in+Brooklyn/1%2C5%2C5%2CB/browse"><img src="/screens/csul.gif " alt="Search Link+ Catalog" border="0"/></a>
<select name="HISTORY" onchange="onSelectChange(this, '~S1')"><option value="">(Search History)</option><option value="XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D">Keyword: A Tree Grows in Brooklyn in View Entire Collection
</option><option value="+/search~S1/X?A+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D&amp;clear_history">(Clear Search History)</option><option value="+/">(End Search Session)</option></select></form>
</div>


<div id="footer" class="fineprint" align="left">
<img src="/screens/city_seal.gif" alt="City of San Francisco seal" width="44" height="44" style="float:left;margin:7px;"/><br/><a href="http://sfpl.org/index.php?pg=2000034301" target="Resource_Window">Contact</a>&#160;|&#160;
<a href="http://sfpl.org/index.php?pg=2000034401" target="Resource_Window">FAQ</a>&#160;|&#160;
<a href="http://sfpl.org/index.php?pg=2000001701" target="Resource_Window">Ask A Librarian</a>&#160;|&#160;
<a href="http://sfpl.org/index.php?pg=2000028601" target="Resource_Window">Articles &amp; Databases</a>&#160;|&#160;
<a href="http://sfpl.org/index.php?pg=2000004401" target="Resource_Window">Suggest a Title </a>&#160;|&#160;
<a href="http://sfpl.org/index.php?pg=2000031901" target="Resource_Window">Interlibrary Loan </a>
<br/>
Copyright &#169; 2002-2012 San Francisco Public Library. All rights 
reserved.&#160;|&#160;
<a href="http://sfpl.org/index.php?pg=2000001301" target="Resource_Window">Privacy policy</a>&#160;|&#160;Internet &amp; Computer 
<a href="http://sfpl.org/index.php?pg=2000377401">Help/</a><a href="http://sfpl.org/index.php?pg=2000004301">Rules</a>      
</div>



</td></tr></table></body></html>
>>> detail = data("p.detail).children("a")
  File "<stdin>", line 1
    detail = data("p.detail).children("a")
                                       ^
SyntaxError: invalid syntax
>>> detail = data("p.detail).eq(0)
  File "<stdin>", line 1
    detail = data("p.detail).eq(0)
                                 ^
SyntaxError: EOL while scanning string literal
>>> detail = data("p.detail").eq(0)
>>> print detail
<p class="detail">
<a href="/search~S1?/XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D/XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D&amp;SUBKEY=A+Tree+Grows+in+Brooklyn/1%2C5%2C5%2CB/frameset&amp;FF=XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D&amp;1%2C1%2C"><img src="/screens/isitavailable.gif" alt="Is it available?" border="0"/></a></p>
      
>>> area = data(detail.children("a")
... print area
  File "<stdin>", line 2
    print area
        ^
SyntaxError: invalid syntax
>>> area = data(detail).children("a")
>>> print area
<a href="/search~S1?/XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D/XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D&amp;SUBKEY=A+Tree+Grows+in+Brooklyn/1%2C5%2C5%2CB/frameset&amp;FF=XA+Tree+Grows+in+Brooklyn&amp;searchscope=1&amp;p=&amp;l=eng&amp;m=a&amp;Da=&amp;Db=&amp;SORT=D&amp;1%2C1%2C"><img src="/screens/isitavailable.gif" alt="Is it available?" border="0"/></a>
>>> href = data(area).attr("href")
>>> print href
/search~S1?/XA+Tree+Grows+in+Brooklyn&searchscope=1&p=&l=eng&m=a&Da=&Db=&SORT=D/XA+Tree+Grows+in+Brooklyn&searchscope=1&p=&l=eng&m=a&Da=&Db=&SORT=D&SUBKEY=A+Tree+Grows+in+Brooklyn/1%2C5%2C5%2CB/frameset&FF=XA+Tree+Grows+in+Brooklyn&searchscope=1&p=&l=eng&m=a&Da=&Db=&SORT=D&1%2C1%2C
>>> url = http://www.goodreads.com/search?utf8=%E2%9C%93&q=atlas+shrugged+ayn+rand&search_type=books
  File "<stdin>", line 1
    url = http://www.goodreads.com/search?utf8=%E2%9C%93&q=atlas+shrugged+ayn+rand&search_type=books
              ^
SyntaxError: invalid syntax
>>> url = "http://www.goodreads.com/search?utf8=%E2%9C%93&q=atlas+shrugged+ayn+rand&search_type=books"
>>> response = requests.get(url)
>>> print response
<Response [200]>
>>> data = pq(response.content)
>>> print data
<html><head><meta name="google-site-verification" content="PfFjeZ9OK1RrUrKlmAPn_iZJ_vgHaZO1YQ-QlG2VsJs"/><title>Search results for "atlas shrugged ayn rand" (showing 1-16 of 16 books)</title><meta name="description" content="Search results for atlas shrugged ayn rand: Atlas Shrugged, Atlas Shrugged &amp; The Fountainhead, Essays on Ayn Rand's Atlas Shrugged, Quicklet-Ayn Rand's A..."/><meta name="verify-v1" content="cEf8XOH0pulh1aYQeZ1gkXHsQ3dMPSyIGGYqmF53690="/><meta name="apple-itunes-app" content="app-id=355833469"/><link href="http://s.gr-assets.com/assets/goodreads-4db08e118d7ff1c08adc9db069c433f3.css" media="screen" rel="stylesheet" type="text/css"/><script src="http://s.gr-assets.com/assets/application-2f2a647aee98bd5a09abb63a7ed24da2.js" type="text/javascript"/><meta content="authenticity_token" name="csrf-param"/><meta content="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA=" name="csrf-token"/><meta name="robots" content="noindex"/><!--[if lte IE 6]>
    <link href="http://s.gr-assets.com/assets/ie6-4b79910cd43c47d41679e594015f7812.css" media="screen" rel="stylesheet" type="text/css" />

    <script type="text/javascript">
//<![CDATA[

      try {
        document.execCommand("BackgroundImageCache", false, true);
      }
      catch(err) {}

//]]>
</script>  <![endif]--><!--[if lt IE 9]>
    <link href="http://s.gr-assets.com/assets/ie-eceebdfd8a734989e3084ce9e3e5b0d6.css" media="screen" rel="stylesheet" type="text/css" />
  <![endif]--><!--[if lt IE 8]>
    <link href="http://s.gr-assets.com/assets/common_images_ie-dada5b234de40a7e790683ee7a72e00c.css" media="screen" rel="stylesheet" type="text/css" />
  <![endif]--><!--[if gte IE 8]><!--><link href="http://s.gr-assets.com/assets/common_images-f0478bd9a9b956ca6aab1e98bddd8b69.css" media="screen" rel="stylesheet" type="text/css"/><!--<![endif]--><style type="text/css" media="screen">
    #searchButton {
        padding-top: 5px;
    }
</style><link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="Goodreads"/></head><body><div class="content">
  

    <div class="uitext" id="siteheader">
<div class="mainContent">
<ul class="nav" id="usernav"><li>
<strong>
<a href="/user/new" class="navlink" rel="nofollow">register</a>
</strong>
</li>
<li>
<a href="/about/how_it_works" class="navlink" rel="nofollow">tour</a>
</li>
<li>
<a href="/user/sign_in?returnurl=%2Fsearch%3Futf8%3D%25E2%259C%2593%26q%3Datlas%2Bshrugged%2Bayn%2Brand%26search_type%3Dbooks" class="navlink" rel="nofollow">sign in</a>
</li>
</ul><div id="logo">
<a href="/">
<img alt="Goodreads: Book reviews, recommendations, and discussion" border="0" src="http://s.gr-assets.com/assets/layout/goodreads_logo_140-d09dedbb00ba4219b00b356d39a980a8.png"/></a>
</div>
<div id="sitesearch">
<form accept-charset="UTF-8" action="/search" method="get" name="headerSearchForm"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/></div>
<div class="auto_complete_field_wrapper">
<input id="sitesearch_field" name="query" type="text"/><script type="text/javascript" charset="utf-8">
          setDefaultText('sitesearch_field', 'Title / Author / ISBN')
        </script><div id="sitesearch_autocomplete"/>
<img alt="Loading-trans" class="loading" id="sitesearch_field_loading" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif" style="display: none"/></div>
<a class="submitLink" href="#" onclick="clearDefaultText('sitesearch_field', 'Title / Author / ISBN'); document.headerSearchForm.submit(); return false;"><img alt="search" src="http://s.gr-assets.com/assets/layout/magnifying_glass-06024a120abc83578b9c0b45241ee394.png" title="Title / Author / ISBN" width="16"/></a>
</form>
</div>

<ul class="nav" id="sitenav"><li>
<a href="/" class="navlink">Home</a>
</li>
<li>
<a href="/review/list" class="navlink" rel="nofollow">My Books</a>
</li>
<li>
<a href="/friend" class="navlink" rel="nofollow">Friends</a>
</li>
<li>
<a href="/recommendations" class="navlink" rel="nofollow">Recommendations</a>
</li>
<li class="withsubnav">
<div class="subnav">
<ul class="content"><li>
<a href="/list" title="Popular lists of books">listopia</a>
</li>
<li>
<a href="/giveaway" title="Free book giveaways">giveaways</a>
</li>
<li>
<a href="/book/popular_by_date/2012/11" title="Popular New Releases">popular</a>
</li>
<li>
<a href="/voice">goodreads voice</a>
</li>
<li>
<a href="/ebooks">ebooks</a>
</li>
</ul><ul class="content"><li>
<b>
fun
</b>
</li>
<li>
<a href="/trivia">trivia</a>
</li>
<li>
<a href="/quizzes">quizzes</a>
</li>
<li>
<a href="/quotes">quotes</a>
</li>
</ul><ul class="content"><li>
<b>
community
</b>
</li>
<li>
<a href="/group">groups</a>
</li>
<li>
<a href="/story">creative writing</a>
</li>
<li>
<a href="/user/online_now" rel="nofollow">people</a>
</li>
<li>
<a href="/event">events</a>
</li>
</ul></div>
<a href="/book" class="navlink" title="Explore books">Explore</a>
<a class="subnavlink inlineblock" href="#" onclick="HeaderNav.toggleSubnav({target: this}); return false;">&#160;</a>
</li>
</ul></div>
</div>


  

  <div class="mainContentContainer ">
    
    <div class="mainContent">
      


<script type="text/javascript" src="http://partner.googleadservices.com/gampad/google_service.js">
</script><script type="text/javascript">
    GS_googleAddAdSenseService("ca-pub-7284881071421289")
    GS_googleEnableAllServices()
</script><script type="text/javascript">
    GA_googleAddAttr("sid", "b9fe794f93b4abf1f23fe5c541245708")
            GA_googleAddAttr("shelf", "novel")
            GA_googleAddAttr("shelf", "philosophy")
            GA_googleAddAttr("shelf", "fantasy")
            GA_googleAddAttr("shelf", "own")
            GA_googleAddAttr("shelf", "kindle")
            GA_googleAddAttr("shelf", "library")
            GA_googleAddAttr("shelf", "iown")
            GA_googleAddAttr("shelf", "sciencefiction")
            GA_googleAddAttr("shelf", "capitalism")
            GA_googleAddAttr("shelf", "american")
            GA_googleAddAttr("shelf", "audiobook")
            GA_googleAddAttr("shelf", "bookclub")
        GA_googleAddAttr("gtargeting", "bstqdj64n5")
</script><div class="mainContentFloat">
        <div id="flashContainer">

</div>
        

<div class="leftContainer">
  <form accept-charset="UTF-8" action="/search" class="stacked" method="get" name="searchForm" style="width: 100%"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/></div>
    <h1>
    Search by Book Title, Author, or ISBN
</h1>
<div class="greyText" style="padding-bottom: 10px">
  <input type="text" name="q" size="55" value="atlas shrugged ayn rand" id="search_query_main" style=""/><input type="hidden" name="search_type" value="books"/></div>
<input class="button smallButton" style="margin-top: 2px" type="submit" value="search"/><div class="clear"/>

</form>
  <script type="text/javascript">
    document.searchForm.search_query_main.focus();
  </script><div>
    <div class="tabs mediumTabs">
        <a href="/search?q=atlas+shrugged+ayn+rand&amp;search%5Bsource%5D=goodreads&amp;search_type=all_results&amp;tab=all_results" class=" tab" id="all_resultsLink">all results</a>
        <span class=" selectedTab" id="booksLink" url="{:q=&gt;&quot;atlas shrugged ayn rand&quot;, :search_type=&gt;&quot;books&quot;, :&quot;search[source]&quot;=&gt;&quot;goodreads&quot;, :&quot;search[field]&quot;=&gt;nil, :tab=&gt;&quot;books&quot;}">books</span>
        <a href="/search?q=atlas+shrugged+ayn+rand&amp;search%5Bsource%5D=goodreads&amp;search_type=groups&amp;tab=groups" class=" tab" id="groupsLink">groups</a>
        <a href="/search?q=atlas+shrugged+ayn+rand&amp;search%5Bsource%5D=goodreads&amp;search_type=quotes&amp;tab=quotes" class=" tab" id="quotesLink">quotes</a>
        <a href="/search?q=atlas+shrugged+ayn+rand&amp;search%5Bsource%5D=goodreads&amp;search_type=events&amp;tab=events" class=" tab" id="eventsLink">events</a>
        <a href="/search?q=atlas+shrugged+ayn+rand&amp;search%5Bsource%5D=goodreads&amp;search_type=stories&amp;tab=stories" class=" tab" id="storiesLink">stories</a>
        <a href="/search?q=atlas+shrugged+ayn+rand&amp;search%5Bsource%5D=goodreads&amp;search_type=people&amp;tab=people" class=" tab" id="peopleLink">people</a>
        <a href="/search?q=atlas+shrugged+ayn+rand&amp;search%5Bsource%5D=goodreads&amp;search_type=lists&amp;tab=lists" class=" tab" id="listsLink">listopia</a>
        <a href="/search?q=atlas+shrugged+ayn+rand&amp;search%5Bsource%5D=goodreads&amp;search_type=trivia&amp;tab=trivia" class=" tab" id="triviaLink">trivia</a>
<div class="clear"> </div></div><script type="text/javascript" charset="utf-8">
  current_tabs[404085792] = 'books';

  Event.observe(window, 'load', function(e) {
    // Switch to an anchored tab if specified in the URL
    if (location.href.include('#')) {
      var tabID = location.href.split('#')[1];
      if (tabID != '' &amp;&amp; $(tabID)) {
        changeTab(tabID)
      }
    }
  })
</script></div>


    <div id="adcontainer1"/>

    <h3 class="searchSubNavContainer">Showing 1-16 of  16 results for 'atlas shrugged ayn rand' <span class="smallText"> (Goodreads search in 0.05s)</span></h3>


            
<script type="text/javascript" charset="utf-8">
  document.onclick = checkOpenSelects;

  function submitShelfLink(unique_id, book_id, shelf_id, shelf_name, submit_form, exclusive) {
    var checkbox_id = 'shelf_name_' + unique_id + '_' + shelf_id;
    var element = document.getElementById(checkbox_id)

    var checked = element.checked
    if (checked &amp;&amp; exclusive) {
      // can't uncheck a radio by clicking it!
      return
    }
    if(document.getElementById("savingMessage")){
      Element.show('savingMessage')
    }
    var element_id = 'shelfInDropdownName_' + unique_id + '_' + shelf_id;
    Element.update(element_id, "saving...");
    if (submit_form) {
      Element.hide('shelfDropdown_' + unique_id)
      var form = document.getElementById('addBookForm' + book_id)
      if (form) {
        form.shelf.value = shelf_name
        form.onsubmit()
      }
    }
    else {
      var action = checked ? 'remove' : ''
      element.checked = !element.checked
      new Ajax.Request('/shelf/add_to_shelf', {asynchronous:true, evalScripts:true, onSuccess:function(request){shelfSubmitted(request, book_id, checkbox_id, element_id, unique_id, shelf_name)}, parameters:'book_id=' + book_id + '&amp;name=' + shelf_name + '&amp;a=' + action + '&amp;authenticity_token=' + encodeURIComponent('FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA=')})
    }
  }

  function shelfSubmitted(request, book_id, checkbox_id, element_id, unique_id, shelf_name) {
    Element.update('shelfListfalse_' + book_id, request.responseText)
    afterShelfSave(checkbox_id, element_id, unique_id, shelf_name.escapeHTML())
  }

  function refreshGroupBox(group_id, book_id) {
    new Ajax.Updater('addGroupBooks' + book_id + '', '/group/add_book_box', {asynchronous:true, evalScripts:true, onSuccess:function(request){refreshGroupBoxComplete(request, book_id);}, parameters:'id=' + group_id + '&amp;book_id=' + book_id + '&amp;refresh=true' + '&amp;authenticity_token=' + encodeURIComponent('FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA=')})
  }
</script><table cellspacing="0" cellpadding="0" border="0" width="100%" class="tableList"><tr itemscope="" itemtype="http://schema.org/Book"><td width="5%" valign="top">
      <a name="662"/>
      <a href="/book/show/662.Atlas_Shrugged" title="Atlas Shrugged">
          <img alt="Atlas Shrugged" class="bookSmallImg" src="http://d.gr-assets.com/books/1347633289s/662.jpg"/></a>    </td>
    <td width="100%" valign="top">
      <a href="/book/show/662.Atlas_Shrugged" class="bookTitle" itemprop="url">
        <span itemprop="name">Atlas Shrugged</span>
</a>      <br/><span class="by smallText">by</span>
<span itemprop="author" itemscope="" itemtype="http://schema.org/Person">
<a href="http://www.goodreads.com/author/show/432.Ayn_Rand" class="authorName" itemprop="url"><span itemprop="name">Ayn Rand</span></a>, 
<a href="http://www.goodreads.com/author/show/1421.Leonard_Peikoff" class="authorName" itemprop="url"><span itemprop="name">Leonard Peikoff</span></a> <span class="greyText">(Goodreads Author)</span> <span class="authorName greyText smallText role">(Introduction)</span>
</span>

        <br/><span class="greyText smallText uitext">
          <span class="minirating"><span class="stars"><img alt="3.69 of 5 stars" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.69 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.69 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.69 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/stars/red_star_66pct-a2f513494595fa112f4762672b33daef.png" title="3.69 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="3.69 of 5 stars" width="12"/></span> 3.69 avg rating &#8212; 119,430 ratings</span>
            &#8212;
              published
             1957
            &#8212;
            <a href="/work/editions/817219-atlas-shrugged" class="greyText" rel="nofollow">76 editions</a>
        </span>
        


    </td>

      <td width="130px">
          <div class="wtrButtonContainer wtrSignedOut" id="1_book_662">
<div class="wtrUp wtrLeft">
<form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="book_id" name="book_id" type="hidden" value="662"/><input id="name" name="name" type="hidden" value="to-read"/><input id="unique_id" name="unique_id" type="hidden" value="1_book_662"/><input id="wtr_new" name="wtr_new" type="hidden" value="true"/><button class="wtrToRead" type="submit">
<span class="progressTrigger">Want to Read</span>
<span class="progressIndicator">saving&#226;&#128;&#166;</span>
</button>
</form>

</div>

<div class="wtrDivider"/>
<div class="wtrRight">
<button class="wtrShelfButton wtrUp">
<img alt="pick shelf" src="http://s.gr-assets.com/assets/wtr_button/books-0866015891eb128cdc57e550383532a0.png"/></button>
<div class="wtrShelfMenu">
<ul class="wtrExclusiveShelves"><li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="1_book_662"/><input id="book_id" name="book_id" type="hidden" value="662"/><button class="wtrExclusiveShelf" name="name" type="submit" value="to-read">
<span class="progressTrigger">Want to Read</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="1_book_662"/><input id="book_id" name="book_id" type="hidden" value="662"/><button class="wtrExclusiveShelf" name="name" type="submit" value="currently-reading">
<span class="progressTrigger">Currently Reading</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="1_book_662"/><input id="book_id" name="book_id" type="hidden" value="662"/><button class="wtrExclusiveShelf" name="name" type="submit" value="read">
<span class="progressTrigger">Read</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
</ul></div>
</div>

<div class="ratingStars wtrRating">
<form accept-charset="UTF-8" action="/review/rate/662.Atlas_Shrugged" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<button class="greyText uitext myRating" disabled="disabled" name="button" type="submit">Rate this book</button>
<div class="clearRating uitext">Clear rating</div>
<input id="rating" name="rating" type="hidden" value="0"/><input id="wtr_button_id" name="wtr_button_id" type="hidden" value="1_book_662"/></form>

<span class="stars" id="starsstars_for_1_book_662" onmouseout="mouseOutStars('stars_for_1_book_662')"><a rel="nofollow"><img alt="didn't like it " class="star" height="15" id="starstars_for_1_book_662_0" onclick="submitStars('stars_for_1_book_662', 0, '/review/rate/662?rating=1&amp;wtr_button_id=1_book_662', 0);  return false;" onmouseover="checkStars('stars_for_1_book_662', 0)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="didn't like it" width="15"/></a><a rel="nofollow"><img alt="it was ok " class="star" height="15" id="starstars_for_1_book_662_1" onclick="submitStars('stars_for_1_book_662', 1, '/review/rate/662?rating=2&amp;wtr_button_id=1_book_662', 0);  return false;" onmouseover="checkStars('stars_for_1_book_662', 1)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was ok" width="15"/></a><a rel="nofollow"><img alt="liked it " class="star" height="15" id="starstars_for_1_book_662_2" onclick="submitStars('stars_for_1_book_662', 2, '/review/rate/662?rating=3&amp;wtr_button_id=1_book_662', 0);  return false;" onmouseover="checkStars('stars_for_1_book_662', 2)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="liked it" width="15"/></a><a rel="nofollow"><img alt="really liked it " class="star" height="15" id="starstars_for_1_book_662_3" onclick="submitStars('stars_for_1_book_662', 3, '/review/rate/662?rating=4&amp;wtr_button_id=1_book_662', 0);  return false;" onmouseover="checkStars('stars_for_1_book_662', 3)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="really liked it" width="15"/></a><a rel="nofollow"><img alt="it was amazing " class="star" height="15" id="starstars_for_1_book_662_4" onclick="submitStars('stars_for_1_book_662', 4, '/review/rate/662?rating=5&amp;wtr_button_id=1_book_662', 0);  return false;" onmouseover="checkStars('stars_for_1_book_662', 4)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was amazing" width="15"/></a></span><script language="javascript" type="text/javascript">starRatings[ratingIndex++] = [ 'stars_for_1_book_662', -1]; checkStars('stars_for_1_book_662', -1);</script></div>

</div>

      </td>

  </tr><tr itemscope="" itemtype="http://schema.org/Book"><td width="5%" valign="top">
      <a name="2115"/>
      <a href="/book/show/2115.Atlas_Shrugged_The_Fountainhead" title="Atlas Shrugged &amp; The Fountainhead">
          <img alt="Atlas Shrugged &amp; The Founta..." class="bookSmallImg" src="http://d.gr-assets.com/books/1159932401s/2115.jpg"/></a>    </td>
    <td width="100%" valign="top">
      <a href="/book/show/2115.Atlas_Shrugged_The_Fountainhead" class="bookTitle" itemprop="url">
        <span itemprop="name">Atlas Shrugged &amp; The Fountainhead</span>
</a>      <br/><span class="by smallText">by</span>
<span itemprop="author" itemscope="" itemtype="http://schema.org/Person">
<a href="http://www.goodreads.com/author/show/432.Ayn_Rand" class="authorName" itemprop="url"><span itemprop="name">Ayn Rand</span></a>
</span>

        <br/><span class="greyText smallText uitext">
          <span class="minirating"><span class="stars"><img alt="4.02 of 5 stars" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.02 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.02 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.02 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.02 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/stars/red_star_33pct-69a219b6d79a91503f292bf5ac039d6b.png" title="4.02 of 5 stars" width="12"/></span> 4.02 avg rating &#8212; 2,283 ratings</span>
            &#8212;
              published
             1995
            &#8212;
            <a href="/work/editions/817229-atlas-shrugged-the-fountainhead" class="greyText" rel="nofollow">3 editions</a>
        </span>
        


    </td>

      <td width="130px">
          <div class="wtrButtonContainer wtrSignedOut" id="2_book_2115">
<div class="wtrUp wtrLeft">
<form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="book_id" name="book_id" type="hidden" value="2115"/><input id="name" name="name" type="hidden" value="to-read"/><input id="unique_id" name="unique_id" type="hidden" value="2_book_2115"/><input id="wtr_new" name="wtr_new" type="hidden" value="true"/><button class="wtrToRead" type="submit">
<span class="progressTrigger">Want to Read</span>
<span class="progressIndicator">saving&#226;&#128;&#166;</span>
</button>
</form>

</div>

<div class="wtrDivider"/>
<div class="wtrRight">
<button class="wtrShelfButton wtrUp">
<img alt="pick shelf" src="http://s.gr-assets.com/assets/wtr_button/books-0866015891eb128cdc57e550383532a0.png"/></button>
<div class="wtrShelfMenu">
<ul class="wtrExclusiveShelves"><li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="2_book_2115"/><input id="book_id" name="book_id" type="hidden" value="2115"/><button class="wtrExclusiveShelf" name="name" type="submit" value="to-read">
<span class="progressTrigger">Want to Read</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="2_book_2115"/><input id="book_id" name="book_id" type="hidden" value="2115"/><button class="wtrExclusiveShelf" name="name" type="submit" value="currently-reading">
<span class="progressTrigger">Currently Reading</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="2_book_2115"/><input id="book_id" name="book_id" type="hidden" value="2115"/><button class="wtrExclusiveShelf" name="name" type="submit" value="read">
<span class="progressTrigger">Read</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
</ul></div>
</div>

<div class="ratingStars wtrRating">
<form accept-charset="UTF-8" action="/review/rate/2115.Atlas_Shrugged_The_Fountainhead" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<button class="greyText uitext myRating" disabled="disabled" name="button" type="submit">Rate this book</button>
<div class="clearRating uitext">Clear rating</div>
<input id="rating" name="rating" type="hidden" value="0"/><input id="wtr_button_id" name="wtr_button_id" type="hidden" value="2_book_2115"/></form>

<span class="stars" id="starsstars_for_2_book_2115" onmouseout="mouseOutStars('stars_for_2_book_2115')"><a rel="nofollow"><img alt="didn't like it " class="star" height="15" id="starstars_for_2_book_2115_0" onclick="submitStars('stars_for_2_book_2115', 0, '/review/rate/2115?rating=1&amp;wtr_button_id=2_book_2115', 0);  return false;" onmouseover="checkStars('stars_for_2_book_2115', 0)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="didn't like it" width="15"/></a><a rel="nofollow"><img alt="it was ok " class="star" height="15" id="starstars_for_2_book_2115_1" onclick="submitStars('stars_for_2_book_2115', 1, '/review/rate/2115?rating=2&amp;wtr_button_id=2_book_2115', 0);  return false;" onmouseover="checkStars('stars_for_2_book_2115', 1)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was ok" width="15"/></a><a rel="nofollow"><img alt="liked it " class="star" height="15" id="starstars_for_2_book_2115_2" onclick="submitStars('stars_for_2_book_2115', 2, '/review/rate/2115?rating=3&amp;wtr_button_id=2_book_2115', 0);  return false;" onmouseover="checkStars('stars_for_2_book_2115', 2)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="liked it" width="15"/></a><a rel="nofollow"><img alt="really liked it " class="star" height="15" id="starstars_for_2_book_2115_3" onclick="submitStars('stars_for_2_book_2115', 3, '/review/rate/2115?rating=4&amp;wtr_button_id=2_book_2115', 0);  return false;" onmouseover="checkStars('stars_for_2_book_2115', 3)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="really liked it" width="15"/></a><a rel="nofollow"><img alt="it was amazing " class="star" height="15" id="starstars_for_2_book_2115_4" onclick="submitStars('stars_for_2_book_2115', 4, '/review/rate/2115?rating=5&amp;wtr_button_id=2_book_2115', 0);  return false;" onmouseover="checkStars('stars_for_2_book_2115', 4)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was amazing" width="15"/></a></span><script language="javascript" type="text/javascript">starRatings[ratingIndex++] = [ 'stars_for_2_book_2115', -1]; checkStars('stars_for_2_book_2115', -1);</script></div>

</div>

      </td>

  </tr><tr itemscope="" itemtype="http://schema.org/Book"><td width="5%" valign="top">
      <a name="6234337"/>
      <a href="/book/show/6234337-essays-on-ayn-rand-s-atlas-shrugged" title="Essays on Ayn Rand's Atlas Shrugged">
          <img alt="Essays on Ayn Rand's Atlas ..." class="bookSmallImg" src="http://d.gr-assets.com/books/1348746577s/6234337.jpg"/></a>    </td>
    <td width="100%" valign="top">
      <a href="/book/show/6234337-essays-on-ayn-rand-s-atlas-shrugged" class="bookTitle" itemprop="url">
        <span itemprop="name">Essays on Ayn Rand's Atlas Shrugged</span>
</a>      <br/><span class="by smallText">by</span>
<span itemprop="author" itemscope="" itemtype="http://schema.org/Person">
<a href="http://www.goodreads.com/author/show/1422.Robert_Mayhew" class="authorName" itemprop="url"><span itemprop="name">Robert Mayhew</span></a> <span class="authorName greyText smallText role">(Editor)</span>
</span>

        <br/><span class="greyText smallText uitext">
          <span class="minirating"><span class="stars"><img alt="3.89 of 5 stars" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.89 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.89 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.89 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/stars/red_star_66pct-a2f513494595fa112f4762672b33daef.png" title="3.89 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="3.89 of 5 stars" width="12"/></span> 3.89 avg rating &#8212; 18 ratings</span>
            &#8212;
              published
             2009
            &#8212;
            <a href="/work/editions/6416993-essays-on-ayn-rand-s-atlas-shrugged" class="greyText" rel="nofollow">2 editions</a>
        </span>
        


    </td>

      <td width="130px">
          <div class="wtrButtonContainer wtrSignedOut" id="3_book_6234337">
<div class="wtrUp wtrLeft">
<form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="book_id" name="book_id" type="hidden" value="6234337"/><input id="name" name="name" type="hidden" value="to-read"/><input id="unique_id" name="unique_id" type="hidden" value="3_book_6234337"/><input id="wtr_new" name="wtr_new" type="hidden" value="true"/><button class="wtrToRead" type="submit">
<span class="progressTrigger">Want to Read</span>
<span class="progressIndicator">saving&#226;&#128;&#166;</span>
</button>
</form>

</div>

<div class="wtrDivider"/>
<div class="wtrRight">
<button class="wtrShelfButton wtrUp">
<img alt="pick shelf" src="http://s.gr-assets.com/assets/wtr_button/books-0866015891eb128cdc57e550383532a0.png"/></button>
<div class="wtrShelfMenu">
<ul class="wtrExclusiveShelves"><li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="3_book_6234337"/><input id="book_id" name="book_id" type="hidden" value="6234337"/><button class="wtrExclusiveShelf" name="name" type="submit" value="to-read">
<span class="progressTrigger">Want to Read</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="3_book_6234337"/><input id="book_id" name="book_id" type="hidden" value="6234337"/><button class="wtrExclusiveShelf" name="name" type="submit" value="currently-reading">
<span class="progressTrigger">Currently Reading</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="3_book_6234337"/><input id="book_id" name="book_id" type="hidden" value="6234337"/><button class="wtrExclusiveShelf" name="name" type="submit" value="read">
<span class="progressTrigger">Read</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
</ul></div>
</div>

<div class="ratingStars wtrRating">
<form accept-charset="UTF-8" action="/review/rate/6234337-essays-on-ayn-rand-s-atlas-shrugged" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<button class="greyText uitext myRating" disabled="disabled" name="button" type="submit">Rate this book</button>
<div class="clearRating uitext">Clear rating</div>
<input id="rating" name="rating" type="hidden" value="0"/><input id="wtr_button_id" name="wtr_button_id" type="hidden" value="3_book_6234337"/></form>

<span class="stars" id="starsstars_for_3_book_6234337" onmouseout="mouseOutStars('stars_for_3_book_6234337')"><a rel="nofollow"><img alt="didn't like it " class="star" height="15" id="starstars_for_3_book_6234337_0" onclick="submitStars('stars_for_3_book_6234337', 0, '/review/rate/6234337?rating=1&amp;wtr_button_id=3_book_6234337', 0);  return false;" onmouseover="checkStars('stars_for_3_book_6234337', 0)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="didn't like it" width="15"/></a><a rel="nofollow"><img alt="it was ok " class="star" height="15" id="starstars_for_3_book_6234337_1" onclick="submitStars('stars_for_3_book_6234337', 1, '/review/rate/6234337?rating=2&amp;wtr_button_id=3_book_6234337', 0);  return false;" onmouseover="checkStars('stars_for_3_book_6234337', 1)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was ok" width="15"/></a><a rel="nofollow"><img alt="liked it " class="star" height="15" id="starstars_for_3_book_6234337_2" onclick="submitStars('stars_for_3_book_6234337', 2, '/review/rate/6234337?rating=3&amp;wtr_button_id=3_book_6234337', 0);  return false;" onmouseover="checkStars('stars_for_3_book_6234337', 2)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="liked it" width="15"/></a><a rel="nofollow"><img alt="really liked it " class="star" height="15" id="starstars_for_3_book_6234337_3" onclick="submitStars('stars_for_3_book_6234337', 3, '/review/rate/6234337?rating=4&amp;wtr_button_id=3_book_6234337', 0);  return false;" onmouseover="checkStars('stars_for_3_book_6234337', 3)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="really liked it" width="15"/></a><a rel="nofollow"><img alt="it was amazing " class="star" height="15" id="starstars_for_3_book_6234337_4" onclick="submitStars('stars_for_3_book_6234337', 4, '/review/rate/6234337?rating=5&amp;wtr_button_id=3_book_6234337', 0);  return false;" onmouseover="checkStars('stars_for_3_book_6234337', 4)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was amazing" width="15"/></a></span><script language="javascript" type="text/javascript">starRatings[ratingIndex++] = [ 'stars_for_3_book_6234337', -1]; checkStars('stars_for_3_book_6234337', -1);</script></div>

</div>

      </td>

  </tr><tr itemscope="" itemtype="http://schema.org/Book"><td width="5%" valign="top">
      <a name="13607666"/>
      <a href="/book/show/13607666-quicklet-ayn-rand-s-atlas-shrugged" title="Quicklet-Ayn Rand's Atlas Shrugged">
          <img alt="Quicklet-Ayn Rand's Atlas S..." class="bookSmallImg" src="http://www.goodreads.com/assets/nocover/60x80.png"/></a>    </td>
    <td width="100%" valign="top">
      <a href="/book/show/13607666-quicklet-ayn-rand-s-atlas-shrugged" class="bookTitle" itemprop="url">
        <span itemprop="name">Quicklet-Ayn Rand's Atlas Shrugged</span>
</a>      <br/><span class="by smallText">by</span>
<span itemprop="author" itemscope="" itemtype="http://schema.org/Person">
<a href="http://www.goodreads.com/author/show/2990982.Jason_Malcolm_Stewart" class="authorName" itemprop="url"><span itemprop="name">Jason Malcolm Stewart</span></a> <span class="greyText">(Goodreads Author)</span>
</span>

        <br/><span class="greyText smallText uitext">
          <span class="minirating"><span class="stars"><img alt="5.0 of 5 stars" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="5.0 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="5.0 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="5.0 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="5.0 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="5.0 of 5 stars" width="12"/></span> 5.00 avg rating &#8212; 1 rating</span>
            &#8212;
              published
             2012
            &#8212;
            <a href="/work/editions/19203737-quicklet-ayn-rand-s-atlas-shrugged" class="greyText" rel="nofollow">1 edition</a>
        </span>
        


    </td>

      <td width="130px">
          <div class="wtrButtonContainer wtrSignedOut" id="4_book_13607666">
<div class="wtrUp wtrLeft">
<form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="book_id" name="book_id" type="hidden" value="13607666"/><input id="name" name="name" type="hidden" value="to-read"/><input id="unique_id" name="unique_id" type="hidden" value="4_book_13607666"/><input id="wtr_new" name="wtr_new" type="hidden" value="true"/><button class="wtrToRead" type="submit">
<span class="progressTrigger">Want to Read</span>
<span class="progressIndicator">saving&#226;&#128;&#166;</span>
</button>
</form>

</div>

<div class="wtrDivider"/>
<div class="wtrRight">
<button class="wtrShelfButton wtrUp">
<img alt="pick shelf" src="http://s.gr-assets.com/assets/wtr_button/books-0866015891eb128cdc57e550383532a0.png"/></button>
<div class="wtrShelfMenu">
<ul class="wtrExclusiveShelves"><li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="4_book_13607666"/><input id="book_id" name="book_id" type="hidden" value="13607666"/><button class="wtrExclusiveShelf" name="name" type="submit" value="to-read">
<span class="progressTrigger">Want to Read</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="4_book_13607666"/><input id="book_id" name="book_id" type="hidden" value="13607666"/><button class="wtrExclusiveShelf" name="name" type="submit" value="currently-reading">
<span class="progressTrigger">Currently Reading</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="4_book_13607666"/><input id="book_id" name="book_id" type="hidden" value="13607666"/><button class="wtrExclusiveShelf" name="name" type="submit" value="read">
<span class="progressTrigger">Read</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
</ul></div>
</div>

<div class="ratingStars wtrRating">
<form accept-charset="UTF-8" action="/review/rate/13607666-quicklet-ayn-rand-s-atlas-shrugged" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<button class="greyText uitext myRating" disabled="disabled" name="button" type="submit">Rate this book</button>
<div class="clearRating uitext">Clear rating</div>
<input id="rating" name="rating" type="hidden" value="0"/><input id="wtr_button_id" name="wtr_button_id" type="hidden" value="4_book_13607666"/></form>

<span class="stars" id="starsstars_for_4_book_13607666" onmouseout="mouseOutStars('stars_for_4_book_13607666')"><a rel="nofollow"><img alt="didn't like it " class="star" height="15" id="starstars_for_4_book_13607666_0" onclick="submitStars('stars_for_4_book_13607666', 0, '/review/rate/13607666?rating=1&amp;wtr_button_id=4_book_13607666', 0);  return false;" onmouseover="checkStars('stars_for_4_book_13607666', 0)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="didn't like it" width="15"/></a><a rel="nofollow"><img alt="it was ok " class="star" height="15" id="starstars_for_4_book_13607666_1" onclick="submitStars('stars_for_4_book_13607666', 1, '/review/rate/13607666?rating=2&amp;wtr_button_id=4_book_13607666', 0);  return false;" onmouseover="checkStars('stars_for_4_book_13607666', 1)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was ok" width="15"/></a><a rel="nofollow"><img alt="liked it " class="star" height="15" id="starstars_for_4_book_13607666_2" onclick="submitStars('stars_for_4_book_13607666', 2, '/review/rate/13607666?rating=3&amp;wtr_button_id=4_book_13607666', 0);  return false;" onmouseover="checkStars('stars_for_4_book_13607666', 2)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="liked it" width="15"/></a><a rel="nofollow"><img alt="really liked it " class="star" height="15" id="starstars_for_4_book_13607666_3" onclick="submitStars('stars_for_4_book_13607666', 3, '/review/rate/13607666?rating=4&amp;wtr_button_id=4_book_13607666', 0);  return false;" onmouseover="checkStars('stars_for_4_book_13607666', 3)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="really liked it" width="15"/></a><a rel="nofollow"><img alt="it was amazing " class="star" height="15" id="starstars_for_4_book_13607666_4" onclick="submitStars('stars_for_4_book_13607666', 4, '/review/rate/13607666?rating=5&amp;wtr_button_id=4_book_13607666', 0);  return false;" onmouseover="checkStars('stars_for_4_book_13607666', 4)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was amazing" width="15"/></a></span><script language="javascript" type="text/javascript">starRatings[ratingIndex++] = [ 'stars_for_4_book_13607666', -1]; checkStars('stars_for_4_book_13607666', -1);</script></div>

</div>

      </td>

  </tr><tr itemscope="" itemtype="http://schema.org/Book"><td width="5%" valign="top">
      <a name="201237"/>
      <a href="/book/show/201237.Ayn_Rand_s_Atlas_Shrugged" title="Ayn Rand's Atlas Shrugged: A Philosophical and Literary Companion">
          <img alt="Ayn Rand's Atlas Shrugged: ..." class="bookSmallImg" src="http://d.gr-assets.com/books/1266494900s/201237.jpg"/></a>    </td>
    <td width="100%" valign="top">
      <a href="/book/show/201237.Ayn_Rand_s_Atlas_Shrugged" class="bookTitle" itemprop="url">
        <span itemprop="name">Ayn Rand's Atlas Shrugged: A Philosophical and Literary Companion</span>
</a>      <br/><span class="by smallText">by</span>
<span itemprop="author" itemscope="" itemtype="http://schema.org/Person">
<a href="http://www.goodreads.com/author/show/117359.Edward_Wayne_Younkins" class="authorName" itemprop="url"><span itemprop="name">Edward Wayne Younkins</span></a>
</span>

        <br/><span class="greyText smallText uitext">
          <span class="minirating"><span class="stars"><img alt="3.86 of 5 stars" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.86 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.86 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.86 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/stars/red_star_66pct-a2f513494595fa112f4762672b33daef.png" title="3.86 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="3.86 of 5 stars" width="12"/></span> 3.86 avg rating &#8212; 7 ratings</span>
            &#8212;
              published
             2007
            &#8212;
            <a href="/work/editions/194705-ayn-rand-s-atlas-shrugged-a-philosophical-and-literary-companion" class="greyText" rel="nofollow">1 edition</a>
        </span>
        


    </td>

      <td width="130px">
          <div class="wtrButtonContainer wtrSignedOut" id="5_book_201237">
<div class="wtrUp wtrLeft">
<form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="book_id" name="book_id" type="hidden" value="201237"/><input id="name" name="name" type="hidden" value="to-read"/><input id="unique_id" name="unique_id" type="hidden" value="5_book_201237"/><input id="wtr_new" name="wtr_new" type="hidden" value="true"/><button class="wtrToRead" type="submit">
<span class="progressTrigger">Want to Read</span>
<span class="progressIndicator">saving&#226;&#128;&#166;</span>
</button>
</form>

</div>

<div class="wtrDivider"/>
<div class="wtrRight">
<button class="wtrShelfButton wtrUp">
<img alt="pick shelf" src="http://s.gr-assets.com/assets/wtr_button/books-0866015891eb128cdc57e550383532a0.png"/></button>
<div class="wtrShelfMenu">
<ul class="wtrExclusiveShelves"><li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="5_book_201237"/><input id="book_id" name="book_id" type="hidden" value="201237"/><button class="wtrExclusiveShelf" name="name" type="submit" value="to-read">
<span class="progressTrigger">Want to Read</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="5_book_201237"/><input id="book_id" name="book_id" type="hidden" value="201237"/><button class="wtrExclusiveShelf" name="name" type="submit" value="currently-reading">
<span class="progressTrigger">Currently Reading</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="5_book_201237"/><input id="book_id" name="book_id" type="hidden" value="201237"/><button class="wtrExclusiveShelf" name="name" type="submit" value="read">
<span class="progressTrigger">Read</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
</ul></div>
</div>

<div class="ratingStars wtrRating">
<form accept-charset="UTF-8" action="/review/rate/201237.Ayn_Rand_s_Atlas_Shrugged" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<button class="greyText uitext myRating" disabled="disabled" name="button" type="submit">Rate this book</button>
<div class="clearRating uitext">Clear rating</div>
<input id="rating" name="rating" type="hidden" value="0"/><input id="wtr_button_id" name="wtr_button_id" type="hidden" value="5_book_201237"/></form>

<span class="stars" id="starsstars_for_5_book_201237" onmouseout="mouseOutStars('stars_for_5_book_201237')"><a rel="nofollow"><img alt="didn't like it " class="star" height="15" id="starstars_for_5_book_201237_0" onclick="submitStars('stars_for_5_book_201237', 0, '/review/rate/201237?rating=1&amp;wtr_button_id=5_book_201237', 0);  return false;" onmouseover="checkStars('stars_for_5_book_201237', 0)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="didn't like it" width="15"/></a><a rel="nofollow"><img alt="it was ok " class="star" height="15" id="starstars_for_5_book_201237_1" onclick="submitStars('stars_for_5_book_201237', 1, '/review/rate/201237?rating=2&amp;wtr_button_id=5_book_201237', 0);  return false;" onmouseover="checkStars('stars_for_5_book_201237', 1)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was ok" width="15"/></a><a rel="nofollow"><img alt="liked it " class="star" height="15" id="starstars_for_5_book_201237_2" onclick="submitStars('stars_for_5_book_201237', 2, '/review/rate/201237?rating=3&amp;wtr_button_id=5_book_201237', 0);  return false;" onmouseover="checkStars('stars_for_5_book_201237', 2)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="liked it" width="15"/></a><a rel="nofollow"><img alt="really liked it " class="star" height="15" id="starstars_for_5_book_201237_3" onclick="submitStars('stars_for_5_book_201237', 3, '/review/rate/201237?rating=4&amp;wtr_button_id=5_book_201237', 0);  return false;" onmouseover="checkStars('stars_for_5_book_201237', 3)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="really liked it" width="15"/></a><a rel="nofollow"><img alt="it was amazing " class="star" height="15" id="starstars_for_5_book_201237_4" onclick="submitStars('stars_for_5_book_201237', 4, '/review/rate/201237?rating=5&amp;wtr_button_id=5_book_201237', 0);  return false;" onmouseover="checkStars('stars_for_5_book_201237', 4)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was amazing" width="15"/></a></span><script language="javascript" type="text/javascript">starRatings[ratingIndex++] = [ 'stars_for_5_book_201237', -1]; checkStars('stars_for_5_book_201237', -1);</script></div>

</div>

      </td>

  </tr><tr itemscope="" itemtype="http://schema.org/Book"><td width="5%" valign="top">
      <a name="5755462"/>
      <a href="/book/show/5755462-atlas-shrugged-part-a" title="Atlas Shrugged Part A: New Edition">
          <img alt="Atlas Shrugged Part A: New ..." class="bookSmallImg" src="http://d.gr-assets.com/books/1348463450s/5755462.jpg"/></a>    </td>
    <td width="100%" valign="top">
      <a href="/book/show/5755462-atlas-shrugged-part-a" class="bookTitle" itemprop="url">
        <span itemprop="name">Atlas Shrugged Part A: New Edition</span>
</a>      <br/><span class="by smallText">by</span>
<span itemprop="author" itemscope="" itemtype="http://schema.org/Person">
<a href="http://www.goodreads.com/author/show/432.Ayn_Rand" class="authorName" itemprop="url"><span itemprop="name">Ayn Rand</span></a>, 
<a href="http://www.goodreads.com/author/show/44554.Scott_Brick" class="authorName" itemprop="url"><span itemprop="name">Scott Brick</span></a> <span class="authorName greyText smallText role">(Read by)</span>
</span>

        <br/><span class="greyText smallText uitext">
          <span class="minirating"><span class="stars"><img alt="4.0 of 5 stars" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.0 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.0 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.0 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.0 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="4.0 of 5 stars" width="12"/></span> 4.00 avg rating &#8212; 84 ratings</span>
            &#8212;
            <a href="/work/editions/21836607-atlas-shrugged-part-a-new-edition" class="greyText" rel="nofollow">5 editions</a>
        </span>
        


    </td>

      <td width="130px">
          <div class="wtrButtonContainer wtrSignedOut" id="6_book_5755462">
<div class="wtrUp wtrLeft">
<form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="book_id" name="book_id" type="hidden" value="5755462"/><input id="name" name="name" type="hidden" value="to-read"/><input id="unique_id" name="unique_id" type="hidden" value="6_book_5755462"/><input id="wtr_new" name="wtr_new" type="hidden" value="true"/><button class="wtrToRead" type="submit">
<span class="progressTrigger">Want to Read</span>
<span class="progressIndicator">saving&#226;&#128;&#166;</span>
</button>
</form>

</div>

<div class="wtrDivider"/>
<div class="wtrRight">
<button class="wtrShelfButton wtrUp">
<img alt="pick shelf" src="http://s.gr-assets.com/assets/wtr_button/books-0866015891eb128cdc57e550383532a0.png"/></button>
<div class="wtrShelfMenu">
<ul class="wtrExclusiveShelves"><li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="6_book_5755462"/><input id="book_id" name="book_id" type="hidden" value="5755462"/><button class="wtrExclusiveShelf" name="name" type="submit" value="to-read">
<span class="progressTrigger">Want to Read</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="6_book_5755462"/><input id="book_id" name="book_id" type="hidden" value="5755462"/><button class="wtrExclusiveShelf" name="name" type="submit" value="currently-reading">
<span class="progressTrigger">Currently Reading</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="6_book_5755462"/><input id="book_id" name="book_id" type="hidden" value="5755462"/><button class="wtrExclusiveShelf" name="name" type="submit" value="read">
<span class="progressTrigger">Read</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
</ul></div>
</div>

<div class="ratingStars wtrRating">
<form accept-charset="UTF-8" action="/review/rate/5755462-atlas-shrugged-part-a" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<button class="greyText uitext myRating" disabled="disabled" name="button" type="submit">Rate this book</button>
<div class="clearRating uitext">Clear rating</div>
<input id="rating" name="rating" type="hidden" value="0"/><input id="wtr_button_id" name="wtr_button_id" type="hidden" value="6_book_5755462"/></form>

<span class="stars" id="starsstars_for_6_book_5755462" onmouseout="mouseOutStars('stars_for_6_book_5755462')"><a rel="nofollow"><img alt="didn't like it " class="star" height="15" id="starstars_for_6_book_5755462_0" onclick="submitStars('stars_for_6_book_5755462', 0, '/review/rate/5755462?rating=1&amp;wtr_button_id=6_book_5755462', 0);  return false;" onmouseover="checkStars('stars_for_6_book_5755462', 0)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="didn't like it" width="15"/></a><a rel="nofollow"><img alt="it was ok " class="star" height="15" id="starstars_for_6_book_5755462_1" onclick="submitStars('stars_for_6_book_5755462', 1, '/review/rate/5755462?rating=2&amp;wtr_button_id=6_book_5755462', 0);  return false;" onmouseover="checkStars('stars_for_6_book_5755462', 1)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was ok" width="15"/></a><a rel="nofollow"><img alt="liked it " class="star" height="15" id="starstars_for_6_book_5755462_2" onclick="submitStars('stars_for_6_book_5755462', 2, '/review/rate/5755462?rating=3&amp;wtr_button_id=6_book_5755462', 0);  return false;" onmouseover="checkStars('stars_for_6_book_5755462', 2)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="liked it" width="15"/></a><a rel="nofollow"><img alt="really liked it " class="star" height="15" id="starstars_for_6_book_5755462_3" onclick="submitStars('stars_for_6_book_5755462', 3, '/review/rate/5755462?rating=4&amp;wtr_button_id=6_book_5755462', 0);  return false;" onmouseover="checkStars('stars_for_6_book_5755462', 3)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="really liked it" width="15"/></a><a rel="nofollow"><img alt="it was amazing " class="star" height="15" id="starstars_for_6_book_5755462_4" onclick="submitStars('stars_for_6_book_5755462', 4, '/review/rate/5755462?rating=5&amp;wtr_button_id=6_book_5755462', 0);  return false;" onmouseover="checkStars('stars_for_6_book_5755462', 4)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was amazing" width="15"/></a></span><script language="javascript" type="text/javascript">starRatings[ratingIndex++] = [ 'stars_for_6_book_5755462', -1]; checkStars('stars_for_6_book_5755462', -1);</script></div>

</div>

      </td>

  </tr><tr itemscope="" itemtype="http://schema.org/Book"><td width="5%" valign="top">
      <a name="831567"/>
      <a href="/book/show/831567.Ayn_Rand_s_Atlas_Shrugged" title="Ayn Rand's Atlas Shrugged: A Philosophical and Literary Companion">
          <img alt="Ayn Rand's Atlas Shrugged: ..." class="bookSmallImg" src="http://d.gr-assets.com/books/1266654752s/831567.jpg"/></a>    </td>
    <td width="100%" valign="top">
      <a href="/book/show/831567.Ayn_Rand_s_Atlas_Shrugged" class="bookTitle" itemprop="url">
        <span itemprop="name">Ayn Rand's Atlas Shrugged: A Philosophical and Literary Companion</span>
</a>      <br/><span class="by smallText">by</span>
<span itemprop="author" itemscope="" itemtype="http://schema.org/Person">
<a href="http://www.goodreads.com/author/show/432722.Edward_W_Younkins" class="authorName" itemprop="url"><span itemprop="name">Edward W. Younkins</span></a> <span class="authorName greyText smallText role">(Editor)</span>
</span>

        <br/><span class="greyText smallText uitext">
          <span class="minirating"><span class="stars"><img alt="3.5 of 5 stars" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.5 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.5 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.5 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/stars/red_star_66pct-a2f513494595fa112f4762672b33daef.png" title="3.5 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="3.5 of 5 stars" width="12"/></span> 3.50 avg rating &#8212; 2 ratings</span>
            &#8212;
              published
             2007
            &#8212;
            <a href="/work/editions/817220-ayn-rand-s-atlas-shrugged-a-philosophical-and-literary-companion" class="greyText" rel="nofollow">2 editions</a>
        </span>
        


    </td>

      <td width="130px">
          <div class="wtrButtonContainer wtrSignedOut" id="7_book_831567">
<div class="wtrUp wtrLeft">
<form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="book_id" name="book_id" type="hidden" value="831567"/><input id="name" name="name" type="hidden" value="to-read"/><input id="unique_id" name="unique_id" type="hidden" value="7_book_831567"/><input id="wtr_new" name="wtr_new" type="hidden" value="true"/><button class="wtrToRead" type="submit">
<span class="progressTrigger">Want to Read</span>
<span class="progressIndicator">saving&#226;&#128;&#166;</span>
</button>
</form>

</div>

<div class="wtrDivider"/>
<div class="wtrRight">
<button class="wtrShelfButton wtrUp">
<img alt="pick shelf" src="http://s.gr-assets.com/assets/wtr_button/books-0866015891eb128cdc57e550383532a0.png"/></button>
<div class="wtrShelfMenu">
<ul class="wtrExclusiveShelves"><li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="7_book_831567"/><input id="book_id" name="book_id" type="hidden" value="831567"/><button class="wtrExclusiveShelf" name="name" type="submit" value="to-read">
<span class="progressTrigger">Want to Read</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="7_book_831567"/><input id="book_id" name="book_id" type="hidden" value="831567"/><button class="wtrExclusiveShelf" name="name" type="submit" value="currently-reading">
<span class="progressTrigger">Currently Reading</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="7_book_831567"/><input id="book_id" name="book_id" type="hidden" value="831567"/><button class="wtrExclusiveShelf" name="name" type="submit" value="read">
<span class="progressTrigger">Read</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
</ul></div>
</div>

<div class="ratingStars wtrRating">
<form accept-charset="UTF-8" action="/review/rate/831567.Ayn_Rand_s_Atlas_Shrugged" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<button class="greyText uitext myRating" disabled="disabled" name="button" type="submit">Rate this book</button>
<div class="clearRating uitext">Clear rating</div>
<input id="rating" name="rating" type="hidden" value="0"/><input id="wtr_button_id" name="wtr_button_id" type="hidden" value="7_book_831567"/></form>

<span class="stars" id="starsstars_for_7_book_831567" onmouseout="mouseOutStars('stars_for_7_book_831567')"><a rel="nofollow"><img alt="didn't like it " class="star" height="15" id="starstars_for_7_book_831567_0" onclick="submitStars('stars_for_7_book_831567', 0, '/review/rate/831567?rating=1&amp;wtr_button_id=7_book_831567', 0);  return false;" onmouseover="checkStars('stars_for_7_book_831567', 0)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="didn't like it" width="15"/></a><a rel="nofollow"><img alt="it was ok " class="star" height="15" id="starstars_for_7_book_831567_1" onclick="submitStars('stars_for_7_book_831567', 1, '/review/rate/831567?rating=2&amp;wtr_button_id=7_book_831567', 0);  return false;" onmouseover="checkStars('stars_for_7_book_831567', 1)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was ok" width="15"/></a><a rel="nofollow"><img alt="liked it " class="star" height="15" id="starstars_for_7_book_831567_2" onclick="submitStars('stars_for_7_book_831567', 2, '/review/rate/831567?rating=3&amp;wtr_button_id=7_book_831567', 0);  return false;" onmouseover="checkStars('stars_for_7_book_831567', 2)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="liked it" width="15"/></a><a rel="nofollow"><img alt="really liked it " class="star" height="15" id="starstars_for_7_book_831567_3" onclick="submitStars('stars_for_7_book_831567', 3, '/review/rate/831567?rating=4&amp;wtr_button_id=7_book_831567', 0);  return false;" onmouseover="checkStars('stars_for_7_book_831567', 3)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="really liked it" width="15"/></a><a rel="nofollow"><img alt="it was amazing " class="star" height="15" id="starstars_for_7_book_831567_4" onclick="submitStars('stars_for_7_book_831567', 4, '/review/rate/831567?rating=5&amp;wtr_button_id=7_book_831567', 0);  return false;" onmouseover="checkStars('stars_for_7_book_831567', 4)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was amazing" width="15"/></a></span><script language="javascript" type="text/javascript">starRatings[ratingIndex++] = [ 'stars_for_7_book_831567', -1]; checkStars('stars_for_7_book_831567', -1);</script></div>

</div>

      </td>

  </tr><tr itemscope="" itemtype="http://schema.org/Book"><td width="5%" valign="top">
      <a name="9364"/>
      <a href="/book/show/9364.Atlas_Shrugged" title="Atlas Shrugged">
          <img alt="Atlas Shrugged" class="bookSmallImg" src="http://d.gr-assets.com/books/1348366796s/9364.jpg"/></a>    </td>
    <td width="100%" valign="top">
      <a href="/book/show/9364.Atlas_Shrugged" class="bookTitle" itemprop="url">
        <span itemprop="name">Atlas Shrugged</span>
</a>      <br/><span class="by smallText">by</span>
<span itemprop="author" itemscope="" itemtype="http://schema.org/Person">
<a href="http://www.goodreads.com/author/show/1423.Andrew_Bernstein" class="authorName" itemprop="url"><span itemprop="name">Andrew Bernstein</span></a>, 
<a href="http://www.goodreads.com/author/show/3899673.CliffsNotes" class="authorName" itemprop="url"><span itemprop="name">CliffsNotes</span></a>, <a href="http://www.goodreads.com/author/show/432.Ayn_Rand" class="authorName" itemprop="url"><span itemprop="name">Ayn Rand</span></a>
</span>

        <br/><span class="greyText smallText uitext">
          <span class="minirating"><span class="stars"><img alt="4.12 of 5 stars" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.12 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.12 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.12 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.12 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/stars/red_star_33pct-69a219b6d79a91503f292bf5ac039d6b.png" title="4.12 of 5 stars" width="12"/></span> 4.12 avg rating &#8212; 41 ratings</span>
            &#8212;
              published
             2000
            &#8212;
            <a href="/work/editions/12225-atlas-shrugged-cliffs-notes" class="greyText" rel="nofollow">10 editions</a>
        </span>
        


    </td>

      <td width="130px">
          <div class="wtrButtonContainer wtrSignedOut" id="8_book_9364">
<div class="wtrUp wtrLeft">
<form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="book_id" name="book_id" type="hidden" value="9364"/><input id="name" name="name" type="hidden" value="to-read"/><input id="unique_id" name="unique_id" type="hidden" value="8_book_9364"/><input id="wtr_new" name="wtr_new" type="hidden" value="true"/><button class="wtrToRead" type="submit">
<span class="progressTrigger">Want to Read</span>
<span class="progressIndicator">saving&#226;&#128;&#166;</span>
</button>
</form>

</div>

<div class="wtrDivider"/>
<div class="wtrRight">
<button class="wtrShelfButton wtrUp">
<img alt="pick shelf" src="http://s.gr-assets.com/assets/wtr_button/books-0866015891eb128cdc57e550383532a0.png"/></button>
<div class="wtrShelfMenu">
<ul class="wtrExclusiveShelves"><li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="8_book_9364"/><input id="book_id" name="book_id" type="hidden" value="9364"/><button class="wtrExclusiveShelf" name="name" type="submit" value="to-read">
<span class="progressTrigger">Want to Read</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="8_book_9364"/><input id="book_id" name="book_id" type="hidden" value="9364"/><button class="wtrExclusiveShelf" name="name" type="submit" value="currently-reading">
<span class="progressTrigger">Currently Reading</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="8_book_9364"/><input id="book_id" name="book_id" type="hidden" value="9364"/><button class="wtrExclusiveShelf" name="name" type="submit" value="read">
<span class="progressTrigger">Read</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
</ul></div>
</div>

<div class="ratingStars wtrRating">
<form accept-charset="UTF-8" action="/review/rate/9364.Atlas_Shrugged" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<button class="greyText uitext myRating" disabled="disabled" name="button" type="submit">Rate this book</button>
<div class="clearRating uitext">Clear rating</div>
<input id="rating" name="rating" type="hidden" value="0"/><input id="wtr_button_id" name="wtr_button_id" type="hidden" value="8_book_9364"/></form>

<span class="stars" id="starsstars_for_8_book_9364" onmouseout="mouseOutStars('stars_for_8_book_9364')"><a rel="nofollow"><img alt="didn't like it " class="star" height="15" id="starstars_for_8_book_9364_0" onclick="submitStars('stars_for_8_book_9364', 0, '/review/rate/9364?rating=1&amp;wtr_button_id=8_book_9364', 0);  return false;" onmouseover="checkStars('stars_for_8_book_9364', 0)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="didn't like it" width="15"/></a><a rel="nofollow"><img alt="it was ok " class="star" height="15" id="starstars_for_8_book_9364_1" onclick="submitStars('stars_for_8_book_9364', 1, '/review/rate/9364?rating=2&amp;wtr_button_id=8_book_9364', 0);  return false;" onmouseover="checkStars('stars_for_8_book_9364', 1)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was ok" width="15"/></a><a rel="nofollow"><img alt="liked it " class="star" height="15" id="starstars_for_8_book_9364_2" onclick="submitStars('stars_for_8_book_9364', 2, '/review/rate/9364?rating=3&amp;wtr_button_id=8_book_9364', 0);  return false;" onmouseover="checkStars('stars_for_8_book_9364', 2)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="liked it" width="15"/></a><a rel="nofollow"><img alt="really liked it " class="star" height="15" id="starstars_for_8_book_9364_3" onclick="submitStars('stars_for_8_book_9364', 3, '/review/rate/9364?rating=4&amp;wtr_button_id=8_book_9364', 0);  return false;" onmouseover="checkStars('stars_for_8_book_9364', 3)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="really liked it" width="15"/></a><a rel="nofollow"><img alt="it was amazing " class="star" height="15" id="starstars_for_8_book_9364_4" onclick="submitStars('stars_for_8_book_9364', 4, '/review/rate/9364?rating=5&amp;wtr_button_id=8_book_9364', 0);  return false;" onmouseover="checkStars('stars_for_8_book_9364', 4)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was amazing" width="15"/></a></span><script language="javascript" type="text/javascript">starRatings[ratingIndex++] = [ 'stars_for_8_book_9364', -1]; checkStars('stars_for_8_book_9364', -1);</script></div>

</div>

      </td>

  </tr><tr itemscope="" itemtype="http://schema.org/Book"><td width="5%" valign="top">
      <a name="5430955"/>
      <a href="/book/show/5430955-atlas-shrugged-part-b" title="Atlas Shrugged Part B: New Edition">
          <img alt="Atlas Shrugged Part B: New ..." class="bookSmallImg" src="http://d.gr-assets.com/books/1348469426s/5430955.jpg"/></a>    </td>
    <td width="100%" valign="top">
      <a href="/book/show/5430955-atlas-shrugged-part-b" class="bookTitle" itemprop="url">
        <span itemprop="name">Atlas Shrugged Part B: New Edition</span>
</a>      <br/><span class="by smallText">by</span>
<span itemprop="author" itemscope="" itemtype="http://schema.org/Person">
<a href="http://www.goodreads.com/author/show/432.Ayn_Rand" class="authorName" itemprop="url"><span itemprop="name">Ayn Rand</span></a>, 
<a href="http://www.goodreads.com/author/show/44554.Scott_Brick" class="authorName" itemprop="url"><span itemprop="name">Scott Brick</span></a> <span class="authorName greyText smallText role">(Narrator)</span>
</span>

        <br/><span class="greyText smallText uitext">
          <span class="minirating"><span class="stars"><img alt="3.93 of 5 stars" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.93 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.93 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.93 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/stars/red_star_66pct-a2f513494595fa112f4762672b33daef.png" title="3.93 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="3.93 of 5 stars" width="12"/></span> 3.93 avg rating &#8212; 28 ratings</span>
            &#8212;
            <a href="/work/editions/21836608-atlas-shrugged-part-b-new-edition" class="greyText" rel="nofollow">4 editions</a>
        </span>
        


    </td>

      <td width="130px">
          <div class="wtrButtonContainer wtrSignedOut" id="9_book_5430955">
<div class="wtrUp wtrLeft">
<form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="book_id" name="book_id" type="hidden" value="5430955"/><input id="name" name="name" type="hidden" value="to-read"/><input id="unique_id" name="unique_id" type="hidden" value="9_book_5430955"/><input id="wtr_new" name="wtr_new" type="hidden" value="true"/><button class="wtrToRead" type="submit">
<span class="progressTrigger">Want to Read</span>
<span class="progressIndicator">saving&#226;&#128;&#166;</span>
</button>
</form>

</div>

<div class="wtrDivider"/>
<div class="wtrRight">
<button class="wtrShelfButton wtrUp">
<img alt="pick shelf" src="http://s.gr-assets.com/assets/wtr_button/books-0866015891eb128cdc57e550383532a0.png"/></button>
<div class="wtrShelfMenu">
<ul class="wtrExclusiveShelves"><li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="9_book_5430955"/><input id="book_id" name="book_id" type="hidden" value="5430955"/><button class="wtrExclusiveShelf" name="name" type="submit" value="to-read">
<span class="progressTrigger">Want to Read</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="9_book_5430955"/><input id="book_id" name="book_id" type="hidden" value="5430955"/><button class="wtrExclusiveShelf" name="name" type="submit" value="currently-reading">
<span class="progressTrigger">Currently Reading</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="9_book_5430955"/><input id="book_id" name="book_id" type="hidden" value="5430955"/><button class="wtrExclusiveShelf" name="name" type="submit" value="read">
<span class="progressTrigger">Read</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
</ul></div>
</div>

<div class="ratingStars wtrRating">
<form accept-charset="UTF-8" action="/review/rate/5430955-atlas-shrugged-part-b" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<button class="greyText uitext myRating" disabled="disabled" name="button" type="submit">Rate this book</button>
<div class="clearRating uitext">Clear rating</div>
<input id="rating" name="rating" type="hidden" value="0"/><input id="wtr_button_id" name="wtr_button_id" type="hidden" value="9_book_5430955"/></form>

<span class="stars" id="starsstars_for_9_book_5430955" onmouseout="mouseOutStars('stars_for_9_book_5430955')"><a rel="nofollow"><img alt="didn't like it " class="star" height="15" id="starstars_for_9_book_5430955_0" onclick="submitStars('stars_for_9_book_5430955', 0, '/review/rate/5430955?rating=1&amp;wtr_button_id=9_book_5430955', 0);  return false;" onmouseover="checkStars('stars_for_9_book_5430955', 0)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="didn't like it" width="15"/></a><a rel="nofollow"><img alt="it was ok " class="star" height="15" id="starstars_for_9_book_5430955_1" onclick="submitStars('stars_for_9_book_5430955', 1, '/review/rate/5430955?rating=2&amp;wtr_button_id=9_book_5430955', 0);  return false;" onmouseover="checkStars('stars_for_9_book_5430955', 1)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was ok" width="15"/></a><a rel="nofollow"><img alt="liked it " class="star" height="15" id="starstars_for_9_book_5430955_2" onclick="submitStars('stars_for_9_book_5430955', 2, '/review/rate/5430955?rating=3&amp;wtr_button_id=9_book_5430955', 0);  return false;" onmouseover="checkStars('stars_for_9_book_5430955', 2)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="liked it" width="15"/></a><a rel="nofollow"><img alt="really liked it " class="star" height="15" id="starstars_for_9_book_5430955_3" onclick="submitStars('stars_for_9_book_5430955', 3, '/review/rate/5430955?rating=4&amp;wtr_button_id=9_book_5430955', 0);  return false;" onmouseover="checkStars('stars_for_9_book_5430955', 3)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="really liked it" width="15"/></a><a rel="nofollow"><img alt="it was amazing " class="star" height="15" id="starstars_for_9_book_5430955_4" onclick="submitStars('stars_for_9_book_5430955', 4, '/review/rate/5430955?rating=5&amp;wtr_button_id=9_book_5430955', 0);  return false;" onmouseover="checkStars('stars_for_9_book_5430955', 4)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was amazing" width="15"/></a></span><script language="javascript" type="text/javascript">starRatings[ratingIndex++] = [ 'stars_for_9_book_5430955', -1]; checkStars('stars_for_9_book_5430955', -1);</script></div>

</div>

      </td>

  </tr><tr itemscope="" itemtype="http://schema.org/Book"><td width="5%" valign="top">
      <a name="5141345"/>
      <a href="/book/show/5141345-atlas-shrugged-part-c" title="Atlas Shrugged Part C: New Edition">
          <img alt="Atlas Shrugged Part C: New ..." class="bookSmallImg" src="http://d.gr-assets.com/books/1348467302s/5141345.jpg"/></a>    </td>
    <td width="100%" valign="top">
      <a href="/book/show/5141345-atlas-shrugged-part-c" class="bookTitle" itemprop="url">
        <span itemprop="name">Atlas Shrugged Part C: New Edition</span>
</a>      <br/><span class="by smallText">by</span>
<span itemprop="author" itemscope="" itemtype="http://schema.org/Person">
<a href="http://www.goodreads.com/author/show/432.Ayn_Rand" class="authorName" itemprop="url"><span itemprop="name">Ayn Rand</span></a>
</span>

        <br/><span class="greyText smallText uitext">
          <span class="minirating"><span class="stars"><img alt="3.78 of 5 stars" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.78 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.78 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.78 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/stars/red_star_66pct-a2f513494595fa112f4762672b33daef.png" title="3.78 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="3.78 of 5 stars" width="12"/></span> 3.78 avg rating &#8212; 23 ratings</span>
            &#8212;
            <a href="/work/editions/21836609-atlas-shrugged-part-c-new-edition" class="greyText" rel="nofollow">4 editions</a>
        </span>
        


    </td>

      <td width="130px">
          <div class="wtrButtonContainer wtrSignedOut" id="10_book_5141345">
<div class="wtrUp wtrLeft">
<form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="book_id" name="book_id" type="hidden" value="5141345"/><input id="name" name="name" type="hidden" value="to-read"/><input id="unique_id" name="unique_id" type="hidden" value="10_book_5141345"/><input id="wtr_new" name="wtr_new" type="hidden" value="true"/><button class="wtrToRead" type="submit">
<span class="progressTrigger">Want to Read</span>
<span class="progressIndicator">saving&#226;&#128;&#166;</span>
</button>
</form>

</div>

<div class="wtrDivider"/>
<div class="wtrRight">
<button class="wtrShelfButton wtrUp">
<img alt="pick shelf" src="http://s.gr-assets.com/assets/wtr_button/books-0866015891eb128cdc57e550383532a0.png"/></button>
<div class="wtrShelfMenu">
<ul class="wtrExclusiveShelves"><li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="10_book_5141345"/><input id="book_id" name="book_id" type="hidden" value="5141345"/><button class="wtrExclusiveShelf" name="name" type="submit" value="to-read">
<span class="progressTrigger">Want to Read</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="10_book_5141345"/><input id="book_id" name="book_id" type="hidden" value="5141345"/><button class="wtrExclusiveShelf" name="name" type="submit" value="currently-reading">
<span class="progressTrigger">Currently Reading</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="10_book_5141345"/><input id="book_id" name="book_id" type="hidden" value="5141345"/><button class="wtrExclusiveShelf" name="name" type="submit" value="read">
<span class="progressTrigger">Read</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
</ul></div>
</div>

<div class="ratingStars wtrRating">
<form accept-charset="UTF-8" action="/review/rate/5141345-atlas-shrugged-part-c" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<button class="greyText uitext myRating" disabled="disabled" name="button" type="submit">Rate this book</button>
<div class="clearRating uitext">Clear rating</div>
<input id="rating" name="rating" type="hidden" value="0"/><input id="wtr_button_id" name="wtr_button_id" type="hidden" value="10_book_5141345"/></form>

<span class="stars" id="starsstars_for_10_book_5141345" onmouseout="mouseOutStars('stars_for_10_book_5141345')"><a rel="nofollow"><img alt="didn't like it " class="star" height="15" id="starstars_for_10_book_5141345_0" onclick="submitStars('stars_for_10_book_5141345', 0, '/review/rate/5141345?rating=1&amp;wtr_button_id=10_book_5141345', 0);  return false;" onmouseover="checkStars('stars_for_10_book_5141345', 0)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="didn't like it" width="15"/></a><a rel="nofollow"><img alt="it was ok " class="star" height="15" id="starstars_for_10_book_5141345_1" onclick="submitStars('stars_for_10_book_5141345', 1, '/review/rate/5141345?rating=2&amp;wtr_button_id=10_book_5141345', 0);  return false;" onmouseover="checkStars('stars_for_10_book_5141345', 1)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was ok" width="15"/></a><a rel="nofollow"><img alt="liked it " class="star" height="15" id="starstars_for_10_book_5141345_2" onclick="submitStars('stars_for_10_book_5141345', 2, '/review/rate/5141345?rating=3&amp;wtr_button_id=10_book_5141345', 0);  return false;" onmouseover="checkStars('stars_for_10_book_5141345', 2)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="liked it" width="15"/></a><a rel="nofollow"><img alt="really liked it " class="star" height="15" id="starstars_for_10_book_5141345_3" onclick="submitStars('stars_for_10_book_5141345', 3, '/review/rate/5141345?rating=4&amp;wtr_button_id=10_book_5141345', 0);  return false;" onmouseover="checkStars('stars_for_10_book_5141345', 3)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="really liked it" width="15"/></a><a rel="nofollow"><img alt="it was amazing " class="star" height="15" id="starstars_for_10_book_5141345_4" onclick="submitStars('stars_for_10_book_5141345', 4, '/review/rate/5141345?rating=5&amp;wtr_button_id=10_book_5141345', 0);  return false;" onmouseover="checkStars('stars_for_10_book_5141345', 4)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was amazing" width="15"/></a></span><script language="javascript" type="text/javascript">starRatings[ratingIndex++] = [ 'stars_for_10_book_5141345', -1]; checkStars('stars_for_10_book_5141345', -1);</script></div>

</div>

      </td>

  </tr><tr itemscope="" itemtype="http://schema.org/Book"><td width="5%" valign="top">
      <a name="9017523"/>
      <a href="/book/show/9017523-novels-by-ayn-rand" title="Novels by Ayn Rand: We the Living, Atlas Shrugged, the Fountainhead">
          <img alt="Novels by Ayn Rand: We the ..." class="bookSmallImg" src="http://d.gr-assets.com/books/1348368069s/9017523.jpg"/></a>    </td>
    <td width="100%" valign="top">
      <a href="/book/show/9017523-novels-by-ayn-rand" class="bookTitle" itemprop="url">
        <span itemprop="name">Novels by Ayn Rand: We the Living, Atlas Shrugged, the Fountainhead</span>
</a>      <br/><span class="by smallText">by</span>
<span itemprop="author" itemscope="" itemtype="http://schema.org/Person">
<a href="http://www.goodreads.com/author/show/4340042.Books_LLC" class="authorName" itemprop="url"><span itemprop="name">Books LLC</span></a>
</span>

        <br/><span class="greyText smallText uitext">
          <span class="minirating"><span class="stars"><img alt="4.5 of 5 stars" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.5 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.5 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.5 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.5 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/stars/red_star_66pct-a2f513494595fa112f4762672b33daef.png" title="4.5 of 5 stars" width="12"/></span> 4.50 avg rating &#8212; 16 ratings</span>
            &#8212;
              published
             2010
            &#8212;
            <a href="/work/editions/13895034-novels-by-ayn-rand-we-the-living-atlas-shrugged-the-fountainhead" class="greyText" rel="nofollow">1 edition</a>
        </span>
        


    </td>

      <td width="130px">
          <div class="wtrButtonContainer wtrSignedOut" id="11_book_9017523">
<div class="wtrUp wtrLeft">
<form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="book_id" name="book_id" type="hidden" value="9017523"/><input id="name" name="name" type="hidden" value="to-read"/><input id="unique_id" name="unique_id" type="hidden" value="11_book_9017523"/><input id="wtr_new" name="wtr_new" type="hidden" value="true"/><button class="wtrToRead" type="submit">
<span class="progressTrigger">Want to Read</span>
<span class="progressIndicator">saving&#226;&#128;&#166;</span>
</button>
</form>

</div>

<div class="wtrDivider"/>
<div class="wtrRight">
<button class="wtrShelfButton wtrUp">
<img alt="pick shelf" src="http://s.gr-assets.com/assets/wtr_button/books-0866015891eb128cdc57e550383532a0.png"/></button>
<div class="wtrShelfMenu">
<ul class="wtrExclusiveShelves"><li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="11_book_9017523"/><input id="book_id" name="book_id" type="hidden" value="9017523"/><button class="wtrExclusiveShelf" name="name" type="submit" value="to-read">
<span class="progressTrigger">Want to Read</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="11_book_9017523"/><input id="book_id" name="book_id" type="hidden" value="9017523"/><button class="wtrExclusiveShelf" name="name" type="submit" value="currently-reading">
<span class="progressTrigger">Currently Reading</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="11_book_9017523"/><input id="book_id" name="book_id" type="hidden" value="9017523"/><button class="wtrExclusiveShelf" name="name" type="submit" value="read">
<span class="progressTrigger">Read</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
</ul></div>
</div>

<div class="ratingStars wtrRating">
<form accept-charset="UTF-8" action="/review/rate/9017523-novels-by-ayn-rand" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<button class="greyText uitext myRating" disabled="disabled" name="button" type="submit">Rate this book</button>
<div class="clearRating uitext">Clear rating</div>
<input id="rating" name="rating" type="hidden" value="0"/><input id="wtr_button_id" name="wtr_button_id" type="hidden" value="11_book_9017523"/></form>

<span class="stars" id="starsstars_for_11_book_9017523" onmouseout="mouseOutStars('stars_for_11_book_9017523')"><a rel="nofollow"><img alt="didn't like it " class="star" height="15" id="starstars_for_11_book_9017523_0" onclick="submitStars('stars_for_11_book_9017523', 0, '/review/rate/9017523?rating=1&amp;wtr_button_id=11_book_9017523', 0);  return false;" onmouseover="checkStars('stars_for_11_book_9017523', 0)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="didn't like it" width="15"/></a><a rel="nofollow"><img alt="it was ok " class="star" height="15" id="starstars_for_11_book_9017523_1" onclick="submitStars('stars_for_11_book_9017523', 1, '/review/rate/9017523?rating=2&amp;wtr_button_id=11_book_9017523', 0);  return false;" onmouseover="checkStars('stars_for_11_book_9017523', 1)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was ok" width="15"/></a><a rel="nofollow"><img alt="liked it " class="star" height="15" id="starstars_for_11_book_9017523_2" onclick="submitStars('stars_for_11_book_9017523', 2, '/review/rate/9017523?rating=3&amp;wtr_button_id=11_book_9017523', 0);  return false;" onmouseover="checkStars('stars_for_11_book_9017523', 2)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="liked it" width="15"/></a><a rel="nofollow"><img alt="really liked it " class="star" height="15" id="starstars_for_11_book_9017523_3" onclick="submitStars('stars_for_11_book_9017523', 3, '/review/rate/9017523?rating=4&amp;wtr_button_id=11_book_9017523', 0);  return false;" onmouseover="checkStars('stars_for_11_book_9017523', 3)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="really liked it" width="15"/></a><a rel="nofollow"><img alt="it was amazing " class="star" height="15" id="starstars_for_11_book_9017523_4" onclick="submitStars('stars_for_11_book_9017523', 4, '/review/rate/9017523?rating=5&amp;wtr_button_id=11_book_9017523', 0);  return false;" onmouseover="checkStars('stars_for_11_book_9017523', 4)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was amazing" width="15"/></a></span><script language="javascript" type="text/javascript">starRatings[ratingIndex++] = [ 'stars_for_11_book_9017523', -1]; checkStars('stars_for_11_book_9017523', -1);</script></div>

</div>

      </td>

  </tr><tr itemscope="" itemtype="http://schema.org/Book"><td width="5%" valign="top">
      <a name="181147"/>
      <a href="/book/show/181147.Atlas_Shrugged" title="Atlas Shrugged">
          <img alt="Atlas Shrugged (SparkNotes ..." class="bookSmallImg" src="http://d.gr-assets.com/books/1328853108s/181147.jpg"/></a>    </td>
    <td width="100%" valign="top">
      <a href="/book/show/181147.Atlas_Shrugged" class="bookTitle" itemprop="url">
        <span itemprop="name">Atlas Shrugged (SparkNotes Literature Guides)</span>
</a>      <br/><span class="by smallText">by</span>
<span itemprop="author" itemscope="" itemtype="http://schema.org/Person">
<a href="http://www.goodreads.com/author/show/6460726.SparkNotes_Editors" class="authorName" itemprop="url"><span itemprop="name">SparkNotes Editors</span></a>, 
<a href="http://www.goodreads.com/author/show/432.Ayn_Rand" class="authorName" itemprop="url"><span itemprop="name">Ayn Rand</span></a>, <a href="http://www.goodreads.com/author/show/2904509.SparkNotes" class="authorName" itemprop="url"><span itemprop="name">SparkNotes</span></a>
</span>

        <br/><span class="greyText smallText uitext">
          <span class="minirating"><span class="stars"><img alt="4.25 of 5 stars" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.25 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.25 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.25 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.25 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/stars/red_star_33pct-69a219b6d79a91503f292bf5ac039d6b.png" title="4.25 of 5 stars" width="12"/></span> 4.25 avg rating &#8212; 8 ratings</span>
            &#8212;
              published
             2003
            &#8212;
            <a href="/work/editions/175035-spark-notes-atlas-shrugged-sparknotes-literature-guides" class="greyText" rel="nofollow">3 editions</a>
        </span>
        


    </td>

      <td width="130px">
          <div class="wtrButtonContainer wtrSignedOut" id="12_book_181147">
<div class="wtrUp wtrLeft">
<form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="book_id" name="book_id" type="hidden" value="181147"/><input id="name" name="name" type="hidden" value="to-read"/><input id="unique_id" name="unique_id" type="hidden" value="12_book_181147"/><input id="wtr_new" name="wtr_new" type="hidden" value="true"/><button class="wtrToRead" type="submit">
<span class="progressTrigger">Want to Read</span>
<span class="progressIndicator">saving&#226;&#128;&#166;</span>
</button>
</form>

</div>

<div class="wtrDivider"/>
<div class="wtrRight">
<button class="wtrShelfButton wtrUp">
<img alt="pick shelf" src="http://s.gr-assets.com/assets/wtr_button/books-0866015891eb128cdc57e550383532a0.png"/></button>
<div class="wtrShelfMenu">
<ul class="wtrExclusiveShelves"><li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="12_book_181147"/><input id="book_id" name="book_id" type="hidden" value="181147"/><button class="wtrExclusiveShelf" name="name" type="submit" value="to-read">
<span class="progressTrigger">Want to Read</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="12_book_181147"/><input id="book_id" name="book_id" type="hidden" value="181147"/><button class="wtrExclusiveShelf" name="name" type="submit" value="currently-reading">
<span class="progressTrigger">Currently Reading</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="12_book_181147"/><input id="book_id" name="book_id" type="hidden" value="181147"/><button class="wtrExclusiveShelf" name="name" type="submit" value="read">
<span class="progressTrigger">Read</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
</ul></div>
</div>

<div class="ratingStars wtrRating">
<form accept-charset="UTF-8" action="/review/rate/181147.Atlas_Shrugged" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<button class="greyText uitext myRating" disabled="disabled" name="button" type="submit">Rate this book</button>
<div class="clearRating uitext">Clear rating</div>
<input id="rating" name="rating" type="hidden" value="0"/><input id="wtr_button_id" name="wtr_button_id" type="hidden" value="12_book_181147"/></form>

<span class="stars" id="starsstars_for_12_book_181147" onmouseout="mouseOutStars('stars_for_12_book_181147')"><a rel="nofollow"><img alt="didn't like it " class="star" height="15" id="starstars_for_12_book_181147_0" onclick="submitStars('stars_for_12_book_181147', 0, '/review/rate/181147?rating=1&amp;wtr_button_id=12_book_181147', 0);  return false;" onmouseover="checkStars('stars_for_12_book_181147', 0)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="didn't like it" width="15"/></a><a rel="nofollow"><img alt="it was ok " class="star" height="15" id="starstars_for_12_book_181147_1" onclick="submitStars('stars_for_12_book_181147', 1, '/review/rate/181147?rating=2&amp;wtr_button_id=12_book_181147', 0);  return false;" onmouseover="checkStars('stars_for_12_book_181147', 1)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was ok" width="15"/></a><a rel="nofollow"><img alt="liked it " class="star" height="15" id="starstars_for_12_book_181147_2" onclick="submitStars('stars_for_12_book_181147', 2, '/review/rate/181147?rating=3&amp;wtr_button_id=12_book_181147', 0);  return false;" onmouseover="checkStars('stars_for_12_book_181147', 2)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="liked it" width="15"/></a><a rel="nofollow"><img alt="really liked it " class="star" height="15" id="starstars_for_12_book_181147_3" onclick="submitStars('stars_for_12_book_181147', 3, '/review/rate/181147?rating=4&amp;wtr_button_id=12_book_181147', 0);  return false;" onmouseover="checkStars('stars_for_12_book_181147', 3)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="really liked it" width="15"/></a><a rel="nofollow"><img alt="it was amazing " class="star" height="15" id="starstars_for_12_book_181147_4" onclick="submitStars('stars_for_12_book_181147', 4, '/review/rate/181147?rating=5&amp;wtr_button_id=12_book_181147', 0);  return false;" onmouseover="checkStars('stars_for_12_book_181147', 4)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was amazing" width="15"/></a></span><script language="javascript" type="text/javascript">starRatings[ratingIndex++] = [ 'stars_for_12_book_181147', -1]; checkStars('stars_for_12_book_181147', -1);</script></div>

</div>

      </td>

  </tr><tr itemscope="" itemtype="http://schema.org/Book"><td width="5%" valign="top">
      <a name="16135783"/>
      <a href="/book/show/16135783-atlas-shrugged" title="Atlas Shrugged">
          <img alt="Atlas Shrugged" class="bookSmallImg" src="http://www.goodreads.com/assets/nocover/60x80.png"/></a>    </td>
    <td width="100%" valign="top">
      <a href="/book/show/16135783-atlas-shrugged" class="bookTitle" itemprop="url">
        <span itemprop="name">Atlas Shrugged</span>
</a>      <br/><span class="by smallText">by</span>
<span itemprop="author" itemscope="" itemtype="http://schema.org/Person">
<a href="http://www.goodreads.com/author/show/432.Ayn_Rand" class="authorName" itemprop="url"><span itemprop="name">Ayn Rand</span></a>
</span>

        <br/><span class="greyText smallText uitext">
          <span class="minirating"><span class="stars"><img alt="0.0 of 5 stars" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="0.0 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="0.0 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="0.0 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="0.0 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="0.0 of 5 stars" width="12"/></span> 0.00 avg rating &#8212; 0 ratings</span>
            &#8212;
              published
             1957
            &#8212;
            <a href="/work/editions/21963920-atlas-shrugged" class="greyText" rel="nofollow">1 edition</a>
        </span>
        


    </td>

      <td width="130px">
          <div class="wtrButtonContainer wtrSignedOut" id="13_book_16135783">
<div class="wtrUp wtrLeft">
<form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="book_id" name="book_id" type="hidden" value="16135783"/><input id="name" name="name" type="hidden" value="to-read"/><input id="unique_id" name="unique_id" type="hidden" value="13_book_16135783"/><input id="wtr_new" name="wtr_new" type="hidden" value="true"/><button class="wtrToRead" type="submit">
<span class="progressTrigger">Want to Read</span>
<span class="progressIndicator">saving&#226;&#128;&#166;</span>
</button>
</form>

</div>

<div class="wtrDivider"/>
<div class="wtrRight">
<button class="wtrShelfButton wtrUp">
<img alt="pick shelf" src="http://s.gr-assets.com/assets/wtr_button/books-0866015891eb128cdc57e550383532a0.png"/></button>
<div class="wtrShelfMenu">
<ul class="wtrExclusiveShelves"><li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="13_book_16135783"/><input id="book_id" name="book_id" type="hidden" value="16135783"/><button class="wtrExclusiveShelf" name="name" type="submit" value="to-read">
<span class="progressTrigger">Want to Read</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="13_book_16135783"/><input id="book_id" name="book_id" type="hidden" value="16135783"/><button class="wtrExclusiveShelf" name="name" type="submit" value="currently-reading">
<span class="progressTrigger">Currently Reading</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="13_book_16135783"/><input id="book_id" name="book_id" type="hidden" value="16135783"/><button class="wtrExclusiveShelf" name="name" type="submit" value="read">
<span class="progressTrigger">Read</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
</ul></div>
</div>

<div class="ratingStars wtrRating">
<form accept-charset="UTF-8" action="/review/rate/16135783-atlas-shrugged" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<button class="greyText uitext myRating" disabled="disabled" name="button" type="submit">Rate this book</button>
<div class="clearRating uitext">Clear rating</div>
<input id="rating" name="rating" type="hidden" value="0"/><input id="wtr_button_id" name="wtr_button_id" type="hidden" value="13_book_16135783"/></form>

<span class="stars" id="starsstars_for_13_book_16135783" onmouseout="mouseOutStars('stars_for_13_book_16135783')"><a rel="nofollow"><img alt="didn't like it " class="star" height="15" id="starstars_for_13_book_16135783_0" onclick="submitStars('stars_for_13_book_16135783', 0, '/review/rate/16135783?rating=1&amp;wtr_button_id=13_book_16135783', 0);  return false;" onmouseover="checkStars('stars_for_13_book_16135783', 0)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="didn't like it" width="15"/></a><a rel="nofollow"><img alt="it was ok " class="star" height="15" id="starstars_for_13_book_16135783_1" onclick="submitStars('stars_for_13_book_16135783', 1, '/review/rate/16135783?rating=2&amp;wtr_button_id=13_book_16135783', 0);  return false;" onmouseover="checkStars('stars_for_13_book_16135783', 1)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was ok" width="15"/></a><a rel="nofollow"><img alt="liked it " class="star" height="15" id="starstars_for_13_book_16135783_2" onclick="submitStars('stars_for_13_book_16135783', 2, '/review/rate/16135783?rating=3&amp;wtr_button_id=13_book_16135783', 0);  return false;" onmouseover="checkStars('stars_for_13_book_16135783', 2)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="liked it" width="15"/></a><a rel="nofollow"><img alt="really liked it " class="star" height="15" id="starstars_for_13_book_16135783_3" onclick="submitStars('stars_for_13_book_16135783', 3, '/review/rate/16135783?rating=4&amp;wtr_button_id=13_book_16135783', 0);  return false;" onmouseover="checkStars('stars_for_13_book_16135783', 3)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="really liked it" width="15"/></a><a rel="nofollow"><img alt="it was amazing " class="star" height="15" id="starstars_for_13_book_16135783_4" onclick="submitStars('stars_for_13_book_16135783', 4, '/review/rate/16135783?rating=5&amp;wtr_button_id=13_book_16135783', 0);  return false;" onmouseover="checkStars('stars_for_13_book_16135783', 4)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was amazing" width="15"/></a></span><script language="javascript" type="text/javascript">starRatings[ratingIndex++] = [ 'stars_for_13_book_16135783', -1]; checkStars('stars_for_13_book_16135783', -1);</script></div>

</div>

      </td>

  </tr><tr itemscope="" itemtype="http://schema.org/Book"><td width="5%" valign="top">
      <a name="9577604"/>
      <a href="/book/show/9577604-why-businessmen-need-philosophy" title="Why Businessmen Need Philosophy: The Capitalist's Guide to the Ideas Behind Ayn Rand's AtlasShrugged">
          <img alt="Why Businessmen Need Philos..." class="bookSmallImg" src="http://d.gr-assets.com/books/1347770922s/9577604.jpg"/></a>    </td>
    <td width="100%" valign="top">
      <a href="/book/show/9577604-why-businessmen-need-philosophy" class="bookTitle" itemprop="url">
        <span itemprop="name">Why Businessmen Need Philosophy: The Capitalist's Guide to the Ideas Behind Ayn Rand's AtlasShrugged</span>
</a>      <br/><span class="by smallText">by</span>
<span itemprop="author" itemscope="" itemtype="http://schema.org/Person">
<a href="http://www.goodreads.com/author/show/89107.Richard_E_Ralston" class="authorName" itemprop="url"><span itemprop="name">Richard E. Ralston</span></a> <span class="authorName greyText smallText role">(Editor)</span>, 
<a href="http://www.goodreads.com/author/show/5145756.John_A_Allison" class="authorName" itemprop="url"><span itemprop="name">John A. Allison</span></a> <span class="authorName greyText smallText role">(Introduction)</span>
</span>

        <br/><span class="greyText smallText uitext">
          <span class="minirating"><span class="stars"><img alt="4.08 of 5 stars" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.08 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.08 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.08 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.08 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/stars/red_star_33pct-69a219b6d79a91503f292bf5ac039d6b.png" title="4.08 of 5 stars" width="12"/></span> 4.08 avg rating &#8212; 12 ratings</span>
            &#8212;
              published
             2011
            &#8212;
            <a href="/work/editions/14464481-why-businessmen-need-philosophy-the-capitalist-s-guide-to-the-ideas-beh" class="greyText" rel="nofollow">3 editions</a>
        </span>
        


    </td>

      <td width="130px">
          <div class="wtrButtonContainer wtrSignedOut" id="14_book_9577604">
<div class="wtrUp wtrLeft">
<form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="book_id" name="book_id" type="hidden" value="9577604"/><input id="name" name="name" type="hidden" value="to-read"/><input id="unique_id" name="unique_id" type="hidden" value="14_book_9577604"/><input id="wtr_new" name="wtr_new" type="hidden" value="true"/><button class="wtrToRead" type="submit">
<span class="progressTrigger">Want to Read</span>
<span class="progressIndicator">saving&#226;&#128;&#166;</span>
</button>
</form>

</div>

<div class="wtrDivider"/>
<div class="wtrRight">
<button class="wtrShelfButton wtrUp">
<img alt="pick shelf" src="http://s.gr-assets.com/assets/wtr_button/books-0866015891eb128cdc57e550383532a0.png"/></button>
<div class="wtrShelfMenu">
<ul class="wtrExclusiveShelves"><li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="14_book_9577604"/><input id="book_id" name="book_id" type="hidden" value="9577604"/><button class="wtrExclusiveShelf" name="name" type="submit" value="to-read">
<span class="progressTrigger">Want to Read</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="14_book_9577604"/><input id="book_id" name="book_id" type="hidden" value="9577604"/><button class="wtrExclusiveShelf" name="name" type="submit" value="currently-reading">
<span class="progressTrigger">Currently Reading</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="14_book_9577604"/><input id="book_id" name="book_id" type="hidden" value="9577604"/><button class="wtrExclusiveShelf" name="name" type="submit" value="read">
<span class="progressTrigger">Read</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
</ul></div>
</div>

<div class="ratingStars wtrRating">
<form accept-charset="UTF-8" action="/review/rate/9577604-why-businessmen-need-philosophy" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<button class="greyText uitext myRating" disabled="disabled" name="button" type="submit">Rate this book</button>
<div class="clearRating uitext">Clear rating</div>
<input id="rating" name="rating" type="hidden" value="0"/><input id="wtr_button_id" name="wtr_button_id" type="hidden" value="14_book_9577604"/></form>

<span class="stars" id="starsstars_for_14_book_9577604" onmouseout="mouseOutStars('stars_for_14_book_9577604')"><a rel="nofollow"><img alt="didn't like it " class="star" height="15" id="starstars_for_14_book_9577604_0" onclick="submitStars('stars_for_14_book_9577604', 0, '/review/rate/9577604?rating=1&amp;wtr_button_id=14_book_9577604', 0);  return false;" onmouseover="checkStars('stars_for_14_book_9577604', 0)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="didn't like it" width="15"/></a><a rel="nofollow"><img alt="it was ok " class="star" height="15" id="starstars_for_14_book_9577604_1" onclick="submitStars('stars_for_14_book_9577604', 1, '/review/rate/9577604?rating=2&amp;wtr_button_id=14_book_9577604', 0);  return false;" onmouseover="checkStars('stars_for_14_book_9577604', 1)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was ok" width="15"/></a><a rel="nofollow"><img alt="liked it " class="star" height="15" id="starstars_for_14_book_9577604_2" onclick="submitStars('stars_for_14_book_9577604', 2, '/review/rate/9577604?rating=3&amp;wtr_button_id=14_book_9577604', 0);  return false;" onmouseover="checkStars('stars_for_14_book_9577604', 2)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="liked it" width="15"/></a><a rel="nofollow"><img alt="really liked it " class="star" height="15" id="starstars_for_14_book_9577604_3" onclick="submitStars('stars_for_14_book_9577604', 3, '/review/rate/9577604?rating=4&amp;wtr_button_id=14_book_9577604', 0);  return false;" onmouseover="checkStars('stars_for_14_book_9577604', 3)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="really liked it" width="15"/></a><a rel="nofollow"><img alt="it was amazing " class="star" height="15" id="starstars_for_14_book_9577604_4" onclick="submitStars('stars_for_14_book_9577604', 4, '/review/rate/9577604?rating=5&amp;wtr_button_id=14_book_9577604', 0);  return false;" onmouseover="checkStars('stars_for_14_book_9577604', 4)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was amazing" width="15"/></a></span><script language="javascript" type="text/javascript">starRatings[ratingIndex++] = [ 'stars_for_14_book_9577604', -1]; checkStars('stars_for_14_book_9577604', -1);</script></div>

</div>

      </td>

  </tr><tr itemscope="" itemtype="http://schema.org/Book"><td width="5%" valign="top">
      <a name="9935187"/>
      <a href="/book/show/9935187-works-by-ayn-rand-book-guide" title="Works by Ayn Rand (Book Guide): Ayn Rand Characters, Books by Ayn Rand, Novels by Ayn Rand, Plays by Ayn Rand, We the Living, Atlas Shrugged">
          <img alt="Works by Ayn Rand (Book Gui..." class="bookSmallImg" src="http://d.gr-assets.com/books/1347935031s/9935187.jpg"/></a>    </td>
    <td width="100%" valign="top">
      <a href="/book/show/9935187-works-by-ayn-rand-book-guide" class="bookTitle" itemprop="url">
        <span itemprop="name">Works by Ayn Rand (Book Guide): Ayn Rand Characters, Books by Ayn Rand, Novels by Ayn Rand, Plays by Ayn Rand, We the Living, Atlas Shrugged</span>
</a>      <br/><span class="by smallText">by</span>
<span itemprop="author" itemscope="" itemtype="http://schema.org/Person">
<a href="http://www.goodreads.com/author/show/5153555.Source_Wikipedia" class="authorName" itemprop="url"><span itemprop="name">Source Wikipedia</span></a>
</span>

        <br/><span class="greyText smallText uitext">
          <span class="minirating"><span class="stars"><img alt="5.0 of 5 stars" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="5.0 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="5.0 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="5.0 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="5.0 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="5.0 of 5 stars" width="12"/></span> 5.00 avg rating &#8212; 1 rating</span>
            &#8212;
              published
             2010
            &#8212;
            <a href="/work/editions/14828345-works-by-ayn-rand-book-guide-ayn-rand-characters-books-by-ayn-rand" class="greyText" rel="nofollow">1 edition</a>
        </span>
        


    </td>

      <td width="130px">
          <div class="wtrButtonContainer wtrSignedOut" id="15_book_9935187">
<div class="wtrUp wtrLeft">
<form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="book_id" name="book_id" type="hidden" value="9935187"/><input id="name" name="name" type="hidden" value="to-read"/><input id="unique_id" name="unique_id" type="hidden" value="15_book_9935187"/><input id="wtr_new" name="wtr_new" type="hidden" value="true"/><button class="wtrToRead" type="submit">
<span class="progressTrigger">Want to Read</span>
<span class="progressIndicator">saving&#226;&#128;&#166;</span>
</button>
</form>

</div>

<div class="wtrDivider"/>
<div class="wtrRight">
<button class="wtrShelfButton wtrUp">
<img alt="pick shelf" src="http://s.gr-assets.com/assets/wtr_button/books-0866015891eb128cdc57e550383532a0.png"/></button>
<div class="wtrShelfMenu">
<ul class="wtrExclusiveShelves"><li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="15_book_9935187"/><input id="book_id" name="book_id" type="hidden" value="9935187"/><button class="wtrExclusiveShelf" name="name" type="submit" value="to-read">
<span class="progressTrigger">Want to Read</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="15_book_9935187"/><input id="book_id" name="book_id" type="hidden" value="9935187"/><button class="wtrExclusiveShelf" name="name" type="submit" value="currently-reading">
<span class="progressTrigger">Currently Reading</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="15_book_9935187"/><input id="book_id" name="book_id" type="hidden" value="9935187"/><button class="wtrExclusiveShelf" name="name" type="submit" value="read">
<span class="progressTrigger">Read</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
</ul></div>
</div>

<div class="ratingStars wtrRating">
<form accept-charset="UTF-8" action="/review/rate/9935187-works-by-ayn-rand-book-guide" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<button class="greyText uitext myRating" disabled="disabled" name="button" type="submit">Rate this book</button>
<div class="clearRating uitext">Clear rating</div>
<input id="rating" name="rating" type="hidden" value="0"/><input id="wtr_button_id" name="wtr_button_id" type="hidden" value="15_book_9935187"/></form>

<span class="stars" id="starsstars_for_15_book_9935187" onmouseout="mouseOutStars('stars_for_15_book_9935187')"><a rel="nofollow"><img alt="didn't like it " class="star" height="15" id="starstars_for_15_book_9935187_0" onclick="submitStars('stars_for_15_book_9935187', 0, '/review/rate/9935187?rating=1&amp;wtr_button_id=15_book_9935187', 0);  return false;" onmouseover="checkStars('stars_for_15_book_9935187', 0)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="didn't like it" width="15"/></a><a rel="nofollow"><img alt="it was ok " class="star" height="15" id="starstars_for_15_book_9935187_1" onclick="submitStars('stars_for_15_book_9935187', 1, '/review/rate/9935187?rating=2&amp;wtr_button_id=15_book_9935187', 0);  return false;" onmouseover="checkStars('stars_for_15_book_9935187', 1)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was ok" width="15"/></a><a rel="nofollow"><img alt="liked it " class="star" height="15" id="starstars_for_15_book_9935187_2" onclick="submitStars('stars_for_15_book_9935187', 2, '/review/rate/9935187?rating=3&amp;wtr_button_id=15_book_9935187', 0);  return false;" onmouseover="checkStars('stars_for_15_book_9935187', 2)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="liked it" width="15"/></a><a rel="nofollow"><img alt="really liked it " class="star" height="15" id="starstars_for_15_book_9935187_3" onclick="submitStars('stars_for_15_book_9935187', 3, '/review/rate/9935187?rating=4&amp;wtr_button_id=15_book_9935187', 0);  return false;" onmouseover="checkStars('stars_for_15_book_9935187', 3)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="really liked it" width="15"/></a><a rel="nofollow"><img alt="it was amazing " class="star" height="15" id="starstars_for_15_book_9935187_4" onclick="submitStars('stars_for_15_book_9935187', 4, '/review/rate/9935187?rating=5&amp;wtr_button_id=15_book_9935187', 0);  return false;" onmouseover="checkStars('stars_for_15_book_9935187', 4)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was amazing" width="15"/></a></span><script language="javascript" type="text/javascript">starRatings[ratingIndex++] = [ 'stars_for_15_book_9935187', -1]; checkStars('stars_for_15_book_9935187', -1);</script></div>

</div>

      </td>

  </tr><tr itemscope="" itemtype="http://schema.org/Book"><td width="5%" valign="top">
      <a name="12716520"/>
      <a href="/book/show/12716520-articles-on-novels-by-ayn-rand-including" title="Articles on Novels by Ayn Rand, Including: The Fountainhead, Anthem (Novella), We the Living, Atlas Shrugged">
          <img alt="Articles on Novels by Ayn R..." class="bookSmallImg" src="http://d.gr-assets.com/books/1348641370s/12716520.jpg"/></a>    </td>
    <td width="100%" valign="top">
      <a href="/book/show/12716520-articles-on-novels-by-ayn-rand-including" class="bookTitle" itemprop="url">
        <span itemprop="name">Articles on Novels by Ayn Rand, Including: The Fountainhead, Anthem (Novella), We the Living, Atlas Shrugged</span>
</a>      <br/><span class="by smallText">by</span>
<span itemprop="author" itemscope="" itemtype="http://schema.org/Person">
<a href="http://www.goodreads.com/author/show/5167894.Hephaestus_Books" class="authorName" itemprop="url"><span itemprop="name">Hephaestus Books</span></a>
</span>

        <br/><span class="greyText smallText uitext">
          <span class="minirating"><span class="stars"><img alt="3.0 of 5 stars" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.0 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.0 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.0 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="3.0 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="3.0 of 5 stars" width="12"/></span> 3.00 avg rating &#8212; 1 rating</span>
            &#8212;
              published
             2011
            &#8212;
            <a href="/work/editions/17851307-articles-on-novels-by-ayn-rand-including-the-fountainhead-anthem-nov" class="greyText" rel="nofollow">1 edition</a>
        </span>
        


    </td>

      <td width="130px">
          <div class="wtrButtonContainer wtrSignedOut" id="16_book_12716520">
<div class="wtrUp wtrLeft">
<form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="book_id" name="book_id" type="hidden" value="12716520"/><input id="name" name="name" type="hidden" value="to-read"/><input id="unique_id" name="unique_id" type="hidden" value="16_book_12716520"/><input id="wtr_new" name="wtr_new" type="hidden" value="true"/><button class="wtrToRead" type="submit">
<span class="progressTrigger">Want to Read</span>
<span class="progressIndicator">saving&#226;&#128;&#166;</span>
</button>
</form>

</div>

<div class="wtrDivider"/>
<div class="wtrRight">
<button class="wtrShelfButton wtrUp">
<img alt="pick shelf" src="http://s.gr-assets.com/assets/wtr_button/books-0866015891eb128cdc57e550383532a0.png"/></button>
<div class="wtrShelfMenu">
<ul class="wtrExclusiveShelves"><li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="16_book_12716520"/><input id="book_id" name="book_id" type="hidden" value="12716520"/><button class="wtrExclusiveShelf" name="name" type="submit" value="to-read">
<span class="progressTrigger">Want to Read</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="16_book_12716520"/><input id="book_id" name="book_id" type="hidden" value="12716520"/><button class="wtrExclusiveShelf" name="name" type="submit" value="currently-reading">
<span class="progressTrigger">Currently Reading</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
<li><form accept-charset="UTF-8" action="/shelf/add_to_shelf" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<input id="unique_id" name="unique_id" type="hidden" value="16_book_12716520"/><input id="book_id" name="book_id" type="hidden" value="12716520"/><button class="wtrExclusiveShelf" name="name" type="submit" value="read">
<span class="progressTrigger">Read</span>
<img alt="saving&#226;&#128;&#166;" class="progressIndicator" src="http://s.gr-assets.com/assets/loading-trans-faf9fc8d53f8134c4979aa23b4e116ad.gif"/></button>
</form>

</li>
</ul></div>
</div>

<div class="ratingStars wtrRating">
<form accept-charset="UTF-8" action="/review/rate/12716520-articles-on-novels-by-ayn-rand-including" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#10003;"/><input name="authenticity_token" type="hidden" value="FMCi9QdW7f6HHsUaAeUh0kEBbgDzbzzrS/yFqPAgdXA="/></div>
<button class="greyText uitext myRating" disabled="disabled" name="button" type="submit">Rate this book</button>
<div class="clearRating uitext">Clear rating</div>
<input id="rating" name="rating" type="hidden" value="0"/><input id="wtr_button_id" name="wtr_button_id" type="hidden" value="16_book_12716520"/></form>

<span class="stars" id="starsstars_for_16_book_12716520" onmouseout="mouseOutStars('stars_for_16_book_12716520')"><a rel="nofollow"><img alt="didn't like it " class="star" height="15" id="starstars_for_16_book_12716520_0" onclick="submitStars('stars_for_16_book_12716520', 0, '/review/rate/12716520?rating=1&amp;wtr_button_id=16_book_12716520', 0);  return false;" onmouseover="checkStars('stars_for_16_book_12716520', 0)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="didn't like it" width="15"/></a><a rel="nofollow"><img alt="it was ok " class="star" height="15" id="starstars_for_16_book_12716520_1" onclick="submitStars('stars_for_16_book_12716520', 1, '/review/rate/12716520?rating=2&amp;wtr_button_id=16_book_12716520', 0);  return false;" onmouseover="checkStars('stars_for_16_book_12716520', 1)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was ok" width="15"/></a><a rel="nofollow"><img alt="liked it " class="star" height="15" id="starstars_for_16_book_12716520_2" onclick="submitStars('stars_for_16_book_12716520', 2, '/review/rate/12716520?rating=3&amp;wtr_button_id=16_book_12716520', 0);  return false;" onmouseover="checkStars('stars_for_16_book_12716520', 2)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="liked it" width="15"/></a><a rel="nofollow"><img alt="really liked it " class="star" height="15" id="starstars_for_16_book_12716520_3" onclick="submitStars('stars_for_16_book_12716520', 3, '/review/rate/12716520?rating=4&amp;wtr_button_id=16_book_12716520', 0);  return false;" onmouseover="checkStars('stars_for_16_book_12716520', 3)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="really liked it" width="15"/></a><a rel="nofollow"><img alt="it was amazing " class="star" height="15" id="starstars_for_16_book_12716520_4" onclick="submitStars('stars_for_16_book_12716520', 4, '/review/rate/12716520?rating=5&amp;wtr_button_id=16_book_12716520', 0);  return false;" onmouseover="checkStars('stars_for_16_book_12716520', 4)" src="http://s.gr-assets.com/assets/layout/gr_orange_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="it was amazing" width="15"/></a></span><script language="javascript" type="text/javascript">starRatings[ratingIndex++] = [ 'stars_for_16_book_12716520', -1]; checkStars('stars_for_16_book_12716520', -1);</script></div>

</div>

      </td>

  </tr></table><br/><div style="float: right">
      

    </div>
      <div id="adcontainer2"/>
    <br/><br/><br/><br/></div>

<div class="rightContainer">
  <br/><a href="/book/new?book%5Btitle%5D=atlas+shrugged+ayn+rand" class="actionLinkLite" rel="nofollow">Manually add a book</a><br/><a href="/review/import" class="actionLinkLite" rel="nofollow">Import books</a><br/><br/><script language="JavaScript">
    GA_googleAddSlot("ca-pub-7284881071421289", "Search")
  </script><script language="JavaScript">
    GA_googleFetchAds()
  </script><script language="JavaScript">
    GA_googleFillSlot("Search")
  </script><div id="self_serve_ads"/>
    <br/><div class=" clearFloats bigBox"><div class="h2Container gradientHeaderContainer"><h2 class="brownBackground"><a href="/shelf/top_shelves">Related Shelves</a></h2></div><div class="bigBoxBody"><div class="bigBoxContent containerWithHeaderContent">
            <a href="/shelf/show/to-read" class="actionLinkLite" style="font-size: 1.1em">to-read</a> <span class="greyText smallText">(63,960,851)</span><br/><a href="/shelf/show/currently-reading" class="actionLinkLite" style="font-size: 1.1em">currently-reading</a> <span class="greyText smallText">(20,886,739)</span><br/><a href="/shelf/show/favorites" class="actionLinkLite" style="font-size: 1.1em">favorites</a> <span class="greyText smallText">(1,284,728)</span><br/><a href="/shelf/show/fiction" class="actionLinkLite" style="font-size: 1.1em">fiction</a> <span class="greyText smallText">(1,274,066)</span><br/><a href="/shelf/show/fantasy" class="actionLinkLite" style="font-size: 1.1em">fantasy</a> <span class="greyText smallText">(1,011,448)</span><br/><a href="/shelf/show/own" class="actionLinkLite" style="font-size: 1.1em">own</a> <span class="greyText smallText">(937,058)</span><br/><a href="/shelf/show/wishlist" class="actionLinkLite" style="font-size: 1.1em">wishlist</a> <span class="greyText smallText">(884,426)</span><br/><a href="/shelf/show/2012" class="actionLinkLite" style="font-size: 1.1em">2012</a> <span class="greyText smallText">(744,412)</span><br/><a href="/shelf/show/owned" class="actionLinkLite" style="font-size: 1.1em">owned</a> <span class="greyText smallText">(561,798)</span><br/><a href="/shelf/show/books-i-own" class="actionLinkLite" style="font-size: 1.1em">books-i-own</a> <span class="greyText smallText">(556,647)</span><br/><a href="/shelf/show/kindle" class="actionLinkLite" style="font-size: 1.1em">kindle</a> <span class="greyText smallText">(436,827)</span><br/><a href="/shelf/show/library" class="actionLinkLite" style="font-size: 1.1em">library</a> <span class="greyText smallText">(425,783)</span><br/><a href="/shelf/show/wish-list" class="actionLinkLite" style="font-size: 1.1em">wish-list</a> <span class="greyText smallText">(412,333)</span><br/><a href="/shelf/show/classics" class="actionLinkLite" style="font-size: 1.1em">classics</a> <span class="greyText smallText">(398,325)</span><br/><a href="/shelf/show/to-buy" class="actionLinkLite" style="font-size: 1.1em">to-buy</a> <span class="greyText smallText">(385,283)</span><br/><a href="/shelf/show/2011" class="actionLinkLite" style="font-size: 1.1em">2011</a> <span class="greyText smallText">(290,333)</span><br/><a href="/shelf/show/science-fiction" class="actionLinkLite" style="font-size: 1.1em">science-fiction</a> <span class="greyText smallText">(283,966)</span><br/><a href="/shelf/show/adult" class="actionLinkLite" style="font-size: 1.1em">adult</a> <span class="greyText smallText">(235,009)</span><br/><a href="/shelf/show/sci-fi" class="actionLinkLite" style="font-size: 1.1em">sci-fi</a> <span class="greyText smallText">(214,918)</span><br/><a href="/shelf/show/i-own" class="actionLinkLite" style="font-size: 1.1em">i-own</a> <span class="greyText smallText">(209,828)</span><br/><a href="/shelf/show/favourites" class="actionLinkLite" style="font-size: 1.1em">favourites</a> <span class="greyText smallText">(178,252)</span><br/><a href="/shelf/show/novels" class="actionLinkLite" style="font-size: 1.1em">novels</a> <span class="greyText smallText">(165,436)</span><br/><a href="/shelf/show/literature" class="actionLinkLite" style="font-size: 1.1em">literature</a> <span class="greyText smallText">(164,380)</span><br/><a href="/shelf/show/novel" class="actionLinkLite" style="font-size: 1.1em">novel</a> <span class="greyText smallText">(147,974)</span><br/><a href="/shelf/show/philosophy" class="actionLinkLite" style="font-size: 1.1em">philosophy</a> <span class="greyText smallText">(136,909)</span><br/><a href="/shelf/show/audiobook" class="actionLinkLite" style="font-size: 1.1em">audiobook</a> <span class="greyText smallText">(130,823)</span><br/><a href="/shelf/show/book-club" class="actionLinkLite" style="font-size: 1.1em">book-club</a> <span class="greyText smallText">(125,319)</span><br/><a href="/shelf/show/adult-fiction" class="actionLinkLite" style="font-size: 1.1em">adult-fiction</a> <span class="greyText smallText">(123,457)</span><br/><a href="/shelf/show/classic" class="actionLinkLite" style="font-size: 1.1em">classic</a> <span class="greyText smallText">(118,967)</span><br/><a href="/shelf/show/audio" class="actionLinkLite" style="font-size: 1.1em">audio</a> <span class="greyText smallText">(113,993)</span><br/><a href="/shelf/show/abandoned" class="actionLinkLite" style="font-size: 1.1em">abandoned</a> <span class="greyText smallText">(108,313)</span><br/><a href="/shelf/show/general-fiction" class="actionLinkLite" style="font-size: 1.1em">general-fiction</a> <span class="greyText smallText">(101,644)</span><br/><a href="/shelf/show/unfinished" class="actionLinkLite" style="font-size: 1.1em">unfinished</a> <span class="greyText smallText">(93,384)</span><br/><a href="/shelf/show/politics" class="actionLinkLite" style="font-size: 1.1em">politics</a> <span class="greyText smallText">(89,549)</span><br/><a href="/shelf/show/american" class="actionLinkLite" style="font-size: 1.1em">american</a> <span class="greyText smallText">(88,748)</span><br/><a href="/shelf/show/all-time-favorites" class="actionLinkLite" style="font-size: 1.1em">all-time-favorites</a> <span class="greyText smallText">(84,012)</span><br/><a href="/shelf/show/dystopian" class="actionLinkLite" style="font-size: 1.1em">dystopian</a> <span class="greyText smallText">(77,522)</span><br/><a href="/shelf/show/dystopia" class="actionLinkLite" style="font-size: 1.1em">dystopia</a> <span class="greyText smallText">(71,292)</span><br/><a href="/shelf/show/literary-fiction" class="actionLinkLite" style="font-size: 1.1em">literary-fiction</a> <span class="greyText smallText">(63,001)</span><br/><a href="/shelf/show/literary" class="actionLinkLite" style="font-size: 1.1em">literary</a> <span class="greyText smallText">(57,512)</span><br/><a href="/shelf/show/never-finished" class="actionLinkLite" style="font-size: 1.1em">never-finished</a> <span class="greyText smallText">(52,305)</span><br/><a href="/shelf/show/political" class="actionLinkLite" style="font-size: 1.1em">political</a> <span class="greyText smallText">(40,048)</span><br/><a href="/shelf/show/classic-literature" class="actionLinkLite" style="font-size: 1.1em">classic-literature</a> <span class="greyText smallText">(30,880)</span><br/><a href="/shelf/show/economics" class="actionLinkLite" style="font-size: 1.1em">economics</a> <span class="greyText smallText">(30,854)</span><br/><a href="/shelf/show/capitalism" class="actionLinkLite" style="font-size: 1.1em">capitalism</a> <span class="greyText smallText">(3,146)</span><br/><a href="/shelf/show/objectivism" class="actionLinkLite" style="font-size: 1.1em">objectivism</a> <span class="greyText smallText">(310)</span><br/><a href="/shelf/show/ayn-rand" class="actionLinkLite" style="font-size: 1.1em">ayn-rand</a> <span class="greyText smallText">(299)</span><br/><a href="/shelf/top_shelves" class="actionLink" style="float: right">More shelves...</a>
<div class="clear"/></div></div><div class="bigBoxBottom"/></div>








</div>

  <script src="http://www.google.com/adsense/search/ads.js" type="text/javascript"/><script type="text/javascript" charset="utf-8">
  var pageOptions = {
    'pubId' : 'pub-7284881071421289',
    'query' : 'atlas shrugged ayn rand buy books',
    'channel' : '4204718441',
    'hl' : 'en'
  };

  var adblock1 = {
    'container' : 'adcontainer1',
    'colorTitleLink' : '#666600',
    'colorDomainLink' : '#215625'
  };

  var adblock2 = {
    'container' : 'adcontainer2',
    'colorTitleLink' : '#666600',
    'colorDomainLink' : '#215625'
  };

  new google.ads.search.Ads(pageOptions, adblock1, adblock2);
  </script></div>
      <div class="clear"/>
    </div>
    <div class="clear"/>
  </div>

  <div class="clear"/>
  <div class="footerContainer">
    <div class="footer">
      <div class="copyright">
        &#169; 2012 Goodreads Inc
      </div>
      <div class="adminLinksContainer">
        <ul class="adminLinks"><li>
            <a href="/about/us" class="first" rel="nofollow">about us</a>
          </li>
          <li>
            <a href="/advertisers" rel="nofollow">advertise</a>
          </li>
          <li>
            <a href="/author/program" rel="nofollow">author program</a>
          </li>
          <li>
            <a href="/jobs" rel="nofollow">jobs</a>
          </li>
          <li>
            <a href="/api" rel="nofollow">api</a>
          </li>
          <li>
            <a href="/blog">our blog</a>
          </li>
          <li>
            <a href="/about/terms" rel="nofollow">terms</a>
          </li>
          <li>
            <a href="/about/privacy" rel="nofollow">privacy</a>
          </li>
          <li>
            <a href="/help" class="last" rel="nofollow">help</a>
          </li>
        </ul><br/><br/></div>
    </div>
  </div>
</div><div id="overlay" style="display:none" onclick="Lightbox.hideBox('dropout')"/><div id="box" style="display:none">
    <img id="close" src="/assets/close.gif" onclick="Lightbox.hideBox('dropout')" alt="Close" title="Close this window"/><div id="boxContents"/>
    <div id="boxContentsLeftovers" style="display:none"/>
    <a class="right actionLinkLite smallText greyText" href="#" id="lightBoxRightClose" onclick="Lightbox.hideBox('dropout'); return false;" style="padding:10px">close</a>
    <div class="clear"/>
</div><div id="fbSigninNotification" style="display:none;">
    <p>Welcome back. Just a moment while we sign you in to your Goodreads account.</p>
    <img alt="Login_animation" src="http://s.gr-assets.com/assets/facebook/login_animation-1e8a0fcfab132f98bfe58ff081c643c5.gif"/></div><script type="text/javascript" src="http://bookads2.goodreads.com/ad?gtargeting=bstqdj64n5&amp;n=3&amp;p=search&amp;sid=b9fe794f93b4abf1f23fe5c541245708&amp;uid=false">
    </script><div id="fb-root"/><script type="text/javascript">
  function loadFacebookScripts() {
    
  }

  window._fb_app_id = '2415071772';

  window._gr_session = 'false'
  window._no_gr_account = 'false'
  window._suppress_auto_login = ""

  window.fbAsyncInit = function() {
    GR_Facebook.initialize();
    loadFacebookScripts();
  };

  (function(d){
     var js, id = 'facebook-jssdk', ref = d.getElementsByTagName('script')[0];
     if (d.getElementById(id)) {return;}
     js = d.createElement('script'); js.id = id; js.async = true;
     js.src = "//connect.facebook.net/en_US/all.js";
     ref.parentNode.insertBefore(js, ref);
   }(document));
</script><script type="text/javascript">
//&lt;![CDATA[

    var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
    document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));

//]]&gt;
</script><script type="text/javascript">
//&lt;![CDATA[

    try {
      var pageTracker = _gat._createTracker("UA-968618-1");
      pageTracker._setCustomVar(1, "User Status", "signed_out", 2);
      pageTracker._trackPageview();
    }
    catch(err) {}

//]]&gt;
</script><script type="text/javascript">
//&lt;![CDATA[

    _qoptions={
    qacct:"p-0dUe_kJAjvkoY"
    };

//]]&gt;
</script><script type="text/javascript" src="http://edge.quantserve.com/quant.js"/><noscript>
  <img src="http://pixel.quantserve.com/pixel/p-0dUe_kJAjvkoY.gif" style="display: none;" border="0" height="1" width="1" alt="Quantcast"/></noscript><script type="text/javascript">
//&lt;![CDATA[

    document.write(unescape("%3Cscript src='" + (document.location.protocol == "https:" ? "https://sb" : "http://b") + ".scorecardresearch.com/beacon.js' %3E%3C/script%3E"));

//]]&gt;
</script><script type="text/javascript">
//&lt;![CDATA[

    COMSCORE.beacon({
      c1:2,
      c2:6035830,
      c3:"",
      c4:"",
      c5:"",
      c6:"",
      c15:""
    });

//]]&gt;
</script><noscript>
    <img src="http://b.scorecardresearch.com/b?c1=2&amp;c2=6035830&amp;c3=&amp;c4=&amp;c5=&amp;c6=&amp;c15=&amp;cv=1.3&amp;cj=1" style="display:none" width="0" height="0" alt=""/></noscript></body></html>
>>> class = data("span.minirating").eq(0)
  File "<stdin>", line 1
    class = data("span.minirating").eq(0)
          ^
SyntaxError: invalid syntax
>>> html_class = data("span.minirating").eg(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'PyQuery' object has no attribute 'eg'
>>> html_class = data("span.minirating").eq(0)
>>> print html_class
<span class="minirating"><span class="stars"><img alt="3.69 of 5 stars" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.69 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.69 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.69 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/stars/red_star_66pct-a2f513494595fa112f4762672b33daef.png" title="3.69 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="3.69 of 5 stars" width="12"/></span> 3.69 avg rating &#8212; 119,430 ratings</span>
            &#8212;
              published
             1957
            &#8212;
            
>>> area = data(html_class).children
>>> ()
()
>>> data(html_class).children
<bound method PyQuery.children of [<span.minirating>]>
>>> history
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'history' is not defined
>>> hist
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'hist' is not defined
>>> print html_class
<span class="minirating"><span class="stars"><img alt="3.69 of 5 stars" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.69 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.69 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.69 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/stars/red_star_66pct-a2f513494595fa112f4762672b33daef.png" title="3.69 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="3.69 of 5 stars" width="12"/></span> 3.69 avg rating &#8212; 119,430 ratings</span>
            &#8212;
              published
             1957
            &#8212;
            
>>> print area
<bound method PyQuery.children of [<span.minirating>]>
>>> spec_area = data(area).children
>>> ("a")
'a'
>>> html_class = data("span.minirating").eg(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'PyQuery' object has no attribute 'eg'
>>> html_class = data("span.minirating").eq(0)
>>> print html_class
<span class="minirating"><span class="stars"><img alt="3.69 of 5 stars" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.69 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.69 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.69 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/stars/red_star_66pct-a2f513494595fa112f4762672b33daef.png" title="3.69 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="3.69 of 5 stars" width="12"/></span> 3.69 avg rating &#8212; 119,430 ratings</span>
            &#8212;
              published
             1957
            &#8212;
            
>>> html_class = data("span.minirating").eq(1)
>>> print html_class
<span class="minirating"><span class="stars"><img alt="4.02 of 5 stars" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.02 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.02 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.02 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="4.02 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/stars/red_star_33pct-69a219b6d79a91503f292bf5ac039d6b.png" title="4.02 of 5 stars" width="12"/></span> 4.02 avg rating &#8212; 2,283 ratings</span>
            &#8212;
              published
             1995
            &#8212;
            
>>> html_class = data("span.minirating").eq(-1)
>>> print html_class

>>> html_class = data("span.minirating").eq
KeyboardInterrupt
>>> ^D
(venv)Michelles-MacBook-Pro-2:BookFairy michelleglauser$ python
Python 2.7.1 (r271:86832, Jun 16 2011, 16:59:05) 
[GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2335.15.00)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 1
1
>>> 2
2
>>> 3
3
>>> 4
4
>>> url = "http://www.goodreads.com/search?utf8=%E2%9C%93&q=atlas+shrugged+ayn+rand&search_type=books"
>>> response = requests.get(url)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'requests' is not defined
>>> data = pq(response.content)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'pq' is not defined
>>> area = data("span.minirating").eq(
... 
... s
... ^D
  File "<stdin>", line 3
    s
    ^
SyntaxError: invalid syntax
>>> 
KeyboardInterrupt
>>> ^D
(venv)Michelles-MacBook-Pro-2:BookFairy michelleglauser$ python
Python 2.7.1 (r271:86832, Jun 16 2011, 16:59:05) 
[GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2335.15.00)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests
>>> from pyquery import PyQuery as pq
>>> 1
1
>>> 2
2
>>> 3
3
>>> 4
4
>>> url = "http://www.goodreads.com/search?utf8=%E2%9C%93&q=atlas+shrugged+ayn+rand&search_type=books"
>>> response = requests.get(url)
>>> data = pq(response.content)
>>> area = data("span.minirating").eq(0)
>>> print area
<span class="minirating"><span class="stars"><img alt="3.69 of 5 stars" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.69 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.69 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.69 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/stars/red_star_66pct-a2f513494595fa112f4762672b33daef.png" title="3.69 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="3.69 of 5 stars" width="12"/></span> 3.69 avg rating &#8212; 119,435 ratings</span>
            &#8212;
              published
             1957
            &#8212;
            
>>> area = data("span.minirating").eq(0).filter("avg rating")
>>> print area

>>> area
[]
>>> area = data("span.minirating")
>>> area
[<span.minirating>, <span.minirating>, <span.minirating>, <span.minirating>, <span.minirating>, <span.minirating>, <span.minirating>, <span.minirating>, <span.minirating>, <span.minirating>, <span.minirating>, <span.minirating>, <span.minirating>, <span.minirating>, <span.minirating>, <span.minirating>]
>>> area = data("span.minirating").eq(0)
>>> area
[<span.minirating>]
>>> print area
<span class="minirating"><span class="stars"><img alt="3.69 of 5 stars" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.69 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.69 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.69 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/stars/red_star_66pct-a2f513494595fa112f4762672b33daef.png" title="3.69 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="3.69 of 5 stars" width="12"/></span> 3.69 avg rating &#8212; 119,435 ratings</span>
            &#8212;
              published
             1957
            &#8212;
            
>>> area
[<span.minirating>]
>>> a = data(area)
>>> a
[<span.minirating>]
>>> print a
<span class="minirating"><span class="stars"><img alt="3.69 of 5 stars" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.69 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.69 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_active-a426a1b922a820d466c383fafb259340.png" title="3.69 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/stars/red_star_66pct-a2f513494595fa112f4762672b33daef.png" title="3.69 of 5 stars" width="12"/><img alt="" height="12" src="http://s.gr-assets.com/assets/layout/gr_red_star_inactive-8e046574eb4e4145e22af66a61ea191b.png" title="3.69 of 5 stars" width="12"/></span> 3.69 avg rating &#8212; 119,435 ratings</span>
            &#8212;
              published
             1957
            &#8212;
            
>>> a.text()
u'3.69 avg rating \u2014 119,435 ratings'
>>> ^D
(venv)Michelles-MacBook-Pro-2:BookFairy michelleglauser$ python
Python 2.7.1 (r271:86832, Jun 16 2011, 16:59:05) 
[GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2335.15.00)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests
>>> from pyquery import PyQuery as pq
>>>     url = "http://www.goodreads.com/search?utf8=%E2%9C%93&q=atlas+shrugged+ayn+rand&search_type=books"
  File "<stdin>", line 1
    url = "http://www.goodreads.com/search?utf8=%E2%9C%93&q=atlas+shrugged+ayn+rand&search_type=books"
    ^
IndentationError: unexpected indent
>>>     response = requests.get(url)
  File "<stdin>", line 1
    response = requests.get(url)
    ^
IndentationError: unexpected indent
>>>     data = pq(response.content)
  File "<stdin>", line 1
    data = pq(response.content)
    ^
IndentationError: unexpected indent
>>>     area = data("span.minirating").eq(0)
  File "<stdin>", line 1
    area = data("span.minirating").eq(0)
    ^
IndentationError: unexpected indent
>>>     a = data(area)
  File "<stdin>", line 1
    a = data(area)
    ^
IndentationError: unexpected indent
>>>     gr_rating = a.text()
  File "<stdin>", line 1
    gr_rating = a.text()
    ^
IndentationError: unexpected indent
>>> url = "http://www.goodreads.com/search?utf8=%E2%9C%93&q=atlas+shrugged+ayn+rand&search_type=books"
>>> response = requests.get(url)
>>> data = pq(response.content)
>>> area = data("span.minirating").eq(0)
>>> a = data(area)
>>> gr_rating = a.text()
>>> print gr_rating 
3.69 avg rating — 119,436 ratings
>>> ^D
(venv)Michelles-MacBook-Pro-2:BookFairy michelleglauser$ python
Python 2.7.1 (r271:86832, Jun 16 2011, 16:59:05) 
[GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2335.15.00)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> ^D
(venv)Michelles-MacBook-Pro-2:BookFairy michelleglauser$ 
(venv)Michelles-MacBook-Pro-2:BookFairy michelleglauser$ python
Python 2.7.1 (r271:86832, Jun 16 2011, 16:59:05) 
[GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2335.15.00)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> gr_search_query = "Atlas Shrugged Ayn Rand"
>>>     joined_query = "+".join(gr_search_query.split())
  File "<stdin>", line 1
    joined_query = "+".join(gr_search_query.split())
    ^
IndentationError: unexpected indent
>>>     url_list = [joined_query, "&search_type=books"]
  File "<stdin>", line 1
    url_list = [joined_query, "&search_type=books"]
    ^
IndentationError: unexpected indent
>>>     #START OF THE URL
...     gr_url = "http://www.goodreads.com/search?utf8=%E2%9C%93&q="
  File "<stdin>", line 2
    gr_url = "http://www.goodreads.com/search?utf8=%E2%9C%93&q="
    ^
IndentationError: unexpected indent
>>> 
>>>     # STICK THE PARTS TOGETHER TO CREATE A URL WITH THE SEARCH
...     for item in url_list:
  File "<stdin>", line 2
    for item in url_list:
    ^
IndentationError: unexpected indent
>>>         gr_url += item
  File "<stdin>", line 1
    gr_url += item
    ^
IndentationError: unexpected indent
>>>     
...     
>>> joined_query = "+".join(gr_search_query.split())
>>> print joined_query
Atlas+Shrugged+Ayn+Rand
>>> url_list = [joined_query, "&search_type=books"]
>>> print url_list
['Atlas+Shrugged+Ayn+Rand', '&search_type=books']
>>> gr_url = "http://www.goodreads.com/search?utf8=%E2%9C%93&q="
>>> 
>>> for item in url_list:
... gr_url += item
  File "<stdin>", line 2
    gr_url += item
         ^
IndentationError: expected an indented block
>>> for item in url_list:
...     gr_url += item
... print gr_url
  File "<stdin>", line 3
    print gr_url
        ^
SyntaxError: invalid syntax
>>> for item in url_list:
...     gr_url = gr_url + item
... retrun gr_url
  File "<stdin>", line 3
    retrun gr_url
         ^
SyntaxError: invalid syntax
>>> return gr_url
  File "<stdin>", line 1
SyntaxError: 'return' outside function
>>> for item in url_list:
...     gr_url = gr_url + item
... return gr_url
  File "<stdin>", line 3
    return gr_url
         ^
SyntaxError: invalid syntax
>>> gr_url
'http://www.goodreads.com/search?utf8=%E2%9C%93&q='
>>> for item in url_list:
...     gr_url = gr_url + item
... return gr_url
  File "<stdin>", line 3
    return gr_url
         ^
SyntaxError: invalid syntax
>>> for item in url_list:
...     gr_url = gr_url + item
... print gr_url
  File "<stdin>", line 3
    print gr_url
        ^
SyntaxError: invalid syntax
>>> for item in url_list:
...     gr_url = gr_url + item
...     print gr_url
... 
http://www.goodreads.com/search?utf8=%E2%9C%93&q=Atlas+Shrugged+Ayn+Rand
http://www.goodreads.com/search?utf8=%E2%9C%93&q=Atlas+Shrugged+Ayn+Rand&search_type=books
>>> clear
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'clear' is not defined
>>> a = ["a", "b", "c", "d"]
>>>     for item in a:
  File "<stdin>", line 1
    for item in a:
    ^
IndentationError: unexpected indent
>>> for item in a:
... for item in a:
  File "<stdin>", line 2
    for item in a:
      ^
IndentationError: expected an indented block
>>> g = "6"
>>> for item in a:
...     g.append(item)
...     g.append(item)
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
AttributeError: 'str' object has no attribute 'append'
>>>     a.append(g)
  File "<stdin>", line 1
    a.append(g)
    ^
IndentationError: unexpected indent
>>> for item in a:
...     a.append(g)
... print a
  File "<stdin>", line 3
    print a
        ^
SyntaxError: invalid syntax
>>> for item in a:
...     a = a.append(g)
... print a
  File "<stdin>", line 3
    print a
        ^
SyntaxError: invalid syntax
>>> for item in a:
...     a = a.append(g)
... a
  File "<stdin>", line 3
    a
    ^
SyntaxError: invalid syntax
>>> ^D
(venv)Michelles-MacBook-Pro-2:BookFairy michelleglauser$ pip install fuzzywuzzy
Downloading/unpacking fuzzywuzzy
  Downloading fuzzywuzzy-0.1.tar.gz
  Running setup.py egg_info for package fuzzywuzzy
    
Installing collected packages: fuzzywuzzy
  Running setup.py install for fuzzywuzzy
    
Successfully installed fuzzywuzzy
Cleaning up...
(venv)Michelles-MacBook-Pro-2:BookFairy michelleglauser$ python
Python 2.7.1 (r271:86832, Jun 16 2011, 16:59:05) 
[GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2335.15.00)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import fuzzywuzzy
>>> s = "The Hobbit Tolkien"
>>> r1 = "Who the hell is Pansy O'Hara? : the fascinating stories behind 50 of the world's best-loved books /"
>>> r2 = 
  File "<stdin>", line 1
    r2 =    
         ^
SyntaxError: invalid syntax
>>> r2 = "The hobbit, or, There and back again / J. R. R. Tolkien ; illustrated by the author."
>>> 
>>> 
>>> from fuzzywuzzy import fuzz
>>> fuzz.ration(s, r1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute 'ration'
>>> fuzz.ratio(s, r1)
13
>>> fuzz.ratio(s, r2)
33
>>> fuzz.token_sort_ratio(s, r2)
26
>>> fuzz.token_sort_ratio(s, r1)
19
>>> fuzz.token_set_ratio(s, r1)
21
>>> fuzz.token_set_ratio(s, r2)
75
>>> fuzz.token_set_ratio("twilight", "the twilight club")
100
>>> fuzz.token_set_ratio("twilight stephenie meyer", "Twilight : the graphic novel. Volume 1 / Stephanie Meyer ; art and adaptation by Young Kim.")
39
>>> 
>>> 
>>> import pyquery
>>> import requests
>>> data = requests.get("http://sflib1.sfpl.org/search/X?SEARCH=The+Hobbit+Tolkien&x=0&y=0&searchscope=15&p=&m=a&Da=&Db=&SORT=D&availlim=1")
>>> 
>>> 
>>> pqd = pyquery.PyQuery(data)
>>> pqd
[]
>>> data
<Response [200]>
>>> pqd = pyquery.PyQuery(data.content)                                                                                       >>> pqd
[<html>]
>>> pqd("p.detail>a")
[<a>, <a>]
>>> a_tags = pqd("p.detail>a")
>>> for a in a_tags:
...     print a.text
... 
None
None
>>> a[0]
<Element img at 0x106be9470>
>>> a
<Element a at 0x106bf3890>
>>> a
<Element a at 0x106bf3890>
>>> a.href
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'HtmlElement' object has no attribute 'href'
>>> a['href']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "lxml.etree.pyx", line 1068, in lxml.etree._Element.__getitem__ (src/lxml/lxml.etree.c:41506)
TypeError: 'str' object cannot be interpreted as an index
>>> dir(a)
['__class__', '__contains__', '__copy__', '__deepcopy__', '__delattr__', '__delitem__', '__dict__', '__doc__', '__format__', '__getattribute__', '__getitem__', '__hash__', '__init__', '__iter__', '__len__', '__module__', '__new__', '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_init', '_label__del', '_label__get', '_label__set', 'addnext', 'addprevious', 'append', 'attrib', 'base', 'base_url', 'body', 'clear', 'cssselect', 'drop_tag', 'drop_tree', 'extend', 'find', 'find_class', 'find_rel_links', 'findall', 'findtext', 'forms', 'get', 'get_element_by_id', 'getchildren', 'getiterator', 'getnext', 'getparent', 'getprevious', 'getroottree', 'head', 'index', 'insert', 'items', 'iter', 'iterancestors', 'iterchildren', 'iterdescendants', 'iterfind', 'iterlinks', 'itersiblings', 'itertext', 'keys', 'label', 'make_links_absolute', 'makeelement', 'nsmap', 'prefix', 'remove', 'replace', 'resolve_base_href', 'rewrite_links', 'set', 'sourceline', 'tag', 'tail', 'text', 'text_content', 'values', 'xpath']
>>> a.text_content
<bound method HtmlElement.text_content of <Element a at 0x106bf3890>>
>>> a.text_content()
''
>>> a
<Element a at 0x106bf3890>
>>> a_tags = pqd("tr>td>a")
>>> a_tags
[<a>, <a>, <a>, <a>, <a>, <a>, <a>, <a>]
>>> a_tags = pqd("tr.briefCitRow tr>td>a")
>>> a_tags
[<a>, <a>, <a>, <a>, <a>, <a>]
>>> a_tags = pqd("tr.briefCitRow")
>>> a_tags
[<tr.briefCitRow>, <tr.briefCitRow>]
>>> a_tags = pqd("tr.briefCitRow tr:first-child>td>a")
>>> a_tags
stuff = pyed_data("tr.'http://schema.org/Book' tr:first-child>td>a")

titles = pyed_data("ul").children().eq(0).html()

titles = pyed_data("h3").children
[<a>, <a>, <a>, <a>]
>>> a_tags[0]
<Element a at 0x106bf3950>
>>> a_tags[0].text
>>> a_tags[1].text()
"Who the hell is Pansy O'Hara? : the fascinating stories behind 50 of the world's best-loved books / "
>>> a_tags[2].text
>>> a_tags[3].text
'The hobbit, or, There and back again / J. R. R. Tolkien ; illustrated by the author.'
>>> a_tags = pqd("tr.briefCitRow>td>table>tbody>tr>td>table>tbody>tr:first-child>td>a")
>>> a_tags
[]
>>> a_tags = pqd("tr.briefCitRow tr:first-child>td>a")
>>> a_tags
[<a>, <a>, <a>, <a>]
>>> a_tags[0].text
>>> a_tags[1].text
"Who the hell is Pansy O'Hara? : the fascinating stories behind 50 of the world's best-loved books / "
>>> a_tags[2].text
>>> a_tags[3].text
'The hobbit, or, There and back again / J. R. R. Tolkien ; illustrated by the author.'
>>> [1,2,3,4,5]
[1, 2, 3, 4, 5]
>>> [1,2,3,4,5].sort()
>>> a = [1,2,3,4,5]
>>> a
[1, 2, 3, 4, 5]
>>> a.sort()
>>> a
[1, 2, 3, 4, 5]
>>> 
>>> 
>>> 
>>> data = requests.get("http://sflib1.sfpl.org/search/X?SEARCH=A+Tree+Grows+in+Brooklyn+Betty+Smith&x=0&y=0&searchscope=15&p=&m=a&Da=&Db=&SORT=D")
>>> content = data.content
>>> pqd = pq
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'pq' is not defined
>>> pqd = pyquery.PyQuery(content)
>>> pqd("td.bibInfoData")
[<td.bibInfoData>, <td.bibInfoData>, <td.bibInfoData>, <td.bibInfoData>, <td.bibInfoData>, <td.bibInfoData>, <td.bibInfoData>, <td.bibInfoData>, <td.bibInfoData>, <td.bibInfoData>]
>>> bibinfo = pqd("td.bibInfoData")
>>> bibinfo[0]
<Element td at 0x106bffa10>
>>> bibinfo[0].text
'\n'
>>> bibinfo[1].text
'\n'
>>> bibinfo[1].textcontent
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'HtmlElement' object has no attribute 'textcontent'
>>> bibinfo[1].text_content()
'\nSmith, Betty, 1896-1972.\n\n'
>>> bibinfo[2].text_content()
'\nA tree grows in Brooklyn : a novel / by Betty Smith.'
>>> bibinfo[2].text_content().strip()
'A tree grows in Brooklyn : a novel / by Betty Smith.'
>>> 


 
def get_books(url):
    r = requests.get(url)
    jQuery = PyQuery(r.content)
    books = jQuery("tr[itemtype='http://schema.org/Book']")
    bookList = []
 
    for b in books:
        bookDict = {}
        allInfo = jQuery(b).children("td").eq(1)
        
        bookInfo = jQuery(allInfo).children("a.bookTitle")
        bookDict['bookTitle'] = jQuery(bookInfo).text()
        bookDict['bookURL'] = jQuery(bookInfo).attr("href")
 
        authorInfo = jQuery(allInfo).find("a.authorName")                                                                                                                                                                                      
        bookDict['author'] = jQuery(authorInfo).text()
        bookDict['authorURL'] = jQuery(authorInfo).attr("href")
 
        bookList.append(bookDict)
 
    return bookList
 
url = "http://www.goodreads.com/search?utf8=%E2%9C%93&q=Their+Eyes+Were+Watching+God+Zora+Neale+Hurston&search_type=books"
books = get_books(url)
print(books)