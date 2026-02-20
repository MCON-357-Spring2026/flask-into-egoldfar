# Reflection Questions

## 1. What does the `@app.route()` decorator actually do?

The `@app.route()` decorator registers a URL rule with the Flask application. It maps a specific URL path to the Python function defined directly below it, so that when a client makes a request to that URL, Flask knows which function to execute. Behind the scenes, it calls `app.add_url_rule()` to add the route to Flask's URL map.

## 2. How does Flask know which function to call when a request arrives?

Flask maintains an internal URL map that stores the mapping between URL patterns and their corresponding view functions (called "endpoints"). When a request arrives, Flask's routing system matches the incoming URL against the registered URL rules in the map. Once a match is found, Flask looks up the associated view function and calls it to generate the response.

## 3. What's the difference between route parameters (`<name>`) and query parameters (`?key=value`)?

Route parameters are part of the URL path itself and are defined directly in the route pattern (e.g., `/greet/<name>`). They are passed as arguments to the view function. Query parameters come after a `?` in the URL (e.g., `/calculate?num1=10&num2=5`) and are not part of the route pattern. They are accessed inside the function using `request.args.get()`. Route parameters are typically used for required values that identify a resource, while query parameters are used for optional or supplementary data.

## 4. Why do we need to use `request.get_json()` for POST requests but `request.args.get()` for GET query parameters?

The data is sent in different parts of the HTTP request. GET query parameters are included in the URL itself (after the `?`), so Flask parses them from the URL and makes them available through `request.args`. POST request data with JSON content is sent in the request body, not in the URL. `request.get_json()` reads the raw body of the request and parses it from JSON format into a Python dictionary. They are two different methods because the data lives in two different places in the HTTP request.

## 5. What happens if you try to access `request.args` outside of a request context?

You will get a `RuntimeError` with a message like: *"Working outside of request context."* The `request` object in Flask is a context-local proxy that only exists while Flask is actively handling a request. Outside of a request (for example, in a standalone script or at module-level code), there is no active request context, so the proxy has nothing to point to and raises an error.
