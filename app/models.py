from django.db import models


class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")

    def __str__(self):
        return f"{self.nome}, {self.uf}"

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"


class Autor(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do autor")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"


class Editora(models.Model):
    nome = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Editora"
        verbose_name_plural = "Editoras"


class Leitor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Leitor"
        verbose_name_plural = "Leitores"


class Genero(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Gênero"
        verbose_name_plural = "Gêneros"


class Livro(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    preco = models.IntegerField()
    data_plub = models.DateField()
    status = models.BooleanField()

    def __str__(self):
        return f"{self.nome}, {self.autor}"

    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"