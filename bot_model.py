import random


def check_message_id(message):

    if hasattr(message, 'message_id'):
        return message.message_id
    elif hasattr(message, 'id') and not message.from_user.is_bot:
        return int(message.id)
    return None


class BOTkash:

    def __init__(self,
                 name: str,
                 memory_context_size: int,
                 sleep_time: tuple,
                 activity: float,
                 token: str):

        self.name = name
        self.memory_context_size = memory_context_size
        self.sleep_time = sleep_time
        self.activity = activity
        self.token = token

        self.memory_context = []
        self.last_message = None

    def check_memory(self):
        if len(self.memory_context) < 1 and self.last_message is not None:
            self.memory_context.append(self.last_message)
        if len(self.memory_context) > self.memory_context_size:
            self.memory_context.pop(0)
            self.check_memory()

    def probability(self):
        return random.random() < self.activity

    def choice_input_text(self):
        in_text = None
        return_message_id = None

        self.check_memory()
        if len(self.memory_context) > 3:

            first_message = random.choice(self.memory_context[:-1])
            last_message = self.memory_context[-1]

            return_message_id = check_message_id(first_message)
            if return_message_id is None:
                return_message_id = check_message_id(last_message)

            if first_message.text != last_message.text:
                in_text = f"{first_message.text} {last_message.text}"
            else:
                in_text = f"{first_message.text}"

            self.memory_context.remove(first_message)
            self.memory_context.remove(last_message)
            return in_text, return_message_id

        elif len(self.memory_context) > 0:

            last_message = self.memory_context[-1]
            return_message_id = check_message_id(last_message)

            in_text = last_message.text

            self.memory_context.remove(last_message)

        return in_text, return_message_id

    def get_sleep(self):
        return random.randint(self.sleep_time[0], self.sleep_time[1])

    def post_message(self, new_message):
        if new_message.text not in [iter.text for iter in self.memory_context]:
            self.memory_context.append(new_message)
            self.check_memory()
