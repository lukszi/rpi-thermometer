class Singleton:
    def __init__(self, decorated):
        self._decorated = decorated

    def __call__(self, *kargs):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated(*kargs)
            return self._instance

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)
