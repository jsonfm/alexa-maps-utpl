import time

# Oauth2

from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session


# Arduino
import iot_api_client as iot
from iot_api_client.configuration import Configuration


# Tokens
from tokens import is_token_expired


#
from config import config


ARDUINO_CLIENT_ID = config.get("ARDUINO_CLIENT_ID", "")
ARDUINO_CLIENT_SECRET_KEY = config.get("ARDUINO_CLIENT_SECRET_KEY", "")
ARDUINO_THING_ID = config.get("ARDUINO_THING_ID", "")
TOKEN_URL = "https://api2.arduino.cc/iot/v1/clients/token"
AUDIENCE = "https://api2.arduino.cc/iot"

DELAY = .2


class ArduinoService:
    """Arduino Service."""

    def __init__(self):
        # Oauth2
        self.oauth_client = BackendApplicationClient(
            client_id=ARDUINO_CLIENT_ID
        )
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
        is_expired = is_token_expired(
            self.access_token
        )

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
                ARDUINO_THING_ID, variable_id, payload)
            return response

    def turn_on_all(self):
        """Turn on all lights."""
        for variable in self.variables:
            self.set_variable(variable, True)
            time.sleep(DELAY)

    def turn_off_all(self):
        """Turn off all lights."""
        for variable in self.variables:
            self.set_variable(variable, False)
            time.sleep(DELAY)


arduinoService = ArduinoService()
arduinoService.login()
arduinoService.update_variables()


# africa = arduinoService.get_variable("africaLightsStatus")
t1 = time.time()
# arduinoService.set_variable("americaLightsStatus", False)
arduinoService.turn_off_all()
# arduinoService.refresh_token()
t2 = time.time()
print("dt: ", t2 - t1)
# print("response: ", response)
