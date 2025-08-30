from potlib.error.base import ServerError

class ArmaError(ServerError):
    def __init__(self, message: str):
        super().__init__(f'Error with an ARMA operation: {message}')

class ModlistNotFound(ArmaError):
    def __init__(self, modlist: str):
        super().__init__(f'Modlist not found: {modlist}')

class ServerConfigNameNotPermitted(ArmaError):
    def __init__(self, config_name: str):
        super().__init__(f'Server config name not permitted: {config_name}')

class ModError(ArmaError):
    def __init__(self, reason: str):
        super().__init__(f'An error occured with a mod: {reason}')


class ModNotDefined(ModError):
    def __init__(self, mod_name: str):
        super().__init__(f'Mod "{mod_name}" is not defined in the configuration.')


class ModAlreadyDefined(ModError):
    def __init__(self, mod_name: str):
        super().__init__(f'Mod "{mod_name}" is already defined.')


class ModMissingField(ModError):
    def __init__(self, mod_name: str, field_name: str):
        super().__init__(f'Mod "{mod_name}" is missing required field "{field_name}".')


class ModFieldInvalid(ModError):
    def __init__(self, mod_name: str, field_name: str, reason: str | None = None):
        if reason:
            super().__init__(f'Mod "{mod_name}" has invalid field "{field_name}": {reason}.')
        else:
            super().__init__(f'Mod "{mod_name}" is has invalid field field "{field_name}".')


class ModInvalidKind(ModError):
    def __init__(self, mod_name: str, kind: str, valid_kinds: list[str]):
        super().__init__(f'Mod "{mod_name}" has invalid kind "{kind}". Must be one of {", ".join(valid_kinds)}.')


class DuplicateModWorkshopID(ModError):
    def __init__(self, workshop_id: str, this_mod_name: str, original_mod_name: str):
        super().__init__(f'Mod "{this_mod_name}" has a workshop ID already defined by "{original_mod_name}" ({workshop_id}).')


class DuplicateModPath(ModError):
    def __init__(self, mod_name: str, existing_mod: str, mod_path: str):
        super().__init__(f'"{mod_name}" has a path already defined by "{existing_mod}": {mod_path}.')

