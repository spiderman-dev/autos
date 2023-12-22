from django.contrib.auth import get_user_model

User = get_user_model()
username = 'admin'
email = 'spiderman.develop@gmail.com'
password = 'JAHA0109'

try:
    # Verificar si ya existe un superusuario con ese nombre de usuario
    existing_user = User.objects.get(username=username)
    print("Ya existe un superusuario")
except User.DoesNotExist:
    # Crear un nuevo superusuario si no existe
    User.objects.create_superuser(username=username, email=email, password=password)

