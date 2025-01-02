# Formations-api-en-python
Cours de programmation de api en python 

# What is an API

- Application Programming Interface
- Application ➡ code that runs an does something
- Programming ➡ providing instructions to perform a task
- Interface
    - How things are allowed to interact with each other

# What is an Interface

    - A car's interface are the steering wheel, the pedals, and the knobs in the dashboard
    - The interface between car ad driver
    - A restaurant's server (waiter) may be thought of as the interface between customer and chef
    - What about a code interface ?
    - Example :
                _db = {}

                def add_post(title, body):
                    _db[title] = body

                def find_post(title):
                    return _db[title]


                from db import add_post, find_post

                add_post("Hello", "Hello, world!")
                print(find_post("Hello"))

# What is a web API ?

    - Just like the code file, but instead of one code file asking another file to do something (by running a function), one program asks another program over the internet
    - This is done by the client sending a request

            GET  /post/Hello
        Method     Endpoint

# What is in a request ?

    - A few pieces of data, wich are interpreted by the server however it wishes
    - Although there are some standards...
    - Method
    - Endpoint
    - Body
    - headers
    - view image schema-http-request

# What is JSON ?

JavaScript Object Notation. It's a language-agnostic way to share data.
Data is comprised of keys and values, like this:

        {
            "title": "Hello",
            "body": "Hello, world!",
            "user_id": 3,
            "tags": ["news", "code"]
        }
Because it's easy to convert to a string, we tend to use it to share data between client and server.

# What is REST ?

Architectural constraints

    - What are the REST constraints
        - Should use the concepts of "client" and "sever"
        - Should use the concpts of "resource"
        - Should be stateless
        - Should be cacheable
        - Should have a uniform, hypermedia-driven interface
        - If the backend uses multiples servers, this should be invisible to the client

# What is a resource ?

    - "Things" that the API deals in
        - Posts, comments, likes, users, etc.
    - When the client makes a request, it's a request about a particular resource
        - E.g give me the post with ID 3
    - When the server reponds to a request, it does so with a resource representation
        - E.g   
                {
                    "id": 123,
                    "title": "post, title here",
                    "body": "body of the post here"
                    "user_id": 3
                }

# What does stateless mean ?

    - The sever doesn't keep any information about the clients
    - For example, let's say the client wants to:
        - Get information about post with ID 3
        - Change the post's title
    - This should be two requests (one GET and one PATCH)
    - In both requests, the client must say what post it's talking about
    - For the second request, the sever can't remember that the first request was about post 3

# What does cacheable mean ?

    - If one client makes a request for information. it should be possible for the backend te save that response
    - So if another client makes a request for the same information, it doesn't have to be recalculated

# What does hypermedia-driven mean ?

    - If a resource is related te another resource, thre should be an actual link in the response which allows the client to "find" the related resources

    Instead of this              ---->           Do this
    {                                           {
        "id": 123,                                  "id": 123,
        "title": "post, title here",                "title": "post, title here",
        "body": "body of the post here"             "body": "body of the post here"
        "user_id": 3                                "user_id": 3
                                                    "user_link": "/user/3"
    }                                           }

# What does multiple servers mean ?

    - Sometimes our backend are made up of multiple servers
    - For example, one server for posts and comments
    - Another for user authentications and registation
    - The client shouldn't care about how the backend is organised



