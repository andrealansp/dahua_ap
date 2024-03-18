import csv
import random
import re
import time

import requests
from openpyxl import load_workbook
from requests.auth import HTTPDigestAuth
from requests.exceptions import Timeout

wb = load_workbook(filename="dados.xlsx")
ws = wb.active
listaDadosLido = []
dados_lido_csv = {}


def gerar_lista_portas(ip, porta):
    try:
        urlport = (
            f"http://{ip}:{porta}/cgi-bin/configManager.cgi?action=getConfig&name=DVRIP"
        )
        s = requests.get(
            urlport, auth=HTTPDigestAuth("admin", "perkons6340"), timeout=1
        )
        returneddata = s.text.split("\r\n")
        time.sleep(0.2)
        resposta = returneddata[8]
        print(resposta)
        return re.sub(r"\w{5}.\w{5}.\w*.\w*[\D\w]{3}.\w{4}=", "PORTA:", returneddata[8])
    except Timeout:
        ...


def gerar_lista_serial(ip, porta):
    try:
        # ttp://<server>/
        urlport = f"http://{ip}:{porta}/cgi-bin/magicBox.cgi?action=getSerialNo"
        s = requests.get(
            urlport, auth=HTTPDigestAuth("admin", "perkons6340"), timeout=1.5
        )
        # (\w{2}=)(\d\w{14})
        returneddata = s.text.split("\r\n")
        time.sleep(0.5)
        return re.sub(r"(\w{2}=)(\d\w{14})", r" \2", returneddata[0])
    except Timeout:
        ...


def gerar_lista_modelos(ip, porta):
    try:
        urlport = f"http://{ip}:{porta}/cgi-bin/magicBox.cgi?action=getDeviceType"
        s = requests.get(
            urlport, auth=HTTPDigestAuth("admin", "perkons6340"), timeout=2
        )
        returneddata = s.text.split("\r\n")
        time.sleep(0.2)
        resposta = returneddata[0]
        return re.sub(r"(\w{4}.)(\w{6}.\w{4}.\w{3})", r" \2", returneddata[0])
    except Timeout:
        ...


def gerar_lista_firmeware(ip, porta):
    try:
        urlport = f"http://{ip}:{porta}/cgi-bin/magicBox.cgi?action=getSoftwareVersion"
        s = requests.get(
            urlport, auth=HTTPDigestAuth("admin", "perkons6340"), timeout=1
        )
        returneddata = s.text.split("\r\n")
        time.sleep(0.2)
        retorno_firmware = re.sub(
            r"(\w{7}.)(\d.\d{3}.[WG0-9]{7}.\d{1,2}.\w,)(\w{5}.)(\d{4}.\d{2}.\d{2})",
            r"Versão: \2 - Build: \4",
            returneddata[0],
        )
        return retorno_firmware
    except Timeout:
        ...
    except requests.exceptions.RetryError:
        ...
    except requests.exceptions.ConnectionError:
        ...


def listar_enconding_strateg(ip, porta):
    try:
        urlport = f"http://{ip}:{porta}/cgi-bin/configManager.cgi?action=getConfig&name=SmartEncode&name=AICoding"
        s = requests.get(
            urlport, auth=HTTPDigestAuth("admin", "perkons6340"), timeout=1
        )
        returneddata = s.text
        time.sleep(0.5)
        resposta_aicode = re.sub(
            r"(\w{5}).(\w{8,11})\D.\D.(\w{6}.)(\w{3,5})", r"\2 -\4", returneddata
        )
        return resposta_aicode
    except Timeout:
        ...


def configura_automaintain(ip, porta, opcao):
    opcoes = {
        "1": {
            "action": "setConfig",
            "AutoMaintain.AutoRebootDay": 1,
            "AutoMaintain.AutoRebootHour": 0,
            "AutoMaintain.AutoRebootMinute": 0,
        },
        "2": {
            "action": "setConfig",
            "AutoMaintain.AutoRebootDay": 2,
            "AutoMaintain.AutoRebootHour": 1,
            "AutoMaintain.AutoRebootMinute": 0,
        },
        "3": {
            "action": "setConfig",
            "AutoMaintain.AutoRebootDay": 3,
            "AutoMaintain.AutoRebootHour": 2,
            "AutoMaintain.AutoRebootMinute": 0,
        },
        "4": {
            "action": "setConfig",
            "AutoMaintain.AutoRebootDay": 4,
            "AutoMaintain.AutoRebootHour": 3,
            "AutoMaintain.AutoRebootMinute": 0,
        },
        "5": {
            "action": "setConfig",
            "AutoMaintain.AutoRebootDay": 5,
            "AutoMaintain.AutoRebootHour": 4,
            "AutoMaintain.AutoRebootMinute": 0,
        },
        "6": {
            "action": "setConfig",
            "AutoMaintain.AutoRebootDay": 6,
            "AutoMaintain.AutoRebootHour": 5,
            "AutoMaintain.AutoRebootMinute": 0,
        },
    }

    try:
        urlport = f"http://{ip}:{porta}/cgi-bin/configManager.cgi"
        s = requests.get(
            urlport,
            params=opcoes[str(opcao)],
            auth=HTTPDigestAuth("admin", "perkons6340"),
            timeout=1,
        )
        time.sleep(0.5)
        return s.status_code
    except Timeout:
        ...


def confiurar_tamanho_fontes(ip, porta) -> list:
    try:
        urlsport = [
            f"http://{ip}:{porta}/cgi-bin/configManager.cgi?action=setConfig&VideoWidget[0].FontSize=0",
            f"http://{ip}:{porta}/cgi-bin/configManager.cgi?action=setConfig&VideoWidget[0].FontSizeExtra1=0",
        ]

        for url in urlsport:
            lista_de_retorno: list = []
            s = requests.get(
                url, auth=HTTPDigestAuth("admin", "perkons6340"), timeout=1
            )
            returneddata: str = s.text.split("\r\n")
            time.sleep(0.2)
            lista_de_retorno.append(returneddata[0])
        return lista_de_retorno
    except Timeout:
        ...
