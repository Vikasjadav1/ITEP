# 30. Chatbot Reply System
# Problem Statement

# Different bots reply differently.

# Create:

# SupportBot
# SalesBot
# FAQBot
# Why These Problems Are Better for Interviews

# These focus on:

# business logic
# abstraction thinking
# code reusability
# real-world implementation
# polymorphism

# instead of only large architectures.


from abc import ABC, abstractmethod

class Chatbot(ABC):

    def __init__(self, bot_name, user_message):
        self.__bot_name = bot_name
        self.__user_message = user_message

    def get_name(self):
        return self.__bot_name

    def get_message(self):
        return self.__user_message

    @abstractmethod
    def reply(self):
        pass

    def display_details(self):
        print("Bot Name:", self.__bot_name)
        print("User Message:", self.__user_message)


class SupportBot(Chatbot):

    def reply(self):
        print("SupportBot: How can I help you with your problem?")


class SalesBot(Chatbot):

    def reply(self):
        print("SalesBot: Would you like to explore our products?")


class FAQBot(Chatbot):

    def reply(self):
        print("FAQBot: Here are the answers to frequently asked questions.")


s = SupportBot("Support Assistant", "I have a problem")
sa = SalesBot("Sales Assistant", "Show me products")
f = FAQBot("FAQ Assistant", "What are your services?")

s.display_details()
s.reply()

sa.display_details()
sa.reply()

f.display_details()
f.reply()