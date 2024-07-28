====================================
Djangoアプリケーションの作成
====================================

今日作成するWebアプリケーション
==========================================

今日、Djangoを使って作ってみるWebアプリケーションについて説明します。

セルフオーダーシステム
-----------------------------

最近は飲食店でもよく使われるようになったセルフオーダーシステムを作ります。

完成後のアプリケーションの操作の流れは次の通りです:

1. トップ画面: テーブル番号を入力
2. メニュー画面: メニューを選ぶ（1つの注文では1個だけ）
3. トッピング選択画面: トッピングと数量を選ぶ（複数のトッピングと数量を入力できる）
4. 確認画面: 選択したメニューとトッピングが表示される
5. 完了画面: 注文が完了した旨が表示される
6. Django管理画面で注文内容を確認できる

.. list-table::

   * - .. image:: images/self-order-top.png
     - .. image:: images/self-order-menu.png
     - .. image:: images/self-order-topping.png
     - .. image:: images/self-order-confirm.png
     - .. image:: images/self-order-complete.png

.. list-table::

   * - .. image:: images/self-order-admin.png

Djangoアプリケーションの作成と有効化
=========================================

Djangoのプロジェクトは、複数のDjangoアプリケーションを組み合わせてシステムを構成します。

Djangoアプリケーションを作成して、まずはトップページを表示してみましょう。

self_orderアプリケーションを作成
----------------------------------------

セルフオーダーシステムのほとんど全部のコードを含むDjangoのアプリケーションとして、 ``self_order`` という名前で作成します。

``python manage.py startapp`` コマンドを使用します。

.. code-block::

   python manage.py startapp self_order

コマンドが成功すると `self_order` フォルダが作成されます。これがDjangoアプリケーションです。DjangoアプリケーションはPythonのモジュールの一種ですので、 `__init__.py` ファイルがフォルダに含まれています。

他にもいくつかのファイルが含まれていますが、編集する際に説明していきます。

self_orderアプリケーションを有効化
----------------------------------------

Djangoアプリケーションは、作成しただけではDjangoプロジェクト内で有効になりません。

`settings.py` ファイルの設定を変更して有効にする必要があります。 ``INSTALLED_APPS`` の項目を探して編集します。

.. code-block:: python

   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'self_order',  # self_orderアプリケーションを有効化
   ]

これで ``self_order`` が有効になりました。

.. tip::

   Djangoのプロジェクトでは、プロジェクトフォルダの中に、プロジェクト名と同名のフォルダがあり、その中にプロジェクトの設定ファイル（`settings.py`）やプロジェクト全体のURL設定（`urls.py`）などがあります。

   Djangoアプリケーションを作成すると、プロジェクトフォルダ内にアプリケーション用のフォルダが作られます。

   プロジェクトフォルダ内には複数のDjangoアプリケーションが配置される構造になります。

   .. image:: images/django-project-structure.png

   このプロジェクトフォルダ内の各フォルダは、 `__init__.py` を含んでいるため、Pythonのモジュールとして ``import`` 文でインポートして読み込むことができる形になっています。
