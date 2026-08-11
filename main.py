import pyautogui
import time
import webbrowser
from urllib.parse import quote_plus

pyautogui.FAILSAFE = True



musicas = [
    "Sweet Child O' Mine",
    "Bohemian Rhapsody",
    "Hotel California",

    #Ponha suas musicas aqui, lembrando de colocar entre aspas e separar por vírgula
]

TEMPO_PAGINA = 5
TEMPO_VIDEO = 3

POSICAO_PRIMEIRO_RESULTADO = (500, 250)



def pesquisar_musica(musica):
    print(f"🔎 Pesquisando: {musica}")

    pesquisa = quote_plus(musica)
    url = f"https://www.youtube.com/results?search_query={pesquisa}"

    webbrowser.open(url)

    print("⏳ Aguardando o YouTube carregar...")
    time.sleep(TEMPO_PAGINA)


def abrir_primeiro_resultado():
    print("🖱️ Abrindo o primeiro resultado...")

    pyautogui.click(*POSICAO_PRIMEIRO_RESULTADO)

    time.sleep(TEMPO_VIDEO)


def tela_cheia():
    print("⛶ Ativando tela cheia...")
    pyautogui.press("f")


def executar_musica(musica):
    try:
        pesquisar_musica(musica)
        abrir_primeiro_resultado()
        tela_cheia()

        print(f"▶️ Reproduzindo: {musica}")

    except Exception as erro:
        print(f"❌ Erro ao executar '{musica}': {erro}")


print("🎵 Automação iniciada!")
print("⚠️ Mova o mouse para o canto superior esquerdo para interromper.\n")

for musica in musicas:
    executar_musica(musica)

    time.sleep(2)

print("\n✅ Todas as músicas foram processadas!")