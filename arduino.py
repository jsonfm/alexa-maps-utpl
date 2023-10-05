import time

#
from enum import Enum

# Arduino
import iot_api_client as iot
from iot_api_client.configuration import Configuration
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

#
from config import config

# Tokens
from tokens import is_token_expired

# Oauth2


ARDUINO_CLIENT_ID = config.get("ARDUINO_CLIENT_ID", "")
ARDUINO_CLIENT_SECRET_KEY = config.get("ARDUINO_CLIENT_SECRET_KEY", "")
ARDUINO_THING_ID = config.get("ARDUINO_THING_ID", "")
TOKEN_URL = "https://api2.arduino.cc/iot/v1/clients/token"
AUDIENCE = "https://api2.arduino.cc/iot"

DELAY = 0.25  # delay time between continuos requests


class ArduinoPins(str, Enum):
    """Pins on the Arduino Device.
    Example:
    america = ArduinoPins.AMERICA.value
    """

    AFRICA = "africaLightsStatus"
    AMERICA = "americaLightsStatus"
    ASIA = "asiaLightsStatus"
    EUROPE = "europaLightsStatus"
    OCEANIA = "oceaniaLightsStatus"
    ANTARCTICA = "antartidaLightsStatus"


class ArduinoService:
    """Arduino Service."""

    def __init__(self):
        # Oauth2
        self.oauth_client = BackendApplicationClient(client_id=ARDUINO_CLIENT_ID)
        self.oauth = OAuth2Session(client=self.oauth_client)

        # Session
        self.client_config = Configuration(host=AUDIENCE)
        self.client = iot.ApiClient(self.client_config)
        self.api = iot.PropertiesV2Api(self.client)
        self.access_token = None

        self.variables = {}

    def get_token(self):
        """Returns `access_token`."""
        token = self.oauth.fetch_token(
            token_url=TOKEN_URL,
            client_id=ARDUINO_CLIENT_ID,
            client_secret=ARDUINO_CLIENT_SECRET_KEY,
            include_client_id=True,
            audience=AUDIENCE,
        )
        access_token = token.get("access_token")
        return access_token

    def set_token(self, access_token: str):
        """Updates `access_token`."""
        self.client_config.access_token = access_token

    def refresh_token(self):
        """makes a relogin if the `access_token` has expired."""
        is_expired = is_token_expired(self.access_token)

        if is_expired:
            self.login()

    def login(self):
        """Saves `access_token`."""
        self.access_token = self.get_token()
        self.set_token(self.access_token)

    def update_variables(self):
        """Return devices."""
        self.refresh_token()
        props = self.get_properties()
        for prop in props:
            key = prop.variable_name
            self.variables[key] = prop.id

    def get_properties(self):
        """get properties."""
        self.refresh_token()
        response = self.api.properties_v2_list(ARDUINO_THING_ID)
        return response

    def get_variables(self):
        """Returns available variables."""
        self.update_variables()
        return self.variables

    def get_property(self, pid: str):
        """Returns an specific property."""
        self.refresh_token()
        response = self.api.properties_v2_show(ARDUINO_THING_ID, pid)
        return response

    def get_variable(self, name: str):
        variable_id = self.variables.get(name)
        prop = self.get_property(variable_id)
        return prop

    def set_variable(self, name: str, value):
        """Update an arduino variable."""
        self.refresh_token()
        variable_id = self.variables.get(name)
        if variable_id is not None:
            payload = {"value": value}
            response = self.api.properties_v2_publish(
                ARDUINO_THING_ID, variable_id, payload
            )
            return response

    def turn_on_all(self):
        """Turn on all lights."""
        for variable in self.variables:
            self.set_variable(variable, False)
            time.sleep(DELAY)

    def turn_off_all(self):
        """Turn off all lights."""
        for variable in self.variables:
            self.set_variable(variable, True)
            time.sleep(DELAY)

    def set_variable_by_continent(self, continent: str, value: bool = True):
        """Sets a new value given a continent."""
        if continent.lower() in "america":
            self.set_variable(ArduinoPins.AMERICA.value, value)
        if continent.lower() in "europe":
            self.set_variable(ArduinoPins.EUROPE.value, value)
        if continent.lower() in "africa":
            self.set_variable(ArduinoPins.AFRICA.value, value)
        if continent.lower() in "asia":
            self.set_variable(ArduinoPins.ASIA.value, value)
        if continent.lower() in "oceania":
            self.set_variable(ArduinoPins.OCEANIA.value, value)


arduinoService = ArduinoService()


if __name__ == "__main__":
    arduinoService.login()
    arduinoService.update_variables()

    # arduinoService.turn_off_all()
    # variables = arduinoService.get_variables()
    # arduinoService.set_variable_with_name_in("africa", True)
    # arduinoService.set_variable_by_continent("america", True)

    pass
