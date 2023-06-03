#!/bin/bash

export remote_username="username"
export remote_hostname="domain"


function tunnel_allow() {
# this version of the tunnel allows direct connections from outside world to remote_hostname:8080
ssh -vvv -N -R 8080:localhost:4949 "$remote_username"@"$remote_hostname"
}

function tunnel_disallow() {
# this only allows access from within the remote server
ssh -vvv -N -R 127.0.0.1:8080:localhost:4949 "$remote_username"@"$remote_hostname"
}

# tunnel_allow
tunnel_disallow
