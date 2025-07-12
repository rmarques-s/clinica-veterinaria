from flask import Flask
from sqlalchemy import text
from database import init_db
from api import clinica_routes, veterinario_routes, tutor_routes, pet_routes, atendimento_routes
from database import init_db, db
from models import clinica, veterinario, tutor, pet, atendimento

app = Flask(__name__)
init_db(app)

app.register_blueprint(clinica_routes.bp, url_prefix="/api")
app.register_blueprint(veterinario_routes.bp, url_prefix="/api")
app.register_blueprint(tutor_routes.bp, url_prefix="/api")
app.register_blueprint(pet_routes.bp, url_prefix="/api")
app.register_blueprint(atendimento_routes.bp, url_prefix="/api")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        try:
            db.session.execute(text('SELECT 1'))
            print("✅ Conexão com o banco de dados bem-sucedida!")
        except Exception as e:
            print("❌ Erro ao conectar com o banco de dados:", e)

    app.run(debug=True)
