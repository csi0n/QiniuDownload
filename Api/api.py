# -*- coding: utf-8 -*-
import wget
import os
from qiniu import Auth
from qiniu import BucketManager


class Api(object):

    def __init__(self, access_key, secret_key):
        self.auth = Auth(access_key, secret_key)
        self.buckManage = BucketManager(self.auth)

    def download(self, bucket_key, bucket_domain):
        data = self.buckManage.list(bucket_key)
        for d, x in data[0].items():
            for k in range(0, len(x)):
                key = x[k]['key']
                base_url = "http://%s/%s" % (bucket_domain, key)
                private_url = self.auth.private_download_url(base_url)
                print('start download %s' % (key,))
                if os.path.exists('download/'+bucket_key):
                    wget.download(private_url, 'download/'+bucket_key)
                else:
                    os.makedirs('download/'+bucket_key)
                    wget.download(private_url, 'download/' + bucket_key)
                print('download %s finish' % (key,))
