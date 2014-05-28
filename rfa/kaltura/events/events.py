from ZPublisher.HTTPRequest import FileUpload as FileUploadClass

from rfa.kaltura.interfaces import IKalturaPlaylist

from rfa.kaltura.kutils import KalturaLoggerInstance as logger
from rfa.kaltura.kutils import kupload, kcreatePlaylist, kcreateVideo
from rfa.kaltura.kutils import kdiff

def initVideo(context, event):
    """Fired when the object is first populated"""

    KMediaEntry = kcreateVideo(context)
    datafile = context.REQUEST.form.get('file_file')
    if isinstance(datafile, FileUploadClass):
        KMediaEntry = kupload(context, KMediaEntry)    
        
    context.setKalturaObject(KMediaEntry)
        
def modifyVideo(context, event):
    """Fired when the object is edited
       Any differences between plone object (context) and kaltura object
       are considered edits to the kaltura object, and are sent to kaltura
    """    
    changed_fields = kdiff(context, context.KalturaObject)
    if changed_fields:
        kwargs = {}
        for (pfield, kfield) in changed_fields:
            #get value from plone object
            val = getattr(context, pfield)
            if callable(val):
                val = val()
           
            #make sure that kfield is an attribute name:
            #not the name of the getter method
            kfieldAttr = getattr(context.KalturaObject, kfield)
            if callable(kfieldAttr):
                #it's a setter or getter.
                if kfield.startswith('get'):
                    kfield = kfield[3:]
                else:
                    #it's simply the name of the attribute... do nothing
                    pass
                
            #scalars:
            if kfield in ['Name', 'Description', 'PartnerId', 'Tags']:
                kwargs[kfield] = val
            elif kfield == 'Categories': #handle categories separately
                context.updateCategories(val)
                
        context._updateRemote(**kwargs)
            
        
    #has video file changed?
    status = context.REQUEST.form.get('file_delete')
    if status in ("nochange", None):
        pass #not modified
    else:
        #File Modification Occured
        context.setKalturaObject(kupload(context))

def addVideo(context, event):
    """When a video is added to a container
       zope.lifecycleevent.interfaces.IObjectAddedEvent"""
    pass
    
    
###Playlist Events###    
    
def initPlaylist(context, event):
    """Fired when the playlist object is created"""
    context.setKalturaObject(kcreatePlaylist(context))
    
def modifyPlaylist(context, event):
    """Fired when the playlist object itself is edited"""
    pass
    
