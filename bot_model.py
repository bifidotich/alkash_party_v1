import random


class BOTkash:

    def __init__(self,
                 name: str,
                 memory_context_size: int,
                 sleep_time: tuple,
                 activity: int,
                 token: str):

        self.name = name
        self.memory_context_size = memory_context_size
        self.sleep_time = sleep_time
        self.activity = activity
        self.token = token

        self.memory_context = [" "]
        self.probability_list = [1] * self.activity + [0] * (100 - self.activity)

    def check_memory(self):
        if len(self.memory_context) < 2: self.memory_context.append(" ")
        if len(self.memory_context) > self.memory_context_size:
            self.memory_context.pop(0)
            self.check_memory()

    def probability(self):
        if random.choice(self.probability_list) == 1: return True
        else: return False

    def choice_input(self):
        in_text = f"{random.choice(self.memory_context)} {self.memory_context[-1]}"
        self.check_memory()
        if self.name == "OLEG":
            in_text = f"{random.choice(self.memory_context)} {self.memory_context[-1]}"
        if self.name == "ANDREY":
            in_text = f"{self.memory_context[-1]}"
        if self.name == "IGOR":
            in_text = f"{self.memory_context[-1]} {random.choice(self.memory_context)}"
        #self.memory_context.remove(in_text)
        return in_text

    def get_sleep(self):
        return random.randint(self.sleep_time[0], self.sleep_time[1])

    def post_message(self, new_message):
        self.memory_context.append(new_message)
        self.check_memory()

    def text_for_generate(self, main_text=None):
        self.check_memory()
        if main_text is None: return f"{str(self.choice_input())}"
        else: return f"{main_text}"











