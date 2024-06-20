## 

### 前端技术

基础：Html+Css+JavaScript

框架：[BootStrap](https://www.bootcss.com/)+[JQuery](https://jquery.com/)

### 后端技术

Django+爬虫+数据清洗与可视化

数据库：MySQL 8.0.26

Python版本：3.9.16

Django版本：4.2.2

## 本地运行

1.安装miniconda 后把pyWeb虚拟环境解压到虚拟环境目录，

你的安装路径\Miniconda3\envs

2.使用 Pycharm 打开项目，配置python编译环境，

**如果不需要爬虫和数据清洗请跳过 4、5、6 步骤，选择执行第 7 步骤**

3.打开Navicat For Mysql（也就是数据库管理工具），创建booksdb数据库（命令行也可以）

4.创建完数据库后，如果要自定义数据，则执行数据库同步指令。
先切换目录分为两步骤 `python manage.py makemigrations` ，再执行 `python manage.py migrate`

5.如果需要自定义数据，请调用 **reptile.py** 爬虫文件，其中 **max_page** 是每个分类最大采集页数。爬虫结果会写入 **data.csv** 文件（如果采集多次记得备份，因为每次调用爬虫会覆盖）

6.爬取数据以后，需要调用 **clean.py** 数据清洗文件，会生成一个 **clean_data.csv** 文件，代码中调用清洗后的文件存入数据库（需要修改数据库相关的内容）

7.复制 **booksdb.sql** 中的文件内容运行。（不需要爬虫和数据清洗可以直接执行）

8.修改 **setting.py** 中数据库相关的内容。

9.使用命令启动 Django 项目 `python manage.py runserver`

10.通过浏览器访问系统主页面（包括后台）

* 前台首页：`http://127.0.0.1:8000/`
* 后台首页：`http://127.0.0.1:8000/admin`

## 注意

* 注意 Django 项目启动应该先切入`cd manage.py所在目录`。
* 注意**修改setting.py**中数据库相关的内容。
* 系统中不存在后台管理员账号，可以**使用命令`python manage.py createsuperuser`创建**即可。
* 自定义数据的话，需要调用 django 里面的数据库同步指令。
* claen.py中的 **create_engine** 需要修改配置数据库信息。

# 
