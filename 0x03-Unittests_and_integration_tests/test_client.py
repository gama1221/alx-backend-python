#!/usr/bin/env python3
"""
Unit tests for the client module.
"""

import sys
import os
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from client import GithubOrgClient

# If utils or client are in another directory, you may append path here
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))


class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the expected value."""
        mock_get_json.return_value = {"login": org_name}

        client = GithubOrgClient(org_name)
        result = client.org

        self.assertEqual(result, {"login": org_name})
        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(expected_url)

    def test_public_repos_url(self):
        """Test GithubOrgClient._public_repos_url property."""
        mock_payload = {"repos_url": "https://api.github.com/orgs/test-org/repos"}

        with patch.object(
            GithubOrgClient,
            "org",
            new_callable=property(lambda self: mock_payload)
        ):
            client = GithubOrgClient("test-org")
            result = client._public_repos_url
            self.assertEqual(result, mock_payload["repos_url"])

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Test GithubOrgClient.public_repos method."""
        test_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        mock_get_json.return_value = test_payload

        client = GithubOrgClient("test-org")

        with patch.object(
            GithubOrgClient,
            "_public_repos_url",
            new_callable=property(lambda self: "https://api.github.com/orgs/test-org/repos")
        ) as mock_url:
            result = client.public_repos()

            self.assertEqual(result, ["repo1", "repo2", "repo3"])
            self.assertTrue(mock_url.fget is not None)
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/test-org/repos"
            )
