import os

import hug

from model_server_rest.domain.model_predict import ModelPredict


class ModelEndpoint:
    @staticmethod
    @hug.get()
    def predict(mod: str, data_path: str, data_key: str,
                client_id: str = 'unknown') -> dict:
        model_predict = ModelPredict(client_id=client_id)

        data = model_predict.load_data(data_path=os.path.join(os.getcwd(), str(data_path)),
                                       key=data_key)

        preds = model_predict.predict(x=data,
                                      model_name=mod)

        preds_path = model_predict.save_data(preds=preds,
                                             mod=mod,
                                             data_path=data_path)

        print(f"Client: {client_id}: Saved preds: {preds_path}")

        return {'preds_path': preds_path}
