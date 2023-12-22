from django.contrib.auth.models import User

if __name__ == '__main__':
    # Crea un superuser con username 'admin', correo electrónico 'admin@example.com' y contraseña 'mypassword'.
    User.objects.create_superuser('admin', 'spiderman.develop@gmail.com', 'JAHA0109hr#')
