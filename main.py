from selenium.webdriver import Chrome 
import platform

def setup_browser():
    """ Esta função organiza todas as chamadas
    relacionadas à instancia do chromedriver """
    if platform.system() == "Linux":
        print("Rodando no Linux")
        browser = Chrome(executable_path="./chromedriver")
    elif platform.system() == "Windows":
        browser = Chrome(executable_path=r".\chromedriver.exe")

setup_browser()