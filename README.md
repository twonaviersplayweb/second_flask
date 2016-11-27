# 2016 1124 
今天主要看了一点关于数据库的相关知识，下面说一点自己的理解
>为什么要看数据库

数据库是数据持久化存储的一种有效方式而且支持有序查询，web开发中根本离不开数据库

>python 数据库访问

pyton 访问数据库主要有两种方式

1. 通过DB-API直接执行SQL语句
2. 通过ORM 操作python对象实现一种映射进而操作数据库

>书籍对比

核心编程侧重讲了如何运用已有的api来实现对数据库的操作，主要讲运用
面向对象编程指南则对数据库访问的实现原理进行了一些讲解

> 明天目标

继续看面向对象编程指南这本书中的第11章，最终的目的是明白python 操作数据库的原理
检验手段

1. 自己可以封装底层的SQL操作
2. 读懂廖雪峰python教程中关于DB模块的设计
