import random
import datetime
from dataclasses import dataclass

COUNT_CHECK_LAST_MESSAGE = 10
MAX_LEN_TEXT = 130


def check_message_id(message):
    if hasattr(message, 'message_id'):
        return message.message_id
    elif hasattr(message, 'id') and not message.from_user.is_bot:
        return int(message.id)
    return None


def find_context_from_list(id_message, context_list):
    for iter_mes in reversed(context_list):
        if iter_mes.message.id == id_message:
            return iter_mes
    return None


@dataclass
class Context:
    message: all
    context_list: list
    tree: all = None

    def __post_init__(self):

        self.attention = {}

        if len(self.context_list) == 0:
            return

        last_context = self.context_list[-1]

        if hasattr(self.message, 'reply_to_message_id'):
            prev_context = find_context_from_list(self.message.reply_to_message_id, self.context_list)
            self.__post_mess(prev_context)

        if last_context.message.date + datetime.timedelta(seconds=15) > self.message.date \
                and last_context.message.from_user.id == self.message.from_user.id:
            self.__post_mess(last_context)

        if self.message.from_user.is_bot and last_context.message.from_user.is_bot:
            self.__post_mess(last_context)

        self.attention[self.message.from_user.id] = 0

    def __post_mess(self, prev_context, user_id=None):

        if self.tree is None:

            if prev_context is None:
                return
            prev_message = prev_context.message
            if user_id is None:
                user_id = prev_message.from_user.id

            self.tree = prev_context

            if user_id in self.attention:
                self.attention[user_id] += 3
            else:
                self.attention[user_id] = 3

            print(f"post mess - {self.message.text} - {prev_context.message.text}")

        return

    def get_context(self, bot_id, text=""):

        if text == "":
            self.attention[bot_id] /= 2

        if len(self.message.text) > len(text) * 2:
            add_text = ""
            cont = self.message.text.split(" ")
            for iter_cont in reversed(sorted(cont, key=len)):
                if len(add_text) < len(text) * 2:
                    add_text += f" {iter_cont}"
        else:
            add_text = self.message.text

        text = f"{add_text} {text}."
        if self.tree is not None:
            if len(f"{self.tree.message.text} {text}") < MAX_LEN_TEXT:
                return self.tree.get_context(bot_id, text=text)
        return text


class BOTkash:

    def __init__(self,
                 name: str,
                 memory_context_size: int,
                 sleep_time: tuple,
                 activity: float,
                 token: str,
                 context_list: list):

        self.name = name
        self.memory_context_size = memory_context_size
        self.sleep_time = sleep_time
        self.activity = activity
        self.token = token
        self.context_list = context_list

    def probability(self):
        return random.random() < self.activity

    def get_sleep(self):
        return random.randint(self.sleep_time[0], self.sleep_time[1])

    def choice_input_text(self):

        context = None
        res_context = None
        res_message_id = None

        if len(self.context_list) > 0:

            bot_id = int(self.token.split(":")[0])

            for iter_context in reversed(self.context_list[-COUNT_CHECK_LAST_MESSAGE:]):
                if bot_id not in iter_context.attention:
                    iter_context.attention[bot_id] = 1
                if iter_context.attention[bot_id] >= 1:
                    if context is None:
                        context = iter_context
                    if int(max(iter_context.attention, key=iter_context.attention.get, default=0)) == bot_id and iter_context.attention[bot_id] > context.attention[bot_id]:
                        context = iter_context

            if context is not None:

                context.attention[bot_id] = context.attention[bot_id] / 2

                res_context = context.get_context(bot_id)
                if not context.message.from_user.is_bot:
                    res_message_id = context.message.id

        return res_context, res_message_id
