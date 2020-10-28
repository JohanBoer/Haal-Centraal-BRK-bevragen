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


class ZakelijkGerechtigdeLinks(object):
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
        '_self': 'HalLink',
        'persoon': 'HalLink',
        'betrokken_partner': 'HalLink',
        'betrokken_samenwerkingsverband': 'HalLink',
        'betrokken_gorzen_en_aanwassen': 'HalLink'
    }

    attribute_map = {
        '_self': 'self',
        'persoon': 'persoon',
        'betrokken_partner': 'betrokkenPartner',
        'betrokken_samenwerkingsverband': 'betrokkenSamenwerkingsverband',
        'betrokken_gorzen_en_aanwassen': 'betrokkenGorzenEnAanwassen'
    }

    def __init__(self, _self=None, persoon=None, betrokken_partner=None, betrokken_samenwerkingsverband=None, betrokken_gorzen_en_aanwassen=None, local_vars_configuration=None):  # noqa: E501
        """ZakelijkGerechtigdeLinks - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self.__self = None
        self._persoon = None
        self._betrokken_partner = None
        self._betrokken_samenwerkingsverband = None
        self._betrokken_gorzen_en_aanwassen = None
        self.discriminator = None

        if _self is not None:
            self._self = _self
        if persoon is not None:
            self.persoon = persoon
        if betrokken_partner is not None:
            self.betrokken_partner = betrokken_partner
        if betrokken_samenwerkingsverband is not None:
            self.betrokken_samenwerkingsverband = betrokken_samenwerkingsverband
        if betrokken_gorzen_en_aanwassen is not None:
            self.betrokken_gorzen_en_aanwassen = betrokken_gorzen_en_aanwassen

    @property
    def _self(self):
        """Gets the _self of this ZakelijkGerechtigdeLinks.  # noqa: E501


        :return: The _self of this ZakelijkGerechtigdeLinks.  # noqa: E501
        :rtype: HalLink
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this ZakelijkGerechtigdeLinks.


        :param _self: The _self of this ZakelijkGerechtigdeLinks.  # noqa: E501
        :type: HalLink
        """

        self.__self = _self

    @property
    def persoon(self):
        """Gets the persoon of this ZakelijkGerechtigdeLinks.  # noqa: E501


        :return: The persoon of this ZakelijkGerechtigdeLinks.  # noqa: E501
        :rtype: HalLink
        """
        return self._persoon

    @persoon.setter
    def persoon(self, persoon):
        """Sets the persoon of this ZakelijkGerechtigdeLinks.


        :param persoon: The persoon of this ZakelijkGerechtigdeLinks.  # noqa: E501
        :type: HalLink
        """

        self._persoon = persoon

    @property
    def betrokken_partner(self):
        """Gets the betrokken_partner of this ZakelijkGerechtigdeLinks.  # noqa: E501


        :return: The betrokken_partner of this ZakelijkGerechtigdeLinks.  # noqa: E501
        :rtype: HalLink
        """
        return self._betrokken_partner

    @betrokken_partner.setter
    def betrokken_partner(self, betrokken_partner):
        """Sets the betrokken_partner of this ZakelijkGerechtigdeLinks.


        :param betrokken_partner: The betrokken_partner of this ZakelijkGerechtigdeLinks.  # noqa: E501
        :type: HalLink
        """

        self._betrokken_partner = betrokken_partner

    @property
    def betrokken_samenwerkingsverband(self):
        """Gets the betrokken_samenwerkingsverband of this ZakelijkGerechtigdeLinks.  # noqa: E501


        :return: The betrokken_samenwerkingsverband of this ZakelijkGerechtigdeLinks.  # noqa: E501
        :rtype: HalLink
        """
        return self._betrokken_samenwerkingsverband

    @betrokken_samenwerkingsverband.setter
    def betrokken_samenwerkingsverband(self, betrokken_samenwerkingsverband):
        """Sets the betrokken_samenwerkingsverband of this ZakelijkGerechtigdeLinks.


        :param betrokken_samenwerkingsverband: The betrokken_samenwerkingsverband of this ZakelijkGerechtigdeLinks.  # noqa: E501
        :type: HalLink
        """

        self._betrokken_samenwerkingsverband = betrokken_samenwerkingsverband

    @property
    def betrokken_gorzen_en_aanwassen(self):
        """Gets the betrokken_gorzen_en_aanwassen of this ZakelijkGerechtigdeLinks.  # noqa: E501


        :return: The betrokken_gorzen_en_aanwassen of this ZakelijkGerechtigdeLinks.  # noqa: E501
        :rtype: HalLink
        """
        return self._betrokken_gorzen_en_aanwassen

    @betrokken_gorzen_en_aanwassen.setter
    def betrokken_gorzen_en_aanwassen(self, betrokken_gorzen_en_aanwassen):
        """Sets the betrokken_gorzen_en_aanwassen of this ZakelijkGerechtigdeLinks.


        :param betrokken_gorzen_en_aanwassen: The betrokken_gorzen_en_aanwassen of this ZakelijkGerechtigdeLinks.  # noqa: E501
        :type: HalLink
        """

        self._betrokken_gorzen_en_aanwassen = betrokken_gorzen_en_aanwassen

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
        if not isinstance(other, ZakelijkGerechtigdeLinks):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ZakelijkGerechtigdeLinks):
            return True

        return self.to_dict() != other.to_dict()
