from diagrams import Diagram, Cluster
from diagrams.onprem.compute import Server
from diagrams.onprem.queue import RabbitMQ

with Diagram("App Architecture"):

    mails_queue = RabbitMQ("Mails Queue")

    with Cluster("N - App Servers"):
        app_servers = [Server("App server - 3"),Server("App server - 2"),Server("App server - 1")]
        app_servers >> mails_queue
    
    with Cluster("N - Mail Sending Workers"):
        mail_processing_workers = [Server("Worker - 2"),Server("Worker - 1")]
        mails_queue >> mail_processing_workers
    