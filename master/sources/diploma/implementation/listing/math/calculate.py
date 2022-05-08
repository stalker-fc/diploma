def calculate_thermal_radiation_areas(
        input_data: InputData,
        configuration: Configuration
) -> Solution:
    thermal_radiation_areas = []
    for flare in input_data.flares:
        thermal_emissivity = get_thermal_emissivity(flare, configuration)
        quantity_of_heat = get_quantity_of_heat_generated_by_flame(flare,
                                                                   configuration.sun_radiation_value,
                                                                   thermal_emissivity)
        flame_deflection_angle = get_flame_deflection_angle(flare, configuration, quantity_of_heat)

        thermal_radiation_areas.extend(get_thermal_radiation_areas(
            flare,
            configuration.sun_radiation_value,
            thermal_emissivity,
            quantity_of_heat,
            flame_deflection_angle
        ))

    return Solution(
        thermal_radiation_areas=thermal_radiation_areas
    )