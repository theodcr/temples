from temples import Data, env


class RawData(Data):
    def __init__(self) -> None:
        super().__init__(path=env["raw_data"], relative_to_config=True)
