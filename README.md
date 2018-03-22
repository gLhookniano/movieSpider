# movieSpider
从imdb 豆瓣 猫眼获取电影相关信息

# 依赖
* scrapy scrapy-redis
* 对应使用mysql 需要python-mysql , 使用mongodb 需要python-mongo

## 使用
1. 数据存储：
    1. 打开settings, 按照需求修改相应数据库参数，与其他参数，或使用默认值（redis,json）
    2. linux坏境下可以运行`./DB`目录下相应的数据库设定脚本，或自行搭建
2. slave节点：
    1. 把项目copy到各个slave分布式环境中
    2. 分别运行`python ./run_slave.py`
3. master节点：
    1. 把项目copy到环境中
    2. 按需求修改run_master.py文件
    3. 运行`python ./run_master.py` 启动