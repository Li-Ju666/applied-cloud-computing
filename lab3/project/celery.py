from celery import Celery

app = Celery('project', 
             broker='pyamqp://guest@localhost//', 
             backend='rpc://', 
             include=['project.tasks'])

if __name__=='__main__':
    app.start()
