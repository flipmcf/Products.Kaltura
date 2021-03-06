from zope import schema
from zope.interface import Interface
from zope.schema.vocabulary import SimpleVocabulary

from plone.app.registry.browser import controlpanel

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('rfa.kaltura')



    

class IRfaKalturaSettings(Interface):
    """ Define settings data structure 
        PARTNER_ID = 54321
        SECRET = "YOUR_USER_SECRET"
        ADMIN_SECRET = "YOUR_ADMIN_SECRET"
        SERVICE_URL = "http://www.kaltura.com"
        USER_NAME = "testUser"
        
        optionally:
        TOP_LEVEL_CATEGORY
        PRIVACY_CONTEXT
    """

    partnerId = schema.Int(title=u"Partner Id",
                           __name__='partnerId',
                           description=u"enter your Partner ID",
                           required=True,
                           default=54321)
    
    secret = schema.TextLine(title=u"User Secret",
                             description=u"enter your 32-character User Secret",
                             required=True,
                             default=u"YOUR_USER_SECRET")
    
    adminSecret = schema.TextLine(title=u"Admin Secret",
                                  description=u"enter your 32-character Admin Secret",
                                  required=True,
                                  default=u"YOUR_ADMIN_SECRET")
    
    serviceUrl =  schema.TextLine(title=u"Service URL",
                                  description=u"enter your service url",
                                  required=True,
                                  default=u"http://www.kaltura.com")
    
    userName = schema.TextLine(title=u"User Name",
                               description=u"enter your username on Kaltura",
                               required=True,
                               default=u"PloneTestUser")
    
    defaultVideoPlayer = schema.TextLine(title=u"Default Video Player ID",
                                         description=u"enter the default Player ID you wish to use when creating Kaltura Videos",
                                         required=False,
                                         default=u'')
    
    #defaultPlaylistPlayer = schema.TextLine(title=u"Default Playlist Player ID",
                                         #description=u"enter the default Player ID you wish to use when creating Kaltura Playlists"
                                         #required=False,
                                         #default='')
    
    topLevelCategory = schema.TextLine(title=u"Top Level Category",
                                       description=u"""Use this to limit this plone site to a single category on the KMC.
                                                       Enter the FULL NAME of a category on the KMC to become the top level category
                                                       for this plone site.  Only this category and sub-categories will be
                                                       visible on edit pages, and all utilities will filter results
                                                       by this category""",
                                       required=False,
                                       default=u""
                                       )
    
    privacyContextString = schema.TextLine(title=u"Privacy Context",
                                           description=u"provide the privacy context if you are using entitlement settings\n Leave blank if unsure",
                                           required=False,
                                           default=u"")
    
    storageMethod = schema.Choice(title=u"Video Storage Method",
                                  description=u"""Choose how Plone will handle local storage of uploaded video content.
                                                 "Blob" (default) will store the file locally with ZODB Blob storage.
                                                 "None" will not store the video file locally at all - the kaltura server will have the only copy known to plone.
                                              """,
                                  required=True,
                                  default=u"Blob",
                                  vocabulary=SimpleVocabulary.fromValues([(u'Blob'),
                                                                          (u'No Local Storage')])
                                  )

    kfileMaxSize = schema.Int(title=u"Kaltura File Max Size",
                           description=u"Provide your maximum kaltura file size you want to set up.(unit: MB)",
                           required=False,
                           default=500)    
    

class SettingsEditForm(controlpanel.RegistryEditForm):
    schema = IRfaKalturaSettings
    label = u"rfa.kaltura settings"
    description = u""""""
    
    def updateFields(self):
        super(SettingsEditForm, self).updateFields()
        self.fields['partnerId'].widgetFactory = IntFieldWidget        
    
    def updateWidgets(self):
        super(SettingsEditForm, self).updateWidgets()    
        
class SettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = SettingsEditForm
    
##############

import zope.interface
import zope.component
import zope.schema.interfaces

import z3c.form.interfaces
from z3c.form.widget import FieldWidget
from z3c.form.browser.text import TextWidget
from z3c.form import converter

class IIntWidget(z3c.form.interfaces.ITextWidget):
    """Int Widget"""
    
class IntWidget(TextWidget):
    zope.interface.implementsOnly(IIntWidget)
    klass = u'int-widget'
    value = u''

@zope.component.adapter(zope.schema.interfaces.IField, z3c.form.interfaces.IFormLayer)
@zope.interface.implementer(z3c.form.interfaces.IFieldWidget)
def IntFieldWidget(field, request):
    """IFieldWidget factory for IntWidget."""
    return FieldWidget(field, IntWidget(request))

zope.component.provideAdapter(IntFieldWidget)

class NoFormatIntegerDataConverter(converter.IntegerDataConverter):
    """ data converter that ignores the formatter, 
        simply returns the unicode representation of the integer value

        The base class for this calls upon the locale for a formatter.
        This completely avoids calling the locale.
    """
    
    zope.component.adapts(zope.schema.interfaces.IInt, IIntWidget)    

    def toWidgetValue(self, value):
        if value is self.field.missing_value:
            return u''
        return unicode(value)
    
zope.component.provideAdapter(NoFormatIntegerDataConverter)