个人博客项目
=
模仿博客园写的个人博客项目。

---
功能描述

实现登录、注册、注销，浏览文章、编写文章、发布文章，点赞与负赞取消赞的效果

---
安装要求
- 下载安装Pycharm
- 下载安装python 3.6
- 下载安装MySql
- 下载Bootstrap
- 下载Kindeditor编辑器

---
安装依赖的库
<pre name = "code" class = "python">
pip install Django==1.11.11
pip install PyMySql
pip install requests
pip install geetest
pip install pillow
pip install urllib3
pip install beautifulsoup4
</pre> 


---
使用到的框架
- Django框架
- Bootstrap框架

---
版本控制

- 使用git进行版本控制

---
项目目录结构
 .  
│  README.MD  
│  manage.py  
│  
├─bk  
│  │  settings.py  
│  │  urls.py  
│  │  wsgi.py  
│  │  __init__.py  
│  
├─blog  
│  │  admin.py  
│  │  apps.py  
│  │  forms.py  
│  │  models.py  
│  │  tests.py  
│  │  views.py  
│  │  __init__.py  
│  
├─log  
│      bk_collect.log  
│      bk_err.log  
│      bk_info.log  
│        
├─media  
│  └─avatars  
│  
├─static  
│  │  jquery-3.3.1.js  
│  │  mystyle.css  
│  │  setupajax.js  
│  │    
│  ├─bootstrap  
│  │            
│  ├─font  
│  │        
│  ├─fontawesome  
│  │        
│  ├─kindeditor  
│  │  
│  └─theme  
│  
└─templates  
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;add_article.html  
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;article_detail.html  
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;base.html  
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;form_test.html  
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;home.html  
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;index.html  
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;left_menu.html  
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;login.html  
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;login2.html  
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;register.html  
 ---
