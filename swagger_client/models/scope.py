# coding: utf-8

"""
    jans-config-api

    jans-config-api - Authorization services  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: xxx@gluu.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Scope(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'dn': 'str',
        'id': 'str',
        'inum': 'str',
        'display_name': 'str',
        'description': 'str',
        'icon_url': 'str',
        'authorization_policies': 'list[str]',
        'default_scope': 'bool',
        'scope_type': 'str',
        'jans_claim': 'list[str]',
        'uma_type': 'bool',
        'uma_authorization_policies': 'list[str]',
        'attributes': 'ScopeAttributes'
    }

    attribute_map = {
        'dn': 'dn',
        'id': 'id',
        'inum': 'inum',
        'display_name': 'displayName',
        'description': 'description',
        'icon_url': 'iconUrl',
        'authorization_policies': 'authorizationPolicies',
        'default_scope': 'defaultScope',
        'scope_type': 'scopeType',
        'jans_claim': 'jansClaim',
        'uma_type': 'umaType',
        'uma_authorization_policies': 'umaAuthorizationPolicies',
        'attributes': 'attributes'
    }

    def __init__(self, dn=None, id=None, inum=None, display_name=None, description=None, icon_url=None, authorization_policies=None, default_scope=None, scope_type=None, jans_claim=None, uma_type=None, uma_authorization_policies=None, attributes=None):  # noqa: E501
        """Scope - a model defined in Swagger"""  # noqa: E501
        self._dn = None
        self._id = None
        self._inum = None
        self._display_name = None
        self._description = None
        self._icon_url = None
        self._authorization_policies = None
        self._default_scope = None
        self._scope_type = None
        self._jans_claim = None
        self._uma_type = None
        self._uma_authorization_policies = None
        self._attributes = None
        self.discriminator = None
        if dn is not None:
            self.dn = dn
        if id is not None:
            self.id = id
        if inum is not None:
            self.inum = inum
        if display_name is not None:
            self.display_name = display_name
        if description is not None:
            self.description = description
        if icon_url is not None:
            self.icon_url = icon_url
        if authorization_policies is not None:
            self.authorization_policies = authorization_policies
        if default_scope is not None:
            self.default_scope = default_scope
        if scope_type is not None:
            self.scope_type = scope_type
        if jans_claim is not None:
            self.jans_claim = jans_claim
        if uma_type is not None:
            self.uma_type = uma_type
        if uma_authorization_policies is not None:
            self.uma_authorization_policies = uma_authorization_policies
        if attributes is not None:
            self.attributes = attributes

    @property
    def dn(self):
        """Gets the dn of this Scope.  # noqa: E501


        :return: The dn of this Scope.  # noqa: E501
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """Sets the dn of this Scope.


        :param dn: The dn of this Scope.  # noqa: E501
        :type: str
        """

        self._dn = dn

    @property
    def id(self):
        """Gets the id of this Scope.  # noqa: E501

        The base64url encoded id.  # noqa: E501

        :return: The id of this Scope.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Scope.

        The base64url encoded id.  # noqa: E501

        :param id: The id of this Scope.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def inum(self):
        """Gets the inum of this Scope.  # noqa: E501

        Unique id identifying the attribute  # noqa: E501

        :return: The inum of this Scope.  # noqa: E501
        :rtype: str
        """
        return self._inum

    @inum.setter
    def inum(self, inum):
        """Sets the inum of this Scope.

        Unique id identifying the attribute  # noqa: E501

        :param inum: The inum of this Scope.  # noqa: E501
        :type: str
        """

        self._inum = inum

    @property
    def display_name(self):
        """Gets the display_name of this Scope.  # noqa: E501

        A human-readable name of the scope.  # noqa: E501

        :return: The display_name of this Scope.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Scope.

        A human-readable name of the scope.  # noqa: E501

        :param display_name: The display_name of this Scope.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this Scope.  # noqa: E501

        A human-readable string describing the scope.  # noqa: E501

        :return: The description of this Scope.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Scope.

        A human-readable string describing the scope.  # noqa: E501

        :param description: The description of this Scope.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def icon_url(self):
        """Gets the icon_url of this Scope.  # noqa: E501

        A URL for a graphic icon representing the scope. The referenced icon MAY be used by the authorization server in any user interface it presents to the resource owner.  # noqa: E501

        :return: The icon_url of this Scope.  # noqa: E501
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        """Sets the icon_url of this Scope.

        A URL for a graphic icon representing the scope. The referenced icon MAY be used by the authorization server in any user interface it presents to the resource owner.  # noqa: E501

        :param icon_url: The icon_url of this Scope.  # noqa: E501
        :type: str
        """

        self._icon_url = icon_url

    @property
    def authorization_policies(self):
        """Gets the authorization_policies of this Scope.  # noqa: E501

        Policies associated with all scopes.  # noqa: E501

        :return: The authorization_policies of this Scope.  # noqa: E501
        :rtype: list[str]
        """
        return self._authorization_policies

    @authorization_policies.setter
    def authorization_policies(self, authorization_policies):
        """Sets the authorization_policies of this Scope.

        Policies associated with all scopes.  # noqa: E501

        :param authorization_policies: The authorization_policies of this Scope.  # noqa: E501
        :type: list[str]
        """

        self._authorization_policies = authorization_policies

    @property
    def default_scope(self):
        """Gets the default_scope of this Scope.  # noqa: E501

        Boolean value to specify default scope.  # noqa: E501

        :return: The default_scope of this Scope.  # noqa: E501
        :rtype: bool
        """
        return self._default_scope

    @default_scope.setter
    def default_scope(self, default_scope):
        """Sets the default_scope of this Scope.

        Boolean value to specify default scope.  # noqa: E501

        :param default_scope: The default_scope of this Scope.  # noqa: E501
        :type: bool
        """

        self._default_scope = default_scope

    @property
    def scope_type(self):
        """Gets the scope_type of this Scope.  # noqa: E501

        The scopes type associated with Access Tokens determine what resources will.  # noqa: E501

        :return: The scope_type of this Scope.  # noqa: E501
        :rtype: str
        """
        return self._scope_type

    @scope_type.setter
    def scope_type(self, scope_type):
        """Sets the scope_type of this Scope.

        The scopes type associated with Access Tokens determine what resources will.  # noqa: E501

        :param scope_type: The scope_type of this Scope.  # noqa: E501
        :type: str
        """
        allowed_values = ["openid", "dynamic", "oauth", "uma"]  # noqa: E501
        if scope_type not in allowed_values:
            raise ValueError(
                "Invalid value for `scope_type` ({0}), must be one of {1}"  # noqa: E501
                .format(scope_type, allowed_values)
            )

        self._scope_type = scope_type

    @property
    def jans_claim(self):
        """Gets the jans_claim of this Scope.  # noqa: E501

        Claim attributes associated with the scope.  # noqa: E501

        :return: The jans_claim of this Scope.  # noqa: E501
        :rtype: list[str]
        """
        return self._jans_claim

    @jans_claim.setter
    def jans_claim(self, jans_claim):
        """Sets the jans_claim of this Scope.

        Claim attributes associated with the scope.  # noqa: E501

        :param jans_claim: The jans_claim of this Scope.  # noqa: E501
        :type: list[str]
        """

        self._jans_claim = jans_claim

    @property
    def uma_type(self):
        """Gets the uma_type of this Scope.  # noqa: E501


        :return: The uma_type of this Scope.  # noqa: E501
        :rtype: bool
        """
        return self._uma_type

    @uma_type.setter
    def uma_type(self, uma_type):
        """Sets the uma_type of this Scope.


        :param uma_type: The uma_type of this Scope.  # noqa: E501
        :type: bool
        """

        self._uma_type = uma_type

    @property
    def uma_authorization_policies(self):
        """Gets the uma_authorization_policies of this Scope.  # noqa: E501


        :return: The uma_authorization_policies of this Scope.  # noqa: E501
        :rtype: list[str]
        """
        return self._uma_authorization_policies

    @uma_authorization_policies.setter
    def uma_authorization_policies(self, uma_authorization_policies):
        """Sets the uma_authorization_policies of this Scope.


        :param uma_authorization_policies: The uma_authorization_policies of this Scope.  # noqa: E501
        :type: list[str]
        """

        self._uma_authorization_policies = uma_authorization_policies

    @property
    def attributes(self):
        """Gets the attributes of this Scope.  # noqa: E501


        :return: The attributes of this Scope.  # noqa: E501
        :rtype: ScopeAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this Scope.


        :param attributes: The attributes of this Scope.  # noqa: E501
        :type: ScopeAttributes
        """

        self._attributes = attributes

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(Scope, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Scope):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
