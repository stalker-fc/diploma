def calculate_thermal_radiation_areas(
        input_data: InputData,
        configuration: Configuration
) -> Solution:
    thermal_radiation_areas = []
    for flare in input_data.flares:
        thermal_radiation_areas.extend(
            get_thermal_radiation_areas(
                flare,
                configuration
            )
        )

    return Solution(
        thermal_radiation_areas=thermal_radiation_areas
    )