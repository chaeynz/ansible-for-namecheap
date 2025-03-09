.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.16.3

.. Anchors

.. _ansible_collections.chaeynz.namecheap.nc_lookup_lookup:

.. Anchors: short name for ansible.builtin

.. Title

chaeynz.namecheap.nc_lookup lookup -- Queries and returns elements from Namecheap
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This lookup plugin is part of the `chaeynz.namecheap collection <https://galaxy.ansible.com/ui/repo/published/chaeynz/namecheap/>`_ (version 0.1.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install chaeynz.namecheap`.
    You need further requirements to be able to use this lookup plugin,
    see :ref:`Requirements <ansible_collections.chaeynz.namecheap.nc_lookup_lookup_requirements>` for details.

    To use it in a playbook, specify: :code:`chaeynz.namecheap.nc_lookup`.

.. version_added

.. rst-class:: ansible-version-added

New in chaeynz.namecheap 0.1.0

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Queries Namecheap via its API to return information


.. Aliases


.. Requirements

.. _ansible_collections.chaeynz.namecheap.nc_lookup_lookup_requirements:

Requirements
------------
The below requirements are needed on the local controller node that executes this lookup.

- xmltodict






.. Options

Keyword parameters
------------------

This describes keyword parameters of the lookup. These are the values ``key1=value1``, ``key2=value2`` and so on in the following
examples: ``lookup('chaeynz.namecheap.nc_lookup', key1=value1, key2=value2, ...)`` and ``query('chaeynz.namecheap.nc_lookup', key1=value1, key2=value2, ...)``

.. tabularcolumns:: \X{1}{3}\X{2}{3}

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1
  :class: longtable ansible-option-table

  * - Parameter
    - Comments

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-api_token"></div>

      .. _ansible_collections.chaeynz.namecheap.nc_lookup_lookup__parameter-api_token:

      .. rst-class:: ansible-option-title

      **api_token**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-api_token" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string` / :ansible-option-required:`required`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The API token created through Namecheap


      .. rst-class:: ansible-option-line

      :ansible-option-configuration:`Configuration:`

      - Environment variable: :envvar:`NAMECHEAP\_TOKEN`

      - Environment variable: :envvar:`NAMECHEAP\_API\_TOKEN`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-api_user"></div>

      .. _ansible_collections.chaeynz.namecheap.nc_lookup_lookup__parameter-api_user:

      .. rst-class:: ansible-option-title

      **api_user**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-api_user" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string` / :ansible-option-required:`required`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The username of the Namecheap account


      .. rst-class:: ansible-option-line

      :ansible-option-configuration:`Configuration:`

      - Environment variable: :envvar:`NAMECHEAP\_USER`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-method"></div>

      .. _ansible_collections.chaeynz.namecheap.nc_lookup_lookup__parameter-method:

      .. rst-class:: ansible-option-title

      **method**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-method" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string` / :ansible-option-required:`required`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The method to use for the API call, as documented at https://www.namecheap.com/support/api/methods/


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"domains.getList"`
      - :ansible-option-choices-entry:`"domains.getContacts"`
      - :ansible-option-choices-entry:`"domains.getTldList"`
      - :ansible-option-choices-entry:`"domains.getRegistrarLock"`
      - :ansible-option-choices-entry:`"domains.getInfo"`
      - :ansible-option-choices-entry:`"domains.dns.getList"`
      - :ansible-option-choices-entry:`"domains.dns.getHosts"`
      - :ansible-option-choices-entry:`"domains.dns.getEmailForwarding"`
      - :ansible-option-choices-entry:`"domains.ns.getInfo"`
      - :ansible-option-choices-entry:`"domains.transfer.getStatus"`
      - :ansible-option-choices-entry:`"domains.transfer.getList"`
      - :ansible-option-choices-entry:`"ssl.getList"`
      - :ansible-option-choices-entry:`"ssl.getApproverEmailList"`
      - :ansible-option-choices-entry:`"ssl.getInfo"`
      - :ansible-option-choices-entry:`"users.getPricing"`
      - :ansible-option-choices-entry:`"users.getBalances"`
      - :ansible-option-choices-entry:`"users.getAddFundsStatus"`
      - :ansible-option-choices-entry:`"users.address.getInfo"`
      - :ansible-option-choices-entry:`"users.address.getList"`
      - :ansible-option-choices-entry:`"whoisguard.getList"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-params"></div>

      .. _ansible_collections.chaeynz.namecheap.nc_lookup_lookup__parameter-params:

      .. rst-class:: ansible-option-title

      **params**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-params" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Optional params, might be required, depending on the API method


      .. raw:: html

        </div>


.. Attributes


.. Notes


.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    tasks:



.. Facts


.. Return values

Return Value
------------

.. tabularcolumns:: \X{1}{3}\X{2}{3}

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1
  :class: longtable ansible-option-table

  * - Key
    - Description

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-_list"></div>

      .. _ansible_collections.chaeynz.namecheap.nc_lookup_lookup__return-_list:

      .. rst-class:: ansible-option-title

      **Return value**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-_list" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      list of composed dictionaries with key and value


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success


      .. raw:: html

        </div>



..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- chaeynz (@chaeynz)


.. hint::
    Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

.. Extra links

Collection links
~~~~~~~~~~~~~~~~

.. ansible-links::

  - title: "Repository (Sources)"
    url: "https://github.com/chaeynz/ansible-for-namecheap"
    external: true


.. Parsing errors
