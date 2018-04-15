from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

from ansible.errors import AnsibleError
# noinspection PyProtectedMember
from ansible.module_utils._text import to_text
from ansible.module_utils.urls import open_url, ConnectionError, SSLValidationError
from ansible.plugins.lookup import LookupBase

from github import Github

try:
    from __main__ import display
except ImportError:
    from ansible.utils.display import Display

    display = Display()


class LookupModule(LookupBase):
    def run(self, terms, variables=None, **kwargs):
        api_key = kwargs.get('api_key', True)
        github_org = kwargs.get('github_org', True)
        github_team = kwargs.get('github_team', True)
        g = Github(api_key)

        ret = []

        teams = {team.slug: team for team in g.get_organization(github_org).get_teams()}
        for member in teams[github_team].get_members():
            ret.append(member.login)

        # for term in terms:
        #    display.vvvv("url lookup connecting to %s" % term)
        #    try:
        #        response = open_url(term, validate_certs=validate_certs, use_proxy=use_proxy)
        #    except HTTPError as e:
        #        raise AnsibleError("Received HTTP error for %s : %s" % (term, str(e)))
        #    except URLError as e:
        #        raise AnsibleError("Failed lookup url for %s : %s" % (term, str(e)))
        #    except SSLValidationError as e:
        #        raise AnsibleError("Error validating the server's certificate for %s: %s" % (term, str(e)))
        #    except ConnectionError as e:
        #        raise AnsibleError("Error connecting to %s: %s" % (term, str(e)))

        #    if split_lines:
        #        for line in response.read().splitlines():
        #            ret.append(to_text(line))
        #    else:
        #        ret.append(to_text(response.read()))
        return ret
