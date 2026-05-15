
from investigacao_criminal import Investigacao


investigacao = Investigacao()

investigacao.registrar("Pegadas próximas à cena do crime")
investigacao.registrar("Impressões digitais na porta")
investigacao.registrar("Câmera de segurança gravou suspeito")
investigacao.registrar("Arma encontrada no local")
investigacao.registrar("Testemunha relatou movimentação estranha")

investigacao.exibir()

investigacao.analisar()
investigacao.exibir()

investigacao.analisar()
investigacao.exibir()

investigacao.registrar("Celular do suspeito apreendido")
investigacao.exibir()
