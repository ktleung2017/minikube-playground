import os


class MLServer:
    def __init__(self):
        self.version = os.environ.get('VERSION', 'dev')

    def predict(self, X, feature_names):
        return X.get('data', 'Have a nice day!')

    def health_status(self):
        return self.predict({}, None)

    def tags(self):
        return {'version': self.version}
