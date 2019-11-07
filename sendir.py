#!/usr/bin/env python3

import os
import pathlib

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

LIGHT_OFF_PATTERN = (str(SCRIPT_DIR) + '/ir_patterns/off.txt')
LIGHT_MAX_PATTERN = (str(SCRIPT_DIR) + '/ir_patterns/max.txt')
LIGHT_NIGHTLIGHT_PATTERN = (str(SCRIPT_DIR) + '/ir_patterns/nightlight.txt')
LIGHT_INCREASE_BRIGHTNESS_PATTERN = (str(SCRIPT_DIR) + '/ir_patterns/increase_brightness.txt')
LIGHT_DECREASE_BRIGHTNESS_PATTERN = (str(SCRIPT_DIR) + '/ir_patterns/decrease_brightness.txt')


def send_ir(pattern_file_path):
    """
    赤外線を送信する

    Parameters
    ----------
    pattern_file_path : str
        送信する赤外線パターンを記録したファイルのパス

    Returns
    -------
    is_succeed : bool
        送信の成功/失敗
    """
    if os.path.isfile(pattern_file_path) is True:
        with open(pattern_file_path, 'r') as file:
            data = file.read()
            os.system('/usr/local/bin/bto_advanced_USBIR_cmd -d ' + data)
            return True
    else:
        return False


def send_light_off():
    """
    照明を消す

    Returns
    -------
    is_succeed : bool
        送信の成功/失敗
    """
    is_succeed = send_ir(LIGHT_OFF_PATTERN)
    if is_succeed:
        return True
    else:
        return False


def send_light_on():
    """
    照明を点ける

    Returns
    -------
    is_succeed : bool
        送信の成功/失敗
    """
    is_succeed = send_ir(LIGHT_MAX_PATTERN)
    if is_succeed:
        return True
    else:
        return False


def send_light_nightlight():
    """
    常夜灯を点ける

    Returns
    -------
    is_succeed : bool
        送信の成功/失敗
    """
    is_succeed = send_ir(LIGHT_NIGHTLIGHT_PATTERN)
    if is_succeed:
        return True
    else:
        return False


def send_light_increase():
    """
    照明の輝度を上げる

    Returns
    -------
    is_succeed : bool
        送信の成功/失敗
    """
    is_succeed = send_ir(LIGHT_INCREASE_BRIGHTNESS_PATTERN)
    if is_succeed:
        return True
    else:
        return False


def send_light_decrease():
    """
    照明の輝度を下げる

    Returns
    -------
    is_succeed : bool
        送信の成功/失敗
    """
    is_succeed = send_ir(LIGHT_DECREASE_BRIGHTNESS_PATTERN)
    if is_succeed:
        return True
    else:
        return False


if __name__ == '__main__':
    send_light_on()
