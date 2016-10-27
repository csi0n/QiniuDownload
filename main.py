from Api.api import Api

access_key = ''
secret_key = ''
bucket_key = ['']
bucket_domain = ['']

api = Api(access_key, secret_key)

if len(bucket_key) == len(bucket_domain):
    for i_bucket in range(0, len(bucket_key)):
        api.download(bucket_key[i_bucket], bucket_domain[i_bucket])
else:
    print('bucket_key and bucket_domain size must be equal')




