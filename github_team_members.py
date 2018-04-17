from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

from ansible.errors import AnsibleError
from ansible.plugins.lookup import LookupBase

from github import Github
from os import getenv

try:
    from __main__ import display
except ImportError:
    from ansible.utils.display import Display

    display = Display()


class LookupModule(LookupBase):
    def run(self, terms, variables=None, **kwargs):
        # Get parameters either from the task parameters or environment variables
        api_key = kwargs.get('api_key', getenv('GITHUB_API_KEY'))
        github_team = kwargs.get('github_team', getenv('GITHUB_TEAM'))
        github_org = kwargs.get('github_org', getenv('GITHUB_ORG'))

        g = Github(api_key)

        try:
            teams = {team.slug: team for team in g.get_organization(github_org).get_teams()}
        except Exception as e:
            raise AnsibleError("Failed to get Organization teams: {error}".format(error=str(e)))

        try:
            logins = [member.login for member in teams[github_team].get_members()]
        except Exception as e:
            raise AnsibleError("Failed to get Team members: {error}".format(error=str(e)))
        return logins
