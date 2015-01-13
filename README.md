# ExpirationDate

Aplicaţie pentru informatizarea
Serviciului Administrare Cimitire Domeniul Public

### Version
0.01

### Tech

ExpirationDate uses certain tehnologies:

* [jQuery] - duh
* [Bootstrap] - boilerplate css
* [Django] - Django makes it easier to build better Web apps more quickly and with less code

### Installation

You need `python3.x` for this to work, also I would recommend [virtualenv]
```sh
$ git clone [git-repo-url]
$ cd expirationDate
$ pip install -r deploy/requirements.txt
$ ./manage.py syncdb
$ ./manage.py migrate
$ ./manage.py runserver_plus
$ ./manage.py collectstatic
```
```sh
Get over here! http://localhost:8000/admin
```

### Development

Want to contribute? Great!
Head over to [trello] and checkout some of the task's posted

### Todo's

 - Write Tests
 - Rethink Everything
 - Add Code Comments

License
----

MIT


**Free Software, Hell Yeah!**
[virtualenv]:https://virtualenv.pypa.io/en/latest/
[Django]:https://www.djangoproject.com/
[Bootstrap]:http://getbootstrap.com/
[jQuery]:http://jquery.com
[trello]:https://trello.com/


