# Ansible Lookup plugin - Github team members

This small project is an [Ansible](https://www.ansible.com/) [lookup
plugin](https://docs.ansible.com/ansible/2.5/plugins/lookup.html) that fetches
[Github](https://github.com/) [users that belong to a given
team](https://developer.github.com/v3/teams/).

Calling the team APi to directly get members of a team is however often not
enough since it actually only returns public members of this team. If you
belong to an organization that has teams, you can view these teams members.

The parameters will either be taken from Ansible task parameters or from
environment, with the former having the priority on the former. So you can call
it like this:

```yaml
- name: "Get Github organization members"
  set_fact:
    users: "{{ lookup('github_team_members',
                        api_key=github_api_key,
                        github_org=github_org,
                        github_team=github_team,
                        wantlist=True) }}"
```

Or just skip the `api_key`, `github_org` and `github_team` if you provide the
 `GITHUB_API_KEY`, `GITHUB_ORG` and `GITHUB_TEAM` environment variables instead.
