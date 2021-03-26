class SeniverseV3ApiError(Exception):
    def __init__(self, status_code, status, *args: object) -> None:
        self.status_code = status_code
        self.status = status
        super().__init__(*args)

    def __repr__(self) -> str:
        return f'<SeniverseV3ApiError {self.status_code}>'

    def __str__(self) -> str:
        return f'{self.status_code} {self.status}'
