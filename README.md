# Wirtualizacja i przetwarzanie w chmurze

## Ansible + python

- utworzenie wirtualnego środowiska pythona
- instalacja niezbędnego oprogramowania
- wykanie ćwiczeń


#### Część pierwsza

> dodatkowe przydatne pakiety `tree`

- sciagamy pakiet lvm - na maszynie instalujemy lvm2 (linux volume manager)

```shell
sudo apt-get install lvm2 python python-pip
sudo pip install --upgrade pip
sudo pip install pika
```

- Tworzymy dyski dodatkowe (wirtualne) do maszyny bezpośrednio w virtual box
  - wchodzimy w Settings > Storage, dodajemy
  - do Controller dodatkowy dysk 'create new dysk' dwa po 20 mb tworzymy.

- Startujemy maszyne
- Zamontowanie dysku (na kolosie bedzie):

```shell
dd if=/dev/zero of=my_file_disc.img bs=1M // (chcemy okreslic nazwe montowanego dysku, 1M dodajemy, zeby sie za dlugo nie generowal dysk
ls -la // (pliki na dysku wyswietla)
```

> mkfs //przez mkfs (make file system) tworzymy system plikow
>
> mkfs. // oczekiwane formaty wyswietla

```shell
mkfs.ext4 -F ./my_file_disc.img // podajemy sciezke do pliku, na ktorym chcemy system plikow stworzyc
mkdir myMountPoint // tworzymy pusty katalog gdzie zamontujemy dysk
sudo mount ./my_file_disc.img ./myMountPoint //montujemy w katalogu dysk, wskazujemy co montujemy i gdzie
mkdir -p ./my/ss/1/2 //tworzymy strukture folderow - dysk powinien dzialac jak normalny dysk
```

> `sudo umount ./myMountPoint` // wymontowujemy dysk

    mkdir s2mount //tworzymy drugi katalog
    sudo mount ./my_file_disc.img ./s2mount // w innym podkatalogu instalujemy ten sam dysk
    sudo lvmdiskscan // wykorzystujemy lvm, widzimy utworzone dyski z przydzielonymi pamięciami
    pvcreate /dev/sdb // pv -physical volume crate, sdb - nazwa urzadzenia na ktorym chcemy grupe stworzyc
    vgcreate myData /dev/sdb// vg - volume group (tworzymy fizyczna grupe logiczna) - na dysku sdb tworzymy grupe myData
    lvcreate -n movies -L 15M myData// lv - logical volume, tworzymy logiczny wolumin, w dysku stworzonym myData, tworzymy partycje movies (-L 15M pamieci alokujemy do myData)

- mamy stworzony logiczny wolumin, teraz musimy stworzyc system plikow, zeby miec fizyczne urzadzenie

```shell
mkfs.ext3 /dev/myData/movies // formatujemy ext3 systemem plikow na partycji movies
mount /dev/mydata/movies ./myMountPoint // montujemy partycje do myMountPoint
ls //sprawdzamy czy sie zamontowalo
cp my_file_disc.img ./myMountPoint // kopiujemy obraz, zeby zajac miejsce na dysku
```

> numerek identyfikujacy 78 (to bedzie ostatni oktet adresu IP, na który bedziemy sie logowac)

    df -h // sprawdzamy ile pamieci mamy zajetej
    cd .. // schodzimy katalog nizej do 'discs'
    pvcreate /dev/sdc //powtarzamy operacje, zeby dysk fizyczny w ramach lvm-a zaczal dzialac
    xgextend mydata /dev/sdc //rozciagamy wolumin i dodatkowe urzadzanie, dwa dyski po 20MB mamy
    lvexted -L +16M /dev/myData/movies // logical volume extend - dodajemy 16mega do urzadzenia myData
> rozszerza nam do 32MB

    resize2fs /dev/myData/movies //zwiekszamy rozmiar partycji
    df -h //sprawdzamy ile M jest zajete i ile pozostało

> możemy dokladac obrazy poprzez dodanie nowych dysków (img(n) wpisujemy incrementalnie tworzac kolejne obrazy)

#### Druga czesc zajec:

> skalowanie pionowe, horyzontalne - w pionowym dodajac nowe zasoby jest koniecznosc wylaczenia urzadzenia
>
> cloud - nie mozna w nieskonczonosc dodawac pamiec pionowo - kończy się to na levelu maszyny fizycznej, czyli nie jestesmy w stanie zasymulowac super szybkiego komputera dołaczajac zasoby wirtualne.
>
> eventy w aplikacji mozemy rozglosic (message broadcast architecture) - rozglaszamy event do kolejki - pozwoli to na skalowalnosc horyzontalną.

> udostepnil IP dla wszystkich:
> - `5` -przekierowanie na porty,
> - `80` - port indywidualny,
> - `22` - domyslny ssh,
>
> haslo do root: `123qwe123`

    ssh root@149.156.208.163 -p 58022

> jestesmy teraz zalogowani do jednego serwera, kazdy ma swoja wirtualke.
