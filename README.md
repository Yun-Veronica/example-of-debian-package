# example-of-debian-package

Basic example of how to create a debian package with a simple Pyhton program. Basic preinst, postint and control file. 

``` git clone https://github.com/Yun-Veronica/example-of-debian-package.git ```- to clone the repo.
``` sudo dpkg -i  example-of-debian-package/my-program.deb ``` - to install.
``` my_program ```- to run.

in case you will need to pack it again: ```dpkg-deb --build /home/user/example-of-debian-package/my-program ```.
