django-bootstrap5の導入
=====================================

スマートフォンでも見た目がよくなるように `Bootstrap5 <https://getbootstrap.jp/>`_ を導入してみましょう

django-bootstrap5を有効化
------------------------------

DjangoからBootstrap5を使う方法はいくつかありますが、 `django-bootstrap5 <https://django-bootstrap5.readthedocs.io/en/latest/>`_ を使うのが簡単です。

すでにインストールはしてあるので、有効化の設定とテンプレートファイルの作成を行います。

`settings.py` の ``INSTALLED_APPS`` に ``'django_bootstrap5',`` を追加します。

.. code-block:: python

   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'self_order',  # self_orderアプリケーションを有効化
       'debug_toolbar',  # django-debug-toolbar
       'django_bootstrap5',  # django-bootstrap5
   ]

テンプレートファイルの作成と変更
-----------------------------------------

テンプレートファイルを継承して使うため、 `bootstrap.html` を作成します。

templates/bootstrap.html:

.. code-block:: html+django

   {% extends 'django_bootstrap5/bootstrap5.html' %}

   {% block bootstrap5_title %}{% block page_title %}{% endblock %}{% endblock %}

`base.html` の内容も変更します。

templates/base.html:

.. code-block:: html+django

   {% extends 'bootstrap.html' %}
   
   {% load django_bootstrap5 %}
   
   {% block bootstrap5_content %}
   <div class="container">
       <h1>{% block title %}(no title){% endblock %}</h1>
   
       {% autoescape off %}{% bootstrap_messages %}{% endautoescape %}
   
       {% block content %}(no content){% endblock %}
   </div>
   {% endblock %}

`form.html` も変更します。

templates/form.html:

.. code-block:: html+django

   {% load django_bootstrap5 %}
   
   {% if form.management_form %}
     {% bootstrap_formset form layout='horizontal' %}
   {% else %}
     {% bootstrap_form form layout='horizontal' %}
   {% endif %}
   
   <div>
     {% bootstrap_button button_type="submit" content=submit_text %}
   </div>

これでスマートフォンから再度確認すると、Bootstrap5が適用されて見やすくなりました。

.. image:: images/bootstrap5.png
