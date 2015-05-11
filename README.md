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
