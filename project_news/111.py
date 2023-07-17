from django.contrib.auth.hashers import check_password

password_from_db = "pbkdf2_sha256$600000$HSWdzL2UycGH2BO4MbxZEf$MBisyNb3vVYLTI5xs4H0wmenzSA02c11928FMNb3U5M="
password_entered_by_user = "123456789"

# Сравниваем введенный пользователем пароль с паролем из базы данных
password_matched = check_password(password_entered_by_user, password_from_db)

if password_matched:
    print("Пароль совпадает")
else:
    print("Пароль не совпадает")