#!/bin/bash
set -e

# BASED in:
# https://github.com/do-community/automated-setups/blob/master/Ubuntu-18.04/initial_server_setup.sh
# https://www.digitalocean.com/community/tutorials/automating-initial-server-setup-with-ubuntu-18-04

###############################
# Configure unattended-upgrade
###############################

echo "Updating security packages..."
sudo unattended-upgrade


######################################
# Changes in /etc/ssh/sshd_config
######################################

# TEST REGEX

# SED_TEST_TEXT="
# PermitRootLogin yes
# PermitRootLogin The quick brown fox jumps over the lazy dog.
# #PermitRootLogin yes
# #PermitRootLogin yes
# # Other text PermitRootLogin yes
# "
# sed 's/^PermitRootLogin.*/PermitRootLogin no/g' <<<"$SED_TEST_TEXT"


# Disable root SSH login with password
sed --in-place 's/^PermitRootLogin.*/PermitRootLogin no/g' /etc/ssh/sshd_config
sed --in-place 's/^#PermitRootLogin.*/PermitRootLogin no/g' /etc/ssh/sshd_config

sed --in-place 's/^PasswordAuthentication.*/PasswordAuthentication no/g' /etc/ssh/sshd_config
sed --in-place 's/^#PasswordAuthentication.*/PasswordAuthentication no/g' /etc/ssh/sshd_config

sed --in-place 's/^PermitEmptyPasswords.*/PermitEmptyPasswords no/g' /etc/ssh/sshd_config
sed --in-place 's/^#PermitEmptyPasswords.*/PermitEmptyPasswords no/g' /etc/ssh/sshd_config



# https://www.linode.com/docs/security/securing-your-server/#ssh-daemon-options
echo "Listen only ipv4"
echo 'AddressFamily inet' | sudo tee -a /etc/ssh/sshd_config

# Why putting SSH on another port than 22 is bad idea
# https://www.adayinthelifeof.nl/2012/03/12/why-putting-ssh-on-another-port-than-22-is-bad-idea/
# sed --in-place 's/^Port.*/Port 2222/g' /etc/ssh/sshd_config
sudo systemctl restart sshd

# Wait before try update
sleep 1

sudo apt-get -qq update
# Add exception for SSH and then enable UFW firewall
echo "Installing ufw"
apt-get install -y -qq ufw

echo "Configuring ufw"
ufw allow OpenSSH
ufw --force enable

apt-get install -y -qq unzip
echo "Installing unattended-upgrades"
sudo apt-get install -y -qq unattended-upgrades

######################################
# Configure unattended-upgrades
######################################


######################################
# Fail2Ban
######################################
echo "Installing fail2ban"

apt-get install -y -qq fail2ban
# apt-get install -y -q sendmail-bin sendmail

