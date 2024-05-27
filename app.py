import pandas as pd
from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')


car = pd.read_csv("car.csv")

@app.route('/')
def index():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    year = sorted(car['year'].unique(), reverse=True)

    # Check if "fuel_types" exists (case-sensitive)
    if 'fuel_types' in car.columns:
        fuel_types = sorted(car['fuel_types'].unique())
    else:
        # Handle missing column (e.g., create from another column if available)
        fuel_types = None  # Or create a placeholder

    return render_template('index.html', companies=companies, car_models=car_models, years=year, fuel_type=fuel_types)

if __name__ == '__main__':
    app.run(debug=True)
