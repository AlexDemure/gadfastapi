from gadopenapi.extensions.errors import APIError


class DummyNotFoundError(APIError): ...


class DummyAlreadyExistsError(APIError): ...
