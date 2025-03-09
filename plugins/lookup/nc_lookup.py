# -*- coding: utf-8 -*-

# Copyright: (c) 2025. chaeynz <@chaeynz>
# WTFPL
"""
A lookup plugin designed to return data from the Namecheap API
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
    author: chaeynz (@chaeynz)
    name: nc_lookup
    collection: namecheap
    version_added: "0.1.0"
    short_description: Queries and returns elements from Namecheap
    description:
        - Queries Namecheap via its API to return information
    options:
        api_user:
            description:
                - The username of the Namecheap account
            env:
                # in order of precendence
                - name: NAMECHEAP_USER
            required: true
        api_token:
            description:
                - The API token created through Namecheap
            env:
                # in order of precendence
                - name: NAMECHEAP_TOKEN
                - name: NAMECHEAP_API_TOKEN
            required: true
        params:
            description:
                - Optional params, might be required, depending on the API method
            type: dict
            required: false
        method:
            description:
                - The method to use for the API call, as documented at https://www.namecheap.com/support/api/methods/
            choices:
              - domains.getList
              - domains.getContacts
              - domains.getTldList
              - domains.getRegistrarLock
              - domains.getInfo
              - domains.dns.getList
              - domains.dns.getHosts
              - domains.dns.getEmailForwarding
              - domains.ns.getInfo
              - domains.transfer.getStatus
              - domains.transfer.getList
              - ssl.getList
              - ssl.getApproverEmailList
              - ssl.getInfo
              - users.getPricing
              - users.getBalances
              - users.getAddFundsStatus
              - users.address.getInfo
              - users.address.getList
              - whoisguard.getList
            type: str
            required: true

    requirements:
        - xmltodict
"""

EXAMPLES = """
tasks:
"""

RETURN = """
  _list:
    description:
      - list of composed dictionaries with key and value
    type: list
"""

import os
import requests

from ansible.errors import AnsibleError
from ansible.plugins.lookup import LookupBase
from ansible.module_utils.six import raise_from

try:
    import xmltodict
except ImportError as imp_exc:
    XMLTODICT_LIBRARY_IMPORT_ERROR = imp_exc
else:
    XMLTODICT_LIBRARY_IMPORT_ERROR = None

try:
    import requests
except ImportError as imp_exc:
    REQUESTS_LIBRARY_IMPORT_ERROR = imp_exc
else:
    REQUESTS_LIBRARY_IMPORT_ERROR = None

API_METHODS_ENDPOINTS = {
    "domains.getList": {
        "response_keys": [
            'DomainGetListResult',
            'Domain',
        ],
        "required_params": []
    },
    "domains.getContacts": {
        "response_keys": [
           "DomainContactsResult",
        ],
        "required_params": [
            "DomainName",
        ]
    },
    "domains.getTldList": {
        "response_keys": [
            "Tlds",
        ],
        "required_params": []
    },
    "domains.getRegistrarLock": {
        "response_keys": [
            "DomainGetRegistrarLockResult",
        ],
        "required_params": [
            "DomainName",
        ]
    },
    "domains.getInfo": {
        "response_keys": [
            "DomainGetInfoResult",
        ],
        "required_params": [
            "DomainName",
        ]
    },
    "domains.dns.getList": {
        "response_keys": [
            "DomainDNSGetListResult",
        ],
        "required_params": [
            "SLD",
            "TLD",
        ]
    },
    "domains.dns.getHosts": {
        "response_keys": [
            "DomainDNSGetHostsResult",
        ],
        "required_params": [
            "SLD",
            "TLD",
        ]
    },
    "domains.dns.getEmailForwarding": {
        "response_keys": [
            "DomainDNSGetEmailForwardingResult",
        ],
        "required_params": [
            "DomainName",
        ]
    },
    "domains.ns.getInfo": {
        "response_keys": [],
        "required_params": [
            "SLD",
            "TLD",
            "Nameserver",
        ]
    },
    "domains.transfer.getStatus": {
        "response_keys": [
            "DomainTransferGetStatusResult",
        ],
        "required_params": [
            "TransferID"
        ]
    },
    "domains.transfer.getList": {
        "response_keys": [
            "TransferGetListResult",
            "Transfer",
        ],
        "required_params": []
    },
    "ssl.getList": {
        "response_keys": [
            "SSLListResult",
        ],
        "required_params": []
    },
    "ssl.getApproverEmailList": {
        "response_keys": [],
        "required_params": [
            "DomainName",
        ]
    },
    "ssl.getInfo": {
        "response_keys": [],
        "required_params": [
            "CertificateID",
        ]
    },
    "users.getPricing": {
        "response_keys": [],
        "required_params": [
            "ProductType",
        ]
    },
    "users.getBalances": {
        "response_keys": [
            "UserGetBalancesResult",
        ],
        "required_params": []
    },
    "users.getAddFundsStatus": {
        "response_keys": [],
        "required_params": [
            "TokenID",
        ]
    },
    "users.address.getInfo": {
        "response_keys": [
            "GetAddressInfoResult",
        ],
        "required_params": [
            "AddressId",
        ]
    },
    "users.address.getList": {
        "response_keys": [
            "AddressGetListResult",
            "List",
        ],
        "required_params": []
    },
    "whoisguard.getList": { # namecheap.domainprivacy.getList
        "response_keys": [
            "WhoisguardGetListResult",
            "Whoisguard",
        ],
        "required_params": []
    }

}

