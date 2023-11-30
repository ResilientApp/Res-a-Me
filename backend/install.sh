cd ./..
git clone https://github.com/resilientdb/resilientdb.git
cd ./resilientdb
./INSTALL.sh
cd ../Res-a-Me/backend
git clone https://github.com/ResilientApp/ResilientDB-GraphQL.git
mv ResilientDB-GraphQL ResilientDB_GraphQL

conda create --name RDB python=3.10
conda activate RDB

pip install -r requirements.txt
cd ResilientDB_GraphQL
pip install -r requirements.txt

bazel build service/http_server:crow_service_main
cd ..