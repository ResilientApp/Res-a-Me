#!/bin/bash

# Function to handle cleanup on script exit or interrupt
cleanup() {
    echo "Stopping servers..."
    kill $pid1 $pid2 $pid3
    exit
}

# Trap signals and call the cleanup function
trap cleanup EXIT SIGINT SIGTERM

cd ./resilientdb

# Start the resilient db server creating replicas
./service/tools/kv/server_tools/start_kv_service.sh &

# Store the PID of the resilient DB server
pid1=$!

cd ./../ResilientDB_GraphQL

# Start the Bazel-built HTTP server
bazel-bin/service/http_server/crow_service_main service/tools/config/interface/service.config service/http_server/server_config.config &

# Store the PID of the Bazel-built server
pid2=$!

cd ./..

# Start the Flask server
python main.py &

# Store the PID of the Flask server
pid3=$!

echo "ResilientDB server is running with PID $pid1"
echo "Bazel-built HTTP server is running with PID $pid2"
echo "Flask server is running with PID $pid3"

# Wait for both servers to finish (comment the line below if you want to run them indefinitely)
wait $pid1 $pid2 $pid3
