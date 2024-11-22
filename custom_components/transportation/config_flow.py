import logging

import voluptuous
from homeassistant import config_entries
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback

from custom_components.transportation.consts.configs import CONF_SETUP_COUNTRY_INPUT, CONF_SETUP_SERVICE_INPUT
from custom_components.transportation.consts.defaults import DOMAIN
from custom_components.transportation.services.setup import country_list, country_name
from custom_components.transportation.utilities.list import Lu

_LOGGER = logging.getLogger(__name__)


class TransportationConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):

    async def async_step_reconfigure(self, user_input: dict = None):
        pass

    async def async_migrate_entry(
            self,
            hass: HomeAssistant,
            config_entry: ConfigEntry
    ) -> bool:
        """Migrate old entry."""
        _LOGGER.debug("Migrate entry (config-flow) Flow id - %s %s %s", self.flow_id, hass, config_entry)

        return False

    async def async_step_import(self, import_info):
        return await self.async_step_user(import_info)

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return TransportationOptionsFlowHandler(config_entry)

    async def async_step_user(self, user_input: dict = None):
        return await self.async_step_select_country_service(user_input=user_input)

    async def async_step_select_country_service(self, user_input: dict = None):
        """Select support country"""
        errors = {}
        schema = {}
        input_form = user_input or {}
        # Step - Select Country
        if CONF_SETUP_COUNTRY_INPUT not in input_form:
            schema = {
                **schema,
                **{
                    voluptuous.Required(
                        schema=CONF_SETUP_COUNTRY_INPUT,
                        msg="Please select a country",
                        default=input_form.get(CONF_SETUP_COUNTRY_INPUT, None)
                    ): voluptuous.In(Lu.map(country_list(), lambda country: {
                        country: country_name(country)
                    }))
                }
            }

            return self.async_show_form(
                step_id="select_country_service",
                data_schema=voluptuous.Schema(schema)
            )

        # Step - Select Service
        if CONF_SETUP_SERVICE_INPUT not in input_form:
            schema = {
                **schema,
                **{
                    voluptuous.Required(
                        schema=CONF_SETUP_COUNTRY_INPUT,
                        msg="Please select a country",
                        default=input_form.get(CONF_SETUP_COUNTRY_INPUT, None)
                    ): voluptuous.In(Lu.map(country_list(), lambda country: {
                        country: country_name(country)
                    }))
                }
            }

            return self.async_show_form(
                step_id="select_country_service",
                data_schema=voluptuous.Schema(schema)
            )

        # Step - Go to setup
        pass

    async def async_step_service_setup(self):
        pass


class TransportationOptionsFlowHandler(config_entries.OptionsFlow):
    def __init__(self, config_entry: config_entries.ConfigEntry) -> None:
        self.config_entry: config_entries.ConfigEntry = config_entry
