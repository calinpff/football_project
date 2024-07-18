from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from football_project.settings import EMAIL_HOST_USER
from players.forms import MatchForm, PlayerForm, FieldForm, FieldUpdateForm
from players.models import Match, Player, Field


class MatchCreateView(LoginRequiredMixin, CreateView):
    model = Match
    form_class = MatchForm
    template_name = 'matches/create_match.html'
    success_url = reverse_lazy('list_of_matches')

    def form_valid(self, form):
        if form.is_valid():
            match = form.save(commit=False)
            match.organizer = self.request.user
            match.save()
            # match.participants.add(self.request.user)
            # match.save()

            return redirect(self.success_url)
        return super(MatchCreateView, self).form_valid(form)


class MatchListView(LoginRequiredMixin, ListView):
    template_name = 'matches/list_of_matches.html'
    model = Match
    context_object_name = 'all_matches'


class MatchUpdateView(LoginRequiredMixin, UpdateView):
    model = Match
    form_class = MatchForm
    template_name = 'matches/update_match.html'

    def get_success_url(self):
        return reverse_lazy('match_details', kwargs={'pk': self.object.pk})


class MatchDetailView(LoginRequiredMixin, DetailView):
    template_name = 'matches/match_details.html'
    model = Match


class MatchDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'matches/delete_match.html'
    model = Match
    success_url = reverse_lazy('list_of_matches')


class FieldCreateView(LoginRequiredMixin, CreateView):
    model = Field
    form_class = FieldForm
    template_name = 'fields/add_field.html'
    success_url = reverse_lazy('field_list')


class FieldListView(LoginRequiredMixin, ListView):
    template_name = 'fields/list_of_fields.html'
    model = Field
    context_object_name = 'all_fields'


class FieldDetailView(LoginRequiredMixin, DetailView):
    template_name = 'fields/field_details.html'
    model = Field


class FieldUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'fields/update_field.html'
    model = Field
    form_class = FieldUpdateForm

    def get_success_url(self):
        return reverse_lazy('field_details', kwargs={'pk': self.object.pk})


class FieldDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'fields/delete_field.html'
    model = Field
    success_url = reverse_lazy('field_list')


class PlayerCreateView(CreateView):
    model = Player
    form_class = PlayerForm
    template_name = 'registration/create_user.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save(commit=False)

            new_user.first_name = new_user.first_name.title()
            new_user.last_name = new_user.last_name.title()
            new_user.save()

            details_user = {
                'fullname': f'{new_user.first_name.title()} {new_user.last_name.title()}',
                'user_name': new_user.username
            }

            subject = 'Welcome to Footbal4Everyone!'
            message = get_template('mail_account_created.html').render(details_user)
            mail = EmailMessage(
                subject,
                message,
                EMAIL_HOST_USER,
                [new_user.email]
            )
            mail.content_subtype = 'html'
            mail.send()

            return redirect(self.success_url)

        return super(PlayerCreateView, self).form_valid(form)


@login_required
def join_match_view(request, match_pk):
    match = Match.objects.get(pk=match_pk)
    if match.participants.count() < match.number_of_slots:
        user = request.user
        match.participants.add(user)
        match.save()
        messages.success(request, f'You have joined the match {match}')
    else:
        messages.error(request, f'There are no slots available')
    return redirect('match_details', pk=match.pk)


@login_required
def leave_match_view(request, match_pk):
    match = Match.objects.get(pk=match_pk)
    user = request.user
    if user in match.participants.all():
        match.participants.remove(user)
        match.save()
        messages.success(request, f'You have left the match {match}')

    return redirect('match_details', pk=match.pk)
