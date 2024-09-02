from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import Client, Users
from diagrams.generic.device import Mobile
from diagrams.onprem.network import Nginx
from diagrams.onprem.compute import Server
from diagrams.onprem.queue import RabbitMQ
from diagrams.onprem.database import PostgreSQL
from diagrams.generic.blank import Blank

with Diagram("App Architecture"):

    ingress = Nginx("Nginx")
    likes_queue = RabbitMQ("Likes Queue")
    likes_processed_queue = RabbitMQ("Saved Likes Queue")
    database = PostgreSQL("Likes Database")

    with Cluster("Clients") as clients:
        clients = Users("A lot of users hit \nlike to a post") >> Mobile("Mobile")

        clients >> ingress

    with Cluster("App Servers - N"):
        servers = [
            Server("app-server-3"),
            Server("app-server-2"),
            Server("app-server-1")
            ]
        servers >> likes_queue
        
    with Cluster("Background Workers - N"):
        workers = [
            Server("worker 3"),
            Server("worker 2"),
            Server("worker 1"),
            ]
        
        likes_queue >> workers
        
    with Cluster("Push Notification Servers - N"):
        push_notification_servers = [
            Server("To Mobile"),
            Server("To Mobile"),
            Server("To Mobile")
            ]
        
        workers >> likes_processed_queue >> push_notification_servers
        workers >> database
        
    ingress >> servers