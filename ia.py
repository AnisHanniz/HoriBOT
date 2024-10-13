import json
import requests
import os
from conf import API_KEY, API_URL, KNOWLEDGE_FILE, MAX_TOKENS, TEMPERATURE

class IAAvancee:
    def __init__(self):
        self.knowledge = []
        self.api_key = API_KEY
        self.api_url = API_URL

    def learn(self, question, answer):
        self.knowledge.append({"question": question, "answer": answer})

    def answer(self, question):
        # Vérifie d'abord la base de connaissances locale
        for item in self.knowledge:
            if isinstance(item, dict):
                item_question = item.get("question", "") or item.get("pattern", "")
                if question.lower() in item_question.lower():
                    return item.get("answer", "Désolé, je n'ai pas de réponse pour cette question.")
            elif isinstance(item, str):
                if question.lower() in item.lower():
                    return "Désolé, je n'ai pas de réponse spécifique pour cette question."
        
        # Si pas de réponse locale, utilise l'API AI21 Labs
        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            data = {
                "prompt": f"Human: {question}\nAI:",
                "maxTokens": MAX_TOKENS,
                "temperature": TEMPERATURE
            }
            response = requests.post(self.api_url, headers=headers, json=data)
            response.raise_for_status()
            ai_response = response.json()["completions"][0]["data"]["text"].strip()
            return ai_response
        except Exception as e:
            return f"Désolé, je n'ai pas pu générer une réponse. Erreur: {str(e)}"

    def save_knowledge(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.knowledge, f)

    def load_knowledge(self, filename):
        try:
            with open(filename, 'r') as f:
                self.knowledge = json.load(f)
            print(f"Connaissances chargées depuis {filename}")
        except FileNotFoundError:
            print("Fichier de connaissances non trouvé. Création d'une nouvelle base de connaissances.")
        except json.JSONDecodeError:
            print("Erreur lors de la lecture du fichier de connaissances. Création d'une nouvelle base de connaissances.")
            self.knowledge = []

def main():
    ia = IAAvancee()
    
    ia.load_knowledge(KNOWLEDGE_FILE)

    print("Bienvenue dans votre assistant IA interactif amélioré avec AI21 Labs!")
    print("Vous pouvez poser des questions, ajouter de nouvelles connaissances, ou quitter.")
    print("Commandes spéciales:")
    print("  'apprendre' : pour ajouter une nouvelle connaissance")
    print("  'quitter' : pour terminer la session")

    while True:
        try:
            user_input = input("\nVotre question (ou commande) : ").strip()

            if user_input.lower() == 'quitter':
                print("Merci d'avoir utilisé l'assistant IA. Au revoir!")
                ia.save_knowledge(KNOWLEDGE_FILE)
                break

            elif user_input.lower() == 'apprendre':
                question = input("Entrez la question : ")
                answer = input("Entrez la réponse : ")
                ia.learn(question, answer)
                print("Nouvelle connaissance ajoutée!")

            else:
                response = ia.answer(user_input)
                print(f"HariBOT: {response}")

        except KeyboardInterrupt:
            print("\nInterruption détectée. Voulez-vous quitter ? (o/n)")
            if input().lower() == 'o':
                print("Merci d'avoir utilisé l'assistant IA. Au revoir!")
                ia.save_knowledge(KNOWLEDGE_FILE)
                break
            else:
                continue

if __name__ == "__main__":
    main()