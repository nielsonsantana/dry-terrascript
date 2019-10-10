######################################
# SCRIPT VARIABLES
######################################

export DEBIAN_FRONTEND=noninteractive

# Name of the user to create and grant sudo privileges
USERNAME=agnosticuser

# User with no privileges to run apps
USERNAME_APP=apprunner

# Whether to copy over the root user's `authorized_keys` file to the new sudo
# user.
COPY_AUTHORIZED_KEYS_FROM_ROOT=true
COPY_AUTHORIZED_KEYS_FROM_UBUNTU=true
AUTHORIZED_KEYS_FROM_UBUNTU_PATH=/home/ubuntu/.ssh/authorized_keys
AUTHORIZED_KEYS_FROM_ROOT_PATH=/root/.ssh/authorized_keys
######################################
# SCRIPT LOGIC
######################################

# Add sudo user and grant privileges
useradd --create-home --shell "/bin/bash" --groups sudo "${USERNAME}"
useradd --create-home --shell "/bin/bash" "${USERNAME_APP}"

# Expire the sudo user's password immediately to force a change
# chage --lastday 0 "${USERNAME}"

# Create SSH directory for sudo user
HOME_DIRECTORY="$(eval echo ~${USERNAME})"
mkdir --parents "${HOME_DIRECTORY}/.ssh"

# Copy `authorized_keys` file from root if requested
if [ "${COPY_AUTHORIZED_KEYS_FROM_ROOT}" = true ]; then
	if [ -f "$AUTHORIZED_KEYS_FROM_ROOT_PATH" ]; then
    	cp /root/.ssh/authorized_keys "${HOME_DIRECTORY}/.ssh"
    fi
fi

# Copy `authorized_keys` file from ubuntu if requested
if [ "${COPY_AUTHORIZED_KEYS_FROM_UBUNTU}" = true ]; then
	if [ -f "$AUTHORIZED_KEYS_FROM_UBUNTU_PATH" ]; then
    	cp $AUTHORIZED_KEYS_FROM_UBUNTU_PATH "${HOME_DIRECTORY}/.ssh"
	fi
fi

# Adjust SSH configuration ownership and permissions
chmod 0700 "${HOME_DIRECTORY}/.ssh"
chmod 0600 "${HOME_DIRECTORY}/.ssh/authorized_keys"
chown --recursive "${USERNAME}":"${USERNAME}" "${HOME_DIRECTORY}/.ssh"

rm -f /etc/init.d/add-default-user.sh

######################################
# Create a default user
######################################

# Remove existing sudoers users
# sudo rm /etc/sudoers.d/*

# Given all privileges to new user
cat > /tmp/99-agnostic-users <<EOF
# Created by create-base-user.sh $( date )

# User rules for ubuntu
${USERNAME} ALL=(ALL) NOPASSWD:ALL
EOF

sudo mv /tmp/99-agnostic-users /etc/sudoers.d/99-agnostic-users

echo "User ${USERNAME} created successfull"