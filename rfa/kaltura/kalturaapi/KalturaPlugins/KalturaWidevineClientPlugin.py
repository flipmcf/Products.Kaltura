# ===================================================================================================
#                           _  __     _ _
#                          | |/ /__ _| | |_ _  _ _ _ __ _
#                          | ' </ _` | |  _| || | '_/ _` |
#                          |_|\_\__,_|_|\__|\_,_|_| \__,_|
#
# This file is part of the Kaltura Collaborative Media Suite which allows users
# to do with audio, video, and animation what Wiki platfroms allow them to do with
# text.
#
# Copyright (C) 2006-2011  Kaltura Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http:#www.gnu.org/licenses/>.
#
# @ignore
# ===================================================================================================
# @package External
# @subpackage Kaltura
import os.path
import sys

clientRoot = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
if not clientRoot in sys.path:
    sys.path.append(clientRoot)

from KalturaCoreClient import *
from KalturaClientBase import *

########## enums ##########
# @package External
# @subpackage Kaltura
class KalturaWidevineRepositorySyncMode:
    MODIFY = 0

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package External
# @subpackage Kaltura
class KalturaWidevineFlavorAssetOrderBy:
    CREATED_AT_ASC = "+createdAt"
    DELETED_AT_ASC = "+deletedAt"
    SIZE_ASC = "+size"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    DELETED_AT_DESC = "-deletedAt"
    SIZE_DESC = "-size"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package External
