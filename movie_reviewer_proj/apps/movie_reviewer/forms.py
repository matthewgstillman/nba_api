from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Movie
from django.core.exceptions import ValidationError

YEAR_CHOICES = (
    ('2018', '2018'),('2017', '2017.'),('2016', '2016'),('2015', '2015'),('2014', '2014'),('2013', '2013'),('2012', '2012'),('2011', '2011'),('2010', '2010'),('2009', '2009'),('2008', '2008'),('2007', '2007'),('2006', '2006'),('2005', '2005'),('2004', '2004'),('2003', '2003'),('2002', '2002'),('2001', '2001'),('2000', '2000'),('1999', '1999'),('1998', '1998'),('1997', '1997'),('1996', '1996'),('1995', '1995'),('1994', '1994'),('1993', '1993'),('1992', '1992'),('1991', '1991'),('1990', '1990'),('1989', '1989'),('1988', '1988'),('1987', '1987'),('1986', '1986'),('1985', '1985'), ('1984', '1984'),('1983', '1983'),('1982', '1982'),('1981', '1981'),('1980', '1980'),('1979', '1979'),('1978', '1978'),('1977', '1977'),('1976', '1976'),('1975', '1975'),('1974', '1974'),('1973', '1973'),('1972', '1972'),('1971', '1971'),('1970', '1970'),('1969', '1969'),('1968', '1968'),('1967', '1967'),('1966', '1966'),('1965', '1965'),('1964', '1964'),('1963', '1963'),('1962', '1962'),('1961', '1961'),('1960', '1960')
    )

GENRE_CHOICES = (
    ('ACTION', 'Action'), ('ACTION-ADVENTURE', 'Action-Adventure'), ('ACTION-COMEDY', 'Action-Comedy'), ('ADAPTATION' 'Adaptation'),  ('ADVENTURE', 'Adventure'), ('ANIMATED', 'Animated'), ('ANIME', 'Anime'), ('BOLLYWOOD', 'Bollywood'), ('CHICK-FLICK', 'Chick-Flick'), ('CHILDRENS', 'Childrens'), ('COMEDY', 'Comedy'), ('COMIC-BOOK-MOVIE', 'Comic-Book-Movie'), ('CRIME', 'Crime'), ('CULT-CLASSIC', 'Cult-Classic'),  ('DOCUMENTARY', 'Documentary'), ('DOCU-DRAMA', 'Docu-Drama'), ('DRAMA', 'Drama'),  ('FAIRY-TALE', 'Fairy-Tale'), ('GANGSTER', 'Gangster'), ('HISTORICAL', 'Historical'), ('HORROR', 'Horror'), ('MOBSTER', 'Mobster'), ('MONSTER', 'Monster'), ('MYSTERY', 'Mystery'), ('ROMANTIC-COMEDY', 'Romantic-Comedy'), ('SCIENCE-FICTION', 'Science-Fiction'), ('SEQUEL', 'Sequel'), ('SUPERHERO-MOVIE', 'Superhero-Movie'), ('TRUE-CRIME', 'True-Crime'), ('WAR', 'War'), ('WESTERN', 'Western'), ('ZOMBIE', 'Zombie') 
    )

RATING_CHOICES = (
    ('ONE-STAR', 'One-Star'), ('TWO-STARS', 'Two-Stars'), ('THREE-STARS', 'Three-Stars'), ('FOUR-STARS', 'Four-Stars'), ('FIVE-STARS', 'Five-Stars')
)

class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    email = forms.CharField(label='Enter email')
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists!")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists!")
        return email

    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match!")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = (
            'title',
            'year',
            'genre',
            'director',
            'lead_role_1',
            'lead_role_2',
            'rating',
            'review'
        )

    def save(self, commit=True):
        movie = super(MovieForm, self).save(commit=False)
        movie.title = self.cleaned_data['title']
        movie.year = self.cleaned_data['year']
        movie.genre = self.cleaned_data['genre']
        movie.director = self.cleaned_data['director']
        movie.lead_role_1 = self.cleaned_data['lead_role_1']
        movie.lead_role_2 = self.cleaned_data['lead_role_2']
        movie.rating = self.cleaned_data['rating']
        movie.review = self.cleaned_data['review']

        if commit:
            movie.save()
            Movie.objects.create(title=movie.title, year=movie.year, genre=movie.genre, director=movie.director,
            lead_role_1=movie.lead_role_1, lead_role_2=lead_role_2, rating=rating, review=review)

    


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['frist_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user

class EditProfileForm(UserChangeForm):
    
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )


# class Movie

    