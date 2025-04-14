# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC info_manager.InfoManager server."""
import datetime
from concurrent import futures
import logging

import grpc
import info_manager_pb2
import info_manager_pb2_grpc


class InfoManager(info_manager_pb2_grpc.InfoManagerServicer):
    def SendInfo(self, request, context):
        print(' # Received in greeter_server.py # ')
        print(datetime.datetime.now())
        print(request.name)
        print(request.family)
        print(request.age)
        print(request.is_new)
        return info_manager_pb2.IsInfoCorrect(ok=request.is_new)


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    info_manager_pb2_grpc.add_InfoManagerServicer_to_server(InfoManager(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
