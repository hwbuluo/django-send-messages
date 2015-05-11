# django-send-messages
A simple API to send messages，follow django mail design. It includes Yunpian backend and Wechat(weixin) backend. You can easily send sms message and wechat message by it. [Yunpian](http://www.yunpian.com) is a great sms cloud service. And [Wechat](https://mp.weixin.qq.com/) is the most famous social network in china.

And it can easily be extended to other sms backend.

Install
-------
``
pip install django-send-messages
``


Usage
-----

Add ``sms`` to your ``INSTALLED_APPS`` setting and add an
``include('sms.urls')`` at any point in your url-conf.

You can see the testproj for detail.

You can test the app:

1. setup a virtualenv,and activate it.

``
virtualenv --distribute venv
``

``
source venv/bin/activate
``

2. install the dependency

``
pip install -r test-requirements.py
``

3. test it use py.test

``
py.test sms/tests.py
``

Enjoy it!

# About Contribution 

贡献代码指南

我们非常欢迎大家来贡献代码，我们会向贡献者致以最诚挚的敬意。

一般可以通过在Github上提交[Pull Request](https://github.com/hwbuluo/django-send-messages)来贡献代码。

我们计划下一步引入微信的sendbackend，可以通过微信公众平台提供的模版消息接口，给指定人员发送消息，欢迎大家参与进来。

## Pull Request要求

- **代码规范** 遵从pep8，pythonic。

- **代码格式** 提交前 请按 pep8 进行格式化。

- **必须添加测试！** - 如果没有测试，那么提交的补丁是不会通过的。

- **创建feature分支** - 最好不要从你的master分支提交 pull request。

- **一个feature提交一个pull请求** - 如果你的代码变更了多个操作，那就提交多个pull请求吧。

- **清晰的commit历史** - 保证你的pull请求的每次commit操作都是有意义的。如果你开发中需要执行多次的即时commit操作，那么请把它们放到一起再提交pull请求。

## 运行测试

``` bash
py.test sms/tests.py
```

