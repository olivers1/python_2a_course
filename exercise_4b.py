class MyFileContextManager():
    def __init__(self, filename: str, operation: str):
        self._file = open(filename, operation)

    def __enter__(self):
        return self._file

    def __exit__(self, type, value, traceback):
        self._file.close()


class Character:
    def __init__(self, level: int, name: str, trait: str):
        self._level = level
        self._name = name
        self._trait = trait
    
    @property
    def all_attributes(self):
        return "Attributes" + "\n" + str(self._level) + "\n" + self._name + "\n" + self._trait + "\n"

    @property
    def level(self):
        return self._level
    
    @property
    def name(self):
        return self._name
    
    @property
    def trait(self):
        return self._trait


class Settings:
    def __init__(self, resolution: str, difficulty: int):
        self._resolution = resolution
        self._difficulty = difficulty
    
    @property
    def all_settings(self):
        return "\n" + "Settings" + "\n" + self._resolution + "\n" + str(self._difficulty)
    
    @property
    def resolution(self):
        return self._resolution
    
    @property
    def difficulty(self):
        return self._difficulty

character = Character(28, "oliver", "strong")
settings = Settings("1280x720", 8)

with MyFileContextManager("saveFile.txt", "w") as file:
    file.write(character.all_attributes)
    file.write(settings.all_settings)

with MyFileContextManager("saveFile.txt", "r") as file:
    file_content = file.read()

print(file.name)
print(file_content)




