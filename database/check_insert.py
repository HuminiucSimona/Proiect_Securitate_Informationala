from crud import create_framework, get_framework, get_frameworks, update_framework, delete_framework
from database import get_db

db = next(get_db())
#new_framework = create_framework(db, "OpenSSL2")

updated_framework = update_framework(db, 4, "OpenSSL2")
#print(updated_framework)

framework = get_framework(db, 3)
print(framework)

frameworks = get_frameworks(db)
for f in frameworks:
    print(f)

# Ștergere framework
#delete_framework = delete_framework(db, 1)
#print(f"Deleted: {delete_framework}")