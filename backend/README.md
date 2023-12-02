# ResilientDB and ResilientDB GraphQL
ResilientDB local Server and HTTP server

# Get Prepared 

(If you're using this for the first time, the steps below would be useful)

Install **Ubuntu 20.04** on your local machine.

Install miniconda using the command.

    mkdir -p ~/miniconda3
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
    bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
    rm -rf ~/miniconda3/miniconda.sh
    ~/miniconda3/bin/conda init bash

# Using the ResilientDB server

Getting into the backend

    cd ./Res-a-Me/backend/

To use the ResilientDB server, you need to build ResilientDB and deploy 4 replicas and 1 client proxy on your local machine. The proxy acts as an interface for all the clients. It batches client requests and forwards these batches to the replica designated as the leader. The 4 replicas participate in the PBFT consensus to order and execute these batches. Post execution, they return the response to the leader.

    git clone https://github.com/resilientdb/resilientdb.git

Install dependencies:

    ./resilientdb/INSTALL.sh

# Using the HTTP server

To use the HTTP server, you need to start a KV service first, which you can refer to the [resilientdb](https://github.com/resilientdb/resilientdb) repository and the [blog](https://blog.resilientdb.com/2022/09/28/GettingStartedNexRes.html). 

    git clone https://github.com/ResilientApp/ResilientDB-GraphQL.git

You have to change the folder name for this repository because "-" is a problem for python to import package

    mv ResilientDB-GraphQL ResilientDB_GraphQL

Then you should start the crow http service, which may take a few minutes at the first time.

    cd ResilientDB_GraphQL
    bazel build service/http_server:crow_service_main

# Install the requirements

To install the requirements with miniconda, you have to reopen the terminal to enable activating conda
After that, run the below command to install the requirements for backend and HTTP server

    ./install.sh

# Start the Backend server and the HTTP server

In the below command, the shell script starts the http server as well as the backend server. It awaits the signal (Ctrl+C) to kill both server.

    ./run.sh
