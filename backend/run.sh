#!/bin/bash

# Function to handle cleanup on script exit or interrupt
cleanup() {
    echo "Stopping servers..."
    kill $pid1 $pid2
    exit
}

# Trap signals and call the cleanup function
trap cleanup EXIT SIGINT SIGTERM

# Start the Bazel-built HTTP server
bazel-bin/service/http_server/crow_service_main service/tools/config/interface/service.config service/http_server/server_config.config &

# Store the PID of the Bazel-built server
pid1=$!

# Start the Flask server
python main.py &

# Store the PID of the Flask server
pid2=$!

echo "Bazel-built HTTP server is running with PID $pid1"
echo "Flask server is running with PID $pid2"

# Wait for both servers to finish (comment the line below if you want to run them indefinitely)
wait $pid1 $pid2
