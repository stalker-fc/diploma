class GasFlare:
    id: UUID = UUID(int=0)
    diameter_m: float = 0.
    content_type: ContentType = ContentType.FLAMMABLE_LIQUID
    height_m: float = 0.


class InputData:
    flares: List[GasFlare] = field(default_factory=list)


class ThermalRadiationArea:
    flare_id: UUID = UUID(int=0)
    thermal_radiation_level: ThermalRadiationLevel = ThermalRadiationLevel.SAFE
    radius_m: float = 0.


class Solution:
    thermal_radiation_areas: List[ThermalRadiationArea] = field(default_factory=list)
