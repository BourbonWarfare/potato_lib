from pathlib import Path
from potlib.configuration import Configuration
from potlib.arma.mod import Modlist, MODLISTS
from potlib.error import ModlistNotFound, ServerConfigNameNotPermitted


class Server:
    def __init__(self, name: str, config_path: Path):
        present_characters = set(name.lower()).intersection(set('abcdefghijklmnopqrstuvwxyz0123456789-_'))
        if len(present_characters) != len(set(name.lower())):
            raise ServerConfigNameNotPermitted(name)
        self._name = name
        self._config_path = config_path
        self._config = Configuration.load(self._config_path / f'{self._name}.toml')

        SERVER_MAP[self._name] = self

    def server_name(self) -> str:
        return self._name

    def server_password(self) -> str:
        return self._config.require('password').get()

    def server_port(self) -> int:
        return self._config.require('port').get()

    def arma_base_path(self) -> Path:
        return Path(self._config.require('path').get())

    def server_path(self) -> Path:
        return self.arma_base_path() / self.server_name()

    def mod_install_path(self) -> Path:
        return self._config.require('mod_install_path').get()

    def key_install_path(self) -> Path:
        return self.server_path() / 'keys'

    def headless_client_count(self) -> int:
        return self._config.require('hc_count').get()

    def modlist(self) -> Modlist:
        list_name = self._config.require('modlist').get()
        if list_name not in MODLISTS:
            raise ModlistNotFound(list_name)
        return MODLISTS[list_name]


SERVER_MAP: dict[str, Server] = {}
