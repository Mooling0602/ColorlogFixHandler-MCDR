import re

from strip_ansi import strip_ansi
from mcdreforged.utils import string_utils
from mcdreforged.info_reactor.info import InfoSource, Info
from mcdreforged.handler.impl import BukkitHandler

class ANSIRemovedHandler(BukkitHandler):
    def get_name(self) -> str:
        return 'ansi_removed_handler'

    # 从服务器标准输出中解析不含ANSI转义序列的文本日志结果
    @classmethod
    def get_server_stdout_raw_result(cls, text: str) -> Info:
        if type(text) is not str:
            raise TypeError('The text to parse should be a string')
        result = Info(InfoSource.SERVER, text)
        result.content = strip_ansi(string_utils.clean_console_color_code(text))
        return result

def on_load(server, prev_module):
    server.logger.info(server.rtr("ansi_removed_handler.tip1"))
    server.logger.info(server.rtr("ansi_removed_handler.tip2"))
    server.register_server_handler(ANSIRemovedHandler())
