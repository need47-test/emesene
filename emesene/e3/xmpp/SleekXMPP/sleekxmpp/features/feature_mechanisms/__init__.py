"""
    SleekXMPP: The Sleek XMPP Library
    Copyright (C) 2011  Nathanael C. Fritz
    This file is part of SleekXMPP.

    See the file LICENSE for copying permission.
"""

from sleekxmpp.plugins.base import register_plugin

from sleekxmpp.features.feature_mechanisms.mechanisms import FeatureMechanisms
from sleekxmpp.features.feature_mechanisms.stanza import Mechanisms
from sleekxmpp.features.feature_mechanisms.stanza import Auth
from sleekxmpp.features.feature_mechanisms.stanza import Success
from sleekxmpp.features.feature_mechanisms.stanza import Failure


register_plugin(FeatureMechanisms)


# Retain some backwards compatibility
feature_mechanisms = FeatureMechanisms
