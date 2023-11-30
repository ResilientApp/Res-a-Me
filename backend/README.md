# ResilientDB GraphQL
ResilientDB GraphQL Server

# Get Prepared 

(If you're using this for the first time, the steps below would be useful)

Install **Ubuntu 20.04** on your local machine.

Once installed, go to File Explorer -> Linux -> Ubuntu 20.04.

Clone this repository.

Install python3 (version - 3.9+) and ensure pip is installed using the command.

    sudo apt-get install python3-pip

Also make sure to install the venv module which creates a virtual Python environment that helps encapsulate the project's dependencies and prevents possible conflicts with the global Python environment. The command is:

    sudo apt-get install -y python3.10-venv

Create a virtual environment:

    python3 -m venv venv

Start a virtual environment:

    source venv/bin/activate

Go back from the virtual environment when you no longer need it:

    deactivate

# Using the HTTP server

To use the HTTP server, you need to start a KV service first, which you can refer to the [resilientdb](https://github.com/resilientdb/resilientdb) repository and the [blog](https://blog.resilientdb.com/2022/09/28/GettingStartedNexRes.html). 

Then you should start the crow http service, which may take a few minutes at the first time.

    bazel build service/http_server:crow_service_main

# Start the Backend server and the HTTP server

In the below command, the shell script starts the http server as well as the backend server. It awaits the signal (Ctrl+C) to kill both server.

    ./run.sh
