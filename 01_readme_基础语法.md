<!-- TOC -->

- [基础语法](#1-基础语法)
    - [标识符](#11-标识符)
        - [标识符：](#111-标识符：)
        - [标识符命名规则：](#112-标识符命名规则：)
        - [遵循PEP8原则](#113-遵循PEP8原则)
    - [关键字](#12-关键字)
    - [注释](#13-注释)
    - [行与缩进](#14-行与缩进)
    - [多行语句](#15-多行语句)
    - [同一行显示多条语句](#16-同一行显示多条语句)
    - [多个语句构成代码组](#17-多个语句构成代码组)
    - [import 与 from...import](#18-import与from...import)
    - [输入：input(“提示”)](#19-输入：input(“提示”))
    - [输出：print](#110-输出：print)
        - [格式化输出](#1101-格式化输出)
        - [常用格式符](#1102-常用格式符)
        - [转义字符：\n](#1103-转义字符：\n)
        - [不换行：print(“hello word”,end=” ”)](#1104-不换行：print(“helloword”,end=””))

<!-- /TOC -->




<a id="toc_anchor" name="#1-基础语法"></a>

# 1. 基础语法

<a id="toc_anchor" name="#11-标识符"></a>

## 1.1. 标识符

<a id="toc_anchor" name="#111-标识符："></a>

### 1.1.1. 标识符：
* 由字母、下划线和数字组成，且数字不能开头。
* 且区分大小写。
* 在 Python3中，可以用中文作为变量名，非 ASCII 标识符也是允许的了。

<a id="toc_anchor" name="#112-标识符命名规则："></a>

### 1.1.2. 标识符命名规则：
1. 小驼峰式命名法（lower camel case）： 第一个单词以小写字母开始；第二个单词的首字母大写。
2. 大驼峰式命名法（upper camel case）： 每一个单字的首字母都采用大写字母。
3. 蛇形命名法：用下划线“_”来连接所有的单词。

<a id="toc_anchor" name="#113-遵循PEP8原则"></a>

### 1.1.3. 遵循PEP8原则
PEP8原名《Python Enhacement Proposal #8》译为《8 号 Python 增强规范》为代码编写风格提供了指南，变量命名部分规范如下。

* 普通变量，使用蛇形命名法，比如max_value
* 常量，采用全部大写字母，使用下划线连接，比如 MAX_VALUE
* 仅内部使用变量，在变量前增加下划线前缀，比如 _local_var
* 变量名称与python关键字冲突时，在变量末尾追加下划线，比如 class_

<a id="toc_anchor" name="#12-关键字"></a>

## 1.2. 关键字
```python
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', \
'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', \
'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', \
'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', \
'with', 'yield']
```

<a id="toc_anchor" name="#13-注释"></a>

## 1.3. 注释
1. 简介
```python
# 行内注释
'''
多行注释
函数、类的注释也称为接口注释
'''
"""
多行注释
函数、类的注释也称为接口注释
"""
```
2. 编码
   * 在代码第一行写入执行时的python解释器路径，编辑完后需要对此python文件添加'x'权限。之后直接./ 运行
```python
#!/usr/bin/python
#coding=utf-8
```
```python
# -*- coding:utf-8 -*-
```

<a id="toc_anchor" name="#14-行与缩进"></a>

## 1.4. 行与缩进
* python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} 。  
* 缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。

<a id="toc_anchor" name="#15-多行语句"></a>

## 1.5. 多行语句
1. Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠 \ 来实现多行语句
```python
total = item_one + \
        item_two + \
        item_three
```
2. 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠 \，例如：
```python
total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']
```

<a id="toc_anchor" name="#16-同一行显示多条语句"></a>

## 1.6. 同一行显示多条语句
Python 可以在同一行中使用多条语句，语句之间使用<b>分号 ; </b>分割

<a id="toc_anchor" name="#17-多个语句构成代码组"></a>

## 1.7. 多个语句构成代码组
* 缩进相同的一组语句构成一个代码块，我们称之**代码组**。
* 像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成**代码组**。
* 我们将首行及后面的代码组称为一个**子句(clause)**。

<a id="toc_anchor" name="#18-import与from...import"></a>

## 1.8. import 与 from...import
* 在 python 用 import 或者 from...import 来导入相应的模块。
  * 将整个 <b> 模块(somemodule) </b>导入，格式为： <b>import somemodule</b>
  * 从某个模块中导入**某个函数**,格式为： <b>from somemodule import somefunction</b>
  * 从某个模块中导入**多个函数**,格式为： <b>from somemodule import firstfunc, secondfunc, thirdfunc</b>
  * 将某个模块中的**全部函数**导入，格式为： <b>from somemodule import *</b>

<a id="toc_anchor" name="#19-输入：input(“提示”)"></a>

## 1.9. 输入：input(“提示”)
* input()的小括号中放入的是，提示信息，用来在获取数据之前给用户的一个简单提示
* input()在从键盘获取了数据以后，会存放到等号右边的变量中
* input()会把用户输入的任何值都作为字符串来对待  
* eval(input("请输入可执行表达式")) eval可以把输入的字符串转换成可执行的表达式

<a id="toc_anchor" name="#110-输出：print"></a>

## 1.10. 输出：print

<a id="toc_anchor" name="#1101-格式化输出"></a>

### 1.10.1. 格式化输出
```python
   print("我今年%d岁"%age)#没有逗号

   print("我的姓名是%s,年龄是%d"%(name,age))
```
<a id="toc_anchor" name="#1102-常用格式符"></a>

### 1.10.2. 常用格式符
| 格式符号 | 转换                        |
| -------- | --------------------------- |
| %%       | 输出%                       |
| %c       | 字符                        |
| %s       | 通过str()字符串转换来格式化 |
| %i       | 有符号十进制整数            |
| %d       | 有符号十进制整数            |
| %u       | 无符号十进制整数            |
| %o       | 八进制整数                  |
| %x       | 十六进制整数（小写字母）    |
| %X       | 十六进制整数（大写字母）    |
| %e       | 索引符号（小写'e'）         |
| %E       | 索引符号（大写“E”）          |
| %f       | 浮点实数                    |
| %g       | ％f和％e的简写              |
| %G       | ％f和％E的简写              |

<a id="toc_anchor" name="#1103-转义字符：\n"></a>

### 1.10.3. 转义字符：\n

<a id="toc_anchor" name="#1104-不换行：print(“helloword”,end=””)"></a>

### 1.10.4. 不换行：print(“hello word”,end=” ”)

