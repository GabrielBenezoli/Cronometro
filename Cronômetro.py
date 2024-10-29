# importação do programa tkinter
from tkinter import *

# Criação da janela principal do programa //Título//Tamanho//Cor para background//Opção para bloqueio de aumento da janela
janela = Tk()
janela.title('Cronômetro')
janela.geometry('300x180')
janela.configure(bg='black')
janela.resizable(width=FALSE, height=FALSE)

# Criação de variáveis.//Tempo = 'O resultado que estará na tela inicialmente // Funcionamento = 'Variável que irá ser verdadeira ou falsa, de acordo com o funcionamento da aplicação
# Zerar = 'Variável numérica para medição de quantas vezes foi requerida a opção 'começar' = (1), caso seja requerida as opções 'pausar' e 'iniciar' a variável voltará a ser '0'
tempo = '00:00:00'
funcionamento = False
zerar = 0

# Função de inicialização do programa
def iniciar():
  global funcionamento
  global tempo
  
  if funcionamento:
     # Variável 'time' para receber o valor de 'tempo' e alterar o valor para string
     # Opção 'map' para separar os valores de time por casa ':'
     # Variáveis h = Valor para hora // m = Minutos // s = Segundos
     time = str(tempo)
     h,m,s = map(int,time.split(':'))
     s += 1
    
     # Variável 'if' para medir e acrescentar um minuto a cada 60 segundos e uma hora para cada 60 minutos, zerando os segundos e minutos
     if (s >= 60):
       s = 0 
       m += 1
       if (m >= 60):
         m = 0
         h += 1

     # Incrementação de strings para formar o novo resultado de tempo 'time'
     s = str(0) + str(s)
     m = str(0) + str(m)
     h = str(0) + str(h)
     time = str(h[-2:]) + ':' + str(m[-2:]) + ':' + str(s[-2:])
     label_tempo['text'] = time
     tempo = time
     # Aplicação para executar a função 'iniciar' a cada 1 segundo passado 
     label_tempo.after(1000,iniciar)
     
  
# Função de verificação para iniciar o programa
def começar():
  global funcionamento
  global zerar
  zerar += 1
  if zerar == 1:
   funcionamento = True
   iniciar()

# Função 'pausar' para paralisar o programa
def pausar():
  global funcionamento
  global zerar
  zerar = 0
  funcionamento = False

# Função 'reiniciar' para realizar o reiniciamento do valor do programa
def reiniciar():
  global funcionamento
  global tempo
  global zerar
  zerar = 0
  funcionamento = False
  tempo = '00:00:00'
  label_tempo['text'] = tempo

# Configurações do Label tempo para a forma como será exibido na tela, texto/fonte/cor de fundo/cor da escrita/Tamanho da escrita
label_tempo = Label(janela, text= tempo, font=('Times 50 bold'),bg= 'black', fg= 'blue')
label_tempo.place(x=20,y=30)

# Botão iniciar, pausar e reiniciar,simultaneamente, juntamente com suas configurações de cor de fundo, cor da escrita,fonte,tamanho e estilo de botão 
botao_iniciar = Button(janela, text='Iniciar', command=começar, width=10, height=2, bg='black', fg ='white', font=('Ivy 8 bold'), relief ='raised', overrelief='ridge')
botao_iniciar.place(x=25, y=130)
botao_pausar = Button(janela, text='Pausar',command=pausar, width=10, height=2, bg='black', fg ='white', font=('Ivy 8 bold'), relief ='raised', overrelief='ridge')
botao_pausar.place(x=110, y=130)
botao_reiniciar = Button(janela, text='Reiniciar',command=reiniciar, width=10, height=2, bg='black', fg ='white', font=('Ivy 8 bold'), relief ='raised', overrelief='ridge')
botao_reiniciar.place(x=195, y=130)

janela.mainloop()
