class Diet:
    """
    Macronutrients in grams per kg of body weight
    """
    DIETS = {
        'extreme_cutting': {
            'gordura': 0.6,
            'proteina': 2.4
        },
        'cutting': {
            'gordura': 0.7,
            'proteina': 2.2
        },
        'mini_cutting': {
            'gordura': 0.8,
            'proteina': 2.0
        },
        'maintenance': {
            'gordura': 1.0,
            'proteina': 1.6
        },
        'mini_bulking': {
            'gordura': 1.0,
            'proteina': 1.8
        },
        'bulking': {
            'gordura': 1.0,
            'proteina': 1.8
        },
        'extreme_bulking': {
            'gordura': 1.2,
            'proteina': 2.0
        }
    }

    @classmethod
    def get_macros(cls, diet_type):
        return cls.DIETS.get(diet_type.lower(), cls.DIETS['maintenance'])