class HelloWorld:
    def greet(
        self,
        hello_world: str = "Hello World!",
        x: int = 1,
        goodbye_world: str = "Goodbye World!",
    ) -> str:
        output = ""
        if x == 1:
            output = f"{hello_world}\nx is 1\n{goodbye_world}"
        else:
            output = f"{hello_world}\n{goodbye_world}"
        return output
