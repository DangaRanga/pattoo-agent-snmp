#!/usr/bin/env python3
"""Test the files module."""

# Standard imports
import unittest
import os
import sys

# Try to create a working PYTHONPATH
EXEC_DIR = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(
    os.path.abspath(os.path.join(
        EXEC_DIR, os.pardir)), os.pardir))
_EXPECTED = (
    '{0}pattoo-agent-snmp{0}tests{0}pattoo_agent_snmp_'.format(os.sep))
if EXEC_DIR.endswith(_EXPECTED) is True:
    # We need to prepend the path in case PattooShared has been installed
    # elsewhere on the system using PIP. This could corrupt expected results
    sys.path.insert(0, ROOT_DIR)
else:
    print('''This script is not installed in the "}" directory. Please fix.\
'''.format(_EXPECTED))
    sys.exit(2)

# Pattoo imports
from tests.libraries.configuration import UnittestConfig
from pattoo_agent_snmp import PATTOO_AGENT_SNMPD


class TestConstants(unittest.TestCase):
    """Checks all functions and methods."""

    #########################################################################
    # General object setup
    #########################################################################

    def test_constants(self):
        """Testing constants."""
        self.assertEqual(
            PATTOO_AGENT_SNMPD, 'pattoo_agent_snmpd')


if __name__ == '__main__':
    # Make sure the environment is OK to run unittests
    UnittestConfig().create()

    # Do the unit test
    unittest.main()