def remove_at_sign(obj):
    """ Recursively remove '@' from dictionary keys """
    if isinstance(obj, dict):
        return {k.lstrip('@'): remove_at_sign(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [remove_at_sign(item) for item in obj]
    else:
        return obj

class LookupModule(LookupBase):
    """
    LookupModule(LookupBase) is defined by Ansible
    """

    def run(self, terms, variables=None, **kwargs):
        if XMLTODICT_LIBRARY_IMPORT_ERROR:
            raise_from(
                AnsibleError("xmltodict must be installed to use this plugin"),
                XMLTODICT_LIBRARY_IMPORT_ERROR,
            )

        if REQUESTS_LIBRARY_IMPORT_ERROR:
            raise_from(
                AnsibleError("requests must be installed to use this plugin"),
                REQUESTS_LIBRARY_IMPORT_ERROR,
            )

        namecheap_api_user = (
            kwargs.get("api_user")
            or os.getenv("NAMECHEAP_USER")
        )
        namecheap_api_token = (
            kwargs.get("token")
            or os.getenv("NAMECHEAP_TOKEN")
            or os.getenv("NAMECHEAP_API_TOKEN")
        )

        if namecheap_api_user is None:
            raise AnsibleError(
                "Please provide the user"
            )
        if namecheap_api_token is None:
            raise AnsibleError(
                "Please provide the token"
            )

        public_ip = (
            kwargs.get("public_ip")
            or requests.get("https://checkip.amazonaws.com").text.strip("\n")
        )

        method = kwargs.get("method")

        if method not in API_METHODS_ENDPOINTS.keys():
            raise AnsibleError(
                f"Method {method} is not available"
            )


        passed_params = kwargs.get('params') or {}

        if not all(item in API_METHODS_ENDPOINTS[method]['required_params'] for item in passed_params.keys()):
            missing_items = [item for item in passed_params.keys() if item not in API_METHODS_ENDPOINTS[method]['required_params']]
            raise AnsibleError(
                f"The params you passed are not supported: {', '.join(missing_items)}"
            )

        try:
            with requests.Session() as session:
                url = "https://api.namecheap.com/xml.response"
                params = {
                    "ApiUser": namecheap_api_user,
                    "ApiKey": namecheap_api_token,
                    "UserName": namecheap_api_user,
                    "Command": f"namecheap.{method}",
                    "ClientIp": public_ip
                }
                if passed_params:
                    params.update(passed_params)

                response = session.get(url, params=params, timeout=20)
                response.raise_for_status()
                response_dict = xmltodict.parse(response.text)

        except requests.exceptions.RequestException as req_exc:
            raise AnsibleError(f"Request error: {req_exc}") from req_exc
        except xmltodict.expat.ExpatError as xml_exc:
            raise AnsibleError(f"Failed to parse XML: {xml_exc}") from xml_exc
        except Exception as exc:
            raise AnsibleError(f"An unexpected error occurred: {exc}") from exc

        if response_dict['ApiResponse']['@Status'] == "ERROR":
            raise AnsibleError(
                f"An error occurred: {response_dict['ApiResponse']['Errors']}"
            )

        response_data = response_dict['ApiResponse']['CommandResponse']
        for key in API_METHODS_ENDPOINTS[method]['response_keys']:
            response_data = response_data[key]

        results = remove_at_sign(response_data)

        if results is None:
            results = []

        if isinstance(results, dict):
            results = [results]

        return results
