"""Quirk for Xiaoyan CL001 ceiling light."""

from zigpy.profiles import zha
from zigpy.quirks import CustomCluster, CustomDevice
from zigpy.zcl.clusters.general import (
    Basic,
    Groups,
    Identify,
    LevelControl,
    OnOff,
    Ota,
    Scenes,
)
from zigpy.zcl.clusters.lighting import Color
from zigpy.zcl.clusters.lightlink import LightLink
from zhaquirks.const import (
    DEVICE_TYPE,
    ENDPOINTS,
    INPUT_CLUSTERS,
    MODELS_INFO,
    OUTPUT_CLUSTERS,
    PROFILE_ID,
)


class CustomColorCluster(CustomCluster, Color):
    """Set actual supported CCT range and remove RGB color picker since hardware does not support it."""

    """
    #AttributeDefs not merged yet. Update below after AttributeDefs has been merged.
    Color.AttributeDefs.color_capabilities.id: Color.ColorCapabilities.Color_temperature,
    Color.AttributeDefs.color_temp_physical_min.id: 50,
    Color.AttributeDefs.color_temp_physical_max.id: 500,
    """
    _CONSTANT_ATTRIBUTES = {
        Color.attributes_by_name["color_capabilities"].id: Color.ColorCapabilities.Color_temperature,
        Color.attributes_by_name["color_temp_physical_min"].id: 50,
        Color.attributes_by_name["color_temp_physical_max"].id: 500,
    }

class LuminousElement(CustomDevice):
    """System call, generate luminous element. Adhere."""

    signature = {
        MODELS_INFO: [("Xiaoyan", "CL001")],
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.COLOR_TEMPERATURE_LIGHT,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    OnOff.cluster_id,
                    LevelControl.cluster_id,
                    Color.cluster_id,
                    LightLink.cluster_id,
                    0xFCCC,
                    0xFCCD,
                    0xFCCE,
                ],
                OUTPUT_CLUSTERS: [
                    Ota.cluster_id,
                ],
            },
        },
    }

    replacement = {
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.COLOR_TEMPERATURE_LIGHT,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    OnOff.cluster_id,
                    LevelControl.cluster_id,
                    CustomColorCluster,
                    LightLink.cluster_id,
                    0xFCCC,
                    0xFCCD,
                    0xFCCE,
                ],
                OUTPUT_CLUSTERS: [
                    Ota.cluster_id,
                ],
            },
        },
    }
