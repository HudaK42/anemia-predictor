import numpy as np
import pickle
import pandas as pd
from flask import Flask, render_template, request
from forms.anemia_form import AnemiaForm

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = 'any_secret_key'  # Needed for CSRF

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def home():
    form = AnemiaForm()
    if form.validate_on_submit():
        try:
            features = np.array([[  # 🛡️ Try parsing the input
                int(form.Gender.data),
                float(form.Hemoglobin.data),
                float(form.MCH.data),
                float(form.MCHC.data),
                float(form.MCV.data)
            ]])
            df = pd.DataFrame(features, columns=['Gender', 'Hemoglobin', 'MCH', 'MCHC', 'MCV'])
            prediction = model.predict(df)[0]
            result = "You have anemic disease" if prediction == 1 else "You don’t have any anemic disease"
            return render_template('predict.html', prediction_text=result)
        
        except Exception as e:
            print("Error during prediction:", e)
            return render_template('predict.html', prediction_text="Something went wrong. Please check your input.")
    
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True, port=5000)


