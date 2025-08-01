# FitCal

FitCal é um projeto simples de aprendizado para calcular as calorias diárias recomendadas e dividir os macronutrientes entre refeições, de acordo com o perfil do usuário e o objetivo da dieta.

## Funcionalidades

- Calcula o gasto energético basal (TMB) e total.
- Permite selecionar objetivo da dieta (cutting, bulking, manutenção, etc).
- Divide as calorias e macronutrientes entre o número de refeições desejado.
- Interface gráfica intuitiva feita com Tkinter.

## Como usar

1. Instale as dependências (Tkinter já vem com Python padrão).
2. Execute o projeto:

```bash
python main.py
```

3. Preencha os dados solicitados na interface e clique em "Calcular".

## Aviso importante

**Este projeto é apenas para fins de aprendizado. Não utilize os dados gerados para montar uma dieta sem acompanhamento de um profissional de saúde ou nutricionista.**

## Estrutura do projeto

- `main.py`: ponto de entrada do programa.
- `modules/interface.py`: interface gráfica.
- `models/person.py`: lógica do perfil do usuário.
- `models/meal.py`: cálculo e distribuição das refeições.
- `models/diet.py`: definição dos tipos de dieta e macronutrientes.

## Licença

MIT License © 2025