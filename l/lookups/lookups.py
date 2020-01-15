python --version
python3 --version
alias python=python3



	
virtualenv --version
pip install virtualenv
virtualenv venv
#cd to project folder
source venv/bin/activate
pip freeze > requirements.txt
sudo pip install -r requirements.txt
pip install django_rest_framework

django-admin startproject mysite
apt install python3-pip
pip3 install django
sudo pip3 install Django --upgrade
pip3 install django-crispy-forms
pip install --upgrade django-crispy-forms
pip3 install django-import-export
pip3 install Pillow
sudo pip3 install django-imagekit
sudo pip install pillow django-imagekit

sudo apt-get install postgresql
sudo apt-get install python-psycopg2
sudo apt-get install libpq-dev
sudo pip3 install psycopg2

#############################################################

# Django allauth
pip install django-allauth

#############################################################


Digital ocean set up
1) ssh-keygen

#Unzip files
sudo apt-get install unzip
unzip file.zip -d destination_folder


#CLUB
ssh root@104.248.50.1
ssh root@104.248.50.1:/home/django/django_project/

#move all files
scp * root@104.248.50.1:/home/django/django_project/

#move folder
scp -r name root@104.248.50.1:/home/django/django_project/
scp -r *  ..

#move file
scp name root@104.248.50.1:/home/django/django_project/

scp -r root@104.248.50.1:/home/django/django_project/db.sqlite3 ~/Documents/pycharm/club
pass:smartagenda

#change rights
sudo chmod 755 name
sudo chmod 777 db.sqlite3
ls -l

#restart server
service gunicorn restart

################################################################


#KDMEDLINK
ssh root@169.99.232.79
ssh root@169.99.232.79:/home/django/django_project/

#move all files
scp * root@169.99.232.79:/home/django/django_project/

#move folder
scp -r name root@169.99.232.79:/home/django/django_project/
scp -r *  ..

#move file
scp name root@169.99.232.79:/home/django/django_project/


#restart server
service gunicorn restart

################################################################


#PROFAITH
ssh root@157.230.188.60
ssh root@157.230.188.60:/home/django/django_project/

#move all files
scp * root@157.230.188.60:/home/django/django_project/

#move folder
scp -r name root@157.230.188.60:/home/django/django_project/
scp -r root@157.230.188.60:/home/django/django_project/db.sqlite3 ~/Documents/pycharm/templates
scp -r *  ..

#move file
scp name root@157.230.188.60:/home/django/django_project/

#change rights
sudo chmod 755 name
sudo chmod 777 db.sqlite3
ls -l

#change static files
nano /etc/nginx/sites-available/django

#restart server
service gunicorn restart

################################################################
sudo apt install yum
sudo yum install zip
sudo zip -r /home/django/django_project/files-backup.zip /root
sudo rm files-backup.zip

#download backup to local machine
scp -r root@157.230.188.60:/home/django/django_project/db.sqlite3 ~/Documents/pycharm/pro

################################################################

nano /etc/nginx/sites-available/django
STATIC_ROOT ='/home/django/django_project/django_project/static'

pwd
cd /home/django/django_project
scp -r foldername root@157.230.188.60:/home/django/django_project .

##################################################################


#Mysql DB with Django
pip list
sudo pip install mysqlclient

#IIS Server
pip install wfastcgi
wfastcgi-enable

#############################################################
#github commands
git status
git diff
git add .
git status
git commit -m 'commit_message'
git push

git clone https://
git pull

############################################################

# NODE

Build Setup

# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report

# Reinstall NODE
npm cache clean --force
rm -rf node_modules
npm install
npm start
sudo npm i ajv
############################################################

# VUE
# Project Steps
npm --version

# Install Vue
sudo npm install -g vue-cli
vue --version

# Create Project
vue init webpack projectname

# Download Module
npm install vue-awesome-swiper --save



############################################################
# Create Folder
mkdir foldername

# COPY Folder
scp -r foldername destinationFolder

# Delete Folder
rm -R foldername


#Create Image Thumbnails
sudo pip install pillow django-imagekit

#Create folder
mkdir foldername
#Delete foldername
rm -R foldername

