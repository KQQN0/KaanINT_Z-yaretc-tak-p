from app import app, db, User, Visitor
import json

def export_data_to_json():
    with app.app_context():
        
        users = User.query.all()
        users_data = []
        for user in users:
            users_data.append({
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'password': user.password,
                'is_admin': user.is_admin
            })

        
        visitors = Visitor.query.all()
        visitors_data = []
        for visitor in visitors:
            visitors_data.append({
                'id': visitor.id,
                'ad': visitor.ad,
                'soyad': visitor.soyad,
                'ziyaret_saati': visitor.ziyaret_saati,
                'ziyaret_suresi': visitor.ziyaret_suresi,
                'user_id': visitor.user_id
            })

        # JSON dosyalarına yaz
        with open('users.json', 'w', encoding='utf-8') as f:
            json.dump(users_data, f, ensure_ascii=False, indent=4)

        with open('visitors.json', 'w', encoding='utf-8') as f:
            json.dump(visitors_data, f, ensure_ascii=False, indent=4)

        print("✔ Kullanıcılar 'users.json' ve ziyaretçiler 'visitors.json' dosyalarına başarıyla aktarıldı.")

if __name__ == '__main__':
    export_data_to_json()