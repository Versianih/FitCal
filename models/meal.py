from models.person import Person
from models.diet import Diet

class Meal:
    def __init__(self, 
                person: Person,
                meal_quantity: int
                ):
        
        self.person = person
        self.total_kcal = person.diet_expenditure
        self.meal_quantity = meal_quantity
    
    def calculate_macronutrients(self):
        weight = self.person.weight
        diet_macros = Diet.get_macros(self.person.diet_type)
        
        protein_g = weight * diet_macros['proteina']
        fat_g = weight * diet_macros['gordura']
        
        kcal_protein = protein_g * 4
        kcal_fat = fat_g * 9
        kcal_carbohydrate = self.total_kcal - (kcal_protein + kcal_fat)
        carbohydrate_g = kcal_carbohydrate / 4
        
        if kcal_carbohydrate < 0:
            kcal_carbohydrate = 0
            carbohydrate_g = 0
        
        return {
            'proteina': {'gramas': round(protein_g, 1), 'kcal': round(kcal_protein, 1)},
            'gordura': {'gramas': round(fat_g, 1), 'kcal': round(kcal_fat, 1)},
            'carboidrato': {'gramas': round(carbohydrate_g, 1), 'kcal': round(kcal_carbohydrate, 1)}
        }
    
    def distribute_meals(self):
        macros = self.calculate_macronutrients()
        
        distribution = {
            'total_kcal': self.total_kcal,
            'qtd_refeicoes': self.meal_quantity,
            'kcal_por_refeicao': round(self.total_kcal / self.meal_quantity, 1),
            'macros_totais': macros,
            'por_refeicao': {
                'proteina_g': round(macros['proteina']['gramas'] / self.meal_quantity, 1),
                'gordura_g': round(macros['gordura']['gramas'] / self.meal_quantity, 1),
                'carboidrato_g': round(macros['carboidrato']['gramas'] / self.meal_quantity, 1)
            }
        }
        
        return distribution