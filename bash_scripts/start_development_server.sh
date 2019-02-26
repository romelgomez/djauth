# Start the development server
# 
# python manage.py runserver 
# 
# In https >>> test environment only
# 
# python manage.py runserver_plus --cert-file test_server.crt

python manage.py runsslserver --certificate certificates/test_server.crt --key certificates/test_server.key