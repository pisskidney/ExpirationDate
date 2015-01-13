# ExpirationDate

AplicaÅ£ie pentru informatizarea
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
$ pip install -r deploy/requirements.txt
```

```sh
$ git clone [git-repo-url] dillinger
$ cd dillinger
$ npm i -d
$ mkdir -p public/files/{md,html,pdf}
$ gulp build --prod
$ NODE_ENV=production node app
```

### Plugins

Dillinger is currently extended with the following plugins

* Dropbox
* Github
* Google Drive
* OneDrive

Readmes, how to use them in your own application can be found here:

* plugins/dropbox/README.md
* plugins/github/README.md
* plugins/googledrive/README.md
* plugins/onedrive/README.md

### Development

Want to contribute? Great!

Dillinger uses Gulp + Webpack for fast developing.
Make a change in your file and instantanously see your updates!

Open your favorite Terminal and run these commands.

First Tab:
```sh
$ node app
```

Second Tab:
```sh
$ gulp watch
```

(optional) Third:
```sh
$ karma start
```

### Todo's

 - Write Tests
 - Rethink Github Save
 - Add Code Comments
 - Add Night Mode

License
----

MIT


**Free Software, Hell Yeah!**
[virtualenv]:https://virtualenv.pypa.io/en/latest/
[Django]:https://www.djangoproject.com/
[Bootstrap]:http://getbootstrap.com/
[jQuery]:http://jquery.com

