from plone.app.upgrade.utils import alias_module
from zope.interface import Interface
from unwicked import plone


class IBBB(Interface):
    pass

# drop wicked
try:
    from wicked.fieldevent.interfaces import IFieldValueSetter
    IFieldValueSetter  # noqa
except ImportError:
    alias_module('wicked.fieldevent.interfaces.IFieldValueSetter', IBBB)
    alias_module('wicked.plone', plone)
