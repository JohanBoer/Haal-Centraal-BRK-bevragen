# coding: utf-8

"""
    Kadaster - BRK-Bevragen API

    D.m.v. deze toepassing worden meerdere, korte bevragingen op de Basis Registratie Kadaster beschikbaar gesteld. Deze toepassing betreft het verstrekken van Kadastrale Onroerende Zaak informatie.   # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class KadasterPersoon(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'identificatie': 'str',
        'omschrijving': 'str',
        'domein': 'str',
        'indicatie_niet_toonbare_diakriet': 'bool',
        'beschikkingsbevoegdheid': 'Waardelijst',
        'woonadres': 'AdresUitgebreid',
        'postadres': 'Postadres',
        'kadastraal_onroerende_zaak_identificaties': 'list[str]'
    }

    attribute_map = {
        'identificatie': 'identificatie',
        'omschrijving': 'omschrijving',
        'domein': 'domein',
        'indicatie_niet_toonbare_diakriet': 'indicatieNietToonbareDiakriet',
        'beschikkingsbevoegdheid': 'beschikkingsbevoegdheid',
        'woonadres': 'woonadres',
        'postadres': 'postadres',
        'kadastraal_onroerende_zaak_identificaties': 'kadastraalOnroerendeZaakIdentificaties'
    }

    def __init__(self, identificatie=None, omschrijving=None, domein=None, indicatie_niet_toonbare_diakriet=None, beschikkingsbevoegdheid=None, woonadres=None, postadres=None, kadastraal_onroerende_zaak_identificaties=None, local_vars_configuration=None):  # noqa: E501
        """KadasterPersoon - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._identificatie = None
        self._omschrijving = None
        self._domein = None
        self._indicatie_niet_toonbare_diakriet = None
        self._beschikkingsbevoegdheid = None
        self._woonadres = None
        self._postadres = None
        self._kadastraal_onroerende_zaak_identificaties = None
        self.discriminator = None

        if identificatie is not None:
            self.identificatie = identificatie
        if omschrijving is not None:
            self.omschrijving = omschrijving
        if domein is not None:
            self.domein = domein
        if indicatie_niet_toonbare_diakriet is not None:
            self.indicatie_niet_toonbare_diakriet = indicatie_niet_toonbare_diakriet
        if beschikkingsbevoegdheid is not None:
            self.beschikkingsbevoegdheid = beschikkingsbevoegdheid
        if woonadres is not None:
            self.woonadres = woonadres
        if postadres is not None:
            self.postadres = postadres
        if kadastraal_onroerende_zaak_identificaties is not None:
            self.kadastraal_onroerende_zaak_identificaties = kadastraal_onroerende_zaak_identificaties

    @property
    def identificatie(self):
        """Gets the identificatie of this KadasterPersoon.  # noqa: E501

        Unieke identificatie voor de persoon. Voor een Kadasterpersoon is dit de identificatie zoals die door het Kadaster is vastgesteld. Voor een ingeschreven natuurlijk persoon is dit het burgerservicenummer. Voor een ingeschreven niet-natuurlijk persoon is dit het RSIN. Of de waarde in identificatie een burgerservicenummer, een RSIN of een kadasterpersoonidentificatie is kan worden afgeleid uit het type persoon.   # noqa: E501

        :return: The identificatie of this KadasterPersoon.  # noqa: E501
        :rtype: str
        """
        return self._identificatie

    @identificatie.setter
    def identificatie(self, identificatie):
        """Sets the identificatie of this KadasterPersoon.

        Unieke identificatie voor de persoon. Voor een Kadasterpersoon is dit de identificatie zoals die door het Kadaster is vastgesteld. Voor een ingeschreven natuurlijk persoon is dit het burgerservicenummer. Voor een ingeschreven niet-natuurlijk persoon is dit het RSIN. Of de waarde in identificatie een burgerservicenummer, een RSIN of een kadasterpersoonidentificatie is kan worden afgeleid uit het type persoon.   # noqa: E501

        :param identificatie: The identificatie of this KadasterPersoon.  # noqa: E501
        :type: str
        """

        self._identificatie = identificatie

    @property
    def omschrijving(self):
        """Gets the omschrijving of this KadasterPersoon.  # noqa: E501

        Voor mensen leesbare, herkenbare en identificerende omschrijving van de persoon (met bijvoorbeeld de naam).   # noqa: E501

        :return: The omschrijving of this KadasterPersoon.  # noqa: E501
        :rtype: str
        """
        return self._omschrijving

    @omschrijving.setter
    def omschrijving(self, omschrijving):
        """Sets the omschrijving of this KadasterPersoon.

        Voor mensen leesbare, herkenbare en identificerende omschrijving van de persoon (met bijvoorbeeld de naam).   # noqa: E501

        :param omschrijving: The omschrijving of this KadasterPersoon.  # noqa: E501
        :type: str
        """

        self._omschrijving = omschrijving

    @property
    def domein(self):
        """Gets the domein of this KadasterPersoon.  # noqa: E501

        Het domein waartoe de identificatie behoort.   # noqa: E501

        :return: The domein of this KadasterPersoon.  # noqa: E501
        :rtype: str
        """
        return self._domein

    @domein.setter
    def domein(self, domein):
        """Sets the domein of this KadasterPersoon.

        Het domein waartoe de identificatie behoort.   # noqa: E501

        :param domein: The domein of this KadasterPersoon.  # noqa: E501
        :type: str
        """

        self._domein = domein

    @property
    def indicatie_niet_toonbare_diakriet(self):
        """Gets the indicatie_niet_toonbare_diakriet of this KadasterPersoon.  # noqa: E501


        :return: The indicatie_niet_toonbare_diakriet of this KadasterPersoon.  # noqa: E501
        :rtype: bool
        """
        return self._indicatie_niet_toonbare_diakriet

    @indicatie_niet_toonbare_diakriet.setter
    def indicatie_niet_toonbare_diakriet(self, indicatie_niet_toonbare_diakriet):
        """Sets the indicatie_niet_toonbare_diakriet of this KadasterPersoon.


        :param indicatie_niet_toonbare_diakriet: The indicatie_niet_toonbare_diakriet of this KadasterPersoon.  # noqa: E501
        :type: bool
        """

        self._indicatie_niet_toonbare_diakriet = indicatie_niet_toonbare_diakriet

    @property
    def beschikkingsbevoegdheid(self):
        """Gets the beschikkingsbevoegdheid of this KadasterPersoon.  # noqa: E501


        :return: The beschikkingsbevoegdheid of this KadasterPersoon.  # noqa: E501
        :rtype: Waardelijst
        """
        return self._beschikkingsbevoegdheid

    @beschikkingsbevoegdheid.setter
    def beschikkingsbevoegdheid(self, beschikkingsbevoegdheid):
        """Sets the beschikkingsbevoegdheid of this KadasterPersoon.


        :param beschikkingsbevoegdheid: The beschikkingsbevoegdheid of this KadasterPersoon.  # noqa: E501
        :type: Waardelijst
        """

        self._beschikkingsbevoegdheid = beschikkingsbevoegdheid

    @property
    def woonadres(self):
        """Gets the woonadres of this KadasterPersoon.  # noqa: E501


        :return: The woonadres of this KadasterPersoon.  # noqa: E501
        :rtype: AdresUitgebreid
        """
        return self._woonadres

    @woonadres.setter
    def woonadres(self, woonadres):
        """Sets the woonadres of this KadasterPersoon.


        :param woonadres: The woonadres of this KadasterPersoon.  # noqa: E501
        :type: AdresUitgebreid
        """

        self._woonadres = woonadres

    @property
    def postadres(self):
        """Gets the postadres of this KadasterPersoon.  # noqa: E501


        :return: The postadres of this KadasterPersoon.  # noqa: E501
        :rtype: Postadres
        """
        return self._postadres

    @postadres.setter
    def postadres(self, postadres):
        """Sets the postadres of this KadasterPersoon.


        :param postadres: The postadres of this KadasterPersoon.  # noqa: E501
        :type: Postadres
        """

        self._postadres = postadres

    @property
    def kadastraal_onroerende_zaak_identificaties(self):
        """Gets the kadastraal_onroerende_zaak_identificaties of this KadasterPersoon.  # noqa: E501


        :return: The kadastraal_onroerende_zaak_identificaties of this KadasterPersoon.  # noqa: E501
        :rtype: list[str]
        """
        return self._kadastraal_onroerende_zaak_identificaties

    @kadastraal_onroerende_zaak_identificaties.setter
    def kadastraal_onroerende_zaak_identificaties(self, kadastraal_onroerende_zaak_identificaties):
        """Sets the kadastraal_onroerende_zaak_identificaties of this KadasterPersoon.


        :param kadastraal_onroerende_zaak_identificaties: The kadastraal_onroerende_zaak_identificaties of this KadasterPersoon.  # noqa: E501
        :type: list[str]
        """

        self._kadastraal_onroerende_zaak_identificaties = kadastraal_onroerende_zaak_identificaties

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, KadasterPersoon):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KadasterPersoon):
            return True

        return self.to_dict() != other.to_dict()