#Rename Folder
mv oldfoldername newfoldername


# 
ipconfig
############################################################


pip install django
python -m django --version
django-admin startproject mysite
pip install mod_wsgi

############################################################

godaddy
mcmanyika@yahoo.com
smartagenda,1

############################################################
 www.duda.co
 mcmanyik@gmail.com
 Micahgomwe,1
############################################################


#UPDATE WORDPRESS

UPDATE wp_options
SET option_value = 'http://new-domain-name.com'
WHERE option_name = 'home';

UPDATE wp_options
SET option_value = 'http://new-domain-name.com'
WHERE option_name = 'siteurl';

UPDATE wp_posts
SET post_content = REPLACE(post_content,'http://old-domain-name.com','http://new-domain-name.com');

UPDATE wp_posts
SET guid = REPLACE(guid,'http://old-domain-name.com','http://new-domain-name.com');


#To install mod_wsgi
set "MOD_WSGI_APACHE_ROOTDIR=C:\wamp64\bin\apache\apache2.4.27
pip install mod_wsgi==4.5.20



1) sudo pip instal mod_wsgi
2) paste in terminal : mod_wsgi-express module-config
3) copy root : Library/Python/2.7/site-packages/mod_wsgi/server/mod_wsgi-py27.so
4) (in xampp) open httpd.conf 
5) paste this - 
		# Apache httpd.conf settings 
		LoadModule wsgi_module "Library/Python/2.7/site-packages/mod_wsgi/server/mod_wsgi-py27.so"
		WSGIScriptAlias / "Documents/pycharm/sasy/sasy/wsgi.py"
		WSGIPythonHome "Library/Python/2.7"
		WSGIPythonPath "Documents/pycharm/sasy"

		Alias /media/ Documents/pycharm/sasy/static/media/
		Alias /static/ Documents/pycharm/sasy/static/

		<Directory Documents/pycharm/sasy/static>
			Require all granted
		</directory>

		<Directory Documents/pycharm/sasy/static/media>
			Require all granted
		</directory>

		<Directory Documents/pycharm/sasy>
			<Files wsgi.py>
				Require all granted
			</Files>
		</dDrectory>


#How To Set Up Django with Postgres, Nginx, and Gunicorn on Ubuntu 16.04 
sudo apt-get update
sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx

#Create the PostgreSQL Database and User
sudo -u postgres psql
CREATE DATABASE myproject;
CREATE USER myprojectuser WITH PASSWORD 'password';
ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
\q

#Create a Python Virtual Environment for your Project
sudo -H pip3 install --upgrade pip
sudo -H pip3 install virtualenv

mkdir ~/myproject
cd ~/myproject
virtualenv myprojectenv
source myprojectenv/bin/activate

pip install django gunicorn psycopg2

#Create and Configure a New Django Project
django-admin.py startproject myproject ~/myproject

nano ~/myproject/myproject/settings.py
#adjust DB
DATABASES = {
    'bk_db': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'c4765fddcfc924b23ed1b3e345158529',
        'HOST': 'localhost',
        'PORT': '',
    }
}

#edit static area
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

#Complete Initial Project Setup
~/myproject/manage.py makemigrations
~/myproject/manage.py migrate
~/myproject/manage.py createsuperuser
~/myproject/manage.py collectstatic

sudo ufw allow 8000
~/myproject/manage.py runserver 0.0.0.0:8000
http://server_domain_or_IP:8000

#Testing Gunicorn's Ability to Serve the Project
cd ~/myproject
gunicorn --bind 0.0.0.0:8000 myproject.wsgi
deactivate

#Create a Gunicorn systemd Service File
sudo nano /etc/systemd/system/gunicorn.service

#adjust
#####################################
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=sammy
Group=www-data
WorkingDirectory=/home/sammy/myproject
ExecStart=/home/sammy/myproject/myprojectenv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/sammy/myproject/myproject.sock myproject.wsgi:application

[Install]
WantedBy=multi-user.target
#####################################

sudo systemctl start gunicorn
sudo systemctl enable gunicorn

#Check for the Gunicorn Socket File
sudo systemctl status gunicorn
ls /home/sammy/myproject

