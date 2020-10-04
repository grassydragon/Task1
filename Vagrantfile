# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"

  config.vagrant.plugins = "vagrant-hostsupdater"

  config.vm.network "private_network", ip: "192.168.33.10"

  config.hostsupdater.aliases = ["www.helloworld.com", "www.time.com"]

  config.vm.provision "file", source: "html", destination: "html"
  config.vm.provision "file", source: "cgi", destination: "cgi"
  config.vm.provision "file", source: "sites-available", destination: "sites-available"

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y apache2
    a2enmod ssl
    a2enmod cgid
    cp -r html ../../var/www
    cp -r cgi ../../var/www
    cp -r sites-available ../../etc/apache2
    chmod +x ../../var/www/cgi/time.py
    a2ensite default-ssl
    service apache2 restart
  SHELL
end
