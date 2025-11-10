#!/usr/bin/env python3
"""
Unit tests for the client module.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the expected value."""
        # Setup the mock return value
        mock_get_json.return_value = {"login": org_name}

        client = GithubOrgClient(org_name)
        result = client.org

        # Ensure org property returns mock value
        self.assertEqual(result, {"login": org_name})

        # Ensure get_json was called exactly once with the expected URL
        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(expected_url)
        
     def test_public_repos_url(self):
        """Test GithubOrgClient._public_repos_url property."""
        # Define a mock payload for the org property
        mock_payload = {"repos_url": "https://api.github.com/orgs/test-org/repos"}

        # Patch the 'org' property
        with patch.object(
            GithubOrgClient,
            "org",
            new_callable=property(lambda self: mock_payload)
        ):
            client = GithubOrgClient("test-org")
            result = client._public_repos_url

            # Assert that the _public_repos_url matches the mocked repos_url
            self.assertEqual(result, mock_payload["repos_url"])