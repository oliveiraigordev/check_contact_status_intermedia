class HttpBadRequestError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = 'Requisição má-formada'
        self.status_code = 403
