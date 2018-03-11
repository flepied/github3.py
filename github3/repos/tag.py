# -*- coding: utf-8 -*-
"""This module contains the RepoTag object for GitHub's tag API."""
from __future__ import unicode_literals

from . import commit
from .. import models


class RepoTag(models.GitHubCore):
    """Representation of a tag made on a GitHub repository.

    .. note::

        This is distinct from :class:`~github3.git.Tag`. This object
        has information specific to a tag on a *GitHub* repository.
        That includes URLs to the tarball and zipball files auto-generated
        by GitHub.

    See also: http://developer.github.com/v3/repos/#list-tags

    This object has the following attributes:

    .. attribute:: commit

        .. versionchanged:: 1.0.0

            This attribute used to be a two item dictionary.

        A :class:`~github3.repos.commit.MiniCommit` object representing the
        commit this tag references.

    .. attribute:: name

        The name of this tag, e.g., ``v1.0.0``.

    .. attribute:: tarball_url

        The URL for the tarball file generated by GitHub for this tag.

    .. attribute:: zipball_url

        The URL for the zipball file generated by GitHub for this tag.
    """

    def _update_attributes(self, tag):
        self.commit = commit.MiniCommit(tag['commit'], self)
        self.name = tag['name']
        self.tarball_url = tag['tarball_url']
        self.zipball_url = tag['zipball_url']

    def _repr(self):
        return '<Repository Tag [{0}]>'.format(self)

    def __str__(self):
        return self.name
