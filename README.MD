To Install this app
    clone the repo into your directory
    Create and run virtual environment
        Virtualenv venv
        source Venv/Scripts/activate

    Install dependancies
        pip install -r requirements.txt

    go to project
        cd HR_BACKEND_DJANGO

    Runserver to see if it actually works
        python manage.py runserver
    
    🌟🌟🌟🌟🌟 Congrats, You have Successfully installed the HR app 🌟🌟🌟🌟🌟

  
<h2> Backend </h2>
I started with creating the models for the database tables, 
    I sketched on a book then actualized with code and tested my implementations using  django admin

I created the serializers for my models and connected all the related fields

I proceeded to creating the views for the serialized models


Finally, I created the URLs for Routing into the RESTful APIS to get the JSON data


<h2> Frontend </h2>
After Further research I used Single File Component (SFC) for the ease of abstraction of
 different user information and over another level of security for the application 
The SFC is deployed on a different IP which will be connect to this website backend