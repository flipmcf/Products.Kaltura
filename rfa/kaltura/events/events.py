from zope.lifecycleevent.interfaces import IObjectAddedEvent
from Products.CMFCore.utils import getToolByName

from rfa.kaltura.kalturaapi.KalturaClient import *
#kaltura mucks around with sys.path when KalturaClient is imported
# putting the plugins folder as a root package... yuck
#from rfa.kaltura.kalturaapi.plugins.KalturaMetadataClientPlugin import *

from KalturaMetadataClientPlugin import *


from rfa.kaltura.config import PARTNER_ID, SECRET, ADMIN_SECRET, SERVICE_URL, USER_NAME

#XXX Make plone logger, setlevel, etc
class KalturaLogger(IKalturaLogger):
    def log(self, msg):
        logging.info(msg) 

def addVideo(context, event):
    """take video data from context and ship it to Kaltura"""
    
    print "addVideo Event!"
        

def modifyVideo(context, event):
    
    print "modifyVideo Event!"

    
    
def kupload(data):
    
    #XXX Configure Temporary Directory and name better
    #XXX Turn into a file stream from context.get_data to avoid write to file...    
    
    tempfh = open('/tmp/tempfile', 'wr')
    tempfh.write(context.get_data())
    tempfh.close()    
    
    
    config = KalturaConfiguration(PARTNER_ID)
    config.serviceUrl = SERVICE_URL
    config.setLogger(KalturaLogger())
    client = KalturaClient(config)

    # start new session (client session is enough when we do operations in a users scope)
    ks = client.generateSession(ADMIN_SECRET, USER_NAME, KalturaSessionType.ADMIN, PARTNER_ID, 86400, "")    
    client.setKs(ks)
        
    #create an entry
    mediaEntry = KalturaMediaEntry()
    mediaEntry.setName(context.Title())
    mediaEntry.setMediaType(KalturaMediaType(KalturaMediaType.VIDEO))
    mediaEntry.searchProviderId = context.UID()

    
    #do the upload
    uploadTokenId = client.media.upload(file('/temp/tempfile', 'rb'))  
    
    mediaEntry = client.media.addFromUploadedFile(mediaEntry, uploadTokenId)
    
    #grab the playback url
    return mediaEntry.dataUrl

    