# @subpackage Kaltura
class KalturaWidevineFlavorParamsOrderBy:

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package External
# @subpackage Kaltura
class KalturaWidevineFlavorParamsOutputOrderBy:

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
# @package External
# @subpackage Kaltura
class KalturaWidevineRepositorySyncJobData(KalturaJobData):
    def __init__(self,
            syncMode=NotImplemented,
            wvAssetIds=NotImplemented,
            modifiedAttributes=NotImplemented,
            monitorSyncCompletion=NotImplemented):
        KalturaJobData.__init__(self)

        # @var KalturaWidevineRepositorySyncMode
        self.syncMode = syncMode

        # @var string
        self.wvAssetIds = wvAssetIds

        # @var string
        self.modifiedAttributes = modifiedAttributes

        # @var int
        self.monitorSyncCompletion = monitorSyncCompletion


    PROPERTY_LOADERS = {
        'syncMode': (KalturaEnumsFactory.createInt, "KalturaWidevineRepositorySyncMode"), 
        'wvAssetIds': getXmlNodeText, 
        'modifiedAttributes': getXmlNodeText, 
        'monitorSyncCompletion': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaJobData.fromXml(self, node)
        self.fromXmlImpl(node, KalturaWidevineRepositorySyncJobData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaJobData.toParams(self)
        kparams.put("objectType", "KalturaWidevineRepositorySyncJobData")
        kparams.addIntEnumIfDefined("syncMode", self.syncMode)
        kparams.addStringIfDefined("wvAssetIds", self.wvAssetIds)
        kparams.addStringIfDefined("modifiedAttributes", self.modifiedAttributes)
        kparams.addIntIfDefined("monitorSyncCompletion", self.monitorSyncCompletion)
        return kparams

    def getSyncMode(self):
        return self.syncMode

    def setSyncMode(self, newSyncMode):
        self.syncMode = newSyncMode

    def getWvAssetIds(self):
        return self.wvAssetIds

    def setWvAssetIds(self, newWvAssetIds):
        self.wvAssetIds = newWvAssetIds

    def getModifiedAttributes(self):
        return self.modifiedAttributes

    def setModifiedAttributes(self, newModifiedAttributes):
        self.modifiedAttributes = newModifiedAttributes

    def getMonitorSyncCompletion(self):
        return self.monitorSyncCompletion

    def setMonitorSyncCompletion(self, newMonitorSyncCompletion):
        self.monitorSyncCompletion = newMonitorSyncCompletion


# @package External
# @subpackage Kaltura
class KalturaWidevineFlavorAsset(KalturaFlavorAsset):
    def __init__(self,
            id=NotImplemented,
            entryId=NotImplemented,
            partnerId=NotImplemented,
            version=NotImplemented,
            size=NotImplemented,
            tags=NotImplemented,
            fileExt=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            deletedAt=NotImplemented,
            description=NotImplemented,
            partnerData=NotImplemented,
            partnerDescription=NotImplemented,
            actualSourceAssetParamsIds=NotImplemented,
            flavorParamsId=NotImplemented,
            width=NotImplemented,
            height=NotImplemented,
            bitrate=NotImplemented,
            frameRate=NotImplemented,
            isOriginal=NotImplemented,
            isWeb=NotImplemented,
            containerFormat=NotImplemented,
            videoCodecId=NotImplemented,
            status=NotImplemented,
            widevineDistributionStartDate=NotImplemented,
            widevineDistributionEndDate=NotImplemented,
            widevineAssetId=NotImplemented):
        KalturaFlavorAsset.__init__(self,
            id,
            entryId,
            partnerId,
            version,
            size,
            tags,
            fileExt,
            createdAt,
            updatedAt,
            deletedAt,
            description,
            partnerData,
            partnerDescription,
            actualSourceAssetParamsIds,
            flavorParamsId,
            width,
            height,
            bitrate,
            frameRate,
            isOriginal,
            isWeb,
            containerFormat,
            videoCodecId,
            status)

        # License distribution window start date
        # @var int
        self.widevineDistributionStartDate = widevineDistributionStartDate

        # License distribution window end date
        # @var int
        self.widevineDistributionEndDate = widevineDistributionEndDate

        # Widevine unique asset id
        # @var int
        self.widevineAssetId = widevineAssetId


    PROPERTY_LOADERS = {
        'widevineDistributionStartDate': getXmlNodeInt, 
        'widevineDistributionEndDate': getXmlNodeInt, 
        'widevineAssetId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFlavorAsset.fromXml(self, node)
        self.fromXmlImpl(node, KalturaWidevineFlavorAsset.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFlavorAsset.toParams(self)
        kparams.put("objectType", "KalturaWidevineFlavorAsset")
        kparams.addIntIfDefined("widevineDistributionStartDate", self.widevineDistributionStartDate)
        kparams.addIntIfDefined("widevineDistributionEndDate", self.widevineDistributionEndDate)
        kparams.addIntIfDefined("widevineAssetId", self.widevineAssetId)
        return kparams

    def getWidevineDistributionStartDate(self):
        return self.widevineDistributionStartDate

    def setWidevineDistributionStartDate(self, newWidevineDistributionStartDate):
        self.widevineDistributionStartDate = newWidevineDistributionStartDate

    def getWidevineDistributionEndDate(self):
        return self.widevineDistributionEndDate

    def setWidevineDistributionEndDate(self, newWidevineDistributionEndDate):
        self.widevineDistributionEndDate = newWidevineDistributionEndDate

    def getWidevineAssetId(self):
        return self.widevineAssetId

    def setWidevineAssetId(self, newWidevineAssetId):
        self.widevineAssetId = newWidevineAssetId


# @package External
# @subpackage Kaltura
class KalturaWidevineFlavorParams(KalturaFlavorParams):
    def __init__(self,
            id=NotImplemented,
            partnerId=NotImplemented,
            name=NotImplemented,
            systemName=NotImplemented,
            description=NotImplemented,
            createdAt=NotImplemented,
            isSystemDefault=NotImplemented,
            tags=NotImplemented,
            requiredPermissions=NotImplemented,
            sourceRemoteStorageProfileId=NotImplemented,
            remoteStorageProfileIds=NotImplemented,
            mediaParserType=NotImplemented,
            sourceAssetParamsIds=NotImplemented,
            videoCodec=NotImplemented,
            videoBitrate=NotImplemented,
            audioCodec=NotImplemented,
            audioBitrate=NotImplemented,
            audioChannels=NotImplemented,
            audioSampleRate=NotImplemented,
            width=NotImplemented,
            height=NotImplemented,
            frameRate=NotImplemented,
            gopSize=NotImplemented,
            conversionEngines=NotImplemented,
            conversionEnginesExtraParams=NotImplemented,
            twoPass=NotImplemented,
            deinterlice=NotImplemented,
            rotate=NotImplemented,
            operators=NotImplemented,
            engineVersion=NotImplemented,
            format=NotImplemented,
            aspectRatioProcessingMode=NotImplemented,
            forceFrameToMultiplication16=NotImplemented,
            isGopInSec=NotImplemented,
            isAvoidVideoShrinkFramesizeToSource=NotImplemented,
            isAvoidVideoShrinkBitrateToSource=NotImplemented,
            isVideoFrameRateForLowBrAppleHls=NotImplemented,
            anamorphicPixels=NotImplemented,
            isAvoidForcedKeyFrames=NotImplemented,
            maxFrameRate=NotImplemented,
            videoConstantBitrate=NotImplemented,
            videoBitrateTolerance=NotImplemented,
            clipOffset=NotImplemented,
            clipDuration=NotImplemented):
        KalturaFlavorParams.__init__(self,
            id,
            partnerId,
            name,
            systemName,
            description,
            createdAt,
            isSystemDefault,
            tags,
            requiredPermissions,
            sourceRemoteStorageProfileId,
            remoteStorageProfileIds,
            mediaParserType,
            sourceAssetParamsIds,
            videoCodec,
            videoBitrate,
            audioCodec,
            audioBitrate,
            audioChannels,
            audioSampleRate,
            width,
            height,
            frameRate,
            gopSize,
            conversionEngines,
            conversionEnginesExtraParams,
            twoPass,
            deinterlice,
            rotate,
            operators,
            engineVersion,
            format,
            aspectRatioProcessingMode,
            forceFrameToMultiplication16,
            isGopInSec,
            isAvoidVideoShrinkFramesizeToSource,
            isAvoidVideoShrinkBitrateToSource,
            isVideoFrameRateForLowBrAppleHls,
            anamorphicPixels,
            isAvoidForcedKeyFrames,
            maxFrameRate,
            videoConstantBitrate,
            videoBitrateTolerance,
            clipOffset,
            clipDuration)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFlavorParams.fromXml(self, node)
        self.fromXmlImpl(node, KalturaWidevineFlavorParams.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFlavorParams.toParams(self)
        kparams.put("objectType", "KalturaWidevineFlavorParams")
        return kparams


# @package External
# @subpackage Kaltura
class KalturaWidevineFlavorParamsOutput(KalturaFlavorParamsOutput):
    def __init__(self,
            id=NotImplemented,
            partnerId=NotImplemented,
            name=NotImplemented,
            systemName=NotImplemented,
            description=NotImplemented,
            createdAt=NotImplemented,
            isSystemDefault=NotImplemented,
            tags=NotImplemented,
            requiredPermissions=NotImplemented,
            sourceRemoteStorageProfileId=NotImplemented,
            remoteStorageProfileIds=NotImplemented,
            mediaParserType=NotImplemented,
            sourceAssetParamsIds=NotImplemented,
            videoCodec=NotImplemented,
            videoBitrate=NotImplemented,
            audioCodec=NotImplemented,
            audioBitrate=NotImplemented,
            audioChannels=NotImplemented,
            audioSampleRate=NotImplemented,
            width=NotImplemented,
            height=NotImplemented,
            frameRate=NotImplemented,
            gopSize=NotImplemented,
            conversionEngines=NotImplemented,
            conversionEnginesExtraParams=NotImplemented,
            twoPass=NotImplemented,
            deinterlice=NotImplemented,
            rotate=NotImplemented,
            operators=NotImplemented,
            engineVersion=NotImplemented,
            format=NotImplemented,
            aspectRatioProcessingMode=NotImplemented,
            forceFrameToMultiplication16=NotImplemented,
            isGopInSec=NotImplemented,
            isAvoidVideoShrinkFramesizeToSource=NotImplemented,
            isAvoidVideoShrinkBitrateToSource=NotImplemented,
            isVideoFrameRateForLowBrAppleHls=NotImplemented,
            anamorphicPixels=NotImplemented,
            isAvoidForcedKeyFrames=NotImplemented,
            maxFrameRate=NotImplemented,
            videoConstantBitrate=NotImplemented,
            videoBitrateTolerance=NotImplemented,
            clipOffset=NotImplemented,
            clipDuration=NotImplemented,
            flavorParamsId=NotImplemented,
            commandLinesStr=NotImplemented,
            flavorParamsVersion=NotImplemented,
            flavorAssetId=NotImplemented,
            flavorAssetVersion=NotImplemented,
            readyBehavior=NotImplemented,
            widevineDistributionStartDate=NotImplemented,
            widevineDistributionEndDate=NotImplemented):
        KalturaFlavorParamsOutput.__init__(self,
            id,
            partnerId,
            name,
            systemName,
            description,
            createdAt,
            isSystemDefault,
            tags,
            requiredPermissions,
            sourceRemoteStorageProfileId,
            remoteStorageProfileIds,
            mediaParserType,
            sourceAssetParamsIds,
            videoCodec,
            videoBitrate,
            audioCodec,
            audioBitrate,
            audioChannels,
            audioSampleRate,
            width,
            height,
            frameRate,
            gopSize,
            conversionEngines,
            conversionEnginesExtraParams,
            twoPass,
            deinterlice,
            rotate,
            operators,
            engineVersion,
            format,
            aspectRatioProcessingMode,
            forceFrameToMultiplication16,
            isGopInSec,
            isAvoidVideoShrinkFramesizeToSource,
            isAvoidVideoShrinkBitrateToSource,
            isVideoFrameRateForLowBrAppleHls,
            anamorphicPixels,
            isAvoidForcedKeyFrames,
            maxFrameRate,
            videoConstantBitrate,
            videoBitrateTolerance,
            clipOffset,
            clipDuration,
            flavorParamsId,
            commandLinesStr,
            flavorParamsVersion,
            flavorAssetId,
            flavorAssetVersion,
            readyBehavior)

        # License distribution window start date
        # @var int
        self.widevineDistributionStartDate = widevineDistributionStartDate

        # License distribution window end date
        # @var int
        self.widevineDistributionEndDate = widevineDistributionEndDate


    PROPERTY_LOADERS = {
        'widevineDistributionStartDate': getXmlNodeInt, 
        'widevineDistributionEndDate': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFlavorParamsOutput.fromXml(self, node)
        self.fromXmlImpl(node, KalturaWidevineFlavorParamsOutput.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFlavorParamsOutput.toParams(self)
        kparams.put("objectType", "KalturaWidevineFlavorParamsOutput")
        kparams.addIntIfDefined("widevineDistributionStartDate", self.widevineDistributionStartDate)
        kparams.addIntIfDefined("widevineDistributionEndDate", self.widevineDistributionEndDate)
        return kparams

    def getWidevineDistributionStartDate(self):
        return self.widevineDistributionStartDate

    def setWidevineDistributionStartDate(self, newWidevineDistributionStartDate):
        self.widevineDistributionStartDate = newWidevineDistributionStartDate

    def getWidevineDistributionEndDate(self):
        return self.widevineDistributionEndDate

    def setWidevineDistributionEndDate(self, newWidevineDistributionEndDate):
        self.widevineDistributionEndDate = newWidevineDistributionEndDate


# @package External
# @subpackage Kaltura
class KalturaWidevineFlavorAssetBaseFilter(KalturaFlavorAssetFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            entryIdEqual=NotImplemented,
            entryIdIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            sizeGreaterThanOrEqual=NotImplemented,
            sizeLessThanOrEqual=NotImplemented,
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            deletedAtGreaterThanOrEqual=NotImplemented,
            deletedAtLessThanOrEqual=NotImplemented,
            flavorParamsIdEqual=NotImplemented,
            flavorParamsIdIn=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            statusNotIn=NotImplemented):
        KalturaFlavorAssetFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            entryIdEqual,
            entryIdIn,
            partnerIdEqual,
            partnerIdIn,
            sizeGreaterThanOrEqual,
            sizeLessThanOrEqual,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            deletedAtGreaterThanOrEqual,
            deletedAtLessThanOrEqual,
            flavorParamsIdEqual,
            flavorParamsIdIn,
            statusEqual,
            statusIn,
            statusNotIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFlavorAssetFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaWidevineFlavorAssetBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFlavorAssetFilter.toParams(self)
        kparams.put("objectType", "KalturaWidevineFlavorAssetBaseFilter")
        return kparams


# @package External
# @subpackage Kaltura
class KalturaWidevineFlavorParamsBaseFilter(KalturaFlavorParamsFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            isSystemDefaultEqual=NotImplemented,
            tagsEqual=NotImplemented,
            formatEqual=NotImplemented):
        KalturaFlavorParamsFilter.__init__(self,
            orderBy,
            advancedSearch,
            systemNameEqual,
            systemNameIn,
            isSystemDefaultEqual,
            tagsEqual,
            formatEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFlavorParamsFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaWidevineFlavorParamsBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFlavorParamsFilter.toParams(self)
        kparams.put("objectType", "KalturaWidevineFlavorParamsBaseFilter")
        return kparams


# @package External
# @subpackage Kaltura
class KalturaWidevineFlavorAssetFilter(KalturaWidevineFlavorAssetBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            entryIdEqual=NotImplemented,
            entryIdIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            sizeGreaterThanOrEqual=NotImplemented,
            sizeLessThanOrEqual=NotImplemented,
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            deletedAtGreaterThanOrEqual=NotImplemented,
            deletedAtLessThanOrEqual=NotImplemented,
            flavorParamsIdEqual=NotImplemented,
            flavorParamsIdIn=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            statusNotIn=NotImplemented):
        KalturaWidevineFlavorAssetBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            entryIdEqual,
            entryIdIn,
            partnerIdEqual,
            partnerIdIn,
            sizeGreaterThanOrEqual,
            sizeLessThanOrEqual,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            deletedAtGreaterThanOrEqual,
            deletedAtLessThanOrEqual,
            flavorParamsIdEqual,
            flavorParamsIdIn,
            statusEqual,
            statusIn,
            statusNotIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaWidevineFlavorAssetBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaWidevineFlavorAssetFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaWidevineFlavorAssetBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaWidevineFlavorAssetFilter")
        return kparams


# @package External
# @subpackage Kaltura
class KalturaWidevineFlavorParamsFilter(KalturaWidevineFlavorParamsBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            isSystemDefaultEqual=NotImplemented,
            tagsEqual=NotImplemented,
            formatEqual=NotImplemented):
        KalturaWidevineFlavorParamsBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            systemNameEqual,
            systemNameIn,
            isSystemDefaultEqual,
            tagsEqual,
            formatEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaWidevineFlavorParamsBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaWidevineFlavorParamsFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaWidevineFlavorParamsBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaWidevineFlavorParamsFilter")
        return kparams


# @package External
# @subpackage Kaltura
class KalturaWidevineFlavorParamsOutputBaseFilter(KalturaFlavorParamsOutputFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            isSystemDefaultEqual=NotImplemented,
            tagsEqual=NotImplemented,
            formatEqual=NotImplemented,
            flavorParamsIdEqual=NotImplemented,
            flavorParamsVersionEqual=NotImplemented,
            flavorAssetIdEqual=NotImplemented,
            flavorAssetVersionEqual=NotImplemented):
        KalturaFlavorParamsOutputFilter.__init__(self,
            orderBy,
            advancedSearch,
            systemNameEqual,
            systemNameIn,
            isSystemDefaultEqual,
            tagsEqual,
            formatEqual,
            flavorParamsIdEqual,
            flavorParamsVersionEqual,
            flavorAssetIdEqual,
            flavorAssetVersionEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFlavorParamsOutputFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaWidevineFlavorParamsOutputBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFlavorParamsOutputFilter.toParams(self)
        kparams.put("objectType", "KalturaWidevineFlavorParamsOutputBaseFilter")
        return kparams


# @package External
# @subpackage Kaltura
class KalturaWidevineFlavorParamsOutputFilter(KalturaWidevineFlavorParamsOutputBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            isSystemDefaultEqual=NotImplemented,
            tagsEqual=NotImplemented,
            formatEqual=NotImplemented,
            flavorParamsIdEqual=NotImplemented,
            flavorParamsVersionEqual=NotImplemented,
            flavorAssetIdEqual=NotImplemented,
            flavorAssetVersionEqual=NotImplemented):
        KalturaWidevineFlavorParamsOutputBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            systemNameEqual,
            systemNameIn,
            isSystemDefaultEqual,
            tagsEqual,
            formatEqual,
            flavorParamsIdEqual,
            flavorParamsVersionEqual,
            flavorAssetIdEqual,
            flavorAssetVersionEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaWidevineFlavorParamsOutputBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaWidevineFlavorParamsOutputFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaWidevineFlavorParamsOutputBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaWidevineFlavorParamsOutputFilter")
        return kparams


########## services ##########

# @package External
# @subpackage Kaltura
class KalturaWidevineDrmService(KalturaServiceBase):
    """WidevineDrmService serves as a license proxy to a Widevine license server"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def getLicense(self, flavorAssetId, referrer = NotImplemented):
        """Get license for encrypted content playback"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("flavorAssetId", flavorAssetId)
        kparams.addStringIfDefined("referrer", referrer)
        self.client.queueServiceActionCall("widevine_widevinedrm", "getLicense", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

########## main ##########
class KalturaWidevineClientPlugin(KalturaClientPlugin):
    # KalturaWidevineClientPlugin
    instance = None

    # @return KalturaWidevineClientPlugin
    @staticmethod
    def get():
        if KalturaWidevineClientPlugin.instance == None:
            KalturaWidevineClientPlugin.instance = KalturaWidevineClientPlugin()
        return KalturaWidevineClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'widevineDrm': KalturaWidevineDrmService,
        }

    def getEnums(self):
        return {
            'KalturaWidevineRepositorySyncMode': KalturaWidevineRepositorySyncMode,
            'KalturaWidevineFlavorAssetOrderBy': KalturaWidevineFlavorAssetOrderBy,
            'KalturaWidevineFlavorParamsOrderBy': KalturaWidevineFlavorParamsOrderBy,
            'KalturaWidevineFlavorParamsOutputOrderBy': KalturaWidevineFlavorParamsOutputOrderBy,
        }

    def getTypes(self):
        return {
            'KalturaWidevineRepositorySyncJobData': KalturaWidevineRepositorySyncJobData,
            'KalturaWidevineFlavorAsset': KalturaWidevineFlavorAsset,
            'KalturaWidevineFlavorParams': KalturaWidevineFlavorParams,
            'KalturaWidevineFlavorParamsOutput': KalturaWidevineFlavorParamsOutput,
            'KalturaWidevineFlavorAssetBaseFilter': KalturaWidevineFlavorAssetBaseFilter,
            'KalturaWidevineFlavorParamsBaseFilter': KalturaWidevineFlavorParamsBaseFilter,
            'KalturaWidevineFlavorAssetFilter': KalturaWidevineFlavorAssetFilter,
            'KalturaWidevineFlavorParamsFilter': KalturaWidevineFlavorParamsFilter,
            'KalturaWidevineFlavorParamsOutputBaseFilter': KalturaWidevineFlavorParamsOutputBaseFilter,
            'KalturaWidevineFlavorParamsOutputFilter': KalturaWidevineFlavorParamsOutputFilter,
        }

    # @return string
    def getName(self):
        return 'widevine'
