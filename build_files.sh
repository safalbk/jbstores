echo "build start"
pip install -r requirements.txt
python3.9 manage.py collectstatic --noinpout --clear
echo "build finished"