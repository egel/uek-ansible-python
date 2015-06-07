# Wirtualizacja i przetwarzanie w chmurze

Jakub Kanclerz

  - [Github](https://github.com/jkanclerz)


## RabbitMQ + python (Hello World)

- utworzenie wirtualnego środowiska pythona (uekansible)
- instalacja niezbędnego oprogramowania
- wykanie ćwiczeń

#### Instalacja i konfiguracja

- Instalacja oprogramowania

```shell
sudo apt-get install python python-pip git-core
sudo pip install -U pip
sudo pip virtualenvwrapper
```

- tworzymy wirtualne środowisko (separacja dla Pyhtona i jego pakietów)

```shell
mkvirtualenv uekpython27
```
> Aktywujemy środowisko jeśli nie zostało aktywowane poleceniem `workon uekansible`, **dezaktywacja** odbywa się poprzez wpisanie `deactivate`

```
workon uekansible
```

- instalacja wymaganego oprogramowania w naszym wirtualnym środowisku

> yolk -l pokaże nam listę oprogramowania w wirtualnym środowisku

```
sudo apt-get install python python-pip
pip install -U pip
pip install yolk pika
```

- instalujemy rabbitmq (już poza wirtualnym środowiskiem)

```
wget https://www.rabbitmq.com/releases/rabbitmq-server/v3.5.3/rabbitmq-server_3.5.3-1_all.deb -P /tmp
sudo dpkg -i /tmp/rabbitmq-server_3.5.3-1_all.deb
```

- następnie uruchamiamy wirtualne środowisko i przechodzimy do folderu w którym trzymamy repo

```shell
cd ~/workspace/uek-rabbitmq-python
workon uekpython27
./send.py
./receive.py


