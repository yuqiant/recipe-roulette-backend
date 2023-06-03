class UserSettings:

    def __init__(self, language: str = "EN"):
        self.language = language

    @classmethod
    def fromdict(cls, settings_dict: dict):
        return cls(settings_dict.get("language", "EN"))

    def todict(self) -> dict:
        return self.__dict__

    def __str__(self) -> str:
        return self.todict().__str__()

    def __repr__(self) -> str:
        return self.__str__()


if __name__ == "__main__":
    settings = UserSettings(language="DE")
    print(settings)
    # print(settings.language)
    print(settings.language)
