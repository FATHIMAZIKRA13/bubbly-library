from app import app, db
from app.models import User

with app.app_context():
    admin = User.query.filter_by(username='admin').first()
    if not admin:
        admin = User(username='admin', email='admin@bubbly.com', role='admin')
        admin.set_password('admin123')
        db.session.add(admin)
        db.session.commit()
        print("✅ Admin created successfully!")
        print("Email: admin@bubbly.com")
        print("Password: admin123")
    else:
        print("Admin already exists.")