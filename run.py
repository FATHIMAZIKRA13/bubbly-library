from app import app, db

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("✅ Bubbly Library database ready!")
    print("💖 Bubbly Library is running at http://127.0.0.1:5000")
    app.run(debug=True)