cenergy_insights
================

* Start the app: python app.py

* Start celery worker: celery -A app.celery worker -l info -P gevent
(-P gevent, cause we are using gevent socket.io and we're monkeypatching!)
(note: --purge to purge jobs queue before starting the worker)

* Start celerybeat: celery -A app.celery beat -l info
(note: start celerybeat in a stand-alone mode, cause you can't start it with -B option to the worker, as we're using -P)