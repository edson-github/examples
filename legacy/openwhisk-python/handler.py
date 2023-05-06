def hello(params):
    name = params.get("name", "stranger")
    greeting = f"Hello {name}!"
    print(greeting)
    return {"greeting": greeting}
