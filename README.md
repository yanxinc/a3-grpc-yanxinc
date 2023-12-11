Proto Compiler: `python -m grpc_tools.protoc -I./ --python_out=./src --pyi_out=./src --grpc_python_out=./src ./reddit.proto
`

Server: `python src/server/server.py`
    - (Optional) specify host & port: `python src/server/server.py --host {your_host} --port {your_port}`
Client: `python src/client/client.py`
Test: `python src/test.py`