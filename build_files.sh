echo "build start"
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate

python manage.py collectstatic --noinput --clear

echo "build finished"