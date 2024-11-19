.. _overview:

Overview
===============
This project utilizes 3 core technologies:

* `Django <https://www.djangoproject.com>`_ provides the backbone for the backend
* `Django REST Framework (DRF) <https://www.django-rest-framework.org>`_ is the `REST`_ layer atop of Django
* `React-Admin <https://marmelab.com/react-admin/documentation.html>`_ is the React based frontend framework, utilizing `TypeScript`_.

All these tools are actively maintained with frequent releases. When in doubt, check
the official documentation.

Project structure
------------------
Before diving into the code, it may be helpful to get ones baring.

.. code-block:: text
   :emphasize-lines: 2, 10, 11, 20

   .
   ├── app
   │   ├── management
   │   │   └── commands
   │   ├── migrations
   │   ├── models
   │   ├── serializer
   │   ├── templates
   │   └── views
   ├── common
   ├── react-admin
   │   ├── public
   │   └── src
   │       ├── components
   │       ├── pages
   │       └── views
   │           ├── teams
   │           ├── users
   │           └── volunteers
   └── vms


.. note::
   The `docs` folder is excluded above since it is self-explanatory. The `docker_init` folder
   is excluded brevity. Please check its README for more information.

* ``app`` is where all backend code lives. Changes to Django or DRF are made here. This folder is divided into logical sub-folders.
   * `management` is for custom `Django admin commands`_ like ``sync`` or ``mimesis``
   * `migrations` stores Django `migration files`_. These are files used to track changes (e.g., adding/removing fields) to models.
   * `models` contains all the application `models`_ (i.e., tables). Each file corresponds to an individual table and describes the properties and behavior, including `making queries`_.
   * `serializer` includes `DRF serializers`_ that are responsible converting models to JSON for the frontend 
   * `templates` is for `Django templates`_. As a REST based backend, the app does not make heavy use of templates. Out of the box, templates are only used to style and format the ETL report email
   * `views` contains all application views (or API endpoints). Based on the URL, incoming requests are routed to the appropriate view to be handled. The view to URL mapping is done in ``app/urls.py``.
* ``common`` includes utilities and other shared helpers
* ``react-admin`` stores all frontend code. Similar to ``app`` it is divided into sub-folders.
   * `public` allows you to include images and other stuff into the frontend
   * `src` is the source folder for the frontend. It is divided into components (stand-alone React components), pages (stand-alone pages) and views (core views).
* ``vms`` is the Django project configuration folder. A Django project can contain multiple apps (read: sites). As shipped, this project contains only one, simply named ``app``.


.. _REST: https://en.wikipedia.org/wiki/REST
.. _Django admin commands: https://docs.djangoproject.com/en/5.1/ref/django-admin/
.. _migration files: https://docs.djangoproject.com/en/5.1/topics/migrations/
.. _models: https://docs.djangoproject.com/en/5.1/topics/db/models/
.. _making queries: https://docs.djangoproject.com/en/5.1/topics/db/queries/
.. _DRF serializers: https://www.django-rest-framework.org/api-guide/serializers/
.. _Django templates: https://docs.djangoproject.com/en/5.1/topics/templates/
.. _ViewSets: https://www.django-rest-framework.org/api-guide/viewsets/
.. _TypeScript: https://www.typescriptlang.org