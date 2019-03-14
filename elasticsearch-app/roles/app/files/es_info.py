import sys
from elasticsearch import Elasticsearch

es = Elasticsearch()
try:
    print es.info()
except:
    print "get es info failed"
sys.exit(0)
