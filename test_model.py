# ✅ Test local pour valider le modèle avant déploiement
import xgboost as xgb
import numpy as np
import os

def test_model():
    if not os.path.exists("model.json"):
        print("❌ Le fichier model.json est introuvable.")
        return

    try:
        model = xgb.XGBClassifier()
        model.load_model("model.json")
        print("✅ Modèle chargé avec succès")

        # Exemple de test avec 2 ratings
        input_data = np.array([[85.0, 77.0]])
        prediction = model.predict(input_data)[0]
        probabilities = model.predict_proba(input_data)[0]

        result_label = (
            "Team 1 wins" if prediction == 1 else
            "Team 2 wins" if prediction == 2 else
            "Draw"
        )

        print(f"🧠 Résultat : {result_label}")
        print("📊 Probabilités :")
        print(f"  Team 1 : {round(probabilities[1] * 100, 2)}%")
        print(f"  Team 2 : {round(probabilities[2] * 100, 2)}%")
        print(f"  Draw   : {round(probabilities[0] * 100, 2)}%")

    except Exception as e:
        print(f"❌ Erreur lors du test : {e}")

if __name__ == "__main__":
    test_model()
