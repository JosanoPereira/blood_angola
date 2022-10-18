import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy
from .models import Doador


class Doador_Create(LoginRequiredMixin, CreateView):
    model = Doador
    fields = ['nome', 'sobrenome', 'data_nascimento', 'tipo_sangue', 'email', 'telefone', 'provincia', 'hospital']
    success_url = reverse_lazy('login')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        doador = form.save(commit=False)
        username = doador.nome + ' ' + doador.sobrenome
        data_atual = datetime.datetime.now()    # para pegar a data atual do sistema
        date = data_atual.date()
        ano = date.strftime("%Y")
        password = doador.nome+''+ano   # unir o nome do user com o ano atua para a
        # palavra-passe predifinição
        doador.hospital = self.request.user.doador.hospital
        doador.provincia = self.request.user.doador.provincia
        doador.user = User.objects.create_user(username, doador.email, password.lower())

        doador.save()
        return super(Doador_Create, self).form_valid(form)


class Doador_Update(LoginRequiredMixin, UpdateView):
    model = Doador
    fields = ['nome', 'sobrenome', 'data_nascimento', 'tipo_sangue', 'email', 'telefone', 'provincia', 'hospital']
    success_url = reverse_lazy('login')
    login_url = reverse_lazy('login')


class Doador_Delete(LoginRequiredMixin, DeleteView):
    model = Doador
    success_url = reverse_lazy('login')


class Doador_List(LoginRequiredMixin, ListView):
    model = Doador

    def get_queryset(self):
        pro = self.request.user.doador.provincia
        return Doador.objects.filter(provincia=pro)