class Building:
    """
    Параметры здания/строения/сооружения.
    """
    id: UUID = pydantic.Field(default=UUID(int=0), description="id параметров строения")
    building_type_id: UUID = pydantic.Field(default=UUID(int=0), description="тип строения")
    figure: Union[Circle, Rectangle] = pydantic.Field(
        default_factory=Circle,
        discriminator='figure_type',
        description="геометрическая форма строения")
    fire_resistance_rating: FireResistanceRating = pydantic.Field(
        default=FireResistanceRating.ONE,
        description="степень огнестойкости"
    )
    fire_danger_rating: FireDangerRating = pydantic.Field(
        default=FireDangerRating.LOW_FLAMMABLE,
        description="категория по взрывопожарной и пожарной опасности"
    )
    structural_fire_hazard_class: StructuralFireHazardClass = pydantic.Field(
        default=StructuralFireHazardClass.C0,
        description="класс конструктивной пожарной опасности"
    )
    functional_area: FunctionalAreaType = pydantic.Field(
        default=FunctionalAreaType.ONE,
        description="функциональная зона сооружения"
    )
    label: str = pydantic.Field(default_factory=str, description="обозначение на схеме")
    name: str = pydantic.Field(default_factory=str, description="название сооружения")
    capacity_m3: float = pydantic.Field(default=0., description="объем сооружения, м3")
    content_type_id: Optional[UUID] = pydantic.Field(default=None, description="id типа содержимого")
    height_m: Optional[float] = pydantic.Field(
        default=None,
        description="высота сооружения, м (задается только для факелов)"
    )
    flare_stack_diameter_m: Optional[float] = pydantic.Field(
        default=None,
        description="диаметр факельной трубы (задается только для факелов)"
    )
    is_permanent_staff_presence: bool = pydantic.Field(
        default=False,
        description="признак постоянного присутствия персонала на сооружении"
    )
    construction_type: ConstructionType = pydantic.Field(
        default=ConstructionType.OPEN_AREA,
        description="тип сооружения"
    )
    working_pressure_mpa: Optional[float] = pydantic.Field(default=None, description="рабочее давление установки, МПа")
    tank_location_type: Optional[TankLocationType] = pydantic.Field(default=None, description="тип ёмкости")


class BuildingFeature:
    feature_id: UUID = pydantic.Field(default=UUID(int=0), description="идентификатор расчётных данных")

    buildings: List[Building] = pydantic.Field(default_factory=list, description="")
