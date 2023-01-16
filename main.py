import asyncio
import aiohttp
from os import system
from ascii import banner
from termcolor import colored

async def buscar(sessao, url):
    try:
        async with sessao.get(url) as resposta:
            return resposta.status
    except aiohttp.ClientError as e:
        print("Error while sending request: ", e)

async def principal():
    try:
        async with aiohttp.ClientSession() as sessao:
            url = input(colored("Enter the URL: ", 'yellow', 'on_red'))
            try:
                numero_de_requisicoes = int(input(colored("Enter the number of requests to send: ", 'yellow', 'on_red')))
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
                return
            tarefas = []
            for i in range(numero_de_requisicoes):
                tarefas.append(buscar(sessao, url))
            try:
                respostas = await asyncio.gather(*tarefas)
                for resposta in respostas:
                    print(resposta)
            except aiohttp.ClientError as e:
                print("Error: ", e)
    except Exception as e:
        print("Error: ", e)
while True:
    try:
        try:
            system('clear')
        except:
            system('cls')
        banner()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(principal())
    except Exception as e:
        print(colored("Error: conexão negada! tente novamente.", 'red'))
    choice = int(input(colored("2 to break and exit | 1 to continue --> ", 'yellow', 'on_red')))
    if choice == 2:
        break
    else:
        pass