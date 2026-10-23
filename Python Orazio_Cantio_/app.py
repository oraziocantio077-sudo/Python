from flask import Flask, request, render_template, redirect, url_for
import joblib
import pandas as pd

app = Flask(__name__)

pipeline_m = None

try:
    pipeline_m = joblib.load("modello_mutuo.joblib")
except Exception as e:
    print(f"Errore nel caricamento del modello: {e}")

@app.route('/', methods = ['GET'])
def index():
    return render_template('form.html')

@app.route('/mutuo_p', methods = ['POST'])
def mutuo_p():
    try:
        dati_form = {
            'Gender': str(request.form.get('genere', 'Male')).strip(),
            'Married': str(request.form.get('stato_civile', 'No')).strip(),
            'Dependents': str(request.form.get('numero_figli', '0')).strip(),  # Ottima intuizione mantenerlo stringa per la pipeline
            'Education': str(request.form.get('istruzione', 'Graduate')).strip(),
            'ApplicantIncome': int(request.form.get('reddito_richiedente') or 0),
            'CoapplicantIncome': float(request.form.get('reddito_co_richiedente') or 0.0),
            'Self_Employed': str(request.form.get('self_employed', 'No')).strip(),
            'LoanAmount': float(request.form.get('loanamount') or 0.0),
            'Loan_Amount_Term': float(request.form.get('durata_mutuo') or 360.0),  # Default a 360 mesi se vuoto
            'Credit_History': float(request.form.get('credit_history') or 1.0),
            'Property_Area': str(request.form.get('property_area', 'Urban')).strip()     
        }

        df_input = pd.DataFrame([dati_form])
        
        if pipeline_m is not None:
            predizione = pipeline_m.predict(df_input)
            esito = int(predizione[0])
        else:
            esito = 1

        if esito == 1:
            return redirect(url_for('success'))
        else:
            return redirect(url_for('fail'))

    except Exception as e:
        
        print(f"Errore riscontrato: {e}")
        return render_template('form.html')

@app.route('/success', methods = ['GET'])
def success():
    return render_template('success.html')

@app.route('/fail', methods = ['GET'])
def fail():
    return render_template('fail.html')


if __name__ == '__main__':
    app.run(debug=True)