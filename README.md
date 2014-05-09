PyGeckoZabbix ![alt text](https://raw.githubusercontent.com/bobeirasa/PyGeckoZabbix/master/images/PyGeckoZabbix.png "PyGeckoZabbix")

=============

This project is intended to get some data from [Zabbix](http://www.zabbix.com) and post into [Geckoboard](http://www.geckoboard.com)
custom widgets. As we know, Zabbix items are very customizable, and maybe one thing or another may not work correctly
because of input and output formats. I'm trying to make it the most *plug 'n playable* as possible, but if you find
something that does not work, please let me know so as I can fix it on a modular way that will work for others as well.

Also, feel free to fork and send pull requests to improve this "plug and play" capability, or register issues.

Dependencies
------------

This project uses [this](https://github.com/bobeirasa/virtualenvs/tree/master/pygeckozabbix) virtualenv. If you decide to use the mentioned virtualenv, you don won't need to install those
dependencies, but if you like to run this on your *Domain-0*, you would like to install the dependencies listed below:

  * pip install pyzabbix  *# For querying zabbix API using Python*
  * pip install requests  *# For pushing stuff to Geckoboard*

Version History
---------------

##### 20131201
  * Initial public release supporting widgets of 3 custom widgets: Line, Monitoring and List.
