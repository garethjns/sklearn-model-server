import asyncio
from dataclasses import dataclass

from grpclib.server import Server
from grpclib.utils import graceful_exit

from model_server.application.model_endpoint import ModelEndpoint
from model_server.config import Config


@dataclass
class ModelServer:
    _server = None
    _config = Config()

    def start_server(self,
                     block: bool = True):
        """
        Start a server with grpclib, with asyncio.

        First gets event loop, then calls async method self._start_server, which actually starts the
        server.

        :param block: If True, block execution with server running. Done by await-ing server.wait_closed() inside a
                      graceful_exit context. Default True.
        """
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self._start_server(block=block))
        loop.close()

    async def _start_server(self,
                            block: bool = True):

        if self._server is None:
            self._server = Server([ModelEndpoint()])
            with graceful_exit([self._server]):
                print(f"Server starting on {self._config.host}:{self._config.port}")
                await self._server.start(host=self._config.host, port=self._config.port)

                if block:
                    await self._server.wait_closed()

    def stop_server(self):
        if self._server is not None:
            self._server.stop(1)


async def run_server():
    model_server = ModelServer()
    await model_server.start_server()
    model_server.stop_server()


if __name__ == "__main__":
    model_server = ModelServer()
    model_server.start_server()
