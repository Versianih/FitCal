class Person:
    def __init__(self, 
                weight: float,
                height: float,
                age: int,
                gender: str,
                diet_type: str,
                activity_level: str
                ):
        
        self.weight = weight
        self.height = height
        self.age = age
        self.gender = gender
        self.diet_type = diet_type
        self.activity_level = activity_level

        self.basal = self.calculate_bmr()
        self.total_expenditure = self.calculate_total_expenditure()
        self.diet_expenditure = self.calculate_diet_expenditure()

    def calculate_bmr(self):
        if self.gender.lower() == 'male':
            bmr = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) + 5
        else:
            bmr = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) - 161

        return bmr
    
    def calculate_total_expenditure(self):
        factors = {
            'sedentary': 1.2,
            'light': 1.375,
            'moderate': 1.55,
            'intense': 1.725,
            'very_intense': 1.9
        }

        return self.basal * factors.get(self.activity_level, 1.2)

    def calculate_diet_expenditure(self):
        diets = {
            'extreme_cutting': -500,
            'cutting': -300,
            'mini_cutting': -100,
            'maintenance': 0,
            'mini_bulking': 100,
            'bulking': 300,
            'extreme_bulking': 500
        }
        return int(self.total_expenditure + diets.get(self.diet_type, 0))