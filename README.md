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
  注意只需要建立两个database，不需要建立表。
  database使用utf8的编译
  ```

## 3. 网站展示

![1658672330635](https://user-images.githubusercontent.com/61780819/180656588-4f7348cd-b633-45ed-9faf-3c8db4aa844a.jpg)
![1658672273647](https://user-images.githubusercontent.com/61780819/180656590-2b33f038-c7f3-437f-ab0e-cf66079b77da.jpg)




## 4. 数据格式

| 序号 | 校区 | 区域 | 楼栋 | 单元 | 楼层 | 房号 | 几人 | 性别 | 价格 | 学生类型 | 床号 | 分配届别 | 分配院系 | 新生专业 | 层次 | 身份证号 | 姓名 | 班级 | 辅导员 | 辅导员联系方式 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | -------- | ---- | -------- | -------- | -------- | ---- | -------- | ---- | ---- | ------ | -------------- |
|      |      |      |      |      |      |      |      |      |      |          |      |          |          |          |      |          |      |      |        |                |

## 5. Web性能测试

- Lighthouse

  - pc端：
    <img width="1169" alt="image-20220724222235456" src="https://user-images.githubusercontent.com/61780819/180656657-d895e88a-6d8b-4ab5-b2bd-7aad38d08a8f.png">

  - 移动端 --> 适配问题：
    <img width="1169" alt="image-20220724222355408" src="https://user-images.githubusercontent.com/61780819/180656631-ff38cb85-e66d-4f45-93bd-efa417f0e67e.png">

    
-  [Gtmetrix](https://gtmetrix.com)

   <img width="612" alt="image-20220724222746989" src="https://user-images.githubusercontent.com/61780819/180656630-aa24b839-1956-4a8d-a992-f28f30b04797.png">
