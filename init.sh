sudo pip3 install virtualenv
sudo pip3 install pathlib2
virtualenv -p python3 venv
source venv/bin/activate
pip3 install django

sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
gunicorn -w 2 -c /home/box/web/etc/hello.py hello:application