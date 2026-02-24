from app import db, app

#from app import db

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Ensure tables are created before starting the app
    app.run(port=9000, debug=True)