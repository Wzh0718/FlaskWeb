# FlaskWeb
## 1. 网站主要构成

- Admin端：
  - 主要有：
    1. 登陆验证 
    2. 数据清洗、插入Mysql数据库
- Student端：
  - 主要有：
    1. 信息查询
    2. 判空处理

## 2. 网站部署

- 所需包部署命令

  ```python
  # python version >= 3.8
  pip3 install -r ./web/requirements.txt
  ```

- pcre部署命令
  PCRE(Perl Compatible Regular Expressions)是一个轻量级的Perl函数库，包括 perl 兼容的[正则表达式](https://so.csdn.net/so/search?q=正则表达式&spm=1001.2101.3001.7020)库。它比Boost之类的正则表达式库小得多。PCRE十分易用，同时功能也很强大，性能超过了POSIX正则表达式库和一些经典的正则表达式库。

  ```python
  # pcre安装
  cd /usr/src
  # 建议换国内源
  wget http://downloads.sourceforge.net/project/pcre/pcre/8.37/pcre-8.37.tar.gz
  # 解压
  tar -xvf pcre-8.37.tar.gz
  # 进入目录
  cd pcre-8.37
  # 安置 --> 少什么依赖补什么依赖
  ./configure
  # 编译并安装
  make && make install
  # 依赖补充
  yum -y install make zlib zlib-devel gcc-c++ libtool    openssl openssl-devel
  ```

- nginx部署命令

  ```python
  # nginx下载
  wget https://mirrors.huaweicloud.com/nginx/nginx-1.12.2.tar.gz
  # 解压
  tar -xvf nginx-1.12.2.tar.gz
  # 进入目录
  cd nginx-1.12.2
  # 安置
  ./configure
  # 编译并安装
  make && make install
  # 到目录 /usr/local/nginx/下
  cd /usr/local/nginx
  # nginx配置文件 --> 见图
  vim conf/nginx.conf
  ```

  ![b75231122e0b9ddfea35066c0067d531](https://user-images.githubusercontent.com/61780819/180656570-84a96aea-e71c-43be-b305-efa4aa0352f5.png)


  ```py
  # 启动nginx
  sbin/nginx
  ```

  - gunicorn部署命令

  ```python
  # 下载
  pip3 install gunicorn
  # 启动 --> -D 后台启动
  gunicorn -D  -w worker数量 -b ip:端口号 运行文件名：flask实例名
  ```

- Mysql数据库配置

  ```python
  """"此处略过""""
  注意只需要建立1个database，不需要建立表。
  使用Admin界面，需要直接在databse下面的Admin表创建账号和秘密，不支持注册
  database使用utf8的编译
  同时在v2.1版本中已经统一格式，只需要在conMysql文件下写对应信息即可
  ```

## 3. 网站展示

![image](https://user-images.githubusercontent.com/61780819/183365567-889f6690-83e0-40e5-b8e3-867140641fd9.png)
![image](https://user-images.githubusercontent.com/61780819/183365223-3b7b8005-3318-437c-9f9e-facd6a67293d.png)





## 4. 数据格式

| 序号 | 校区 | 区域 | 楼栋 | 单元 | 楼层 | 房号 | 几人 | 性别 | 价格 | 学生类型 | 床号 | 分配届别 | 分配院系 | 新生专业 | 层次 | 身份证号 | 姓名 | 班级 | 辅导员 | 辅导员联系方式 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | -------- | ---- | -------- | -------- | -------- | ---- | -------- | ---- | ---- | ------ | -------------- |
|      |      |      |      |      |      |      |      |      |      |          |      |          |          |          |      |          |      |      |        |                |

## 5. Web性能测试

-  [Gtmetrix](https://gtmetrix.com)

![image](https://user-images.githubusercontent.com/61780819/183365348-9d168e4e-4b84-4c82-82ed-bfcd6bd74793.png)
