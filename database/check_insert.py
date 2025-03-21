from database.database import SessionLocal
from database.models import Algorithm

def check_algorithms():
    db = SessionLocal()
    try:
        algorithms = db.query(Algorithm).all()
        if algorithms:
            print("Algoritmii existenți în baza de date:")
            for algo in algorithms:
                print(f"ID: {algo.id}, Name: {algo.name}")
        else:
            print("Nu există algoritmi în baza de date.")
    except Exception as e:
        print(f"Eroare la interogare: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    check_algorithms()
