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

# Installing ResilientDB

To use the ResilientDB service, you need to build ResilientDB and deploy 4 replicas and 1 client proxy on your local machine. The proxy acts as an interface for all the clients. It batches client requests and forwards these batches to the replica designated as the leader. The 4 replicas participate in the PBFT consensus to order and execute these batches. Post execution, they return the response to the leader.

    git clone https://github.com/resilientdb/resilientdb.git

Install dependencies:

    ./resilientdb/INSTALL.sh

# Installing ResilientDB-GraphQL (the HTTP service)

To use the HTTP service, you need to start a KV service first, which you can refer to the [resilientdb](https://github.com/resilientdb/resilientdb) repository and the [blog](https://blog.resilientdb.com/2022/09/28/GettingStartedNexRes.html). 

    git clone https://github.com/ResilientApp/ResilientDB-GraphQL.git

You have to change the folder name for this repository because "-" is a problem for python to import package

    mv ResilientDB-GraphQL ResilientDB_GraphQL

Getting into ResilientDB_GraphQL to set up the http service, which may take a few minutes at the first time.

    cd ResilientDB_GraphQL
    bazel build service/http_server:crow_service_main

# Start the Backend service and the HTTP service

In the below command, we get back to the previous folder, which is in backend, the shell script starts the resilientdb service, the http service, and backend service. It awaits the signal (Ctrl+C) to kill all services.

    cd ./..
    ./run.sh
