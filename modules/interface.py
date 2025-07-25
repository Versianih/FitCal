import tkinter as tk
from tkinter import ttk, messagebox, font

from models.person import Person
from models.meal import Meal

class Interface:
    COLORS = {
        'primary': "#2c3e50",
        'secondary': "#34495e", 
        'accent': "#e74c3c",
        'success': "#3498db",
        'text_primary': "#ecf0f1",
        'text_secondary': "#bdc3c7"
    }

    GEOMETRY = "500x650"

    DROPDOWN_LABELS = {
        'gender': {
            'Masculino': 'male',
            'Feminino': 'female'
        },
        'diet_type': {
            'Cutting Extremo': 'extreme_cutting',
            'Cutting': 'cutting',
            'Mini Cutting': 'mini_cutting',
            'Manutenção': 'maintenance',
            'Mini Bulking': 'mini_bulking',
            'Bulking': 'bulking',
            'Bulking Extremo': 'extreme_bulking'
        },
        'activity_level': {
            'Sedentário': 'sedentary',
            'Leve': 'light',
            'Moderado': 'moderate',
            'Intenso': 'intense',
            'Muito Intenso': 'very_intense'
        }
    }

    DROPDOWN_VALUES = {
        key: list(label_dict.keys())
        for key, label_dict in DROPDOWN_LABELS.items()
    }

    def __init__(self):
        self._setup_root()
        self._setup_fonts()
        self._setup_variables()
        self.setup_input_screen()

    def _setup_root(self):
        self.root = tk.Tk()
        self.root.title("Calculadora de Calorias")
        self.root.geometry(self.GEOMETRY)
        self.root.configure(bg=self.COLORS['primary'])

        self.style = ttk.Style()
        self.style.theme_use('clam')

    def _setup_fonts(self):
        self.fonts = {
            'title': font.Font(family="Arial", size=16, weight="bold"),
            'label': font.Font(family="Arial", size=10),
            'result': font.Font(family="Arial", size=11)
        }

    def _setup_variables(self):
        self.vars = {
            'weight': tk.StringVar(),
            'height': tk.StringVar(),
            'age': tk.StringVar(),
            'gender': tk.StringVar(),
            'diet_type': tk.StringVar(),
            'activity_level': tk.StringVar(),
            'meal_quantity': tk.StringVar()
        }

    def _clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def _create_main_frame(self):
        frame = tk.Frame(self.root, bg=self.COLORS['primary'])
        frame.pack(expand=True, fill="both", padx=20, pady=20)
        return frame

    def _create_title(self, parent, text, emoji=""):
        title_text = f"{emoji} {text}" if emoji else text
        title = tk.Label(
            parent,
            text=title_text,
            font=self.fonts['title'],
            bg=self.COLORS['primary'],
            fg=self.COLORS['text_primary']
        )
        return title

    def _create_label_frame(self, parent, title, emoji=""):
        frame_title = f"{emoji} {title}" if emoji else title
        frame = tk.LabelFrame(
            parent, 
            text=frame_title, 
            font=self.fonts['label'],
            bg=self.COLORS['secondary'], 
            fg=self.COLORS['text_primary'], 
            bd=2, 
            relief="groove"
        )
        return frame

    def _create_field_label(self, parent, text, row):
        label = tk.Label(
            parent,
            text=text,
            font=self.fonts['label'],
            bg=self.COLORS['primary'],
            fg=self.COLORS['text_secondary']
        )
        label.grid(row=row, column=0, padx=10, pady=5, sticky="e")
        return label

    def _create_entry(self, parent, textvariable, row, width=15):
        entry = tk.Entry(
            parent, 
            textvariable=textvariable, 
            font=self.fonts['label'], 
            width=width
        )
        entry.grid(row=row, column=1, padx=10, pady=5, sticky="w")
        return entry

    def _create_combobox(self, parent, textvariable, values, row, width=12):
        combo = ttk.Combobox(
            parent,
            textvariable=textvariable,
            values=values,
            state="readonly",
            width=width
        )
        combo.grid(row=row, column=1, padx=10, pady=5, sticky="w")
        return combo

    def _create_button(self, parent, text, command, color_key='accent', **kwargs):
        button = tk.Button(
            parent,
            text=text,
            command=command,
            font=self.fonts['label'],
            bg=self.COLORS[color_key],
            fg="white",
            relief="flat",
            padx=20,
            pady=10,
            **kwargs
        )
        return button

    def _create_info_label(self, parent, text):
        label = tk.Label(
            parent, 
            text=text, 
            font=self.fonts['result'],
            bg=self.COLORS['secondary'], 
            fg=self.COLORS['text_secondary'], 
            justify="center"
        )
        return label

    def _create_input_fields(self, parent):
        fields_config = [
            ("Peso (kg):", 'weight', 'entry'),
            ("Altura (cm):", 'height', 'entry'),
            ("Idade:", 'age', 'entry'),
            ("Sexo:", 'gender', 'combo'),
            ("Tipo de Dieta:", 'diet_type', 'combo'),
            ("Nível de Atividade:", 'activity_level', 'combo'),
            ("Qtd. Refeições:", 'meal_quantity', 'entry')
        ]

        for row, (label_text, var_name, field_type) in enumerate(fields_config):
            self._create_field_label(parent, label_text, row)

            if field_type == 'entry':
                self._create_entry(parent, self.vars[var_name], row)
            else:
                values = self.DROPDOWN_VALUES.get(var_name, [])
                self._create_combobox(parent, self.vars[var_name], values, row)

    def _validate_input_data(self):
        try:
            weight = float(self.vars['weight'].get().lower().replace(',', '.').replace('kg', ''))
            height = int(self.vars['height'].get().lower().replace('cm', ''))
            age = int(self.vars['age'].get())
            meal_quantity = int(self.vars['meal_quantity'].get())

            if weight <= 0 or height <= 0 or age <= 0 or meal_quantity <= 0:
                raise ValueError("Valores devem ser positivos")

            dropdown_vars = ['gender', 'diet_type', 'activity_level']
            if not all(self.vars[var].get() for var in dropdown_vars):
                raise ValueError("Selecione todas as opções de dropdowns")

            return {
                'weight': weight,
                'height': height,
                'age': age,
                'gender': self.DROPDOWN_LABELS['gender'][self.vars['gender'].get()],
                'diet_type': self.DROPDOWN_LABELS['diet_type'][self.vars['diet_type'].get()],
                'activity_level': self.DROPDOWN_LABELS['activity_level'][self.vars['activity_level'].get()],
                'meal_quantity': meal_quantity
            }

        except ValueError as e:
            raise e

    def _format_diet_type(self, diet_type):
        reversed_map = {v: k for k, v in self.DROPDOWN_LABELS['diet_type'].items()}
        return reversed_map.get(diet_type, diet_type)

    def _format_activity_level(self, activity_level):
        reversed_map = {v: k for k, v in self.DROPDOWN_LABELS['activity_level'].items()}
        return reversed_map.get(activity_level, activity_level)

    def _create_profile_section(self, parent, person):
        info_frame = self._create_label_frame(parent, "PERFIL", "👤")
        info_frame.pack(fill="x", pady=(0, 15), padx=20)

        profile_info = f"""
        Peso: {person.weight}kg
        Altura: {person.height}cm
        Idade: {person.age} anos
        Sexo: {"Masculino" if person.gender == 'male' else "Feminino"}
        Atividade: {self._format_activity_level(person.activity_level)}
        TMB: {int(person.basal)} kcal
        Gasto Total: {int(person.total_expenditure)} kcal
        """

        info_label = self._create_info_label(info_frame, profile_info)
        info_label.pack(pady=10)

    def _create_diet_plan_section(self, parent, person, distribution):
        plan_frame = self._create_label_frame(parent, "PLANO ALIMENTAR", "🍽️")
        plan_frame.pack(fill="x", pady=(0, 15), padx=20)

        plan_info = f"""
        Dieta: {self._format_diet_type(person.diet_type)}
        Calorias Totais: {distribution['total_kcal']} kcal
        Número de Refeições: {distribution['qtd_refeicoes']}
        Calorias por Refeição: {distribution['kcal_por_refeicao']} kcal
        """

        plan_label = self._create_info_label(plan_frame, plan_info)
        plan_label.pack(pady=10)

    def _create_macros_section(self, parent, macros):
        macro_frame = self._create_label_frame(parent, "MACRONUTRIENTES TOTAIS", "📊")
        macro_frame.pack(fill="x", pady=(0, 15), padx=20)

        macros_info = f"""
        🥩 Proteínas: {macros['proteina']['gramas']}g ({macros['proteina']['kcal']} kcal)
        🧈 Gorduras: {macros['gordura']['gramas']}g ({macros['gordura']['kcal']} kcal)
        🍞 Carboidratos: {macros['carboidrato']['gramas']}g ({macros['carboidrato']['kcal']} kcal)
        """

        macro_label = self._create_info_label(macro_frame, macros_info)
        macro_label.pack(pady=10)

    def _create_per_meal_section(self, parent, per_meal):
        per_meal_frame = self._create_label_frame(parent, "POR REFEIÇÃO", "🍽️")
        per_meal_frame.pack(fill="x", pady=(0, 15), padx=20)

        per_meal_info = f"""
        🥩 Proteínas: {per_meal['proteina_g']}g
        🧈 Gorduras: {per_meal['gordura_g']}g
        🍞 Carboidratos: {per_meal['carboidrato_g']}g
        """

        per_meal_label = self._create_info_label(per_meal_frame, per_meal_info)
        per_meal_label.pack(pady=10)

    def _create_scrollable_canvas(self, parent):
        canvas = tk.Canvas(parent, bg=self.COLORS['primary'], highlightthickness=0)
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=self.COLORS['primary'])

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        def _on_mousewheel(event):
            if event.delta:
                canvas.yview_scroll(int(-1*(event.delta/120)), "units")
            else:
                if event.num == 4:
                    canvas.yview_scroll(-1, "units")
                elif event.num == 5:
                    canvas.yview_scroll(1, "units")

        canvas.bind_all("<MouseWheel>", _on_mousewheel)
        canvas.bind_all("<Button-4>", _on_mousewheel)
        canvas.bind_all("<Button-5>", _on_mousewheel)

        return canvas, scrollbar, scrollable_frame

    def setup_input_screen(self):
        self._clear_screen()

        main_frame = self._create_main_frame()

        title = self._create_title(main_frame, "", "🍎")
        title.pack(pady=(0, 30))

        fields_frame = tk.Frame(main_frame, bg=self.COLORS['primary'])
        fields_frame.pack(expand=True)

        self._create_input_fields(fields_frame)

        calculate_btn = self._create_button(
            fields_frame, 
            "CALCULAR", 
            self.calculate
        )
        calculate_btn.grid(row=7, column=0, columnspan=2, pady=30)

        fields_frame.grid_columnconfigure(0, weight=1)
        fields_frame.grid_columnconfigure(1, weight=1)

    def calculate(self):
        try:
            data = self._validate_input_data()

            person = Person(
                weight=data['weight'], 
                height=data['height'], 
                age=data['age'], 
                gender=data['gender'], 
                diet_type=data['diet_type'], 
                activity_level=data['activity_level']
            )

            meal = Meal(
                person=person,
                meal_quantity=data['meal_quantity']
            )
            self.show_results(person, meal)

        except ValueError as e:
            messagebox.showerror("Erro", "Dados inválidos! \nCertifique-se de preencher os campos adequadamente")
        except Exception as e:
            print(e)
            messagebox.showerror("Erro", "Erro inesperado")

    def show_results(self, person, meal):
        self._clear_screen()

        main_frame = self._create_main_frame()

        title = self._create_title(main_frame, "RESULTADOS", "📊")
        title.pack(pady=(0, 20))

        canvas, scrollbar, scrollable_frame = self._create_scrollable_canvas(main_frame)

        distribution = meal.distribute_meals()

        self._create_profile_section(scrollable_frame, person)
        self._create_diet_plan_section(scrollable_frame, person, distribution)
        self._create_macros_section(scrollable_frame, distribution['macros_totais'])
        self._create_per_meal_section(scrollable_frame, distribution['por_refeicao'])

        back_btn = self._create_button(
            scrollable_frame,
            "⬅️ VOLTAR",
            self.setup_input_screen,
            'success'
        )
        back_btn.pack(pady=20)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        scrollable_frame.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))

    def run(self):
        self.root.mainloop()