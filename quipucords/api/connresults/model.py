#
# Copyright (c) 2017-2018 Red Hat, Inc.
#
# This software is licensed to you under the GNU General Public License,
# version 3 (GPLv3). There is NO WARRANTY for this software, express or
# implied, including the implied warranties of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. You should have received a copy of GPLv3
# along with this software; if not, see
# https://www.gnu.org/licenses/gpl-3.0.txt.
#
"""Defines the models used with the API application.

These models are used in the REST definitions
"""
import api.messages as messages
from api.credential.model import Credential
from api.source.model import Source

from django.db import models
from django.utils.translation import ugettext as _


class SystemConnectionResult(models.Model):
    """A key value pair of captured data."""

    SUCCESS = 'success'
    FAILED = 'failed'
    UNREACHABLE = 'unreachable'
    CONN_STATUS_CHOICES = ((SUCCESS, SUCCESS), (FAILED, FAILED),
                           (UNREACHABLE, UNREACHABLE))

    name = models.TextField()
    credential = models.ForeignKey(Credential,
                                   on_delete=models.SET_NULL,
                                   null=True)
    source = models.ForeignKey(Source,
                               on_delete=models.SET_NULL,
                               null=True)
    status = models.CharField(max_length=12, choices=CONN_STATUS_CHOICES)

    def __str__(self):
        """Convert to string."""
        return '{ id:%s, name:%s, status:%s, source:%s, credential:%s }' % \
            (self.id, self.name, self.status, self.source, self.credential)

    class Meta:
        """Metadata for model."""

        verbose_name_plural = _(messages.PLURAL_SYS_CONN_RESULTS_MSG)


class TaskConnectionResult(models.Model):
    """The captured connection results from a scan."""

    systems = models.ManyToManyField(SystemConnectionResult)

    def __str__(self):
        """Convert to string."""
        return '{ ' + 'id:{}, '\
            'sytems:{}'.format(self.id,
                               self.systems) + ' }'

    class Meta:
        """Metadata for model."""

        verbose_name_plural = _(messages.PLURAL_TASK_CONN_RESULTS_MSG)


class JobConnectionResult(models.Model):
    """The results of a connection scan."""

    task_results = models.ManyToManyField(TaskConnectionResult)

    def __str__(self):
        """Convert to string."""
        return '{ id:%s, task_results:%s }' % (self.id, self.task_results)

    class Meta:
        """Metadata for model."""

        verbose_name_plural = _(messages.PLURAL_JOB_CONN_RESULTS_MSG)
