   #!/bin/bash

   set -o errexit

   cd MyProject  # Navigate to the MyProject directory

   pip install -r requirements.txt

   python manage.py collectstatic --no-input
   python manage.py migrate