from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from user_operaetions import UserOperaetions
from user_dao import UserDao


class Bot:
    def __init__(self):
        self.token = '1570865930:AAFQNWHJW-s4JQVk7G13SbOUMdBhcB_Kkcc'
        self.bot_user_name = 'yad2_zohar_bot'
        self.bot_name = 'yad2_zohar'
        self.updater = Updater(self.token, use_context=True)
        self.user_operations = UserOperaetions()
        self.user_dao = UserDao()
        self.dp = self.updater.dispatcher
        self.updater.start_polling()
        self.updater.idle()


    def start(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

    def create_user(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="adding your values")
        user = self.user_operations.create_user(user_name=context.args[0], password=context.args[1], adv_key=context.args[2])
        self.user_dao.insert_user_name(user)

    def validate_user(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="checking your values")
        user_name = self.user_operations.validate_user_exist(context.args[0])
        if not user_name:
            context.bot.send_message(chat_id=update.effective_chat.id, text="user doesn't exist")
            return False
        return True

    def adv_key(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="checking your values")
        if self.validate_user(update, context):
            streets = self.user_dao.get_streets()
            context.bot.send_message(chat_id=update.effective_chat.id, text=streets)

    def unknown(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


if __name__ == '__main__':
    bot = Bot()
    bot.dp.add_handler(CommandHandler("start", bot.start))
    bot.dp.add_handler(CommandHandler("user", bot.create_user))
    unknown_handler = MessageHandler(Filters.command, bot.unknown)
    bot.dp.add_handler(unknown_handler)


