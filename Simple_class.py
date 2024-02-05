class Person:
    def say(self, message):
        print(message)

    def say_hello(self):
        self.say("Hello, work")


tom = Person()
bob = Person()

tom.say('Hello, Чуваки')
tom.say_hello()
