from celery import Celery

app = Celery('project', 
             broker='pyamqp://admin:admin@rabbit:5672//', 
             backend='rpc://', 
             include=['project.tasks'])

if __name__=='__main__':
    app.start()
