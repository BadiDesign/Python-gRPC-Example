if any changed to `.proto` files run this command:

```shell
python -m grpc_tools.protoc -I ./protos --python_out=. --pyi_out=. --grpc_python_out=. protos/helloworld.proto
```

run Server:

```shell
python greeter_server.py
```

run client:

```shell
python greeter_client.py
```