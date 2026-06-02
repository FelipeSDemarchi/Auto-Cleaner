import pyautogui
import time

print("Limpeza Automática de Arquivos Temporários")

print("0 - Sair")
print("1 - Iniciar Limpeza")

opcao = int(input("Digite a opção desejada: "))

if opcao == 0:
    print("Você escolheu sair. Saindo do programa...")
    exit()

elif opcao == 1:
    print("Iniciando Limpeza...")

else:
    print("[ERRO]Opção Inválida! Saindo do programa...")
    exit()


pyautogui.PAUSE = 0.5

# Abrir o executar
pyautogui.press("win")
pyautogui.write("executar")
pyautogui.press("enter")

# Passo 1: Excluir arquivos da pasta prefetch

pyautogui.write("prefetch")
pyautogui.press("enter")
# Enter de novo para autorizar permissão de administrador
pyautogui.press("enter")

# Selecionar todos os arquivos da pasta
pyautogui.hotkey("ctrl", "a")

# Apagar tudo
pyautogui.press("delete")
pyautogui.press("enter")

# Ignorar arquivos não excluíveis
time.sleep(0.2)
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter")

# Fechar a pasta
time.sleep(1)
pyautogui.hotkey ("alt" , "f4")

# Passo 2: Excluir arquivos da pasta temp

# Abrir o executar novamente
time.sleep(0.5)
pyautogui.press("win")
pyautogui.write("executar")
pyautogui.press("enter")

# Entrar na pasta temp
pyautogui.write("temp")
pyautogui.press("enter")

# Excluir todos os arquivos

pyautogui.hotkey("ctrl" , "a")
pyautogui.press("delete")
pyautogui.press("enter")

# Ignorar arquivos não excluíveis
time.sleep(0.2)
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter")

# Fechar a pasta
time.sleep(1)
pyautogui.hotkey ("alt" , "f4")

# Passo 3: Esvaziar a pasta %temp%

# Abrir o executar novamente
time.sleep(0.5)
pyautogui.press("win")
pyautogui.write("executar")
pyautogui.press("enter")

# Entrar na pasta %temp%
pyautogui.write("%temp%")
pyautogui.press("enter")

# Excluir todos os arquivos
pyautogui.hotkey("ctrl" , "a")
pyautogui.press("delete")
pyautogui.press("enter")

# Ignorar arquivos não excluíveis
time.sleep(0.2)
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter")

# Fechar a pasta
time.sleep(1)
pyautogui.hotkey ("alt" , "f4")

# Passo 4: Esvaziar a lixeira

# Entrar na lixeira
time.sleep(0.5)
pyautogui.press("win")
pyautogui.write("lixeira")
pyautogui.press("enter")

# Esvaziar a lixeira

pyautogui.hotkey("ctrl" , "a")
pyautogui.press("delete")

# Confirmar Exclusão
pyautogui.press("enter")

# Fechar lixeira
time.sleep(1)
pyautogui.hotkey("alt" , "f4")

print("Limpeza Concluída!")
exit()