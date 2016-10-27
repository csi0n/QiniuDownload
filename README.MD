#获取七牛下的资源

---

背景:之前迁移博客的时候很多资源都储存在七牛上,找了半天的资料没有找到一键下载的所有资源的方法,所以自己写了一个.

####配置方法
```
access_key = ''
secret_key = ''
bucket_key = ['', '' ,'']
bucket_domain = ['', '', '']
```

- access_key是AK
- secret_key是SK
- bucket_key是空间名称（数组）
- bucket_domain空间的域名（最后是七牛给的那个）

>>支持多空间

###使用方法
```
python main.py
```
- 如果提示缺少模块的话
```
pip install 模块名
or
easy_install 模块名 
```