sudo journalctl -u gunicorn

sudo systemctl daemon-reload
sudo systemctl restart gunicorn

#Configure Nginx to Proxy Pass to Gunicorn
sudo nano /etc/nginx/sites-available/myproject
#add
#####################################
server {
    listen 80;
    server_name server_domain_or_IP;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/sammy/myproject;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/sammy/myproject/myproject.sock;
    }
}
######################################

sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
sudo ufw delete allow 8000
sudo ufw allow 'Nginx Full'

#######################################

def __unicode__(self):
        return 'UserProfile {}'.format(self.id) 

#######################################

SELECT a.id, 
       count (case when a.gender = 'Female' then a.gender else null end) as female,
       count (case when a.gender = 'Male' then a.gender else null end) as male
       FROM joins_t_accts a



########################################

#print specific area
<script>
function printPageArea(areaID){
    var printContent = document.getElementById(areaID);
    var WinPrint = window.open('', '', 'width=900,height=650');
    WinPrint.document.write(printContent.innerHTML);
    WinPrint.document.close();
    WinPrint.focus();
    WinPrint.print();
    WinPrint.close();
}
</script>

<div id="printableArea">
    All the printable content goes here......
</div>

<a href="javascript:void(0);" onclick="printPageArea('printableArea')">Print</a>

#########################################
 #Blog
 www.tiny.cloud
 pip3 install django-tinymce4-lite


#Django

{{rw.description|truncatechars:150 }}

{{ value|truncatechars_html:9 }}

{{ value|date:"D d M Y" }}

{{ my_date|date:"Y-m-d" }}

{{ value|time:"H:i" }}

{{ headline|upper }}

{{ value|default:"nothing" }}

{{ comment|linebreaks }}

{{ form.name_of_field }}

{{ some_list|slice:":2" }}

{{ value|time:"H:i" }}

{{ value|title }}

{{ value|wordwrap:5 }}

{{ value|wordcount }}

{{ value|rjust:"10" }}

{{ value|ljust:"10" }}

{{ value|random }}

{{ num_messages|pluralize }}    

{{ value|linenumbers }}

{{ value|join:" // " }}

{{ values|dictsort:"0" }}


#############################################################################


# 17 Sublime Text tips and shortcuts to save you tons of time


// 1) CMD+CLICK (CTRL+CLICK) --> Multi-cursor
// 2) CMD+D (CTRL+D) --> Select next occurrence
// 3) CMD+K (CTRL+K) --> Skip occurrence

var something = 1;
something = 2;
something = 3;

// 4) CMD+P (CTRL+P) --> Jump to file

// 5) CMD+ALT+NUMBER (CTRL+ALT+NUMBER) --> Multiple column layout

// 6) CMD+SHIFT+F (CTRL+SHIFT+F) --> Search all files

// 7) Key binding for "console.log();"

// 8) CMD+SHIFT+SPACE (CTRL+SHIFT+SPACE) --> Select entire string

'a string';

// 9) Package Control (packagecontrol.io/installation)

// 10) SidebarEnhancements

// 11) CMD+X (CTRL+X) --> Delete/Cut entire line

var sampleLine = 'sample line';

// 12) CMD+CTRL+UP/DOWN (CTRL+SHIFT+UP/DOWN) --> Move line/lines

var something = [
    {
        key1: 1
    },
    {
        key2: 2,
        key3: 3
    }
];

// 13) CMD+SHIFT+V (CTRL+SHIFT+V) --> Paste with proper formatting

var something = [
    {
        key1: 1
    },
    {
        key2: 2
    }
];

var arr = [
    
];

// 14) CMD+BRACKET (CTRL+BRACKET) --> Indent / De-indent

var testLine = 'test line';

// 15) CMD+L (CTRL+L) --> Select entire line

var lineToSelect = 'line to select';

// 16) Word Wrap

var message = 'this is a test message that is so long that it extends past just one single line';

// 17) CTRL+SHIFT+M (CTRL+SHIFT+M) --> Select entire contents of parentheses, brackets, or braces

var arr = ['item1', 'item2']

######################################################################################################


#Adobe
mcmanyika@gmail.com
Smartagenda,2020











