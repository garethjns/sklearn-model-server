from tests.common.model_client import ModelClient
import asyncio


class ModelClientCrowd:
    def run(self, n_clients: int = 100):
        loop = asyncio.get_event_loop()

        futures = [ModelClient().continuous_chat for _ in range(n_clients)]
        loop.run_until_complete(asyncio.wait(futures))


if __name__ == "__main__":
    ModelClientCrowd().run()
