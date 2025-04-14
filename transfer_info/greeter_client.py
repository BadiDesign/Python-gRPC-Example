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
"""The Python implementation of the GRPC info_manager.Greeter client."""

from __future__ import print_function

import logging
import random

import grpc
import info_manager_pb2
import info_manager_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    print("Will try to greet world ...")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = info_manager_pb2_grpc.InfoManagerStub(channel)
        response = stub.SendInfo(info_manager_pb2.InfoRequest(
            name="Mohammad",
            family="Shekari Badi",
            age=25,
            is_new=random.choice([True, False]),
        ))
        print("Greeter client received: " + str(response.ok))


if __name__ == "__main__":
    logging.basicConfig()
    run()
