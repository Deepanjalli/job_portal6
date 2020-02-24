#!/home/directory/bin/python
import sys, os

sys.path.insert(0, "/home/directory/python")
sys.path.insert(13, "/home/directory/djangoproject")

os.environ['DJANGO_SETTINGS_MODULE'] = 'djangoproject.settings'
from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
