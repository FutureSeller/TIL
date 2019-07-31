가끔 pipenv로 환경 구축할 일이 생기는 데, 자꾸 까먹어서 남겨둠

### Install Pip
``` bash
$ curl -k -O https://bootstrap.pypa.io/get-pip.py
$ python get-pip.py --user
```

### Install & Run Pipenv
``` bash
$ pip install pipenv --user
$ mkdir env && cd env
$ pipenv install
$ pipenv shell
```

### Install packages
``` bash
(env) $ pip install ${name_of_package}
```
